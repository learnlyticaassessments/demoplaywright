"""
Products Page Object
URL: https://www.automationexercise.com/products
"""
from pages.base_page import BasePage
from playwright.sync_api import expect

class ProductsPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
    
    # ============ LOCATORS ============
    
    @property
    def search_box(self):
        """Product search input"""
        return self.page.get_by_placeholder("Search Product")
    
    @property
    def search_button(self):
        """Search submit button"""
        return self.page.locator("#submit_search")
    
    @property
    def all_products(self):
        """All product cards"""
        return self.page.locator(".productinfo")
    
    def product_by_name(self, name):
        """Get specific product by name"""
        return self.page.locator(f"text={name}")
    
    def add_to_cart_button(self, product_number=1):
        """Add to cart button for specific product"""
        return self.page.locator(f"(//a[contains(@data-product-id, '{product_number}')])[1]")
    
    @property
    def continue_shopping_button(self):
        """Continue shopping button in modal"""
        return self.page.locator("button.btn-success")
    
    @property
    def view_cart_button(self):
        """View cart button in modal"""
        return self.page.locator("text=View Cart")
    
    # ============ ACTIONS ============
    
    def navigate_to_products(self):
        """Go to products page"""
        self.navigate("/products")
    
    def search_product(self, product_name):
        """
        Search for a product
        
        STEPS:
        1. Enter product name
        2. Click search
        """
        print(f"🔍 Searching for: {product_name}")
        self.search_box.fill(product_name)
        self.search_button.click()
    
    def add_first_product_to_cart(self):
        """Add first product to cart"""
        print("🛒 Adding first product to cart")
        self.add_to_cart_button(1).click()
        # Handle modal
        self.continue_shopping_button.click()
    
    def add_product_and_view_cart(self, product_number=1):
        """Add product and navigate to cart"""
        print(f"🛒 Adding product {product_number} and viewing cart")
        self.add_to_cart_button(product_number).click()
        self.view_cart_button.click()
    
    # ============ VERIFICATIONS ============
    
    def verify_products_page_loaded(self):
        """Verify products page loaded"""
        expect(self.page).to_have_url("https://www.automationexercise.com/products")
        expect(self.all_products.first).to_be_visible()
        print("✅ Products page verified")
    
    def get_product_count(self):
        """Count visible products"""
        count = self.all_products.count()
        print(f"📦 Products found: {count}")
        return count