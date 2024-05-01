import pandas as pd
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utilities.locators import Locator


class CommonActions:

    def __init__(self, driver):
        self.driver = driver

    def convert_results(self, listings, location):
        df = pd.DataFrame(listings)  # transpose to look just like the sheet above
        df.to_csv('/Users/KARIMAX12/Desktop/Projects/pythonProject/ApartmentHunt/Outputs/{}.csv'.format(location))


