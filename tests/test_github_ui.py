from src.config.config import config
from src.data.test_data import TestData
import time


def test_first_login_test(github_ui):
    github_ui.login_page.open_login_page()
    github_ui.login(config.SHARED_USERNAME, config.SHARED_PASSWORD)
    # TODO: check_title() method returning boolean
    assert github_ui.get_title() == TestData.EXPECTED_LOGIN_PAGE_TITLE


def test_enterprise_contact_form_correct_data(github_enterprise):
    github_enterprise.fill_contact_form(
        TestData.ENTERPRISE_CONTACT_NAME_CORRECT,
        TestData.ENTERPRISE_CONTACT_COMPANY_CORRECT,
        TestData.ENTERPRISE_CONTACT_EMAIL_CORRECT,
        TestData.ENTERPRISE_CONTACT_PHONE_CORRECT,
        TestData.ENTERPRISE_CONTACT_MESSAGE_CORRECT,
    )
    github_enterprise.click_mailing_list_checkbox()
    # Can't finish because of captcha


def test_about_page_twitter_link(github_about):
    # What's better - specific methods for different links or a general method 'get_element_href(locator)' in BaseUIApp?
    twitter_link = github_about.twitter_href
    assert twitter_link == TestData.GITHUB_TWITTER_LINK


def test_blog_link(github_about):
    blog_link = github_about.blog_href
    assert blog_link == TestData.GITHUB_BLOG_LINK
