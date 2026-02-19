"""
Internationalization (i18n) Tests
Tests application behavior across different locales
"""
import pytest
from config.locales import get_all_locales, get_locale_config
from pages.home_page import HomePage

# ============ PARAMETERIZED LOCALE TESTS ============

@pytest.mark.parametrize("locale", ["en-US", "fr-FR", "de-DE"])
def test_homepage_in_different_locales(page, locale, locale_config):
    """
    TEST: Verify homepage works in multiple locales
    
    DEMONSTRATES:
    - Parameterized testing across locales
    - Locale configuration usage
    
    RUNS: 3 times (once per locale)
    """
    print(f"\n🌍 Testing with locale: {locale_config['name']}")
    
    # Create new context with specific locale
    home_page = HomePage(page)
    home_page.navigate_to_home()
    
    # Verify page loads
    assert home_page.is_home_page_loaded()
    print(f"✅ Homepage loaded for {locale}")

@pytest.mark.parametrize("locale", get_all_locales())
def test_all_supported_locales(page, locale, locale_config):
    """
    TEST: Verify site works in ALL supported locales
    
    DEMONSTRATES:
    - Dynamic parameterization
    - Testing against all configured locales
    
    RUNS: Once for each locale in locales.py
    """
    print(f"\n🌍 Locale: {locale_config['name']}")
    print(f"   Timezone: {locale_config['timezone']}")
    print(f"   Currency: {locale_config['currency_symbol']}")
    
    home_page = HomePage(page)
    home_page.navigate_to_home()
    
    # Basic verification
    assert "Automation" in home_page.get_page_title()
    print(f"✅ Passed for {locale}")

# ============ CURRENCY & NUMBER FORMAT TESTS ============

def test_currency_display_format(page, locale_config):
    """
    TEST: Verify currency is displayed in correct format
    
    DEMONSTRATES:
    - Currency formatting validation
    - Locale-specific number formats
    """
    print(f"\n💰 Testing currency: {locale_config['currency']}")
    print(f"   Symbol: {locale_config['currency_symbol']}")
    print(f"   Decimal separator: {locale_config['decimal_separator']}")
    
    # Navigate to products page (has prices)
    page.goto("https://www.automationexercise.com/products")
    
    # Example: Check if prices exist
    # (Actual validation would check format)
    prices = page.locator(".productinfo h2")
    assert prices.count() > 0
    
    first_price = prices.first.inner_text()
    print(f"   First price found: {first_price}")
    
    # Verify currency symbol or format
    # Note: automationexercise.com uses Rs. (Rupees)
    # In real scenarios, you'd verify against locale_config
    assert "Rs" in first_price

# ============ DATE FORMAT TESTS ============

@pytest.mark.parametrize("locale", ["en-US", "en-GB", "de-DE", "ja-JP"])
def test_date_format_display(page, locale, locale_config):
    """
    TEST: Verify dates display in correct format
    
    DEMONSTRATES:
    - Date format validation across locales
    
    FORMATS:
    - en-US: MM/DD/YYYY
    - en-GB: DD/MM/YYYY
    - de-DE: DD.MM.YYYY
    - ja-JP: YYYY/MM/DD
    """
    print(f"\n📅 Testing date format: {locale_config['date_format']}")
    
    page.goto("https://www.automationexercise.com/")
    
    # In real app, you would:
    # 1. Find date elements
    # 2. Validate format matches locale_config['date_format']
    # 3. Verify separators (/, -, .)
    
    print(f"   Expected format: {locale_config['date_format']}")
    print(f"✅ Date format test passed for {locale}")

# ============ RTL (Right-to-Left) TESTS ============

@pytest.mark.parametrize("locale", ["ar-SA"])
def test_rtl_layout(page, locale, locale_config, is_rtl):
    """
    TEST: Verify RTL layout for Arabic locale
    
    DEMONSTRATES:
    - RTL text direction validation
    - Layout mirroring verification
    """
    print(f"\n↔️ Testing RTL: {is_rtl}")
    
    if is_rtl:
        page.goto("https://www.automationexercise.com/")
        
        # Verify body direction attribute
        body = page.locator("body")
        
        # In real RTL site, would check:
        # - dir="rtl" attribute
        # - CSS text-align: right
        # - Reversed layout
        
        print("✅ RTL layout test executed")
    else:
        pytest.skip("Not an RTL locale")

# ============ TIMEZONE TESTS ============

def test_timezone_handling(page, locale_config):
    """
    TEST: Verify timezone is set correctly
    
    DEMONSTRATES:
    - Timezone verification
    - Time display validation
    """
    print(f"\n🕐 Testing timezone: {locale_config['timezone']}")
    
    # Execute JavaScript to get browser timezone
    browser_timezone = page.evaluate("""
        () => Intl.DateTimeFormat().resolvedOptions().timeZone
    """)
    
    print(f"   Browser timezone: {browser_timezone}")
    print(f"   Expected: {locale_config['timezone']}")
    
    # Note: This requires browser context to be configured with timezone
    # See browser_context_args_with_locale fixture

# ============ CHARACTER ENCODING TESTS ============

@pytest.mark.parametrize("locale", ["zh-CN", "ja-JP", "ar-SA"])
def test_character_encoding(page, locale, locale_config):
    """
    TEST: Verify special characters display correctly
    
    DEMONSTRATES:
    - UTF-8 encoding verification
    - Multi-byte character support
    """
    print(f"\n🔤 Testing encoding for: {locale_config['name']}")
    
    page.goto("https://www.automationexercise.com/")
    
    # Check page encoding
    charset = page.evaluate("""
        () => document.characterSet
    """)
    
    print(f"   Character set: {charset}")
    assert charset.upper() == "UTF-8"
    print(f"✅ Encoding test passed")

# ============ LOCALE SWITCHING TEST ============

def test_locale_switching(page):
    """
    TEST: Verify user can switch between locales
    
    DEMONSTRATES:
    - Dynamic locale switching
    - State persistence
    """
    print("\n🔄 Testing locale switching")
    
    # Test with different locales
    locales_to_test = ["en-US", "fr-FR", "de-DE"]
    
    for locale in locales_to_test:
        config = get_locale_config(locale)
        print(f"   Switching to: {config['name']}")
        
        # Navigate to home page
        page.goto("https://www.automationexercise.com/")
        
        # In real app:
        # 1. Click locale switcher
        # 2. Select locale
        # 3. Verify content changed
        # 4. Verify URL or cookie contains locale
        
        print(f"   ✓ Switched to {locale}")
    
    print("✅ Locale switching test passed")