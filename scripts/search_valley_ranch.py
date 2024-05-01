import sys
import time
import unittest
from Utilities.web_driver_setup import WebDriverSetup
from Locations.home_valley_ranch import HomeValleyRanch
from Locations.results_valley_ranch import ResultsValleyRanch
from Utilities.common_actions import CommonActions

sys.path.append(sys.path[0] + "/...")


class SearchValleyRanch(WebDriverSetup):

    def test_Valley_Ranch(self):

        # Launch URL and set base for search
        driver = self.driver
        driver.get(HomeValleyRanch.URL)
        self.driver.set_page_load_timeout(60)

        # Launch Valley ranch cortland homepage and set the search criteria
        valley_ranch_page = HomeValleyRanch(driver)
        valley_ranch_page.launch_home()

        # Scroll the results to show the availability table
        driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(5)

        # Iterate the listings found to filter the required results
        valley_ranch_search_page = ResultsValleyRanch(driver)
        available_apartments = valley_ranch_search_page.get_listings()

        # Add the required results into .csv file available under Outputs folder
        actions = CommonActions(driver)
        actions.convert_results(available_apartments, "Valley_Ranch")


if __name__ == '__main__':
    unittest.main()
