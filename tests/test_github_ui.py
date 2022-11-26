from src.config.config import config
from src.data.test_data import TestData


def test_first_login_test(github_ui_fixture):
    github_ui_fixture.login_page.open_login_page()
    github_ui_fixture.login(config.SHARED_USERNAME, config.SHARED_PASSWORD)
    assert github_ui_fixture.get_title() == TestData.EXPECTED_LOGIN_PAGE_TITLE
