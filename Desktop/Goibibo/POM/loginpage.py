import time
from librery.config import Config
from Data.reading_objects import ReadExel

read_xl = ReadExel()         # Creating object for reading Locators
login_obj=read_xl.read_locater(Config.read_locators)

class login:

    def __init__(self,driver):
        self.driver=driver

    # selecting arrival place in FROM textfield
    def select_arrival_places(self,arrival_point):
        self.driver.find_element(*login_obj['tc_FROM']).send_keys(arrival_point)
        time.sleep(2)

        self.driver.find_element(*login_obj['tc_select_arrival']).click()
        time.sleep(2)

    # For selecting destination place in TO textfield
    def select_destination_places(self,destination_point):
        self.driver.find_element(*login_obj['tc_TO']).send_keys(destination_point)
        time.sleep(2)

        self.driver.find_element(*login_obj['tc_select_departure']).click()
        time.sleep(2)

    # For select date
    def date(self):
        self.driver.find_element(*login_obj['tc_click_date']).click()
        time.sleep(2)

        self.driver.find_element(*login_obj['tc_select_date']).click()
        time.sleep(2)

    # For click on SEARCH button
    def search(self):
        self.driver.find_element(*login_obj['tc_search']).click()
        time.sleep(5)

    # For applying filters
    def filter(self):
        self.driver.find_element(*login_obj['tc_filter_1']).click()
        time.sleep(2)

        '''self.driver.find_element(*login_obj['tc_filter_2']).click()
        time.sleep(2)
        
    # For click on aminities
    def aminities(self):
        self.driver.find_element(*login_obj['tc_bus_details']).click()
        time.sleep(2)

        self.driver.find_element(*login_obj['tc_hide_details']).click()
        time.sleep(2)'''

    # For click on SELECT SEAT
    def select_seat(self):
        self.driver.find_element(*login_obj['tc_select_seat']).click()
        time.sleep(2)

    # For select boarding point
    def select_boarding(self):
        self.driver.find_element(*login_obj['to_select_boarding']).click()
        time.sleep(2)

    # For select dropping point
    def select_dropping(self):
        self.driver.find_element(*login_obj['to_select_dropping']).click()
        time.sleep(2)

    # For choose seat
    def choose_seat(self):
        self.driver.find_element(*login_obj['to_choose_seat']).click()
        time.sleep(2)

    # For click on CONTINUE
    def click_continue(self):
        self.driver.find_element(*login_obj['to_continue']).click()
        time.sleep(2)

    # For click on one INSURANCE radio button
    def insurance(self):
        self.driver.find_element(*login_obj['insurance']).click()
        time.sleep(2)

    # For enter Traveller Name in Full Name text-field
    def traveller_name(self,passenger_name):
        self.driver.find_element(*login_obj['traveller_name']).send_keys(passenger_name)
        time.sleep(2)

    # For enter Traveller age in Age text field
    def age(self,passenger_age):
        self.driver.find_element(*login_obj['tc_age']).send_keys(passenger_age)
        time.sleep(2)

    # For select gender
    def gender(self):
        self.driver.find_element(*login_obj['tc_gender']).click()
        time.sleep(2)

    # For enter email in Contact detail Email-id text-field
    def email(self,passenger_email):
        self.driver.find_element(*login_obj['tc_email']).send_keys(passenger_email)
        time.sleep(2)

    # For enter mobile number in Contact detail's Mobile number text-field
    def mobile_number(self,passenger_mobile_number):
        self.driver.find_element(*login_obj['tc_mobile_number']).send_keys(passenger_mobile_number)
        time.sleep(2)

    # For payment
    def payment(self):
        self.driver.find_element(*login_obj['tc_payment']).click()
        time.sleep(2)



