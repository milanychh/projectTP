from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from project.schemas.menu import MenuSchema
from project.infrastructure.postgres.models import Menu
from project.core.config import settings


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
        query = f"select * from {settings.POSTGRES_SCHEMA}.menu;"

        result = await session.execute(text(query))

        return [MenuSchema.from_orm(item) for item in result.mappings().all()]
