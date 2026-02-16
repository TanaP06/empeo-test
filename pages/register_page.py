from playwright.sync_api import Page, expect


class RegisterPage:
    def __init__(self, page: Page):
        self.page = page

        # Company type
        self.company_thai = page.locator("label:has-text('บริษัทจดทะเบียนในไทย')")
        self.company_other = page.locator("label:has-text('อื่นๆ')")

        # Inputs
        self.tax_id = page.locator("input[placeholder*='เลขประจำตัว']")
        self.email = page.locator("input[placeholder='อีเมล*']")
        self.first_name = page.locator("input[placeholder='ชื่อ*']")
        self.last_name = page.locator("input[placeholder='นามสกุล*']")
        self.phone = page.locator("input[type='tel']")

        # Promo
        self.open_promo_btn = page.locator("span:has-text('ใช้โค้ดส่วนลด')")
        self.promo_input = page.locator("input[placeholder*='โค้ด']")

        # Checkbox
        self.terms_checkbox = page.locator(
            '[data-testid="input_checkbox_registration_checkbox"]'
        )

        # Submit
        self.submit_btn = page.locator("button:has-text('ทดลองใช้ฟรี')")

    # Navigation

    def goto(self):
        self.page.goto("https://portal.uat.gofive.co.th/Register/empeo")

    # Actions

    def select_company_type(self, company_type: str):
        if company_type == "thai":
            self.company_thai.click()
        else:
            self.company_other.click()

    def fill_tax_id(self, value: str):
        self.tax_id.fill(value)
        expect(self.tax_id).to_have_value(value)

    def fill_email(self, value: str):
        self.email.fill(value)

    def fill_name(self, first: str, last: str):
        self.first_name.fill(first)
        self.last_name.fill(last)

    def fill_phone(self, phone: str):
        self.phone.fill(phone)

    def fill_promo(self, promo: str):
        self.open_promo_btn.click()
        self.promo_input.wait_for()
        self.promo_input.fill(promo)

    def accept_terms(self):
        self.terms_checkbox.check()

    def submit(self):
        self.submit_btn.click()

    # Assertions

    def expect_error(self):
        expect(self.page.locator(".error")).to_be_visible()
