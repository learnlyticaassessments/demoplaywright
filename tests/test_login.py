"""
Login/Signup Tests
Covers: Login scenarios, Signup scenarios
"""
import pytest
import time
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def home_page(page):
    return HomePage(page)

def test_navigate_to_login(home_page, login_page):
    """
    TEST 6: Navigate to login page
    """
    home_page.navigate_to_home()
    home_page.click_login()
    login_page.verify_login_page_loaded()

def test_login_with_invalid_email(login_page):
    """
    TEST 7: Login with invalid credentials
    """
    login_page.navigate_to_login()
    login_page.perform_login("invalid@test.com", "wrongpass")
    
    # Verify error
    error = login_page.page.locator("text=Your email or password is incorrect")
    assert error.is_visible()

def test_signup_page_accessible(home_page, login_page):
    """
    TEST 8: Verify signup form is accessible
    """
    home_page.navigate_to_home()
    home_page.click_login()
    
    # Verify signup form visible
    assert login_page.signup_button.is_visible()
    print("✅ Signup form accessible")