from playwright.sync_api import Page, expect

class OTPPage:
    def __init__(self, page: Page):
        self.page = page
        self.otp_inputs = page.locator(".otp-input")
        self.verify_btn = page.locator('button:has-text("Verify")')
        self.error_msg = page.locator(".otp-error")

    def fill_otp(self, otp: str):
        for i, digit in enumerate(otp):
            self.otp_inputs.nth(i).fill(digit)

    def submit(self):
        self.verify_btn.click()

    def expect_error(self):
        expect(self.error_msg).to_be_visible()
