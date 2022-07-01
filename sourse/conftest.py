import pytest

from sourse import settings
from sourse.web_driver import WebDriver

@pytest.fixture(scope='session')
def driver():
    """Данная функция является фикстурой, которая инициализирует браузер.

    Все, что выполняется до метода "yield" по сути является SetUp методом, а после - TearDown методом
    """

    fixture = WebDriver(base_url=settings.BASE_URL)
    yield fixture
    fixture.quit()
