from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from project.schemas.employee import EmployeeSchema
from project.infrastructure.postgres.models import Employee
from project.core.config import settings


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
        query = f"select * from {settings.POSTGRES_SCHEMA}.employees;"

        result = await session.execute(text(query))

        return [EmployeeSchema.from_orm(item) for item in result.mappings().all()]
