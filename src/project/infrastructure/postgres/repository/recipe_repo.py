from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from project.schemas.recipe import RecipeSchema
from project.infrastructure.postgres.models import Recipe
from project.core.config import settings


class RecipeRepository:
    _collection: Type[Recipe] = Recipe

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_recipes(
        self,
        session: AsyncSession,
    ) -> list[RecipeSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.recipes;"

        recipes = await session.execute(text(query))

        return [RecipeSchema.model_validate(obj=recipe) for recipe in recipes.mappings().all()]
