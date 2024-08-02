class Product:
    """Создание класса product"""
    def __str__(self):
        """строковое представление объекта (нужно для теста)"""
        return f"{self.name}, {self.price} руб. Количество: {self.quantity}"

    def __init__(self, name, description, price, quantity):
        """инициализация"""
        self.name = name
        self.description = description
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.price = price
        self.quantity = quantity


class Category:
    """Создание класса category"""
    category_count = 0
    product_count = 0

    def __str__(self):
        """строковое представление объекта (нужно для теста)"""
        return f"{self.name}, количество продуктов: {len(self.products)}"

    def add_product(self, product):
        """функция для проверки продуктов (нужно для теста)"""
        if not isinstance(product, Product):
            raise ValueError("Can only add Product objects")
        if product not in self.products:
            self.products.append(product)
        else:
            raise ValueError("Product already exists in the category")

    def remove_product(self, product):
        """функция для определения продукта (нужно для теста)"""
        if product in self.products:
            self.products.remove(product)
        else:
            raise ValueError("Product not found in the category")

    def __init__(self, name, description, products=None):
        """инициализация"""
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(products)


if __name__ == "__main__":

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                         "функций для удобства жизни",
                         [product1, product2, product3])

    print(f"Название категории: {category1.name}")
    print(f"Описание категории: {category1.description}")
    print(f"Количество продуктов в категории: {len(category1.products)}")
    print()

    for product in [product1, product2, product3]:
        print(f"Название: {product.name}")
        print(f"Описание: {product.description}")
        print(f"Цена: {product.price}")
        print(f"Количество: {product.quantity}")
        print()
    # print(f"Общее количество категорий: {Category.category_count}")
    # print(f"Общее количество товаров: {Category.product_count}")

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, "
                         "станет вашим другом и помощником",
                         [product4])

    print(f"Название категории: {category2.name}")
    print(f"Описание категории: {category2.description}")
    print(f"Количество продуктов в категории: {len(category2.products)}")
    for product in [product4]:
        print()
        print(f"Название: {product.name}")
        print(f"Описание: {product.description}")
        print(f"Цена: {product.price}")
        print(f"Количество: {product.quantity}")
        print()

    print(f"Общее количество категорий: {Category.category_count}")
    print(f"Общее количество товаров: {Category.product_count}")
