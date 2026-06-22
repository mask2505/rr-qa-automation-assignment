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

    # ==========================================================
    # Search bar
    # ==========================================================

    def click_search(self):
        self.page.locator(
            "//div/input[@name='search']"
        ).click()

    def enter_search_text(self, movie_name):

        self.page.locator(
            "//div/input[@name='search']"
        ).fill(movie_name)

    def search_movie(self, movie_name):

        self.click_search()

        self.enter_search_text(movie_name)

        self.page.keyboard.press("Enter")

    def clear_search(self):

        self.click_search()

        self.page.locator(
            "//div/input[@name='search']"
        ).fill("")

        self.page.keyboard.press("Enter")

    # ==========================================================
    # Movie cards
    # ==========================================================

    def get_first_card_title(self):

        return self.page.locator(
            "(//div[contains(@class,'grid')]//div[contains(@class,'flex')]/p)[1]"
        ).text_content().strip()

    def get_first_card_thumbnail(self):

        return self.page.locator(
            "(//div[contains(@class,'grid')]//div[contains(@class,'flex')]/img)[1]"
        )

    def get_first_card_metadata(self):
        return self.page.locator(
            "(//div[contains(@class,'grid')]//div[contains(@class,'flex')]/p)[2]"
        ).text_content().strip()

    def get_first_card_genre(self):
        metadata = self.get_first_card_metadata()
        return metadata.split(",")[0].strip()

    def get_first_card_release_year(self):
        metadata = self.get_first_card_metadata()
        return metadata.split(",")[1].strip()

    # ==========================================================
    # Pagination
    # ==========================================================

    def get_current_page(self):
        self.scroll_to_bottom()
        return self.wait_for_locator(
            "//li[contains(@class,'selected')]"
        ).text_content().strip()

    def click_next_page(self):
        self.scroll_to_bottom()
        self.wait_for_locator("//li[contains(@class,'next')]").click()

    def click_previous_page(self):
        self.scroll_to_bottom()
        self.page.wait_for_selector("//li[contains(@class,'previous')]").click()

    def click_page_number(self, page_number):
        self.scroll_to_bottom()
        self.wait_for_locator(
            f"//li/a[text()='{page_number}']"
        ).click()

    def get_last_page_locator(self):
        self.scroll_to_bottom()
        return self.wait_for_locator(
            "//li[contains(@class,'next')]/preceding-sibling::li[1]/a"
        )

    def get_last_page_number(self):
        self.scroll_to_bottom()
        return self.wait_for_locator(
            "//li[contains(@class,'next')]/preceding-sibling::li[1]/a"
        ).text_content().strip()

    def click_last_page(self):
        self.scroll_to_bottom()
        self.get_last_page_locator().click()

    # ==========================================================
    # Scrolling
    # ==========================================================

    def scroll_to_bottom(self):

        self.page.locator(
            "//div[contains(@class,'overflow-scroll')]"
        ).evaluate(
            "(element) => element.scrollTop = element.scrollHeight"
        )

    def scroll_to_top(self):
        self.page.evaluate(
            "window.scrollTo(0, 0)"
        )

    def get_scroll_position(self):

        return self.page.locator(
            "//div[contains(@class,'overflow-scroll')]"
        ).evaluate(
            "(element) => element.scrollTop"
        )

    def is_discovery_filters_visible(self):
        return self.page.locator(
            "//p[contains(text(),'DISCOVER OPTIONS')]"
        ).is_visible()

    def is_pagination_visible(self):
        return self.page.locator(
            "//li[contains(@class,'next')]"
        ).is_visible()