from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.dishingredient import DishIngredientSchema, DishIngredientCreateUpdateSchema
from project.infrastructure.postgres.models import DishIngredient
from project.core.exceptions import DishIngredientNotFound, DishIngredientAlreadyExists


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
        query = select(self._collection)

        dish_ingredients = await session.scalars(query)

        return [DishIngredientSchema.model_validate(obj=item) for item in dish_ingredients.all()]

    async def get_dish_ingredient_by_id(
        self,
        session: AsyncSession,
        ingredient_id: int,
    ) -> DishIngredientSchema:
        query = (
            select(self._collection)
            .where(self._collection.record_id == ingredient_id)
        )

        ingredient = await session.scalar(query)

        if not ingredient:
            raise DishIngredientNotFound(_id=ingredient_id)

        return DishIngredientSchema.model_validate(obj=ingredient)

    async def create_dish_ingredient(
        self,
        session: AsyncSession,
        dish_ingredient: DishIngredientCreateUpdateSchema,
    ) -> DishIngredientSchema:
        query = (
            insert(self._collection)
            .values(dish_ingredient.model_dump())
            .returning(self._collection)
        )

        try:
            created_ingredient = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise DishIngredientAlreadyExists(
                recipe_id=dish_ingredient.recipe_id,
                product_id=dish_ingredient.product_id,
            )

        return DishIngredientSchema.model_validate(obj=created_ingredient)

    async def update_dish_ingredient(
        self,
        session: AsyncSession,
        ingredient_id: int,
        dish_ingredient: DishIngredientCreateUpdateSchema,
    ) -> DishIngredientSchema:
        query = (
            update(self._collection)
            .where(self._collection.record_id == ingredient_id)
            .values(dish_ingredient.model_dump())
            .returning(self._collection)
        )

        updated_ingredient = await session.scalar(query)

        if not updated_ingredient:
            raise DishIngredientNotFound(_id=ingredient_id)

        return DishIngredientSchema.model_validate(obj=updated_ingredient)

    async def delete_dish_ingredient(
        self,
        session: AsyncSession,
        ingredient_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.record_id == ingredient_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise DishIngredientNotFound(_id=ingredient_id)
