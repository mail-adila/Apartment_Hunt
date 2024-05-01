import os
import sys

import pandas as pd
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.locators import Locator

sys.path.append(sys.path[0] + "/....")


class ResultsNorthPlano(object):

    def __init__(self, driver):
        self.driver = driver
        self.apartment_links = driver.find_elements(By.XPATH, Locator.np_apartment_links)

    def get_apartment_links(self):
        return self.apartment_links

    def get_listings(self):
        main_window = self.driver.current_window_handle
        listings = []
        apartments_on_this_floor = self.get_apartment_links()
        try:
            for apartment in apartments_on_this_floor:
                try:
                    link = apartment.get_attribute('href')
                except NoSuchElementException:
                    continue
                self.driver.execute_script("window.open('');")
                WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
                apartment_window = self.driver.window_handles[1]
                self.driver.switch_to.window(apartment_window)
                self.driver.get(link)
                beds = ((self.driver.find_element(By.XPATH, Locator.np_text_beds).text.split('|')[0]).split(' ')[0])
                floor = (self.driver.find_element(By.XPATH, Locator.np_text_floors).text.split('#')[1])
                floor = int(floor[:1])+1
                if int(beds) > 1 and floor < 3:
                    garage_status = False
                    garage_status_2 = False
                    try:
                        garage_status = self.driver.find_element(By.XPATH, Locator.np_text_garage_status)
                    except NoSuchElementException:
                        garage_found = False
                    try:
                        garage_status_2 = self.driver.find_element(By.XPATH, Locator.np_text_garage_status_2)
                    except NoSuchElementException:
                        garage_found = False
                    garage_found = garage_status or garage_status_2
                    try:
                        availability = self.driver.find_element(By.XPATH, Locator.np_text_availability).text
                        start_date = availability.split(' ')[2]
                    except NoSuchElementException:
                        start_date = "Available Now"
                    if garage_found:
                        apt_with_garages = {"Floor": floor, "Beds": int(beds), "Link": link, "Starting": start_date}
                        listings.append(apt_with_garages)
                self.driver.close()
                self.driver.switch_to.window(main_window)
        except NoSuchElementException:
            for items in listings:
                print(items)
        for items in listings:
            print(items)
        return listings


