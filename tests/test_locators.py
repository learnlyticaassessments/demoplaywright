"""
Learning Different Locator Strategies
Website: https://www.automationexercise.com/
"""
import pytest
from playwright.sync_api import expect

def test_locator_by_text(page):
    """
    Strategy: Finding elements by visible text
    When to use: Links, buttons with text
    """
    page.goto("https://www.automationexercise.com/")
    
    # Find and click "Products" link by text
    page.get_by_text("Products").first.click()
    
    # Verify navigation
    expect(page).to_have_url("https://www.automationexercise.com/products")
    print("✅ Text locator worked")

def test_locator_by_role(page):
    """
    Strategy: Finding by ARIA role (BEST PRACTICE)
    When to use: Buttons, links, inputs with clear roles
    """
    page.goto("https://www.automationexercise.com/")
    
    # Find link by role and name
    page.get_by_role("link", name="Products").click()
    
    # Verify
    expect(page).to_have_url("https://www.automationexercise.com/products")
    print("✅ Role locator worked")

def test_locator_by_placeholder(page):
    """
    Strategy: Finding input by placeholder text
    When to use: Search boxes, input fields
    """
    page.goto("https://www.automationexercise.com/products")
    
    # Find search box by placeholder
    search_box = page.get_by_placeholder("Search Product")
    search_box.fill("Blue Top")
    
    # Click search button
    page.locator("#submit_search").click()
    
    print("✅ Placeholder locator worked")

def test_locator_by_css(page):
    """
    Strategy: CSS selector
    When to use: When no better option available
    """
    page.goto("https://www.automationexercise.com/")
    
    # CSS selector for signup/login link
    page.locator("a[href='/login']").click()
    
    # Verify navigation
    expect(page).to_have_url("https://www.automationexercise.com/login")
    print("✅ CSS locator worked")