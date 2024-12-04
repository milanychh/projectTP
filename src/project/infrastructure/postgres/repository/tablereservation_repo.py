from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from project.schemas.tablereservation import TableReservationSchema
from project.infrastructure.postgres.models import TableReservation
from project.core.config import settings

class TableReservationRepository:
    _collection: Type[TableReservation] = TableReservation

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_table_reservations(
        self,
        session: AsyncSession,
    ) -> list[TableReservationSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.tablereservations;"

        table_reservations = await session.execute(text(query))

        return [TableReservationSchema.model_validate(obj=reservation) for reservation in table_reservations.mappings().all()]
