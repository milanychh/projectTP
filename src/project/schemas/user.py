from pydantic import BaseModel, Field, ConfigDict


class UserCreateUpdateSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str | None = Field(default=None)


class UserSchema(UserCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
