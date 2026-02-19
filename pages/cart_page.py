"""
Cart Page Object
URL: https://www.automationexercise.com/view_cart
"""
from pages.base_page import BasePage
from playwright.sync_api import expect

class CartPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
    
    # ============ LOCATORS ============
    
    @property
    def cart_items(self):
        """All items in cart"""
        return self.page.locator("#cart_info tbody tr")
    
    @property
    def empty_cart_message(self):
        """Message shown when cart is empty"""
        return self.page.locator("text=Cart is empty")
    
    def delete_button(self, product_id):
        """Delete button for specific product"""
        return self.page.locator(f"//a[@data-product-id='{product_id}']")
    
    @property
    def proceed_to_checkout_button(self):
        """Checkout button"""
        return self.page.locator("text=Proceed To Checkout")
    
    # ============ ACTIONS ============
    
    def navigate_to_cart(self):
        """Go to cart page"""
        self.navigate("/view_cart")
    
    def remove_product(self, product_id):
        """Remove product from cart"""
        print(f"🗑️ Removing product: {product_id}")
        self.delete_button(product_id).click()
    
    def proceed_to_checkout(self):
        """Click checkout button"""
        print("💳 Proceeding to checkout")
        self.proceed_to_checkout_button.click()
    
    # ============ VERIFICATIONS ============
    
    def verify_cart_page_loaded(self):
        """Verify cart page loaded"""
        expect(self.page).to_have_url("https://www.automationexercise.com/view_cart")
        print("✅ Cart page verified")
    
    def get_cart_item_count(self):
        """Count items in cart"""
        count = self.cart_items.count()
        print(f"🛒 Cart items: {count}")
        return count
    
    def is_cart_empty(self):
        """Check if cart is empty"""
        is_empty = self.empty_cart_message.is_visible()
        print(f"🛒 Cart empty: {is_empty}")
        return is_empty