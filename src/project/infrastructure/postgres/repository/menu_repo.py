from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError
from project.schemas.menu import MenuSchema, MenuCreateUpdateSchema
from project.infrastructure.postgres.models import Menu
from project.core.config import settings
from project.core.exceptions import MenuNotFound, MenuAlreadyExists


class MenuRepository:
    _collection: Type[Menu] = Menu

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_menu_items(
            self,
            session: AsyncSession,
    ) -> list[MenuSchema]:
        query = select(self._collection)

        result = await session.scalars(query)

        return [MenuSchema.from_orm(item) for item in result.all()]

    async def get_menu_item_by_id(
            self,
            session: AsyncSession,
            menu_item_id: int,
    ) -> MenuSchema:
        query = (
            select(self._collection)
            .where(self._collection.id == menu_item_id)
        )

        menu_item = await session.scalar(query)

        if not menu_item:
            raise MenuNotFound(_id=menu_item_id)

        return MenuSchema.from_orm(menu_item)

    async def create_menu_item(
            self,
            session: AsyncSession,
            menu_item: MenuCreateUpdateSchema,
    ) -> MenuSchema:
        query = (
            insert(self._collection)
            .values(menu_item.model_dump())
            .returning(self._collection)
        )

        try:
            created_menu_item = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise MenuAlreadyExists(name=menu_item.name)

        return MenuSchema.from_orm(created_menu_item)

    async def update_menu_item(
            self,
            session: AsyncSession,
            menu_item_id: int,
            menu_item: MenuCreateUpdateSchema,
    ) -> MenuSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == menu_item_id)
            .values(menu_item.model_dump())
            .returning(self._collection)
        )

        updated_menu_item = await session.scalar(query)

        if not updated_menu_item:
            raise MenuNotFound(_id=menu_item_id)

        return MenuSchema.from_orm(updated_menu_item)

    async def delete_menu_item(
            self,
            session: AsyncSession,
            menu_item_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == menu_item_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise MenuNotFound(_id=menu_item_id)
