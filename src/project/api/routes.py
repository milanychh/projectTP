from fastapi import APIRouter, HTTPException, status


from project.infrastructure.postgres.repository.product_repo import ProductRepository
from project.infrastructure.postgres.repository.supplier_repo import SupplierRepository
from project.infrastructure.postgres.repository.delivery_repo import DeliveryRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.client import ClientSchema, ClientCreateUpdateSchema
from project.schemas.product import ProductSchema, ProductCreateUpdateSchema
from project.schemas.supplier import SupplierSchema, SupplierCreateUpdateSchema
from project.schemas.delivery import DeliverySchema, DeliveryCreateUpdateSchema
from project.schemas.deliveryitem import DeliveryItemSchema, DeliveryItemCreateUpdateSchema
from project.schemas.recipe import RecipeSchema, RecipeCreateUpdateSchema
from project.schemas.dish import DishSchema, DishCreateUpdateSchema
from project.schemas.menu import MenuSchema, MenuCreateUpdateSchema
from project.schemas.dishingredient import DishIngredientSchema, DishIngredientCreateUpdateSchema
from project.schemas.tablereservation import TableReservationSchema, TableReservationCreateUpdateSchema
from project.schemas.discountcard import DiscountCardSchema, DiscountCardCreateUpdateSchema
from project.schemas.employee import EmployeeSchema, EmployeeCreateUpdateSchema
from project.schemas.order import OrderSchema, OrderCreateUpdateSchema
from project.schemas.user import UserSchema, UserCreateUpdateSchema
from project.schemas.healthcheck import HealthCheckSchema
from project.core.exceptions import (UserNotFound, UserAlreadyExists, ClientNotFound, ClientAlreadyExists,
                                     ProductNotFound, ProductAlreadyExists, SupplierNotFound, SupplierAlreadyExists,
                                     DeliveryNotFound, DeliveryAlreadyExists, DeliveryItemNotFound, DeliveryItemAlreadyExists,
                                     RecipeNotFound, RecipeAlreadyExists, DishNotFound, DishAlreadyExists, MenuNotFound, MenuAlreadyExists,
                                     DishIngredientNotFound, DishIngredientAlreadyExists,
                                     TableReservationNotFound, TableReservationAlreadyExists,
                                     DiscountCardNotFound, DiscountCardAlreadyExists,
                                     OrderNotFound, OrderAlreadyExists, EmployeeNotFound, EmployeeAlreadyExists)
from project.api.depends import (database, user_repo, client_repo, product_repo, supplier_repo, delivery_repo, deliveryitem_repo,
                                 recipe_repo, dish_repo, menu_repo, dishingredient_repo, tablereservation_repo,
                                 discountcard_repo, order_repo, employee_repo)


router = APIRouter()

@router.get("/healthcheck", response_model=HealthCheckSchema, status_code=status.HTTP_200_OK)
async def check_health() -> HealthCheckSchema:
    async with database.session() as session:
        db_is_ok = await user_repo.check_connection(session=session)
        client_db_is_ok = await client_repo.check_connection(session=session)
        product_db_is_ok = await product_repo.check_connection(session=session)
        supplier_db_is_ok = await supplier_repo.check_connection(session=session)
        deliveries_db_is_ok = await delivery_repo.check_connection(session=session)
        delivery_items_db_is_ok = await deliveryitem_repo.check_connection(session=session)
        recipes_db_is_ok = await recipe_repo.check_connection(session=session)
        dishes_db_is_ok = await dish_repo.check_connection(session=session)
        menu_db_is_ok = await menu_repo.check_connection(session=session)
        dishingredient_db_is_ok = await dishingredient_repo.check_connection(session=session)
        tablereservation_db_is_ok = await tablereservation_repo.check_connection(session=session)
        discountcard_db_is_ok = await discountcard_repo.check_connection(session=session)
        order_db_is_ok = await order_repo.check_connection(session=session)
        employee_db_is_ok = await employee_repo.check_connection(session=session)

    return HealthCheckSchema(
        db_is_ok=db_is_ok,
        client_db_is_ok=client_db_is_ok,
        product_db_is_ok=product_db_is_ok,
        supplier_db_is_ok=supplier_db_is_ok,
        deliveries_db_is_ok=deliveries_db_is_ok,
        delivery_items_db_is_ok=delivery_items_db_is_ok,
        recipes_db_is_ok=recipes_db_is_ok,
        dishes_db_is_ok=dishes_db_is_ok,
        menu_db_is_ok=menu_db_is_ok,
        dishingredient_db_is_ok=dishingredient_db_is_ok,
        tablereservation_db_is_ok=tablereservation_db_is_ok,
        discountcard_db_is_ok=discountcard_db_is_ok,
        order_db_is_ok=order_db_is_ok,
        employee_db_is_ok=employee_db_is_ok
    )

