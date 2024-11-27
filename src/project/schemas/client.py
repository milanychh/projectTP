from pydantic import BaseModel, Field, ConfigDict

class ClientSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    client_id: int
    full_name: str
    phone_number: str | None = Field(default=None)
    email: str | None = Field(default=None)
