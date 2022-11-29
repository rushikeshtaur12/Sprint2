import datetime
import pytest
import  time
from  POM.loginpage import login
from Data.reading_objects import ReadExel
from  librery.config import Config

class TestLoginPage:
    read_xl=ReadExel()
    data=read_xl.read_testdata(Config.read_test_data_sheet)
    @pytest.mark.parametrize ('arrival_point,  destination_point ,  passenger_name, passenger_age, passenger_email, passenger_mobile_number', data)
    def test_click_rr(self, arrival_point, destination_point, passenger_name, passenger_age, passenger_email, passenger_mobile_number, _driver):
        driver= _driver
        try:
            rr=login(_driver)    #loginpage.py class
            rr.select_arrival_places(arrival_point)
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.select_destination_places(destination_point)
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.date()
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.search()
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.filter()
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.select_seat()
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.select_boarding()
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.select_dropping()
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.choose_seat()
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.click_continue()
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.insurance()
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.traveller_name(passenger_name)
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.age(passenger_age)
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.gender()
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.email(passenger_email)
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.mobile_number(passenger_mobile_number)
            time.sleep(2)
            driver.implicitly_wait(30)
            rr.payment()
            time.sleep(6)
            driver.implicitly_wait(30)
        except AssertionError as error_msg:
            td = datetime.datetime.now()
            name = f'screenshot_{td.hour}{td.minute}{td.second}.png'
            driver.save_screenshot(Config.screenshot_path + name)
            raise error_msg






