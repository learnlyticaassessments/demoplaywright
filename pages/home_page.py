"""
Home Page Object
URL: https://www.automationexercise.com/
Contains: Locators and methods for home page interactions
"""
from pages.base_page import BasePage

class HomePage(BasePage):
    """
    INHERITANCE:
    - Inherits from BasePage
    - Gets navigate(), get_page_title() for free
    
    CONTAINS:
    - Locators specific to home page
    - Methods specific to home page actions
    """
    
    def __init__(self, page):
        """
        Call parent constructor
        """
        super().__init__(page)
    
    # ============ LOCATORS ============
    # WHY SEPARATE?: Easy to maintain, one place to update
    
    @property
    def products_link(self):
        """Products navigation link"""
        return self.page.get_by_role("link", name="Products")
    
    @property
    def login_link(self):
        """Login/Signup navigation link"""
        return self.page.locator("a[href='/login']")
    
    @property
    def home_slider(self):
        """Main carousel/slider on homepage"""
        return self.page.locator("#slider")
    
    # ============ ACTIONS ============
    
    def navigate_to_home(self):
        """Go to homepage"""
        self.navigate("/")
    
    def click_products(self):
        """Navigate to Products page"""
        self.products_link.click()
        print("🖱️ Clicked Products link")
    
    def click_login(self):
        """Navigate to Login page"""
        self.login_link.click()
        print("🖱️ Clicked Login link")
    
    def is_home_page_loaded(self):
        """
        Verify home page loaded correctly
        RETURNS: True if slider visible
        """
        is_visible = self.home_slider.is_visible()
        print(f"🏠 Home page loaded: {is_visible}")
        return is_visible