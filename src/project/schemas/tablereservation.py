from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class TableReservationSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    reservation_id: int
    table_number: int
    reservation_time: datetime
    client_id: int
