"""
Product Tests
Covers: Search, View, Add to Cart
"""
import pytest
from pages.products_page import ProductsPage
from pages.home_page import HomePage

@pytest.fixture
def products_page(page):
    return ProductsPage(page)

def test_view_all_products(home_page, products_page):
    """
    TEST 1: View all products
    """
    # Navigate from home
    home_page.navigate_to_home()
    home_page.click_products()
    
    # Verify products page
    products_page.verify_products_page_loaded()
    
    # Verify products are visible
    assert products_page.get_product_count() > 0

def test_search_product(products_page):
    """
    TEST 2: Search for specific product
    """
    # Navigate and search
    products_page.navigate_to_products()
    products_page.search_product("Blue Top")
    
    # Verify search results
    assert products_page.product_by_name("Blue Top").is_visible()

def test_add_product_to_cart(products_page):
    """
    TEST 3: Add product to cart
    """
    # Navigate to products
    products_page.navigate_to_products()
    
    # Add first product
    products_page.add_first_product_to_cart()
    
    # Verify (we stayed on products page)
    products_page.verify_products_page_loaded()