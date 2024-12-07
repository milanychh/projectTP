from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.tablereservation import TableReservationSchema, TableReservationCreateUpdateSchema
from project.infrastructure.postgres.models import TableReservation
from project.core.exceptions import TableReservationNotFound, TableReservationAlreadyExists

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
        query = select(self._collection)

        table_reservations = await session.scalars(query)

        return [TableReservationSchema.model_validate(obj=reservation) for reservation in table_reservations.all()]

    async def get_table_reservation_by_id(
        self,
        session: AsyncSession,
        reservation_id: int,
    ) -> TableReservationSchema:
        query = (
            select(self._collection)
            .where(self._collection.reservation_id == reservation_id)
        )

        reservation = await session.scalar(query)

        if not reservation:
            raise TableReservationNotFound(_id=reservation_id)

        return TableReservationSchema.model_validate(obj=reservation)

    async def create_table_reservation(
        self,
        session: AsyncSession,
        reservation: TableReservationCreateUpdateSchema,
    ) -> TableReservationSchema:
        query = (
            insert(self._collection)
            .values(reservation.model_dump())
            .returning(self._collection)
        )

        try:
            created_reservation = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise TableReservationAlreadyExists(reservation_id=reservation.id)

        return TableReservationSchema.model_validate(obj=created_reservation)

    async def update_table_reservation(
        self,
        session: AsyncSession,
        reservation_id: int,
        reservation: TableReservationCreateUpdateSchema,
    ) -> TableReservationSchema:
        query = (
            update(self._collection)
            .where(self._collection.reservation_id == reservation_id)
            .values(reservation.model_dump())
            .returning(self._collection)
        )

        updated_reservation = await session.scalar(query)

        if not updated_reservation:
            raise TableReservationNotFound(_id=reservation_id)

        return TableReservationSchema.model_validate(obj=updated_reservation)

    async def delete_table_reservation(
        self,
        session: AsyncSession,
        reservation_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.reservation_id == reservation_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise TableReservationNotFound(_id=reservation_id)
