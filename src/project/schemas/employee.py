from pydantic import BaseModel, Field, ConfigDict
from datetime import date

class EmployeeSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    employee_id: int
    full_name: str
    position: str | None
    hire_date: date | None
