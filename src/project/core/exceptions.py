from typing import Final


class UserNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "User с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class UserAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Пользователь с почтой '{email}' уже существует"

    def __init__(self, email: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(email=email)
        super().__init__(self.message)


class ClientNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Client с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class ClientAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Клиент с почтой '{email}' уже существует"

    def __init__(self, email: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(email=email)
        super().__init__(self.message)


class ProductNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Продукт с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class ProductAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Продукт с названием '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class SupplierNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Поставщик с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class SupplierAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Поставщик с названием '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)


class DeliveryNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Поставка с id {id} не найдена"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class DeliveryAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Поставка с названием '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)

class DeliveryItemNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Товар с id {id} не найден в поставке"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class DeliveryItemAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Товар с id {item_id} уже существует в поставке с id {delivery_id}"

    def __init__(self, item_id: int, delivery_id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(item_id=item_id, delivery_id=delivery_id)
        super().__init__(self.message)

class RecipeNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Рецепт с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class RecipeAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Рецепт с dish_id {dish_id} и product_id {product_id} уже существует"

    def __init__(self, dish_id: int, product_id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(dish_id=dish_id, product_id=product_id)
        super().__init__(self.message)

class DishNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Блюдо с id {id} не найдено"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class DishAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Блюдо с названием '{dish_name}' уже существует"

    def __init__(self, dish_name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(dish_name=dish_name)
        super().__init__(self.message)

class MenuNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Меню с id {id} не найдено"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class MenuAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Меню с названием '{dish_name}' уже существует"

    def __init__(self, dish_name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(dish_name=dish_name)
        super().__init__(self.message)

class DishIngredientNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Ингредиент с id {id} не найден в рецепте"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class DishIngredientAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Ингредиент с recipe_id {recipe_id} и product_id {product_id} уже существует"

    def __init__(self, recipe_id: int, product_id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(recipe_id=recipe_id, product_id=product_id)
        super().__init__(self.message)

class TableReservationNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Резервирование с id {id} не найдено"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class TableReservationAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Резервирование с идентификатором '{reservation_id}' уже существует"

    def __init__(self, reservation_id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(reservation_id=reservation_id)
        super().__init__(self.message)

class DiscountCardNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Карта скидки с id {id} не найдена"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class DiscountCardAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Карта скидки с номером '{card_number}' уже существует"

    def __init__(self, card_number: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(card_number=card_number)
        super().__init__(self.message)

class OrderNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Заказ с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class OrderAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Заказ с номером {order_id} уже существует"

    def __init__(self, order_id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(order_id=order_id)
        super().__init__(self.message)

class EmployeeNotFound(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Сотрудник с id {id} не найден"
    message: str

    def __init__(self, _id: int) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(id=_id)
        super().__init__(self.message)

class EmployeeAlreadyExists(BaseException):
    _ERROR_MESSAGE_TEMPLATE: Final[str] = "Сотрудник с именем '{name}' уже существует"

    def __init__(self, name: str) -> None:
        self.message = self._ERROR_MESSAGE_TEMPLATE.format(name=name)
        super().__init__(self.message)
