import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from librery.config import Config
from webdriver_manager.microsoft import EdgeChromiumDriverManager # cross browsing
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["Chrome","Safari"])
def _driver(request):
    if request.param == "Chrome":
        driver_obj = webdriver.Chrome(ChromeDriverManager().install())

    elif request.param == "Safari":
        driver_obj = webdriver.Safari()


    driver_obj.get(Config.URL)
    driver_obj.implicitly_wait(30)
    driver_obj.maximize_window()
    yield driver_obj
    print(driver_obj.title)
    # driver_obj.save_screenshot("test_loginpage.png")
    # driver_obj.close()