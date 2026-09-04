import pytest
from selenium import webdriver

from api.betting_client import BettingClient
from config import BASE_URL, USER_ID


@pytest.fixture
def api_client():
    return BettingClient(BASE_URL, USER_ID)


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()