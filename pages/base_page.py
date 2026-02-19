"""
Base Page: Parent class for all pages
Contains common functionality used across all pages
"""

class BasePage:
    """
    WHY THIS EXISTS:
    - Avoid code duplication
    - Common methods available to all pages
    - Single place to update navigation logic
    """
    
    def __init__(self, page):
        """
        PARAMETERS:
        - page: Playwright Page object (from fixture)
        
        STORES:
        - self.page: So all child classes can use it
        """
        self.page = page
        self.base_url = "https://www.automationexercise.com"
    
    def navigate(self, path=""):
        """
        Navigate to any path on the website
        
        EXAMPLE:
        - navigate() -> goes to home
        - navigate("/login") -> goes to login page
        """
        url = f"{self.base_url}{path}"
        self.page.goto(url)
        print(f"📍 Navigated to: {url}")
    
    def get_page_title(self):
        """Returns current page title"""
        return self.page.title()
    
    def get_current_url(self):
        """Returns current URL"""
        return self.page.url