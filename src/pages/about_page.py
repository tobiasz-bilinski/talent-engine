from selenium.webdriver.common.by import By
from src.config.config import config


class AboutPage:
    PAGE_URL = "/about"
    twitter_button = (By.CSS_SELECTOR, "a[title='GitHub on Twitter']")
    facebook_button = (By.CSS_SELECTOR, "a[title='GitHub on Facebook']")
    youtube_button = (By.CSS_SELECTOR, "a[title='GitHub on YouTube']")
    linkedin_button = (By.CSS_SELECTOR, "a[title='GitHub on LinkedIn']")
    blog = (By.XPATH, "//a[contains(text(), 'Blog')]")

    def __init__(self, app):
        self.app = app

    def open_about_page(self):
        """Open the About page."""
        self.app.open_page(config.BASE_URL_UI + self.PAGE_URL)

    # TODO: @property on all hrefs
    def get_twitter_href(self):
        """Return href from Twitter button element."""
        return self.app.get_element(self.twitter_button).get_attribute('href')

    def get_blog_href(self):
        """Return href from Blog element."""
        return self.app.get_element(self.blog).get_attribute('href')
