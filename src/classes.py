from abc import ABC, abstractmethod


class LoggingMixin:
    """ Миксин для логирования создания объектов"""
    def __init__(self, *args, **kwargs):
        """Инициализация"""
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {args}, {kwargs}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """Абстрактный базовый класс для продуктов"""
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        """Инициализация"""
        self.name = name
        self.description = description
        self._price = 0
        self._quantity = 0
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        """Строковое представление объекта"""
        pass

    @property
    @abstractmethod
    def price(self):
        """Геттер для цены продукта"""
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """Сеттер для цены продукта"""
        pass

    @property
    @abstractmethod
    def quantity(self):
        """Геттер для количества продукта"""
        pass

    @quantity.setter
    @abstractmethod
    def quantity(self, value):
        """Сеттер для количества продукта"""
        pass


class Product(LoggingMixin, BaseProduct):
    """Базовый класс для продуктов"""
    def __str__(self):
        """Строковое представление объекта"""
        return f"{self.name}, {self.price} руб. Количество: {self.quantity} шт."

    @property
    def price(self):
        """Геттер для цены продукта"""
        return self._price

    @price.setter
    def price(self, value):
        """ Сеттер для цены продукта"""
        if value <= 0:
            print(f'Цена не может быть отрицательной или нулевой: {value}, прежнее значение: {self._price}')
        else:
            self._price = value

    @property
    def quantity(self):
        """Геттер для количества продукта"""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """Сеттер для количества продукта"""
        if value < 0:
            print(f'Количество не может быть отрицательным: {value}, прежнее значение: {self._quantity}')
        else:
            self._quantity = value

    @classmethod
    def new_product(cls, product_data):
        """Класс-метод для создания нового продукта из словаря"""
        return cls(
            product_data['name'],
            product_data['description'],
            product_data['price'],
            product_data['quantity']
        )

    def __add__(self, other):
        """Метод для сложения продуктов"""
        if type(self) != type(other):
            raise TypeError("Можно складывать только объекты одинакового типа")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """Класс для смартфонов"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Инициализация"""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для травы"""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Инициализация"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс для категорий продуктов"""
    category_count = 0
    product_count = 0

    def __str__(self):
        """Строковое представление объекта"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __init__(self, name, description, products=None):
        """Инициализация"""
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        """Метод для добавления продукта в категорию"""
        if not isinstance(product, BaseProduct):
            raise TypeError("Можно добавить только корректный продукт")
        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Продукт уже находится в категории")

    def remove_product(self, product):
        """Метод для удаления продукта из категории"""
        if product in self.__products:
            self.__products.remove(product)
            Category.product_count -= 1
        else:
            raise ValueError("Продукт не найден")

    @property
    def products(self):
        """Геттер для получения списка продуктов в виде строки"""
        return "\n".join(str(product) for product in self.__products)
