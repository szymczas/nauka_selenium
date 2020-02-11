import pytest
from selenium import webdriver

@pytest.fixture()
def test_setup():
    global driver
    chrome_path = r"C:\Users\szymon.hubicki\PycharmProjects\tutorial_selenium\drivers\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.get("https://stag.dazn.com")
    driver.maximize_window()
    yield
    driver.quit()


def test_method(test_setup):
    assert driver.title =="DAZN"

def test_method(test_setup):
    assert driver.title =="DAZN"