import time

from sourse.pages.WB_MainPage import MainPageHelpers
from sourse.pages.SearchResult import SearchPageHelpers


def test_find(driver):
    """Тест поиска запроса

    Parameters
    ----------
    driver
        Фикстура, являющаяся самим браузером
    """

    main_page = MainPageHelpers(driver)
    main_page.go_to_home_page()
    main_page.enter_find_text_in_line('Iphone')
    main_page.click_find_button()
    search_result = SearchPageHelpers.check_search_result(driver)
    text_input = main_page.enter_find_text_in_line
    assert search_result == text_input
#    search_result = SearchPageHelpers
#    search_result.check_search_result()
    time.sleep(10)

    # todo тут можно добавить какую-нибудь проверку
    assert main_page.enter_find_text_in_line() == search_result.check_search_result()
