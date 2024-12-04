from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from project.schemas.dish import DishSchema
from project.infrastructure.postgres.models import Dish
from project.core.config import settings


class DishRepository:
    _collection: Type[Dish] = Dish

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_dishes(
            self,
            session: AsyncSession,
    ) -> list[DishSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.dishes;"

        result = await session.execute(text(query))

        return [DishSchema.from_orm(dish) for dish in result.mappings().all()]
