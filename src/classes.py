class Product:
    """Создание класса product"""

    def __str__(self):
        """строковое представление объекта"""
        return f"{self.name}, {self.price} руб. Количество: {self.quantity}"

    def __init__(self, name, description, price, quantity):
        """инициализация"""
        self.name = name
        self.description = description
        self._price = 0
        self._quantity = 0
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print(f'Цена не может быть отрицательной или нулевой: {value}, прежнее значение:')
        else:
            self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            print(f'Количество не может быть отрицательным: {value}, прежнее значение:')
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


class Category:
    """Создание класса category"""
    category_count = 0
    product_count = 0

    def __str__(self):
        """строковое представление объекта"""
        return f"{self.name}, количество продуктов: {len(self.__products)}"

    def __init__(self, name, description, products=None):
        """инициализация"""
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        """Метод для добавления продукта в категорию"""
        if not isinstance(product, Product):
            raise ValueError("Можно добавить только корректный продукт")
        if product not in self.__products:
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Продукт находится в категории")

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
        return "\n".join([f"{product.name}, {product.price} руб. Количество: {product.quantity} шт." for product
                          in self.__products])
