from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.deliveryitem import DeliveryItemSchema, DeliveryItemCreateUpdateSchema
from project.infrastructure.postgres.models import DeliveryItem

from project.core.exceptions import DeliveryItemNotFound, DeliveryItemAlreadyExists


class DeliveryItemRepository:
    _collection: Type[DeliveryItem] = DeliveryItem

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_delivery_items(
        self,
        session: AsyncSession,
    ) -> list[DeliveryItemSchema]:
        query = select(self._collection)

        result = await session.scalars(query)

        return [DeliveryItemSchema.model_validate(obj=item) for item in result.all()]

    async def get_delivery_item_by_id(
        self,
        session: AsyncSession,
        item_id: int,
    ) -> DeliveryItemSchema:
        query = (
            select(self._collection)
            .where(self._collection.item_id == item_id)
        )

        item = await session.scalar(query)

        if not item:
            raise DeliveryItemNotFound(_id=item_id)

        return DeliveryItemSchema.model_validate(obj=item)

    async def create_delivery_item(
        self,
        session: AsyncSession,
        item: DeliveryItemCreateUpdateSchema,
    ) -> DeliveryItemSchema:
        query = (
            insert(self._collection)
            .values(item.model_dump())
            .returning(self._collection)
        )

        try:
            created_item = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise DeliveryItemAlreadyExists(item_id=item.item_id, delivery_id=item.delivery_id)

        return DeliveryItemSchema.model_validate(obj=created_item)

    async def update_delivery_item(
        self,
        session: AsyncSession,
        item_id: int,
        item: DeliveryItemCreateUpdateSchema,
    ) -> DeliveryItemSchema:
        query = (
            update(self._collection)
            .where(self._collection.item_id == item_id)
            .values(item.model_dump())
            .returning(self._collection)
        )

        updated_item = await session.scalar(query)

        if not updated_item:
            raise DeliveryItemNotFound(_id=item_id)

        return DeliveryItemSchema.model_validate(obj=updated_item)

    async def delete_delivery_item(
        self,
        session: AsyncSession,
        item_id: int,
    ) -> None:
        query = delete(self._collection).where(self._collection.item_id == item_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise DeliveryItemNotFound(_id=item_id)
