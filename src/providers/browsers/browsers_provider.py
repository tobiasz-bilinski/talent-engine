from src.providers.browsers.library.chrome_browser import ChromeBrowser
from src.providers.browsers.library.firefox_browser import FirefoxBrowser
from src.providers.browsers.library.edge_browser import EdgeBrowser
from src.providers.browsers.library.remote_chrome_browser import RemoteChromeBrowser
from src.providers.browsers.library.remote_firefox_browser import RemoteFirefoxBrowser
from src.providers.browsers.library.remote_edge_browser import RemoteEdgeBrowser


class BrowserProvider:
    """Browser provider class."""

    MAPPER = {
        "chrome": ChromeBrowser,
        "firefox": FirefoxBrowser,
        "edge": EdgeBrowser,
        "remote_chrome": RemoteChromeBrowser,
        "remote_firefox": RemoteFirefoxBrowser,
        "remote_edge": RemoteEdgeBrowser,
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
            # what exception?
            raise NotImplementedError("Error - the browser is not registered!")

        return browser_class.get_driver()
