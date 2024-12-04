from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from project.schemas.supplier import SupplierSchema
from project.infrastructure.postgres.models import Supplier
from project.core.config import settings

class SupplierRepository:
    _collection: Type[Supplier] = Supplier

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_suppliers(
        self,
        session: AsyncSession,
    ) -> list[SupplierSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.suppliers;"

        suppliers = await session.execute(text(query))

        return [SupplierSchema.model_validate(obj=supplier) for supplier in suppliers.mappings().all()]
