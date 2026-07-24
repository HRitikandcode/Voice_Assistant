from playwright.sync_api import sync_playwright, TimeoutError


class BrowserController:

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.page = None

    # -----------------------------------------

    def start(self):

        if self.browser:
            return

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            channel="chrome",      # Remove if Chrome isn't installed
            headless=False
        )

        self.page = self.browser.new_page()

        self.page.set_viewport_size({
            "width": 1400,
            "height": 900
        })

    # -----------------------------------------

    def close(self):

        if self.browser:

            self.browser.close()
            self.playwright.stop()

            self.browser = None
            self.page = None
            self.playwright = None

    # -----------------------------------------

    def goto(self, url):

        self.start()

        if not url.startswith("http"):
            url = "https://" + url

        self.page.goto(url)

        self.page.wait_for_load_state("networkidle")

        return self.info()

    # -----------------------------------------

    def back(self):

        self.page.go_back()

        self.page.wait_for_load_state("networkidle")

        return self.info()

    # -----------------------------------------

    def forward(self):

        self.page.go_forward()

        self.page.wait_for_load_state("networkidle")

        return self.info()

    # -----------------------------------------

    def refresh(self):

        self.page.reload()

        self.page.wait_for_load_state("networkidle")

        return self.info()

    # -----------------------------------------

    def wait(self, seconds):

        self.page.wait_for_timeout(seconds * 1000)

    # -----------------------------------------

    def click_text(self, text):

        self.page.get_by_text(
            text,
            exact=False
        ).first.click()

        return self.info()

    # -----------------------------------------

    def click_selector(self, selector):

        self.page.locator(selector).first.click()

        return self.info()

    # -----------------------------------------

    def type(self, selector, text):

        box = self.page.locator(selector).first

        box.click()

        box.fill(text)

    # -----------------------------------------

    def press(self, key):

        self.page.keyboard.press(key)

    # -----------------------------------------

    def html(self):

        return self.page.content()

    # -----------------------------------------

    def text(self):

        return self.page.locator("body").inner_text()

    # -----------------------------------------

    def title(self):

        return self.page.title()

    # -----------------------------------------

    def url(self):

        return self.page.url

    # -----------------------------------------

    def screenshot(self, path="screen.png"):

        self.page.screenshot(path=path)

        return path

    # -----------------------------------------

    def links(self):

        data = []

        anchors = self.page.locator("a").all()

        for a in anchors:

            try:

                data.append({

                    "text": a.inner_text(),

                    "href": a.get_attribute("href")

                })

            except Exception:
                pass

        return data

    # -----------------------------------------

    def info(self):

        return {

            "title": self.title(),

            "url": self.url()
        }