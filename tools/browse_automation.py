from playwright.sync_api import sync_playwright
from urllib.parse import quote


class BrowserAutomation:

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.page = None

    # ----------------------------------------------------

    def start(self):

        if self.browser:
            return

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            channel="chrome",      # remove if Chrome isn't installed
            headless=False
        )

        self.page = self.browser.new_page()

    # ----------------------------------------------------

    def stop(self):

        if self.browser:

            self.browser.close()

            self.playwright.stop()

            self.browser = None
            self.page = None

    # ----------------------------------------------------

    def open(self, url):

        self.start()

        if not url.startswith("http"):

            url = "https://" + url

        self.page.goto(url)

        return f"Opening {url}"

    # ----------------------------------------------------

    def google(self, query):

        self.start()

        self.page.goto(
            f"https://www.google.com/search?q={quote(query)}"
        )

        return f"Searching Google for {query}"

    # ----------------------------------------------------

    def youtube(self, query):

        self.start()

        self.page.goto(
            f"https://www.youtube.com/results?search_query={quote(query)}"
        )

        return f"Searching YouTube for {query}"

    # ----------------------------------------------------

    def github(self, query):

        self.start()

        self.page.goto(
            f"https://github.com/search?q={quote(query)}"
        )

        return f"Searching GitHub for {query}"

    # ----------------------------------------------------

    def click(self, text):

        self.page.get_by_text(
            text,
            exact=False
        ).first.click()

        return f"Clicked {text}"

    # ----------------------------------------------------

    def fill(self, selector, value):

        self.page.locator(selector).fill(value)

    # ----------------------------------------------------

    def press(self, key):

        self.page.keyboard.press(key)

    # ----------------------------------------------------

    def current_url(self):

        return self.page.url

    # ----------------------------------------------------

    def title(self):

        return self.page.title()

    # ----------------------------------------------------

    def html(self):

        return self.page.content()

    # ----------------------------------------------------

    def screenshot(self, path="screen.png"):

        self.page.screenshot(path=path)

        return path

    # ----------------------------------------------------

    def close(self):

        self.stop()