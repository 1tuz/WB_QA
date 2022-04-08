from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriver:
    """Класс WebDriver представляет собой инициализатор запускаемого браузера с необходимыми параметрами

    Parameters
    ----------
    base_url: str
        Базовый url сайта, на котором проводится тестирование. Прописывается в файле settings.py (с его помощью можно
        менять тестируемые сайты)
    """

    def __init__(self, base_url: str):
        options = webdriver.ChromeOptions()

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(options=options, service=service)
        self.driver.maximize_window()
        self.base_url = base_url

    def quit(self):
        """Закрыть браузер"""

        self.driver.quit()
