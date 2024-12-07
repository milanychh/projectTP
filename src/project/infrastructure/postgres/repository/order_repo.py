from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.order import OrderSchema, OrderCreateUpdateSchema
from project.infrastructure.postgres.models import Order
from project.core.exceptions import OrderNotFound, OrderAlreadyExists


class OrderRepository:
    _collection: Type[Order] = Order

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_orders(
        self,
        session: AsyncSession,
    ) -> list[OrderSchema]:
        query = select(self._collection)

        orders = await session.scalars(query)

        return [OrderSchema.model_validate(obj=order) for order in orders.all()]

    async def get_order_by_id(
        self,
        session: AsyncSession,
        order_id: int,
    ) -> OrderSchema:
        query = (
            select(self._collection)
            .where(self._collection.order_id == order_id)
        )

        order = await session.scalar(query)

        if not order:
            raise OrderNotFound(_id=order_id)

        return OrderSchema.model_validate(obj=order)

    async def create_order(
        self,
        session: AsyncSession,
        order: OrderCreateUpdateSchema,
    ) -> OrderSchema:
        query = (
            insert(self._collection)
            .values(order.model_dump())
            .returning(self._collection)
        )

        try:
            created_order = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise OrderAlreadyExists(order_id=order.order_id)

        return OrderSchema.model_validate(obj=created_order)

    async def update_order(
        self,
        session: AsyncSession,
        order_id: int,
        order: OrderCreateUpdateSchema,
    ) -> OrderSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == order_id)
            .values(order.model_dump())
            .returning(self._collection)
        )

        updated_order = await session.scalar(query)

        if not updated_order:
            raise OrderNotFound(_id=order_id)

        return OrderSchema.model_validate(obj=updated_order)

    async def delete_order(
        self,
        session: AsyncSession,
        order_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.order_id == order_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise OrderNotFound(_id=order_id)