@router.get("/all_users", response_model=list[UserSchema], status_code=status.HTTP_200_OK)
async def get_all_users() -> list[UserSchema]:
    async with database.session() as session:
        all_users = await user_repo.get_all_users(session=session)

    return all_users

@router.get("/user/{user_id}", response_model=UserSchema, status_code=status.HTTP_200_OK)
async def get_user_by_id(
    user_id: int,
) -> UserSchema:
    try:
        async with database.session() as session:
            user = await user_repo.get_user_by_id(session=session, user_id=user_id)
    except UserNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return user


@router.post("/add_user", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def add_user(
    user_dto: UserCreateUpdateSchema,
) -> UserSchema:
    try:
        async with database.session() as session:
            new_user = await user_repo.create_user(session=session, user=user_dto)
    except UserAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_user


@router.put(
    "/update_user/{user_id}",
    response_model=UserSchema,
    status_code=status.HTTP_200_OK,
)
async def update_user(
    user_id: int,
    user_dto: UserCreateUpdateSchema,
) -> UserSchema:
    try:
        async with database.session() as session:
            updated_user = await user_repo.update_user(
                session=session,
                user_id=user_id,
                user=user_dto,
            )
    except UserNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_user


@router.delete("/delete_user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
) -> None:
    try:
        async with database.session() as session:
            user = await user_repo.delete_user(session=session, user_id=user_id)
    except UserNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return user

@router.get("/all_clients", response_model=list[ClientSchema], status_code=status.HTTP_200_OK)
async def get_all_clients() -> list[ClientSchema]:
    async with database.session() as session:
        all_clients = await client_repo.get_all_clients(session=session)
    return all_clients

@router.get("/client/{client_id}", response_model=ClientSchema, status_code=status.HTTP_200_OK)
async def get_client_by_id(client_id: int) -> ClientSchema:
    try:
        async with database.session() as session:
            client = await client_repo.get_client_by_id(session=session, client_id=client_id)
    except ClientNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
    return client

@router.post("/add_client", response_model=ClientSchema, status_code=status.HTTP_201_CREATED)
async def add_client(client_dto: ClientCreateUpdateSchema) -> ClientSchema:
    try:
        async with database.session() as session:
            new_client = await client_repo.create_client(session=session, client=client_dto)
    except ClientAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)
    return new_client

@router.put("/update_client/{client_id}", response_model=ClientSchema, status_code=status.HTTP_200_OK)
async def update_client(client_id: int, client_dto: ClientCreateUpdateSchema) -> ClientSchema:
    try:
        async with database.session() as session:
            updated_client = await client_repo.update_client(session=session, client_id=client_id, client=client_dto)
    except ClientNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
    return updated_client


@router.delete("/delete_client/{client_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_client(
        client_id: int,
) -> None:
    try:
        async with database.session() as session:
            client = await client_repo.delete_client(session=session, client_id=client_id)
    except ClientNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return client

@router.get("/all_products", response_model=list[ProductSchema], status_code=status.HTTP_200_OK)
async def get_all_products() -> list[ProductSchema]:
    async with database.session() as session:
        all_products = await product_repo.get_all_products(session=session)
    return all_products

@router.get("/product/{product_id}", response_model=ProductSchema, status_code=status.HTTP_200_OK)
async def get_product_by_id(product_id: int) -> ProductSchema:
    product_repo = ProductRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            product = await product_repo.get_product_by_id(session=session, product_id=product_id)
    except ProductNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return product

