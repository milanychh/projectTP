from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.recipe import RecipeSchema, RecipeCreateUpdateSchema
from project.infrastructure.postgres.models import Recipe
from project.core.exceptions import RecipeNotFound, RecipeAlreadyExists
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

    async def get_recipe_by_id(
        self,
        session: AsyncSession,
        recipe_id: int,
    ) -> RecipeSchema:
        query = (
            select(self._collection)
            .where(self._collection.recipe_id == recipe_id)
        )

        recipe = await session.scalar(query)

        if not recipe:
            raise RecipeNotFound(_id=recipe_id)

        return RecipeSchema.model_validate(obj=recipe)

    async def create_recipe(
        self,
        session: AsyncSession,
        recipe: RecipeCreateUpdateSchema,
    ) -> RecipeSchema:
        query = (
            insert(self._collection)
            .values(recipe.model_dump())
            .returning(self._collection)
        )

        try:
            created_recipe = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise RecipeAlreadyExists(dish_id=recipe.dish_id, product_id=recipe.product_id)

        return RecipeSchema.model_validate(obj=created_recipe)

    async def update_recipe(
        self,
        session: AsyncSession,
        recipe_id: int,
        recipe: RecipeCreateUpdateSchema,
    ) -> RecipeSchema:
        query = (
            update(self._collection)
            .where(self._collection.recipe_id == recipe_id)
            .values(recipe.model_dump())
            .returning(self._collection)
        )

        updated_recipe = await session.scalar(query)

        if not updated_recipe:
            raise RecipeNotFound(_id=recipe_id)

        return RecipeSchema.model_validate(obj=updated_recipe)

    async def delete_recipe(
        self,
        session: AsyncSession,
        recipe_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.recipe_id == recipe_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise RecipeNotFound(_id=recipe_id)
