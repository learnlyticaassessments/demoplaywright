"""
Shopping Cart Tests
Covers: Add to cart, Remove from cart, View cart
"""
import pytest
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.fixture
def products_page(page):
    return ProductsPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

def test_add_to_cart_and_verify(products_page, cart_page):
    """
    TEST 4: Add product and view in cart
    """
    # Add product and view cart
    products_page.navigate_to_products()
    products_page.add_product_and_view_cart(product_number=1)
    
    # Verify cart page
    cart_page.verify_cart_page_loaded()
    
    # Verify item in cart
    assert cart_page.get_cart_item_count() > 0

def test_remove_from_cart(products_page, cart_page):
    """
    TEST 5: Remove product from cart
    """
    # Add product
    products_page.navigate_to_products()
    products_page.add_product_and_view_cart(product_number=1)
    
    # Remove product
    cart_page.remove_product(product_id="1")
    
    # Verify cart is empty (wait for page update)
    cart_page.page.wait_for_timeout(1000)
    assert cart_page.get_cart_item_count() == 0