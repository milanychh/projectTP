from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from project.schemas.discountcard import DiscountCardSchema
from project.infrastructure.postgres.models import DiscountCard
from project.core.config import settings

class DiscountCardRepository:
    _collection: Type[DiscountCard] = DiscountCard

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_discount_cards(
        self,
        session: AsyncSession,
    ) -> list[DiscountCardSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.discount_cards;"

        discount_cards = await session.execute(text(query))

        return [DiscountCardSchema.model_validate(obj=discount_card) for discount_card in discount_cards.mappings().all()]
