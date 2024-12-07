from itertools import product

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


user_repo = UserRepository()
database = PostgresDatabase()
client_repo = ClientRepository()
product_repo = ProductRepository()
supplier_repo = SupplierRepository()
delivery_repo = DeliveryRepository()
deliveryitem_repo = DeliveryItemRepository()
recipe_repo = RecipeRepository()
dish_repo = DishRepository()
menu_repo = MenuRepository()
dishingredient_repo = DishIngredientRepository()
tablereservation_repo = TableReservationRepository()
discountcard_repo = DiscountCardRepository()
order_repo = OrderRepository()
employee_repo = EmployeeRepository()