@router.post("/add_product", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
async def add_product(product_dto: ProductCreateUpdateSchema) -> ProductSchema:
    product_repo = ProductRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            new_product = await product_repo.create_product(session=session, product=product_dto)
    except ProductAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_product


@router.put("/update_product/{product_id}", response_model=ProductSchema, status_code=status.HTTP_200_OK)
async def update_product(product_id: int, product_dto: ProductCreateUpdateSchema) -> ProductSchema:
    product_repo = ProductRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            updated_product = await product_repo.update_product(
                session=session,
                product_id=product_id,
                product=product_dto,
            )
    except ProductNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_product

@router.delete("/delete_product/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: int,
) -> None:
    product_repo = ProductRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            product = await product_repo.delete_product(session=session, product_id=product_id)
    except ProductNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return product

@router.get("/all_suppliers", response_model=list[SupplierSchema], status_code=status.HTTP_200_OK)
async def get_all_suppliers() -> list[SupplierSchema]:
    async with database.session() as session:
        all_suppliers = await supplier_repo.get_all_suppliers(session=session)
    return all_suppliers

@router.get("/supplier/{supplier_id}", response_model=SupplierSchema, status_code=status.HTTP_200_OK)
async def get_supplier_by_id(supplier_id: int) -> SupplierSchema:
    supplier_repo = SupplierRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            supplier = await supplier_repo.get_supplier_by_id(session=session, supplier_id=supplier_id)
    except SupplierNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return supplier


@router.post("/add_supplier", response_model=SupplierSchema, status_code=status.HTTP_201_CREATED)
async def add_supplier(supplier_dto: SupplierSchema) -> SupplierSchema:
    supplier_repo = SupplierRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            new_supplier = await supplier_repo.create_supplier(session=session, supplier=supplier_dto)
    except SupplierAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_supplier


@router.put(
    "/update_supplier/{supplier_id}",
    response_model=SupplierSchema,
    status_code=status.HTTP_200_OK,
)
async def update_supplier(
    supplier_id: int,
    supplier_dto: SupplierCreateUpdateSchema,
) -> SupplierSchema:
    supplier_repo = SupplierRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            updated_supplier = await supplier_repo.update_supplier(
                session=session,
                supplier_id=supplier_id,
                supplier=supplier_dto,
            )
    except SupplierNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_supplier


@router.delete("/delete_supplier/{supplier_id}", status_code=status.HTTP_200_OK)
async def delete_supplier(
    supplier_id: int,
) -> SupplierSchema:
    supplier_repo = SupplierRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            supplier = await supplier_repo.delete_supplier(session=session, supplier_id=supplier_id)
    except SupplierNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return supplier


@router.get("/all_deliveries", response_model=list[DeliverySchema], status_code=status.HTTP_200_OK)
async def get_all_deliveries() -> list[DeliverySchema]:
    async with database.session() as session:
        all_deliveries = await delivery_repo.get_all_deliveries(session=session)

    return all_deliveries

@router.get("/delivery/{delivery_id}", response_model=DeliverySchema, status_code=status.HTTP_200_OK)
async def get_delivery_by_id(delivery_id: int) -> DeliverySchema:
    delivery_repo = DeliveryRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            delivery = await delivery_repo.get_delivery_by_id(session=session, delivery_id=delivery_id)
    except DeliveryNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return delivery

@router.post("/add_delivery", response_model=DeliverySchema, status_code=status.HTTP_201_CREATED)
async def add_delivery(delivery_dto: DeliveryCreateUpdateSchema) -> DeliverySchema:
    delivery_repo = DeliveryRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            new_delivery = await delivery_repo.create_delivery(session=session, delivery=delivery_dto)
    except DeliveryAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_delivery

@router.put("/update_delivery/{delivery_id}", response_model=DeliverySchema, status_code=status.HTTP_200_OK)
async def update_delivery(
    delivery_id: int,
    delivery_dto: DeliveryCreateUpdateSchema
) -> DeliverySchema:
    delivery_repo = DeliveryRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            updated_delivery = await delivery_repo.update_delivery(
                session=session,
                delivery_id=delivery_id,
                delivery=delivery_dto
            )
    except DeliveryNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_delivery

@router.delete("/delete_delivery/{delivery_id}", status_code=status.HTTP_200_OK)
async def delete_delivery(
    delivery_id: int,
) -> DeliverySchema:
    delivery_repo = DeliveryRepository()
    database = PostgresDatabase()

    try:
        async with database.session() as session:
            delivery = await delivery_repo.delete_delivery(session=session, delivery_id=delivery_id)
    except DeliveryNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return delivery

@router.get("/all_delivery_items", response_model=list[DeliveryItemSchema], status_code=status.HTTP_200_OK)
async def get_all_delivery_items() -> list[DeliveryItemSchema]:
    async with database.session() as session:
        all_delivery_items = await deliveryitem_repo.get_all_delivery_items(session=session)
    return all_delivery_items

@router.get("/delivery_item/{item_id}", response_model=DeliveryItemSchema, status_code=status.HTTP_200_OK)
async def get_delivery_item_by_id(item_id: int) -> DeliveryItemSchema:
    try:
        async with database.session() as session:
            delivery_item = await deliveryitem_repo.get_delivery_item_by_id(session=session, item_id=item_id)
    except DeliveryItemNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return delivery_item

@router.post("/add_delivery_item", response_model=DeliveryItemSchema, status_code=status.HTTP_201_CREATED)
async def add_delivery_item(
    delivery_item_dto: DeliveryItemCreateUpdateSchema,
) -> DeliveryItemSchema:
    try:
        async with database.session() as session:
            new_delivery_item = await deliveryitem_repo.create_delivery_item(session=session, delivery_item=delivery_item_dto)
    except DeliveryItemAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_delivery_item

@router.put("/update_delivery_item/{item_id}", response_model=DeliveryItemSchema, status_code=status.HTTP_200_OK)
async def update_delivery_item(
    item_id: int,
    delivery_item_dto: DeliveryItemCreateUpdateSchema,
) -> DeliveryItemSchema:
    try:
        async with database.session() as session:
            updated_delivery_item = await deliveryitem_repo.update_delivery_item(
                session=session,
                item_id=item_id,
                delivery_item=delivery_item_dto,
            )
    except DeliveryItemNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_delivery_item

@router.delete("/delete_delivery_item/{item_id}", status_code=status.HTTP_200_OK)
async def delete_delivery_item(
    item_id: int,
) -> DeliveryItemSchema:
    try:
        async with database.session() as session:
            delivery_item = await deliveryitem_repo.delete_delivery_item(session=session, item_id=item_id)
    except DeliveryItemNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return delivery_item

@router.get("/all_recipes", response_model=list[RecipeSchema], status_code=status.HTTP_200_OK)
async def get_all_recipes() -> list[RecipeSchema]:
    async with database.session() as session:
        all_recipes = await recipe_repo.get_all_recipes(session=session)

    return all_recipes


@router.get("/recipe/{recipe_id}", response_model=RecipeSchema, status_code=status.HTTP_200_OK)
async def get_recipe_by_id(
    recipe_id: int,
) -> RecipeSchema:
    try:
        async with database.session() as session:
            recipe = await recipe_repo.get_recipe_by_id(session=session, recipe_id=recipe_id)
    except RecipeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return recipe


@router.post("/add_recipe", response_model=RecipeSchema, status_code=status.HTTP_201_CREATED)
async def add_recipe(
    recipe_dto: RecipeCreateUpdateSchema,
) -> RecipeSchema:
    try:
        async with database.session() as session:
            new_recipe = await recipe_repo.create_recipe(session=session, recipe=recipe_dto)
    except RecipeAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_recipe

@router.put(
    "/update_recipe/{recipe_id}",
    response_model=RecipeSchema,
    status_code=status.HTTP_200_OK,
)
async def update_recipe(
    recipe_id: int,
    recipe_dto: RecipeCreateUpdateSchema,
) -> RecipeSchema:
    try:
        async with database.session() as session:
            updated_recipe = await recipe_repo.update_recipe(
                session=session,
                recipe_id=recipe_id,
                recipe=recipe_dto,
            )
    except RecipeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_recipe


@router.delete("/delete_recipe/{recipe_id}", status_code=status.HTTP_200_OK)
async def delete_recipe(
    recipe_id: int,
) -> RecipeSchema:
    try:
        async with database.session() as session:
            recipe = await recipe_repo.delete_recipe(session=session, recipe_id=recipe_id)
    except RecipeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return recipe

@router.get("/all_dishes", response_model=list[DishSchema], status_code=status.HTTP_200_OK)
async def get_all_dishes() -> list[DishSchema]:
    async with database.session() as session:
        all_dishes = await dish_repo.get_all_dishes(session=session)

    return all_dishes

@router.get("/dish/{dish_id}", response_model=DishSchema, status_code=status.HTTP_200_OK)
async def get_dish_by_id(
    dish_id: int,
) -> DishSchema:
    try:
        async with database.session() as session:
            dish = await dish_repo.get_dish_by_id(session=session, dish_id=dish_id)
    except DishNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return dish

@router.post("/add_dish", response_model=DishSchema, status_code=status.HTTP_201_CREATED)
async def add_dish(
    dish_dto: DishCreateUpdateSchema,
) -> DishSchema:
    try:
        async with database.session() as session:
            new_dish = await dish_repo.create_dish(session=session, dish=dish_dto)
    except DishAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_dish

@router.put(
    "/update_dish/{dish_id}",
    response_model=DishSchema,
    status_code=status.HTTP_200_OK,
)
async def update_dish(
    dish_id: int,
    dish_dto: DishCreateUpdateSchema,
) -> DishSchema:
    try:
        async with database.session() as session:
            updated_dish = await dish_repo.update_dish(
                session=session,
                dish_id=dish_id,
                dish=dish_dto,
            )
    except DishNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_dish

@router.delete("/delete_dish/{dish_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dish(
    dish_id: int,
) -> None:
    try:
        async with database.session() as session:
            dish = await dish_repo.delete_dish(session=session, dish_id=dish_id)
    except DishNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return dish

@router.get("/all_menus", response_model=list[MenuSchema], status_code=status.HTTP_200_OK)
async def get_all_menus() -> list[MenuSchema]:
    async with database.session() as session:
        all_menus = await menu_repo.get_all_menus(session=session)

    return all_menus

@router.get("/menu/{menu_id}", response_model=MenuSchema, status_code=status.HTTP_200_OK)
async def get_menu_by_id(
    menu_id: int,
) -> MenuSchema:
    try:
        async with database.session() as session:
            menu = await menu_repo.get_menu_by_id(session=session, menu_id=menu_id)
    except MenuNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return menu


@router.post("/add_menu", response_model=MenuSchema, status_code=status.HTTP_201_CREATED)
async def add_menu(
    menu_dto: MenuCreateUpdateSchema,
) -> MenuSchema:
    try:
        async with database.session() as session:
            new_menu = await menu_repo.create_menu(session=session, menu=menu_dto)
    except MenuAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_menu


@router.put(
    "/update_menu/{menu_id}",
    response_model=MenuSchema,
    status_code=status.HTTP_200_OK,
)
async def update_menu(
    menu_id: int,
    menu_dto: MenuCreateUpdateSchema,
) -> MenuSchema:
    try:
        async with database.session() as session:
            updated_menu = await menu_repo.update_menu(
                session=session,
                menu_id=menu_id,
                menu=menu_dto,
            )
    except MenuNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_menu

@router.delete("/delete_menu/{menu_id}", status_code=status.HTTP_200_OK)
async def delete_menu(
    menu_id: int,
) -> None:
    try:
        async with database.session() as session:
            menu = await menu_repo.delete_menu(session=session, menu_id=menu_id)
    except MenuNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return menu

@router.get("/all_dish_ingredients", response_model=list[DishIngredientSchema], status_code=status.HTTP_200_OK)
async def get_all_dish_ingredients() -> list[DishIngredientSchema]:
    async with database.session() as session:
        all_dish_ingredients = await dishingredient_repo.get_all_dish_ingredients(session=session)

    return all_dish_ingredients


@router.get("/dish_ingredient/{ingredient_id}", response_model=DishIngredientSchema, status_code=status.HTTP_200_OK)
async def get_dish_ingredient_by_id(
    ingredient_id: int,
) -> DishIngredientSchema:
    try:
        async with database.session() as session:
            dish_ingredient = await dishingredient_repo.get_dish_ingredient_by_id(session=session, ingredient_id=ingredient_id)
    except DishIngredientNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return dish_ingredient


@router.post("/add_dish_ingredient", response_model=DishIngredientSchema, status_code=status.HTTP_201_CREATED)
async def add_dish_ingredient(
    dish_ingredient_dto: DishIngredientCreateUpdateSchema,
) -> DishIngredientSchema:
    try:
        async with database.session() as session:
            new_dish_ingredient = await dishingredient_repo.create_dish_ingredient(session=session, dish_ingredient=dish_ingredient_dto)
    except DishIngredientAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_dish_ingredient


@router.put("/update_dish_ingredient/{ingredient_id}", response_model=DishIngredientSchema, status_code=status.HTTP_200_OK)
async def update_dish_ingredient(
    ingredient_id: int,
    dish_ingredient_dto: DishIngredientCreateUpdateSchema,
) -> DishIngredientSchema:
    try:
        async with database.session() as session:
            updated_dish_ingredient = await dishingredient_repo.update_dish_ingredient(
                session=session,
                ingredient_id=ingredient_id,
                dish_ingredient=dish_ingredient_dto,
            )
    except DishIngredientNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_dish_ingredient


@router.delete("/delete_dish_ingredient/{ingredient_id}", status_code=status.HTTP_200_OK)
async def delete_dish_ingredient(
    ingredient_id: int,
) -> DishIngredientSchema:
    try:
        async with database.session() as session:
            dish_ingredient = await dishingredient_repo.delete_dish_ingredient(session=session, ingredient_id=ingredient_id)
    except DishIngredientNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return dish_ingredient

@router.get("/all_reservations", response_model=list[TableReservationSchema], status_code=status.HTTP_200_OK)
async def get_all_reservations() -> list[TableReservationSchema]:
    async with database.session() as session:
        all_reservations = await tablereservation_repo.get_all_reservations(session=session)
    return all_reservations

@router.get("/reservation/{reservation_id}", response_model=TableReservationSchema, status_code=status.HTTP_200_OK)
async def get_reservation_by_id(reservation_id: int) -> TableReservationSchema:
    try:
        async with database.session() as session:
            reservation = await tablereservation_repo.get_reservation_by_id(session=session, reservation_id=reservation_id)
    except TableReservationNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
    return reservation

@router.post("/add_reservation", response_model=TableReservationSchema, status_code=status.HTTP_201_CREATED)
async def add_reservation(
    reservation_dto: TableReservationCreateUpdateSchema,
) -> TableReservationSchema:
    try:
        async with database.session() as session:
            new_reservation = await tablereservation_repo.create_reservation(session=session, reservation_dto=reservation_dto)
    except TableReservationAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)
    return new_reservation


