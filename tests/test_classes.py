import pytest
from src.main import Product, Category


def test_product_price_update():
    """Проверяет обновление цены продукта."""
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = 150.0
    assert product.price == 150.0


def test_product_quantity_update():
    """Проверяет обновление количества продукта."""
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.quantity = 15
    assert product.quantity == 15


def test_product_update_attributes():
    """Проверяет изменение продукта"""
    product = Product("Test Product", "Old Description", 100.0, 10)
    product.name = "Updated Product"
    product.description = "New Description"
    product.price = 150.0
    product.quantity = 15
    assert product.name == "Updated Product"
    assert product.description == "New Description"
    assert product.price == 150.0
    assert product.quantity == 15


@pytest.fixture
def reset_category_counts():
    """Сбрасывает статические счетчики Category перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_product():
    """Создает тестовый продукт."""
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_category(sample_product):
    """Создает тестовую категорию."""
    return Category("Test Category", "Test Category Description", [sample_product])


def test_product_initialization(sample_product):
    """Проверяет корректность инициализации объектов класса Product."""
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_product_str_representation(sample_product):
    """Проверяет корректность строкового значения"""
    assert str(sample_product) == "Test Product, 100.0 руб. Количество: 10"


def test_product_price_setter():
    """Проверяет корректность цены (если отрицательная или нулевая, возвращает прежнее значение)"""
    product = Product("Test", "Description", 100, 1)

    product.price = 200
    assert product.price == 200

    product.price = 0
    assert product.price == 200

    product.price = -50
    assert product.price == 200


def test_product_quantity_setter():
    """Проверяет корректность кол-ва, если отрицательное , возвращает прежнее значение)"""
    product = Product("Test", "Description", 100, 1)

    product.quantity = 5
    assert product.quantity == 5

    product.quantity = -1
    assert product.quantity == 5


def test_product_new_product_class_method():
    """Проверяет добавление нового продукта"""
    product_data = {
        "name": "New Product",
        "description": "New Description",
        "price": 150.0,
        "quantity": 7
    }
    new_product = Product.new_product(product_data)

    assert isinstance(new_product, Product)
    assert new_product.name == "New Product"
    assert new_product.description == "New Description"
    assert new_product.price == 150.0
    assert new_product.quantity == 7


def test_category_initialization(sample_category):
    """Проверяет корректность инициализации объектов класса Category."""
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Category Description"
    assert len(sample_category._Category__products) == 1


def test_category_str_representation(sample_category):
    """Проверяет корректность строкового значения"""
    assert str(sample_category) == "Test Category, количество продуктов: 1"


def test_category_add_product(sample_category, sample_product):
    """Проверяет подсчет нового продукта"""
    new_product = Product("New Product", "New Description", 200.0, 5)
    sample_category.add_product(new_product)

    assert len(sample_category._Category__products) == 2
    assert Category.product_count == 4


def test_category_add_duplicate_product(sample_category, sample_product):
    """Разделил на два теста: первый сверяет продукт"""
    with pytest.raises(ValueError, match="Продукт находится в категории"):
        sample_category.add_product(sample_product)


def test_category_add_invalid_product(sample_category):
    """Разделил на два теста: второй проверяет корректность продукта"""
    with pytest.raises(ValueError, match="Можно добавить только корректный продукт"):
        sample_category.add_product("Not a product")


def test_category_remove_nonexistent_product(sample_category):
    """Проверяет наличие продукта"""
    non_existent_product = Product("Non-existent", "Description", 100, 1)

    with pytest.raises(ValueError, match="Продукт не найден"):
        sample_category.remove_product(non_existent_product)


def test_category_products_property(sample_category, sample_product):
    """проверяет корректоность продукта"""
    expected_output = f"{sample_product.name}, {sample_product.price} руб. Количество: {sample_product.quantity} шт."
    assert sample_category.products == expected_output


def test_category_count():
    """проверяет посчет"""
    initial_count = Category.category_count
    Category("New Category", "Description")
    assert Category.category_count == initial_count + 1
