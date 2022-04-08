from selenium.webdriver.common.by import By

from source.pages.BasePage import BasePage


class MainPageLocators:
    LOCATOR_INPUT_FIND_TEXT_LINE = (By.ID, 'searchInput')
    LOCATOR_FIND_BUTTON = (By.ID, 'applySearchBtn')
    LOCATOR_SORT_BY_RATING = (By.Xpath, '//*[@id="catalog_sorter"]/a[2]/span')
    LOCATOR_CLICK_ITEM = (By.Xpath, '//*[@id="c16023990"]/div/a/div[2]/div[2]/span')
    LOCATOR_ADD_TO_THE_CART = (By.Xpath, '//*[@id="infoBlockProductCard"]/div[6]/div/button[1]')




class MainPageHelper(BasePage):

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
