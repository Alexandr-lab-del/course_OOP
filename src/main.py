from src.classes import Product, Category


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(f'Стоимость всех Samsung Galaxy S23 Ultra и Iphone 15: {product1 + product2}')
    print(f'Стоимость всех Samsung Galaxy S23 Ultra и Xiaomi Redmi Note 11: {product1 + product3}')
    print(f'Стоимость всех Iphone 15 и Xiaomi Redmi Note 11: {product2 + product3}')
