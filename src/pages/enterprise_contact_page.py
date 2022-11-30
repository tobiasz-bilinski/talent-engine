from selenium.webdriver.common.by import By
from src.config.config import config


class EnterpriseContactPage:
    PAGE_URL = "/enterprise/contact"
    full_name_field = (By.ID, "site_enterprise_contact_request_full_name")
    company_field = (By.ID, "site_enterprise_contact_request_company")
    work_email_field = (By.ID, "site_enterprise_contact_request_email")
    phone_number_field = (By.ID, "site_enterprise_contact_request_phone")
    message_field = (By.ID, "site_enterprise_contact_request_request_details")
    mailing_list_checkbox = (
        By.ID, "site_enterprise_contact_request_marketing_email_opt_in")
    mailing_list_checkbox_text = (
        By.NAME, "site_enterprise_contact_request[marketing_email_opt_in]")
    submit_button = (By.LINK_TEXT, "Contact Sales")

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        """Open the Enterprise Contact page."""
        self.app.open_page(config.BASE_URL_UI + self.PAGE_URL)

    def fill_contact_form(self, name, company, email, phone, message):
        """Fill contact form with test data."""
        self.app.enter_text(self.full_name_field, name)
        self.app.enter_text(self.company_field, company)
        self.app.enter_text(self.work_email_field, email)
        self.app.enter_text(self.phone_number_field, phone)
        self.app.enter_text(self.message_field, message)

    def click_mailing_list_checkbox(self):
        """Click mailing list checkbox."""
        self.app.click(self.mailing_list_checkbox)
