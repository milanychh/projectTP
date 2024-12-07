from pydantic import BaseModel


class HealthCheckSchema(BaseModel):
    db_is_ok: bool
    client_db_is_ok: bool
    product_db_is_ok: bool
    supplier_db_is_ok: bool
    deliveries_db_is_ok: bool
    delivery_items_db_is_ok: bool
    recipes_db_is_ok: bool
    dishes_db_is_ok: bool
    menu_db_is_ok: bool
    dishingredient_db_is_ok: bool
    tablereservation_db_is_ok: bool
    discountcard_db_is_ok: bool
    orders_db_is_ok: bool
    employee_db_is_ok: bool

