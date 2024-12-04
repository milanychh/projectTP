from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from decimal import Decimal

from project.infrastructure.postgres.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=True)


class Client(Base):
    __tablename__ = "clients"

    client_id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(nullable=False)
    phone_number: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)

class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(nullable=False)
    expiry_date: Mapped[str | None] = mapped_column(nullable=True)

class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id: Mapped[int] = mapped_column(primary_key=True)
    supplier_name: Mapped[str] = mapped_column(nullable=False)
    contact_info: Mapped[str] = mapped_column(nullable=True)

class Delivery(Base):
    __tablename__ = "deliveries"

    delivery_id: Mapped[int] = mapped_column(primary_key=True)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.supplier_id", ondelete="CASCADE"), nullable=False)
    delivery_date: Mapped[date] = mapped_column(nullable=True)

class DeliveryItem(Base):
    __tablename__ = "delivery_items"

    item_id: Mapped[int] = mapped_column(primary_key=True)
    delivery_id: Mapped[int] = mapped_column(ForeignKey("deliveries.delivery_id", ondelete="CASCADE"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(nullable=False)

class Recipe(Base):
    __tablename__ = "recipes"

    recipe_id: Mapped[int] = mapped_column(primary_key=True)
    dish_id: Mapped[int] = mapped_column(ForeignKey("dishes.dish_id", ondelete="CASCADE"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False)
    quantity: Mapped[Decimal] = mapped_column(nullable=False)

class Dish(Base):
    __tablename__ = "dishes"

    dish_id: Mapped[int] = mapped_column(primary_key=True)
    dish_name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)

class Menu(Base):
    __tablename__ = "menu"

    menu_id: Mapped[int] = mapped_column(primary_key=True)
    dish_id: Mapped[int] = mapped_column(ForeignKey("dishes.dish_id", ondelete="CASCADE"), nullable=False)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.recipe_id", ondelete="CASCADE"), nullable=False)
    dish_name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=True)

class DishIngredient(Base):
    __tablename__ = "dishingredients"

    record_id: Mapped[int] = mapped_column(primary_key=True)
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.recipe_id", ondelete="CASCADE"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.product_id", ondelete="CASCADE"), nullable=False)
    quantity: Mapped[Decimal] = mapped_column(nullable=False)

class TableReservation(Base):
    __tablename__ = "tablereservations"

    reservation_id: Mapped[int] = mapped_column(primary_key=True)
    table_number: Mapped[int] = mapped_column(nullable=False)
    reservation_time: Mapped[date] = mapped_column(nullable=False)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.client_id", ondelete="CASCADE"), nullable=False)


class DiscountCard(Base):
    __tablename__ = "discountcards"

    discount_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    discount_percentage: Mapped[Decimal] = mapped_column(nullable=False)
    discount_conditions: Mapped[str | None] = mapped_column(nullable=True)

class Order(Base):
    __tablename__ = "orders"

    order_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_datetime: Mapped[date] = mapped_column(nullable=True)
    client_id: Mapped[int | None] = mapped_column(ForeignKey("clients.client_id", ondelete="CASCADE"), nullable=True)
    employee_id: Mapped[int | None] = mapped_column(ForeignKey("employees.employee_id", ondelete="SET NULL"), nullable=True)
    reservation_id: Mapped[int | None] = mapped_column(ForeignKey("tablereservations.reservation_id", ondelete="SET NULL"), nullable=True)
    discount_id: Mapped[int | None] = mapped_column(ForeignKey("discountcards.discount_id", ondelete="SET NULL"), nullable=True)
    product_id: Mapped[int | None] = mapped_column(ForeignKey("products.product_id", ondelete="SET NULL"), nullable=True)
    dish_id: Mapped[int | None] = mapped_column(ForeignKey("dishes.dish_id", ondelete="SET NULL"), nullable=True)
    order_status: Mapped[str] = mapped_column(nullable=False)
    total_price: Mapped[Decimal] = mapped_column(nullable=True)

class Employee(Base):
    __tablename__ = "employees"

    employee_id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(nullable=False)
    position: Mapped[str | None] = mapped_column(nullable=False)
    hire_date: Mapped[date | None] = mapped_column(nullable=True)