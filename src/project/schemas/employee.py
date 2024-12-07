from pydantic import BaseModel, Field, ConfigDict
from datetime import date

class EmployeeCreateUpdateSchema(BaseModel):
    full_name: str
    position: str | None
    hire_date: date | None

class EmployeeSchema(EmployeeCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    employee_id: int
