"""
Tests Demonstrating Fixture Usage
"""
import pytest

def test_using_base_url_fixture(page, base_url):
    """
    DEMONSTRATES: Using simple fixture
    
    FIXTURES:
    - page: Playwright page
    - base_url: Our custom fixture
    """
    page.goto(base_url)
    assert "Automation Exercise" in page.title()
    print(f"✅ Navigated using fixture URL: {base_url}")

def test_using_test_user_fixture(test_user):
    """
    DEMONSTRATES: Accessing fixture data
    
    FIXTURES:
    - test_user: Dictionary with user data
    """
    print(f"Test user email: {test_user['email']}")
    print(f"Test user name: {test_user['name']}")
    assert "@" in test_user["email"]

def test_using_page_object_fixture(home_page):
    """
    DEMONSTRATES: Page object fixture
    
    FIXTURES:
    - home_page: HomePage instance (auto-created)
    """
    home_page.navigate_to_home()
    assert home_page.is_home_page_loaded()
    print("✅ Used home_page fixture")

def test_using_setup_fixture(setup_home_page, home_page):
    """
    DEMONSTRATES: Setup fixture with automatic navigation
    
    FIXTURES:
    - setup_home_page: Navigates to home automatically
    - home_page: HomePage instance
    
    NOTE: We're already on home page when test starts!
    """
    # Already on home page due to setup_home_page fixture
    home_page.click_products()
    assert "products" in home_page.get_current_url()
    print("✅ Setup fixture handled navigation")

def test_combining_multiple_fixtures(login_page, test_user, base_url):
    """
    DEMONSTRATES: Using multiple fixtures together
    
    FIXTURES:
    - login_page: LoginPage instance
    - test_user: Test credentials
    - base_url: Base URL
    """
    login_page.navigate_to_login()
    login_page.perform_login(
        email=test_user["email"],
        password=test_user["password"]
    )
    print(f"✅ Logged in with fixtures: {test_user['email']} on {base_url}")