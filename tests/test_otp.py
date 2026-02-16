from playwright.sync_api import sync_playwright
from pages.otp_page import OTPPage
from data.user_data import USER_DATA

def test_invalid_otp():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://portal.uat.gofive.co.th/Register/empeo")

        otp = OTPPage(page)

        otp.fill_otp(USER_DATA["otp"])
        otp.submit()
        otp.expect_error()

        browser.close()
