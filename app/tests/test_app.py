from app import get_products


def test_get_products_returns_products():
    products = get_products()

    assert products is not None
    assert len(products) > 0
