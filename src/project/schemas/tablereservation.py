from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class TableReservationCreateUpdateSchema(BaseModel):
    table_number: int
    reservation_time: datetime
    client_id: int

class TableReservationSchema(TableReservationCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    reservation_id: int
