"""
Pytest Fixtures Configuration
WHAT IS conftest.py?
- Special pytest file
- Fixtures defined here available to ALL tests
- No need to import
"""
import sys
from pathlib import Path


project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

# ============ BASIC FIXTURES ============

@pytest.fixture(scope="session")
def base_url():
    """
    FIXTURE: Provides base URL
    
    WHY?
    - Single place to change URL
    - Can be overridden for different environments
    
    USAGE in test:
    def test_something(base_url):
        print(base_url)  # https://www.automationexercise.com
    """
    return "https://www.automationexercise.com"

@pytest.fixture
def test_user():
    """
    FIXTURE: Provides test user credentials
    
    WHY?
    - Avoid hardcoding credentials in tests
    - Easy to manage test data
    
    USAGE:
    def test_login(test_user):
        email = test_user["email"]
        password = test_user["password"]
    """
    return {
        "email": "testuser@example.com",
        "password": "Test@123",
        "name": "Test User"
    }

# ============ PAGE OBJECT FIXTURES ============

@pytest.fixture
def home_page(page):
    """
    FIXTURE: Provides HomePage instance
    
    DEPENDENCY:
    - Needs 'page' fixture (from pytest-playwright)
    
    BENEFITS:
    - Tests don't create page objects
    - Consistent initialization
    
    USAGE:
    def test_home(home_page):
        home_page.navigate_to_home()
        home_page.click_products()
    """
    return HomePage(page)

@pytest.fixture
def login_page(page):
    """
    FIXTURE: Provides LoginPage instance
    
    USAGE:
    def test_login(login_page, test_user):
        login_page.navigate_to_login()
        login_page.perform_login(
            test_user["email"],
            test_user["password"]
        )
    """
    return LoginPage(page)

# ============ SETUP/TEARDOWN FIXTURES ============

@pytest.fixture(scope="function")
def setup_home_page(home_page):
    """
    FIXTURE: Automatically navigates to home page before test
    
    SCOPE: function (runs for each test)
    
    STRUCTURE:
    - Code before yield: SETUP (runs before test)
    - yield: Test runs here
    - Code after yield: TEARDOWN (runs after test)
    
    USAGE:
    def test_something(setup_home_page, home_page):
        # Already on home page!
        home_page.click_products()
    """
    # SETUP
    print("\n🔧 Setup: Navigating to home page")
    home_page.navigate_to_home()
    
    # Test runs here
    yield home_page
    
    # TEARDOWN
    print("🧹 Teardown: Test complete")

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    FIXTURE: Configure browser context
    
    SCOPE: session (runs once for entire test run)
    
    PURPOSE:
    - Set viewport size
    - Configure locale
    - Set timezone
    
    RETURNS:
    - Modified browser_context_args dictionary
    """
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080
        },
        "locale": "en-US",
        "timezone_id": "America/New_York"
    }