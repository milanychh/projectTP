from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from project.schemas.dishingredient import DishIngredientSchema
from project.infrastructure.postgres.models import DishIngredient
from project.core.config import settings


class DishIngredientRepository:
    _collection: Type[DishIngredient] = DishIngredient

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_dish_ingredients(
            self,
            session: AsyncSession,
    ) -> list[DishIngredientSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.dishingredients;"

        result = await session.execute(text(query))

        return [DishIngredientSchema.from_orm(item) for item in result.mappings().all()]
