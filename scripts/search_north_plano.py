import sys
import time
import unittest
from Utilities.web_driver_setup import WebDriverSetup
from Locations.home_north_plano import HomeNorthPlano
from Locations.results_north_plano import ResultsNorthPlano
from Utilities.common_actions import CommonActions

sys.path.append(sys.path[0] + "/...")


class SearchNorthPlano(WebDriverSetup):

    def test_North_Plano(self):

        # Launch URL and set base for search
        driver = self.driver
        driver.get(HomeNorthPlano.URL)
        self.driver.set_page_load_timeout(60)

        # Launch Valley ranch cortland homepage and set the search criteria
        valley_ranch_page = HomeNorthPlano(driver)
        valley_ranch_page.launch_home()

        # Scroll the results to show the availability table
        driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(5)

        # Iterate the listings found to filter the required results
        north_plano_search_page = ResultsNorthPlano(driver)
        available_apartments = north_plano_search_page.get_listings()

        # Add the required results into .csv file available under Outputs folder
        actions = CommonActions(driver)
        actions.convert_results(available_apartments, "North_Plano")


if __name__ == '__main__':
    unittest.main()
