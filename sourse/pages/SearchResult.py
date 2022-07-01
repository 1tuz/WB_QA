from selenium.webdriver.common.by import By

from sourse.pages.BasePage import BasePage


class SearchPageLocators:
    LOCATOR_SEARCH_RESULT = (By.CLASS_NAME, 'searching-results')


class SearchPageHelpers(BasePage):

    def check_search_result(self):
        all_list = self.find_element_visibility(BasePage, time=2)
        search_result = [x.text for x in all_list if len(x.text) > 0]
        return search_result
