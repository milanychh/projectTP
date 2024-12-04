from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from project.schemas.delivery import DeliverySchema
from project.infrastructure.postgres.models import Delivery
from project.core.config import settings

class DeliveryRepository:
    _collection: Type[Delivery] = Delivery

    async def check_connection(self, session: AsyncSession) -> bool:
        query = "select 1;"
        result = await session.scalar(text(query))
        return True if result else False

    async def get_all_deliveries(self, session: AsyncSession) -> list[DeliverySchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.deliveries;"
        deliveries = await session.execute(text(query))
        return [DeliverySchema.model_validate(obj=delivery) for delivery in deliveries.mappings().all()]
