"""
Pytest Fixtures Configuration
WHAT IS conftest.py?
- Special pytest file
- Fixtures defined here available to ALL tests
- No need to import
"""
import sys
from pathlib import Path
from config.locales import get_all_locales,get_locale_config

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



# ============ LOCALE FIXTURES ============

@pytest.fixture
def locale(request):
    """
    FIXTURE: Provides locale code
    
    Can be parameterized:
    @pytest.mark.parametrize("locale", ["en-US", "fr-FR"])
    """
    return request.param if hasattr(request, 'param') else "en-US"

@pytest.fixture
def locale_config(locale):
    """
    FIXTURE: Provides complete locale configuration
    
    RETURNS:
    {
        "locale": "en-US",
        "timezone": "America/New_York",
        "currency": "USD",
        ...
    }
    """
    return get_locale_config(locale)

@pytest.fixture(scope="session")
def browser_context_args_with_locale(browser_context_args, request):
    """
    FIXTURE: Configure browser context with locale
    
    USAGE: Run tests with specific locale
    pytest --locale=fr-FR
    """
    locale = request.config.getoption("--locale", default="en-US")
    config = get_locale_config(locale)
    
    return {
        **browser_context_args,
        "locale": config["locale"],
        "timezone_id": config["timezone"],
        "viewport": {"width": 1920, "height": 1080}
    }

# ============ COMMAND LINE OPTIONS ============

def pytest_addoption(parser):
    """
    Add custom command line options
    
    USAGE:
    pytest --locale=fr-FR
    pytest --browser=firefox
    """
    parser.addoption(
        "--locale",
        action="store",
        default="en-US",
        help="Locale for testing (e.g., en-US, fr-FR)"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        help="Browser to use (chromium, firefox, webkit)"
    )

# ============ RTL (Right-to-Left) FIXTURE ============

@pytest.fixture
def is_rtl(locale_config):
    """
    FIXTURE: Check if locale uses RTL layout
    
    USAGE:
    def test_layout(is_rtl):
        if is_rtl:
            # Test RTL-specific behavior
    """
    return locale_config.get("rtl", False)