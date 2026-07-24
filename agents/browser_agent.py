from urllib.parse import quote

from tools.browser import browser


class BrowserAgent:

    def __init__(self):
        self.browser = browser

    # -------------------------------------------------
    # Browser
    # -------------------------------------------------

    def open(self, website):

        website = website.lower().strip()

        websites = {
            "google": "https://www.google.com",
            "youtube": "https://www.youtube.com",
            "github": "https://github.com",
            "linkedin": "https://linkedin.com",
            "amazon": "https://amazon.in",
            "flipkart": "https://flipkart.com",
            "chatgpt": "https://chat.openai.com",
            "gmail": "https://mail.google.com",
            "internshala": "https://internshala.com"
        }

        if website in websites:
            return self.browser.goto(websites[website])

        return self.browser.goto(website)

    # -------------------------------------------------
    # Google Search
    # -------------------------------------------------

    def google(self, query):

        url = (
            "https://www.google.com/search?q="
            + quote(query)
        )

        return self.browser.goto(url)

    # -------------------------------------------------
    # YouTube Search
    # -------------------------------------------------

    def youtube(self, query):

        url = (
            "https://www.youtube.com/results?search_query="
            + quote(query)
        )

        return self.browser.goto(url)

    # -------------------------------------------------
    # GitHub Search
    # -------------------------------------------------

    def github(self, query):

        url = (
            "https://github.com/search?q="
            + quote(query)
        )

        return self.browser.goto(url)

    # -------------------------------------------------
    # Read Current Page
    # -------------------------------------------------

    def read(self):

        return self.browser.text()

    # -------------------------------------------------
    # Read Links
    # -------------------------------------------------

    def links(self):

        return self.browser.links()

    # -------------------------------------------------
    # Click
    # -------------------------------------------------

    def click(self, text):

        return self.browser.click_text(text)

    # -------------------------------------------------
    # Type
    # -------------------------------------------------

    def type(self, selector, text):

        self.browser.type(selector, text)

        return {
            "success": True
        }

    # -------------------------------------------------
    # Keyboard
    # -------------------------------------------------

    def press(self, key):

        self.browser.press(key)

        return {
            "success": True
        }

    # -------------------------------------------------
    # Navigation
    # -------------------------------------------------

    def back(self):

        return self.browser.back()

    def forward(self):

        return self.browser.forward()

    def refresh(self):

        return self.browser.refresh()

    # -------------------------------------------------
    # Screenshot
    # -------------------------------------------------

    def screenshot(self):

        path = self.browser.screenshot()

        return {
            "success": True,
            "image": path
        }

    # -------------------------------------------------
    # Page Info
    # -------------------------------------------------

    def info(self):

        return {
            "title": self.browser.title(),
            "url": self.browser.url()
        }

    # -------------------------------------------------

    def close(self):

        self.browser.close()

        return {
            "success": True
        }