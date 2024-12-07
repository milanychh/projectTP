from pydantic import BaseModel, Field, ConfigDict


class SupplierCreateUpdateSchema(BaseModel):
    supplier_name: str
    contact_info: str | None = Field(default=None)


class SupplierSchema(SupplierCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    supplier_id: int
    supplier_name: str
    contact_info: str | None = Field(default=None)
