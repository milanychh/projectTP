from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from project.schemas.order import OrderSchema
from project.infrastructure.postgres.models import Order
from project.core.config import settings


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
        query = f"select * from {settings.POSTGRES_SCHEMA}.orders;"

        result = await session.execute(text(query))

        return [OrderSchema.from_orm(item) for item in result.mappings().all()]
