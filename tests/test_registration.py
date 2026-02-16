from playwright.sync_api import sync_playwright
from pages.register_page import RegisterPage
from data.user_data import USER_DATA


def test_register_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        register = RegisterPage(page)

        register.goto()
        register.select_company_type(USER_DATA["company_type"])
        register.fill_tax_id(USER_DATA["tax_id"])
        register.fill_email(USER_DATA["email"])
        register.fill_name(USER_DATA["first_name"], USER_DATA["last_name"])
        register.fill_phone(USER_DATA["phone"])
        register.fill_promo(USER_DATA["promo"])

        if USER_DATA["accept_terms"]:
            register.accept_terms()

        register.submit()

        page.wait_for_timeout(3000)
        browser.close()
