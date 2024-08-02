import pytest
from src.main import Product, Category


@pytest.fixture
def reset_category_counts():
    """Сбрасывает статические счетчики Category перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_products():
    """Создает набор тестовых продуктов."""
    return [
        Product("Test Product 1", "Description 1", 100.0, 5),
        Product("Test Product 2", "Description 2", 200.0, 10),
        Product("Test Product 3", "Description 3", 300.0, 15),
    ]


def test_product_initialization():
    """Проверяет корректность инициализации объектов класса Product."""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization(reset_category_counts, sample_products):
    """Проверяет корректность инициализации объектов класса Category."""
    category = Category("Test Category", "Test Description", sample_products)
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.products == sample_products
    assert len(category.products) == 3


def test_product_count(reset_category_counts, sample_products):
    """Проверяет корректность подсчета количества продуктов."""
    Category("Test Category 1", "Description 1", sample_products[:2])
    assert Category.product_count == 2

    Category("Test Category 2", "Description 2", sample_products[2:])
    assert Category.product_count == 3


def test_category_count(reset_category_counts, sample_products):
    """Проверяет корректность подсчета количества категорий."""
    Category("Test Category 1", "Description 1", sample_products[:2])
    assert Category.category_count == 1

    Category("Test Category 2", "Description 2", sample_products[2:])
    assert Category.category_count == 2


def test_multiple_categories(reset_category_counts, sample_products):
    """Проверяет корректность подсчета при создании нескольких категорий."""
    Category("Test Category 1", "Description 1", sample_products[:1])
    Category("Test Category 2", "Description 2", sample_products[1:2])
    Category("Test Category 3", "Description 3", sample_products[2:])

    assert Category.category_count == 3
    assert Category.product_count == 3


def test_product_str_representation():
    """Проверяет корректность строкового значения"""
    product = Product("Test Product", "Test Description", 100.0, 10)
    expected_str = "Test Product, 100.0 руб. Количество: 10"
    assert str(product) == expected_str


def test_category_str_representation(sample_products):
    """Проверяет корректность строкового значения"""
    category = Category("Test Category", "Test Description", sample_products)
    expected_str = "Test Category, количество продуктов: 3"
    assert str(category) == expected_str


def test_category_add_product(reset_category_counts):
    """Проверяет создание нового продукта"""
    category = Category("Test Category", "Test Description", [])
    new_product = Product("New Product", "New Description", 150.0, 5)
    category.add_product(new_product)
    assert len(category.products) == 1
    assert category.products[0] == new_product


def test_category_remove_product(sample_products):
    """Проверяет новый продукт"""
    category = Category("Test Category", "Test Description", sample_products)
    initial_count = len(category.products)
    product_to_remove = category.products[0]
    category.remove_product(product_to_remove)
    assert len(category.products) == initial_count - 1
    assert product_to_remove not in category.products


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


def test_category_empty_products(reset_category_counts):
    """Проверяет создание категории без продуктов."""
    category = Category("Empty Category", "No products", [])
    assert len(category.products) == 0
    assert Category.product_count == 0


def test_category_description_update(sample_products):
    """Проверяет обновление описания категории."""
    category = Category("Test Category", "Old Description", sample_products)
    new_description = "New Description"
    category.description = new_description
    assert category.description == new_description


def test_multiple_categories_same_product(reset_category_counts):
    """Проверяет, что один и тот же продукт может быть в нескольких категориях."""
    product = Product("Shared Product", "In multiple categories", 100.0, 5)
    category1 = Category("Category 1", "Description 1", [product])
    category2 = Category("Category 2", "Description 2", [product])
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_category_add_invalid_product():
    """Проверяет на соответствие продукта"""
    category = Category("Test Category", "Test Description", [])
    with pytest.raises(ValueError):
        category.add_product("Not a Product")


def test_category_remove_nonexistent_product(sample_products):
    category = Category("Test Category", "Test Description", sample_products)
    non_existent_product = Product("Non-existent", "Does not exist", 1000.0, 1)
    with pytest.raises(ValueError):
        category.remove_product(non_existent_product)


def test_product_negative_values():
    """Проверяет корректность продукта (отрицательная цена/кол-во"""
    with pytest.raises(ValueError):
        Product("Invalid Product", "Invalid", -100.0, 10)
    with pytest.raises(ValueError):
        Product("Invalid Product", "Invalid", 100.0, -10)


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


def test_category_unique_products():
    """Тестирует, что при создании категории с дублирующимися продуктами
    все продукты сохраняются в списке (не удаляются дубликаты)"""
    product = Product("Unique Product", "Test", 100.0, 5)
    category = Category("Test Category", "Test Description", [product, product])
    assert len(category.products) == 2


def test_empty_category_operations():
    """Тестирует операции с пустой категорией товаров"""
    category = Category("Empty Category", "No products", [])
    assert len(category.products) == 0
    assert str(category) == "Empty Category, количество продуктов: 0"

    new_product = Product("New Product", "Test", 100.0, 5)
    category.add_product(new_product)
    assert len(category.products) == 1

    category.remove_product(new_product)
    assert len(category.products) == 0
