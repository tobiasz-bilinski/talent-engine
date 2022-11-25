from src.providers.browsers.library.chrome_browser import ChromeBrowser
from src.providers.browsers.library.firefox_browser import FirefoxBrowser
from src.providers.browsers.library.edge_browser import EdgeBrowser


class BrowserProvider:
    """Browser provider class."""
    MAPPER = {
        "chrome": ChromeBrowser,
        "firefox": FirefoxBrowser,
        "edge": EdgeBrowser
    }

    @classmethod
    def get_driver(cls, browser_name: str):
        """Return driver object from browser class.

        Args:
            browser_name (str): Browser name ("chrome", "firefox", "edge"...)

        Returns:
            Driver for the specified class.
        """
        browser_class = cls.MAPPER.get(browser_name)
        if browser_class is None:
            # TODO: Logger instead of print
            print("Error - Browser not registered.")

        return browser_class.get_driver()
