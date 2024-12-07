from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.employee import EmployeeSchema, EmployeeCreateUpdateSchema
from project.infrastructure.postgres.models import Employee
from project.core.exceptions import EmployeeNotFound, EmployeeAlreadyExists


class EmployeeRepository:
    _collection: Type[Employee] = Employee

    async def check_connection(
        self,
        session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_employees(
        self,
        session: AsyncSession,
    ) -> list[EmployeeSchema]:
        query = select(self._collection)

        employees = await session.scalars(query)

        return [EmployeeSchema.model_validate(obj=employee) for employee in employees.all()]

    async def get_employee_by_id(
        self,
        session: AsyncSession,
        employee_id: int,
    ) -> EmployeeSchema:
        query = (
            select(self._collection)
            .where(self._collection.employee_id == employee_id)
        )

        employee = await session.scalar(query)

        if not employee:
            raise EmployeeNotFound(_id=employee_id)

        return EmployeeSchema.model_validate(obj=employee)

    async def create_employee(
        self,
        session: AsyncSession,
        employee: EmployeeCreateUpdateSchema,
    ) -> EmployeeSchema:
        query = (
            insert(self._collection)
            .values(employee.model_dump())
            .returning(self._collection)
        )

        try:
            created_employee = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise EmployeeAlreadyExists(name=employee.name)

        return EmployeeSchema.model_validate(obj=created_employee)

    async def update_employee(
        self,
        session: AsyncSession,
        employee_id: int,
        employee: EmployeeCreateUpdateSchema,
    ) -> EmployeeSchema:
        query = (
            update(self._collection)
            .where(self._collection.employee_id == employee_id)
            .values(employee.model_dump())
            .returning(self._collection)
        )

        updated_employee = await session.scalar(query)

        if not updated_employee:
            raise EmployeeNotFound(_id=employee_id)

        return EmployeeSchema.model_validate(obj=updated_employee)

    async def delete_employee(
        self,
        session: AsyncSession,
        employee_id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.employee_id == employee_id)

        result = await session.execute(query)

        if not result.rowcount:
            raise EmployeeNotFound(_id=employee_id)