@router.put("/update_reservation/{reservation_id}", response_model=TableReservationSchema, status_code=status.HTTP_200_OK)
async def update_reservation(
    reservation_id: int,
    reservation_dto: TableReservationCreateUpdateSchema,
) -> TableReservationSchema:
    try:
        async with database.session() as session:
            updated_reservation = await tablereservation_repo.update_reservation(
                session=session, reservation_id=reservation_id, reservation_dto=reservation_dto
            )
    except TableReservationNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)
    return updated_reservation


@router.delete("/delete_reservation/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_reservation(reservation_id: int) -> None:
    try:
        async with database.session() as session:
            reservation = await tablereservation_repo.delete_reservation(session=session, reservation_id=reservation_id)
    except TableReservationNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return reservation

@router.get("/all_discount_cards", response_model=list[DiscountCardSchema], status_code=status.HTTP_200_OK)
async def get_all_discount_cards() -> list[DiscountCardSchema]:
    async with database.session() as session:
        all_discount_cards = await discountcard_repo.get_all_discount_cards(session=session)

    return all_discount_cards

@router.get("/discount_card/{discount_id}", response_model=DiscountCardSchema, status_code=status.HTTP_200_OK)
async def get_discount_card_by_id(
    discount_id: int,
) -> DiscountCardSchema:
    try:
        async with database.session() as session:
            discount_card = await discountcard_repo.get_discount_card_by_id(session=session, discount_id=discount_id)
    except DiscountCardNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return discount_card

@router.post("/add_discount_card", response_model=DiscountCardSchema, status_code=status.HTTP_201_CREATED)
async def add_discount_card(
    discount_card_dto: DiscountCardCreateUpdateSchema,
) -> DiscountCardSchema:
    try:
        async with database.session() as session:
            new_discount_card = await discountcard_repo.create_discount_card(session=session, discount_card=discount_card_dto)
    except DiscountCardAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_discount_card

@router.put(
    "/update_discount_card/{discount_id}",
    response_model=DiscountCardSchema,
    status_code=status.HTTP_200_OK,
)
async def update_discount_card(
    discount_id: int,
    discount_card_dto: DiscountCardCreateUpdateSchema,
) -> DiscountCardSchema:
    try:
        async with database.session() as session:
            updated_discount_card = await discountcard_repo.update_discount_card(
                session=session,
                discount_id=discount_id,
                discount_card=discount_card_dto,
            )
    except DiscountCardNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_discount_card

@router.delete("/delete_discount_card/{discount_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_discount_card(
    discount_id: int,
) -> None:
    try:
        async with database.session() as session:
            discount_card = await discountcard_repo.delete_discount_card(session=session, discount_id=discount_id)
    except DiscountCardNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return discount_card

@router.get("/all_orders", response_model=list[OrderSchema], status_code=status.HTTP_200_OK)
async def get_all_orders() -> list[OrderSchema]:
    async with database.session() as session:
        all_orders = await order_repo.get_all_orders(session=session)

    return all_orders


@router.get("/order/{order_id}", response_model=OrderSchema, status_code=status.HTTP_200_OK)
async def get_order_by_id(order_id: int) -> OrderSchema:
    try:
        async with database.session() as session:
            order = await order_repo.get_order_by_id(session=session, order_id=order_id)
    except OrderNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return order


@router.post("/add_order", response_model=OrderSchema, status_code=status.HTTP_201_CREATED)
async def add_order(order_dto: OrderCreateUpdateSchema) -> OrderSchema:
    try:
        async with database.session() as session:
            new_order = await order_repo.create_order(session=session, order=order_dto)
    except OrderAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error.message)

    return new_order


