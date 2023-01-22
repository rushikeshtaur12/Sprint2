# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions
# driver_obj = webdriver.Chrome(ChromeDriverManager().install())
# driver_obj.get("https://www.goibibo.com/bus/")
# driver_obj.maximize_window()
# time.sleep(2)
# driver_obj.implicitly_wait(30)
#
# '''FROM'''
# driver_obj.find_element_by_id('autosuggestBusSRPSrcHome').send_keys("pun")
# driver_obj.find_element("xpath","//span[text()='Pune, Maharashtra']").click()
# time.sleep(2)
# '''TO'''
# driver_obj.find_element_by_id('autosuggestBusSRPDestHome').send_keys("Madiwal")
# driver_obj.find_element("xpath","//span[text()='Madiwala, Bangalore']").click()
# time.sleep(2)
# '''Date'''
#
# '''Search'''
# driver_obj.find_element("xpath","//button[text()='Search Bus']").click()
# time.sleep(2)
#
# '''apply filter'''
# driver_obj.find_element("xpath","//span[@class='Checkboxstyles__Checkmark-sc-17an8c7-1 cXxQSq'][1]").click() #Select popular
# time.sleep(2)
# driver_obj.find_element("xpath","//div[@class='FiltersBlockstyles__BusTypeFilterTab-sc-v6hq3g-12 djZxHm'][3]").click() #select bus type
# time.sleep(2)
#
# '''aminities'''
# # driver_obj.find_element("xpath","//a[text()='Amenities, Policies & Bus Details']").click() # select aminities
# # time.sleep(2)
# # driver_obj.find_element("xpath","//a[text()='Hide Details']").click()
# # time.sleep(2)
#
# '''click on select seat button'''
# driver_obj.find_element("xpath","//span[@class='SrpActiveCardstyles__PayTxtSpan-sc-yk1110-31 klFZUT'][1]").click()
# time.sleep(2)
#
# '''click on select droping button'''
# driver_obj.find_element("xpath","(//div[@class="BoardingDropingBoxstyles__WrapperBox-sc-djxci-0 cUIdyJ"])[2]//label[2]").click()
# time.sleep(2)
#
# '''select boarding '''
# driver_obj.find_element("xpath","//div[@class='BoardingDropingBoxstyles__WrapperBox-sc-djxci-0 cUIdyJ']//label[2]").click()
# time.sleep(2)
#
# '''select seat'''
# driver_obj.find_element("xpath","//div[@class='SeatWithTooltipstyles__BusSleeper-sc-dkrka-1 egpDPe']").click()
# time.sleep(2)
#
# '''click on continue'''
# driver_obj.find_element("xpath","//button[@class='SelectSeatTabContentstyles__Button-sc-aw7o7o-9 cZetwz']").click()
# time.sleep(2)
#
# '''Insurance'''
# driver_obj.find_element("xpath","//div[@class='InsuranceBlockstyles__CheckboxWrap-sc-jgljyo-7 UusRp']//label[2]").click()
# time.sleep(2)
#
# '''Traveller details'''
# name
# driver_obj.find_element("xpath","//input[@placeholder='Enter Full Name']").send_keys("Rushikesh Taur")
# time.sleep(2)
#
# '''Age'''
# driver_obj.find_element("xpath","//input[@placeholder='Age']").send_keys("22")
# time.sleep(2)
#
# '''gender'''
# # driver_obj.find_element("xpath","//li[@class='genderTabsList selected']").click()
# # time.sleep(2)
#
# '''Contact deatils'''
# '''Email '''
# driver_obj.find_element("xpath","//input[@placeholder='Enter Email Address']").send_keys("rushikeshtaur12@gmail.com")
# time.sleep(2)
#
# '''mobile number'''
# driver_obj.find_element("xpath","//input[@placeholder='Enter Mobile Number']").send_keys("7057456772")
# time.sleep(2)
#
# '''payment'''
# driver_obj.find_element("xpath","//button[@class='ReviewPagestyles__PayButton-sc-fmjc42-13 bYqmLn']").click()
# time.sleep(2)