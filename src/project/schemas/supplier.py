from pydantic import BaseModel, Field, ConfigDict

class SupplierSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    supplier_id: int
    supplier_name: str
    contact_info: str | None = Field(default=None)