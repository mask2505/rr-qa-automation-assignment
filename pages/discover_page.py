from playwright.sync_api import Page


class DiscoverPage:

    def __init__(self, page: Page):
        self.page = page

    def get_current_url(self):
        return self.page.url

    def wait_for_locator(self, xpath: str, timeout: int = 10000):
        locator = self.page.locator(xpath)

        locator.first.wait_for(
            state="visible",
            timeout=timeout
        )

        return locator

    # ==========================================================
    # Header
    # ==========================================================

    def get_title(self):
        return self.wait_for_locator(
            "//header/a/p[contains(@class,'text-2xl')]"
        ).text_content()

    def click_title(self):
        self.wait_for_locator(
            "//header/a/p[contains(@class,'text-2xl')]"
        ).click()

    def click_popular(self):
        self.wait_for_locator(
            "//header/nav/ul/li[1]"
        ).click()

    def click_trending(self):
        self.wait_for_locator(
            "//header/nav/ul/li[2]"
        ).click()

    def click_newest(self):
        self.wait_for_locator(
            "//header/nav/ul/li[3]"
        ).click()

    def click_top_rated(self):
        self.wait_for_locator(
            "//header/nav/ul/li[4]"
        ).click()

    # ==========================================================
    # Movie Cards
    # ==========================================================

    def get_card_count(self):
        cards = self.page.locator(
            "//div[contains(@class,'grid')]//div[contains(@class,'flex')]"
        )

        return cards.count()

    # ==========================================================
    # Type Filter
    # ==========================================================

    def get_type_options(self):

        self.page.locator(
            "(//div[contains(@class,'control')])[1]"
        ).click()

        options = self.page.locator(
            "//div[contains(@class,'option')]"
        )

        return [
            options.nth(i).text_content().strip()
            for i in range(options.count())
        ]

    def select_type(self, option):

        self.page.locator(
            "(//div[contains(@class,'control')])[1]"
        ).click()

        self.page.locator(
            f"//div[contains(@class,'option') and normalize-space()='{option}']"
        ).click()

    def get_selected_type(self):

        return self.page.locator(
            "(//div[contains(@class,'singleValue')])[1]"
        ).text_content().strip()

    # ==========================================================
    # Genre Filter
    # ==========================================================

    def get_genre_options(self):

        self.page.locator(
            "(//div[contains(@class,'control')])[2]"
        ).click()

        options = self.page.locator(
            "//div[contains(@class,'option')]"
        )

        return [
            options.nth(i).text_content().strip()
            for i in range(options.count())
        ]

    def select_genre(self, genre):

        self.page.locator(
            "(//div[contains(@class,'control')])[2]"
        ).click()

        self.page.locator(
            f"//div[contains(@class,'option') and normalize-space()='{genre}']"
        ).click()

    def get_selected_genre(self):

        return self.page.locator(
            "(//div[contains(@class,'singleValue')])[2]"
        ).text_content().strip()

    # ==========================================================
    # Year Filter
    # ==========================================================

    def select_from_year(self, year):

        self.page.locator(
            "(//div[contains(@class,'control')])[3]"
        ).click()

        self.page.locator(
            f"//div[contains(@class,'option') and normalize-space()='{year}']"
        ).click()

    def select_to_year(self, year):

        self.page.locator(
            "(//div[contains(@class,'control')])[4]"
        ).click()

        self.page.locator(
            f"//div[contains(@class,'option') and normalize-space()='{year}']"
        ).click()

    def get_selected_from_year(self):
        return self.page.locator(
            "(//div[contains(@class,'singleValue')])[2]"
        ).text_content().strip()

    def get_selected_to_year(self):
        return self.page.locator(
            "(//div[contains(@class,'singleValue')])[3]"
        ).text_content().strip()

    # ==========================================================
    # Rating Filter
    # ==========================================================

    def select_rating(self, rating: float):

        star_number = int(rating)

        if rating % 1 == 0.5:

            xpath = (
                f"(//li[contains(@class,'rc-rate-star')]"
                f"/div/div[contains(@class,'first')])[{star_number + 1}]"
            )

        else:

            xpath = (
                f"(//li[contains(@class,'rc-rate-star')]"
                f"/div/div[contains(@class,'second')])[{star_number}]"
            )

        self.page.locator(xpath).click(force=True)