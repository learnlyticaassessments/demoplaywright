"""
Login Tests using Page Object Model
Demonstrates: How to use page objects in tests
"""
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_navigate_to_login_page(page):
    """
    TEST: Verify user can navigate to login page
    
    FIXTURES USED:
    - page: Playwright's page fixture
    
    PAGE OBJECTS USED:
    - HomePage
    - LoginPage
    """
    # ARRANGE: Create page objects
    home_page = HomePage(page)
    login_page = LoginPage(page)
    
    # ACT: Navigate to home, then login
    home_page.navigate_to_home()
    home_page.click_login()
    
    # ASSERT: Verify we're on login page
    login_page.verify_login_page_loaded()

def test_login_with_invalid_credentials(page):
    """
    TEST: Login with wrong credentials shows error
    
    DEMONSTRATES:
    - Page object methods
    - Negative testing
    """
    # ARRANGE
    login_page = LoginPage(page)
    
    # ACT
    login_page.navigate_to_login()
    login_page.perform_login("wrong@email.com", "wrongpassword")
    
    # ASSERT: Error message appears
    error = page.locator("text=Your email or password is incorrect")
    assert error.is_visible()
    print("✅ Error message displayed correctly")