"""
Homepage Tests
Covers: Homepage functionality
"""
import pytest
from pages.home_page import HomePage

@pytest.fixture
def home_page(page):
    return HomePage(page)

def test_homepage_loads(home_page):
    """
    TEST 9: Verify homepage loads correctly
    """
    home_page.navigate_to_home()
    assert home_page.is_home_page_loaded()
    assert "Automation Exercise" in home_page.get_page_title()

def test_homepage_navigation_links(home_page):
    """
    TEST 10: Verify all main navigation links are visible
    """
    home_page.navigate_to_home()
    
    # Verify key links visible
    assert home_page.products_link.is_visible()
    assert home_page.login_link.is_visible()
    
    print("✅ All navigation links visible")