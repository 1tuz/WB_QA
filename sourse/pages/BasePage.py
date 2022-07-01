from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from sourse.web_driver import WebDriver


class BasePageLocators:
    """Класс BasePageLocators является хранилищем локаторов для поиска элементов. Здесь собраны общие локаторы, которые
    будут актуальны на всех страницах и вкладках.
    """
    pass


class BasePage:
    """Класс BasePage является родительским классом всех остальных объектов страниц. В нем собраны основные методы,
    которые могут быть использованы почти на всех страницах

    Parameters
    ----------
    driver
        Драйвер, который управляет браузером и действиями. Определен в методе driver() файла conftest.py.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver.driver
        self.base_url = driver.base_url

    def find_element_visibility(self, locator: tuple, time: int = 10):
        """Поиск элемента на странице. Элемент будет найден, если он будет визуально отображен на ней.

        Parameters
        ----------
        locator: tuple
            Локатор элемента по которому осуществляется поиск.
        time: int, optional, default=10
            Время, в течение которого будет осуществляться поиск в секундах.

        Raises
        -------
        selenium.common.exceptions.TimeoutException
            Элемент не найден за указанное время

        Returns
        -------
        field
            Найденный элемент
        """

        field = WebDriverWait(self.driver, time).until(
            ec.visibility_of_element_located(locator),
            message=f"Не найден элемент по локатору - {locator}"
        )
        return field

    def find_elements_visibility(self, locator: tuple, time: int or float = 10):
        """Поиск элементов на странице. Элементы будут найдены, если они будут визуально отображены на ней.
        Может найти не все элементы если во время запроса некоторые уже отобразились, то будут возвращены те,
        что загрузились. Часто случается, что возвращает один элемент, а остальные не успевают прогрузиться.
        Возможно лучше будет использовать метод "find_elements_presence".

        Parameters
        ----------
        locator: tuple
            Локатор элемента по которому осуществляется поиск.
        time: int or float, optional, default=10
            Время, в течение которого будет осуществляться поиск в секундах.

        Raises
        -------
        selenium.common.exceptions.TimeoutException
            Элементы не найдены

        Returns
        -------
        fields:
            Список найденных элементов
        """

        fields = WebDriverWait(self.driver, time).until(
            ec.visibility_of_all_elements_located(locator),
            message=f"Не найдены элементы по локатору - {locator}"
        )
        return fields

    def find_element_presence(self, locator: tuple, time: int = 10):
        """Поиск элемента на странице. Элемент будет найден, если он присутствует в коде страницы.

        Parameters
        ----------
        locator: tuple
            Локатор элемента по которому осуществляется поиск.
        time: int, optional, default=10
            Время, в течение которого будет осуществляться поиск в секундах.

        Raises
        -------
        selenium.common.exceptions.TimeoutException
            Элемент не найден за указанное время

        Returns
        -------
        field
            Найденный элемент
        """

        field = WebDriverWait(self.driver, time).until(
            ec.presence_of_element_located(locator),
            message=f"Не найден элемент по локатору - {locator}"
        )
        return field

    def find_elements_presence(self, locator: tuple, time: int = 10):
        """Поиск элементов на странице. Элементы будут найдены, если они присутствуют в коде страницы.

        Parameters
        ----------
        locator: tuple
            Локатор элемента по которому осуществляется поиск.
        time: int, optional, default=10
            Время, в течение которого будет осуществляться поиск в секундах.

        Raises
        -------
        selenium.common.exceptions.TimeoutException
            Элемент не найден за указанное время

        Returns
        -------
        fields
            Список найденных элементов
        """

        fields = WebDriverWait(self.driver, time).until(
            ec.presence_of_all_elements_located(locator),
            message=f"Не найдены элементы по локатору - {locator}"
        )
        return fields

    def invisibility_element(self, locator: tuple, time: int = 10):
        """Поиск элемента на странице при условии его невидимости на странице

        Parameters
        ----------
        locator: tuple
            Локатор элемента по которому осуществляется поиск.
        time: int, optional, default=10
            Время, в течение которого будет осуществляться поиск в секундах.

        Raises
        -------
        selenium.common.exceptions.TimeoutException
            Элемент не найден за указанное время

        Returns
        -------
        field
            возвращает найденный элемент
        """

        field = WebDriverWait(self.driver, time).until(
            ec.invisibility_of_element(locator),
            message=f"Не найден элемент по локатору - {locator}"
        )
        return field

    def go_to_home_page(self):
        """Переход на домашнюю страницу"""

        self.driver.get(self.base_url)

    def get_current_url(self):
        """Получить текущий url-адрес

        Returns
        -------
        current_url: str
            Текущий url
        """

        return self.driver.current_url

    def refresh(self):
        """Перезагрузка страницы"""

        return self.driver.refresh()


    def clear_field(self, field):
        """Очистить поле ввода от текста. Поле должно быть заполнено без прокрутки. Очищает только видимую часть
        текста. Если текста больше, то следует использовать несколько раз

        Parameters
        ----------
        field
            Объект поля, подлежащий очистке

        Returns
        -------
        field:
            Объект поля, с которым при необходимости можно взаимодействовать
        """

        field.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
        return field

    def scroll_up_page(self):
        """Прокрутить вверх страницы"""

        self.driver.execute_script("window.scrollTo(0, 0)")


    def go_to_url(self, url):
        """Переход на url

        Parameters
        ----------
        url
           Адрес на который необходимо перейти
        """

        self.driver.get(url)
