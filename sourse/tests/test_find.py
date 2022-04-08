import time

from source.pages.MainPage import MainPageHelper



def test_find(driver):
    """Тест поиска запроса

    Parameters
    ----------
    driver
        Фикстура, являющаяся самим браузером
    """

    main_page = MainPageHelper(driver)
    main_page.go_to_home_page()
    main_page.enter_find_text_in_line('Iphone')
    main_page.click_find_button()

    # fixme добавил строку ниже для наглядности, что все выполняется. Когда тест пойдет дальше и будет нормальная
    #  проверка - надо будет убрать
    time.sleep(10)

    # todo тут можно добавить какую-нибудь проверку
    assert 5
