from selenium.webdriver.common.by import By

from sourse.pages.BasePage import BasePage


class MainPageLocators:
    LOCATOR_INPUT_FIND_TEXT_LINE = (By.ID, 'searchInput')
    LOCATOR_FIND_BUTTON = (By.ID, 'applySearchBtn')
    LOCATOR_SORT_BY_RATING = (By.XPATH, '//*[@id="catalog_sorter"]/a[2]/span')
    LOCATOR_CLICK_ITEM = (By.XPATH, '//*[@id="c16023990"]/div/a/div[2]/div[2]/span')
    LOCATOR_ADD_TO_THE_CART = (By.XPATH, '//*[@id="infoBlockProductCard"]/div[6]/div/button[1]')
    LOCATOR_MAIN_BANNER = (By.ID, 'app')


class MainPageHelpers(BasePage):

    def enter_find_text_in_line(self, text: str):
        line = self.find_element_visibility(MainPageLocators.LOCATOR_INPUT_FIND_TEXT_LINE)
        line.click()
        line.send_keys(text)
        return line

    def click_find_button(self):
        find_button = self.find_element_visibility(MainPageLocators.LOCATOR_FIND_BUTTON)
        find_button.click()
        return find_button

    def click_rating_button(self):
        rating_button = self.find_element_visibility(MainPageLocators.LOCATOR_SORT_BY_RATING)
        rating_button.click()
        return rating_button

    def click_item_button(self):
        item_button = self.find_element_visibility(MainPageLocators.LOCATOR_CLICK_ITEM)
        item_button.click()
        return item_button

    def add_to_cart_button(self):
        cart_button = self.find_element_visibility(MainPageLocators.LOCATOR_ADD_TO_THE_CART)
        cart_button.click()
        return cart_button

    def check_search_result(self):
        all_list = self.find_elements(MainPageLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu
