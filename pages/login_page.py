"""
Login Page Object
URL: https://www.automationexercise.com/login
Contains: Login and Signup functionality
"""
from pages.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    """
    Handles both Login and Signup forms
    """
    
    def __init__(self, page):
        super().__init__(page)
    
    # ============ LOCATORS - LOGIN SECTION ============
    
    @property
    def login_email(self):
        """Email input in login form"""
        return self.page.locator("input[data-qa='login-email']")
    
    @property
    def login_password(self):
        """Password input in login form"""
        return self.page.locator("input[data-qa='login-password']")
    
    @property
    def login_button(self):
        """Login submit button"""
        return self.page.locator("button[data-qa='login-button']")
    
    # ============ LOCATORS - SIGNUP SECTION ============
    
    @property
    def signup_name(self):
        """Name input in signup form"""
        return self.page.locator("input[data-qa='signup-name']")
    
    @property
    def signup_email(self):
        """Email input in signup form"""
        return self.page.locator("input[data-qa='signup-email']")
    
    @property
    def signup_button(self):
        """Signup submit button"""
        return self.page.locator("button[data-qa='signup-button']")
    
    # ============ ACTIONS - LOGIN ============
    
    def navigate_to_login(self):
        """Go to login page"""
        self.navigate("/login")
    
    def perform_login(self, email, password):
        """
        Complete login workflow
        
        PARAMETERS:
        - email: User email
        - password: User password
        
        STEPS:
        1. Fill email
        2. Fill password
        3. Click login button
        """
        print(f"🔐 Logging in with: {email}")
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()
        print("✅ Login form submitted")
    
    # ============ ACTIONS - SIGNUP ============
    
    def perform_signup(self, name, email):
        """
        Complete signup workflow
        
        PARAMETERS:
        - name: User's name
        - email: User's email
        
        STEPS:
        1. Fill name
        2. Fill email
        3. Click signup button
        """
        print(f"📝 Signing up with: {name} ({email})")
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()
        print("✅ Signup form submitted")
    
    # ============ VERIFICATIONS ============
    
    def verify_login_page_loaded(self):
        """Verify we're on login page"""
        expect(self.page).to_have_url("https://www.automationexercise.com/login")
        expect(self.login_button).to_be_visible()
        print("✅ Login page verified")