@router.put("/update_order/{order_id}", response_model=OrderSchema, status_code=status.HTTP_200_OK)
async def update_order(
    order_id: int,
    order_dto: OrderCreateUpdateSchema
) -> OrderSchema:
    try:
        async with database.session() as session:
            updated_order = await order_repo.update_order(session=session, order_id=order_id, order=order_dto)
    except OrderNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_order

@router.delete("/delete_order/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_order(order_id: int) -> None:
    try:
        async with database.session() as session:
            order = await order_repo.delete_order(session=session, order_id=order_id)
    except OrderNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return order

@router.get("/all_employees", response_model=list[EmployeeSchema], status_code=status.HTTP_200_OK)
async def get_all_employees() -> list[EmployeeSchema]:
    async with database.session() as session:
        all_employees = await employee_repo.get_all_employees(session=session)

    return all_employees

@router.get("/employee/{employee_id}", response_model=EmployeeSchema, status_code=status.HTTP_200_OK)
async def get_employee_by_id(employee_id: int) -> EmployeeSchema:
    try:
        async with database.session() as session:
            employee = await employee_repo.get_employee_by_id(session=session, employee_id=employee_id)
    except EmployeeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return employee

@router.post("/add_employee", response_model=EmployeeSchema, status_code=status.HTTP_201_CREATED)
async def add_employee(employee_dto: EmployeeCreateUpdateSchema) -> EmployeeSchema:
    try:
        async with database.session() as session:
            new_employee = await employee_repo.create_employee(session=session, employee=employee_dto)
    except EmployeeAlreadyExists as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=error.message)

    return new_employee

@router.put("/update_employee/{employee_id}", response_model=EmployeeSchema, status_code=status.HTTP_200_OK)
async def update_employee(employee_id: int, employee_dto: EmployeeCreateUpdateSchema) -> EmployeeSchema:
    try:
        async with database.session() as session:
            updated_employee = await employee_repo.update_employee(
                session=session,
                employee_id=employee_id,
                employee=employee_dto,
            )
    except EmployeeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return updated_employee

@router.delete("/delete_employee/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_employee(employee_id: int) -> None:
    try:
        async with database.session() as session:
            employee = await employee_repo.delete_employee(session=session, employee_id=employee_id)
    except EmployeeNotFound as error:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error.message)

    return employee