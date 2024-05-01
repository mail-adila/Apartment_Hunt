import sys
from selenium.webdriver.common.by import By
from Utilities.locators import Locator

sys.path.append(sys.path[0] + "/....")


# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())


class HomeMacArthur(object):

    URL = "https://cortland.com/apartments/cortland-macarthur/"

    def __init__(self, driver):
        self.driver = driver
        self.label_bedrooms = driver.find_element(By.XPATH, Locator.ma_label_bedrooms)
        self.checkbox_beds = driver.find_element(By.XPATH, Locator.ma_checkbox_beds)
        self.button_search = driver.find_element(By.XPATH, Locator.ma_button_search)
        self.close_cookies = driver.find_element(By.XPATH, Locator.ma_button_cookie_close)

    def get_cookie_close_button(self):
        return self.close_cookies

    def get_bedroom_label(self):
        return self.label_bedrooms

    def get_beds_checkbox(self):
        return self.checkbox_beds

    def get_search_button(self):
        return self.button_search

    def launch_home(self):
        self.get_bedroom_label().click()
        self.get_beds_checkbox().click()
        self.get_search_button().click()