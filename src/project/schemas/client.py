from pydantic import BaseModel, Field, ConfigDict


class ClientCreateUpdateSchema(BaseModel):
    full_name: str
    email: str | None = Field(default=None)
    phone_number: str | None = Field(default=None)


class ClientSchema(ClientCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    client_id: int
