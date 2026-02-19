"""
Our very first Playwright test
Learning: Basic page interaction
"""

def test_open_website(page):
    """
    WHAT THIS DOES:
    1. Opens automation practice website
    2. Verifies title
    
    FIXTURE USED:
    - page: Playwright's built-in fixture (browser page object)
    """
    # Step 1: Navigate to website
    page.goto("https://www.automationexercise.com/")
    
    # Step 2: Verify we're on correct site
    assert "Automation Exercise" in page.title()
    
    print("✅ Test Passed: Website opened successfully")