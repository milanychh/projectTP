from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from project.schemas.deliveryitem import DeliveryItemSchema
from project.infrastructure.postgres.models import DeliveryItem
from project.core.config import settings


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
        query = f"select * from {settings.POSTGRES_SCHEMA}.delivery_items;"

        result = await session.execute(text(query))

        return [DeliveryItemSchema.from_orm(item) for item in result.mappings().all()]
