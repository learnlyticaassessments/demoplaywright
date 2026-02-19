"""
Internationalization Configuration
Defines supported locales and their settings
"""

SUPPORTED_LOCALES = {
    "en-US": {
        "name": "English (US)",
        "locale": "en-US",
        "timezone": "America/New_York",
        "currency": "USD",
        "currency_symbol": "$",
        "date_format": "MM/DD/YYYY",
        "decimal_separator": ".",
        "thousands_separator": ","
    },
    "en-GB": {
        "name": "English (UK)",
        "locale": "en-GB",
        "timezone": "Europe/London",
        "currency": "GBP",
        "currency_symbol": "£",
        "date_format": "DD/MM/YYYY",
        "decimal_separator": ".",
        "thousands_separator": ","
    },
    "fr-FR": {
        "name": "French (France)",
        "locale": "fr-FR",
        "timezone": "Europe/Paris",
        "currency": "EUR",
        "currency_symbol": "€",
        "date_format": "DD/MM/YYYY",
        "decimal_separator": ",",
        "thousands_separator": " "
    },
    "de-DE": {
        "name": "German (Germany)",
        "locale": "de-DE",
        "timezone": "Europe/Berlin",
        "currency": "EUR",
        "currency_symbol": "€",
        "date_format": "DD.MM.YYYY",
        "decimal_separator": ",",
        "thousands_separator": "."
    },
    "ja-JP": {
        "name": "Japanese (Japan)",
        "locale": "ja-JP",
        "timezone": "Asia/Tokyo",
        "currency": "JPY",
        "currency_symbol": "¥",
        "date_format": "YYYY/MM/DD",
        "decimal_separator": ".",
        "thousands_separator": ","
    },
    "es-ES": {
        "name": "Spanish (Spain)",
        "locale": "es-ES",
        "timezone": "Europe/Madrid",
        "currency": "EUR",
        "currency_symbol": "€",
        "date_format": "DD/MM/YYYY",
        "decimal_separator": ",",
        "thousands_separator": "."
    },
    "zh-CN": {
        "name": "Chinese (Simplified)",
        "locale": "zh-CN",
        "timezone": "Asia/Shanghai",
        "currency": "CNY",
        "currency_symbol": "¥",
        "date_format": "YYYY-MM-DD",
        "decimal_separator": ".",
        "thousands_separator": ","
    },
    "ar-SA": {
        "name": "Arabic (Saudi Arabia)",
        "locale": "ar-SA",
        "timezone": "Asia/Riyadh",
        "currency": "SAR",
        "currency_symbol": "﷼",
        "date_format": "DD/MM/YYYY",
        "decimal_separator": ".",
        "thousands_separator": ",",
        "rtl": True  # Right-to-left
    }
}

def get_locale_config(locale_code):
    """Get configuration for specific locale"""
    return SUPPORTED_LOCALES.get(locale_code, SUPPORTED_LOCALES["en-US"])

def get_all_locales():
    """Get list of all supported locale codes"""
    return list(SUPPORTED_LOCALES.keys())