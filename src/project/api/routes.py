from fastapi import APIRouter

from project.infrastructure.postgres.repository.user_repo import UserRepository
from project.infrastructure.postgres.repository.client_repo import ClientRepository
from project.infrastructure.postgres.repository.product_repo import ProductRepository
from project.infrastructure.postgres.repository.supplier_repo import SupplierRepository
from project.infrastructure.postgres.repository.delivery_repo import DeliveryRepository
from project.infrastructure.postgres.repository.deliveryitem_repo import DeliveryItemRepository
from project.infrastructure.postgres.repository.recipe_repo import RecipeRepository
from project.infrastructure.postgres.repository.dish_repo import DishRepository
from project.infrastructure.postgres.repository.menu_repo import MenuRepository
from project.infrastructure.postgres.repository.dishingredient_repo import DishIngredientRepository
from project.infrastructure.postgres.repository.tablereservation_repo import TableReservationRepository
from project.infrastructure.postgres.repository.discountcard_repo import DiscountCardRepository
from project.infrastructure.postgres.repository.order_repo import OrderRepository
from project.infrastructure.postgres.repository.employee_repo import EmployeeRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.user import UserSchema
from project.schemas.client import ClientSchema
from project.schemas.product import ProductSchema
from project.schemas.supplier import SupplierSchema
from project.schemas.delivery import DeliverySchema
from project.schemas.deliveryitem import DeliveryItemSchema
from project.schemas.recipe import RecipeSchema
from project.schemas.dish import DishSchema
from project.schemas.menu import MenuSchema
from project.schemas.dishingredient import DishIngredientSchema
from project.schemas.tablereservation import TableReservationSchema
from project.schemas.discountcard import DiscountCardSchema
from project.schemas.employee import EmployeeSchema
from project.schemas.order import OrderSchema


router = APIRouter()


@router.get("/all_users", response_model=list[UserSchema])
async def get_all_users() -> list[UserSchema]:
    user_repo = UserRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await user_repo.check_connection(session=session)
        all_users = await user_repo.get_all_users(session=session)

    return all_users

@router.get("/all_clients", response_model=list[ClientSchema])
async def get_all_clients() -> list[ClientSchema]:
    client_repo = ClientRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await client_repo.check_connection(session=session)
        all_clients = await client_repo.get_all_clients(session=session)

    return all_clients

@router.get("/all_products", response_model=list[ProductSchema])
async def get_all_products() -> list[ProductSchema]:
    product_repo = ProductRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await product_repo.check_connection(session=session)
        all_products = await product_repo.get_all_products(session=session)

    return all_products

@router.get("/all_suppliers", response_model=list[SupplierSchema])
async def get_all_suppliers() -> list[SupplierSchema]:
    supplier_repo = SupplierRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await supplier_repo.check_connection(session=session)
        all_suppliers = await supplier_repo.get_all_suppliers(session=session)

    return all_suppliers

@router.get("/all_deliveries", response_model=list[DeliverySchema])
async def get_all_deliveries() -> list[DeliverySchema]:
    delivery_repo = DeliveryRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await delivery_repo.check_connection(session=session)
        all_deliveries = await delivery_repo.get_all_deliveries(session=session)

    return all_deliveries

@router.get("/all_delivery_items", response_model=list[DeliveryItemSchema])
async def get_all_delivery_items() -> list[DeliveryItemSchema]:
    delivery_item_repo = DeliveryItemRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await delivery_item_repo.check_connection(session=session)
        all_delivery_items = await delivery_item_repo.get_all_delivery_items(session=session)

    return all_delivery_items

@router.get("/all_recipes", response_model=list[RecipeSchema])
async def get_all_recipes() -> list[RecipeSchema]:
    recipe_repo = RecipeRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await recipe_repo.check_connection(session=session)
        all_recipes = await recipe_repo.get_all_recipes(session=session)

    return all_recipes

@router.get("/all_dishes", response_model=list[DishSchema])
async def get_all_dishes() -> list[DishSchema]:
    dish_repo = DishRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await dish_repo.check_connection(session=session)
        all_dishes = await dish_repo.get_all_dishes(session=session)

    return all_dishes

@router.get("/all_menu_items", response_model=list[MenuSchema])
async def get_all_menu_items() -> list[MenuSchema]:
    menu_repo = MenuRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await menu_repo.check_connection(session=session)
        all_menu_items = await menu_repo.get_all_menu_items(session=session)

    return all_menu_items

@router.get("/all_dish_ingredients", response_model=list[DishIngredientSchema])
async def get_all_dish_ingredients() -> list[DishIngredientSchema]:
    dish_ingredient_repo = DishIngredientRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await dish_ingredient_repo.check_connection(session=session)
        all_dish_ingredients = await dish_ingredient_repo.get_all_dish_ingredients(session=session)

    return all_dish_ingredients

@router.get("/all_table_reservations", response_model=list[TableReservationSchema])
async def get_all_table_reservations() -> list[TableReservationSchema]:
    table_reservation_repo = TableReservationRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await table_reservation_repo.check_connection(session=session)
        all_table_reservations = await table_reservation_repo.get_all_table_reservations(session=session)

    return all_table_reservations

@router.get("/all_discount_cards", response_model=list[DiscountCardSchema])
async def get_all_discount_cards() -> list[DiscountCardSchema]:
    discount_card_repo = DiscountCardRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await discount_card_repo.check_connection(session=session)
        all_discount_cards = await discount_card_repo.get_all_discount_cards(session=session)

    return all_discount_cards

@router.get("/all_orders", response_model=list[OrderSchema])
async def get_all_orders() -> list[OrderSchema]:
    order_repo = OrderRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await order_repo.check_connection(session=session)
        all_orders = await order_repo.get_all_orders(session=session)

    return all_orders

@router.get("/all_employees", response_model=list[EmployeeSchema])
async def get_all_employees() -> list[EmployeeSchema]:
    employee_repo = EmployeeRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await employee_repo.check_connection(session=session)
        all_employees = await employee_repo.get_all_employees(session=session)

    return all_employees