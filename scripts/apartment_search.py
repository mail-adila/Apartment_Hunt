import time
import pandas as pd
import ssl
import smtplib, email

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from email.message import EmailMessage
from selenium.webdriver.support import expected_conditions as EC

URL = "https://cortland.com/apartments/cortland-at-valley-ranch/"
driver = webdriver.Chrome()


def launch():
    driver.maximize_window()
    driver.get(URL)


def set_search_criteria():
    driver.implicitly_wait(10)
    bedrooms = driver.find_element(By.XPATH, "(//button//span[contains(text(),'Bedrooms')])[1]")
    bedrooms.click()
    beds = driver.find_element(By.XPATH, "//label[@for='faux-bed-3']")
    beds.click()
    search_button = driver.find_element(By.XPATH, "//button[@data-js-hook='filter-form-submit']")
    search_button.click()

    driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(5)
    driver.find_element(By.XPATH,
                        "//button[@class='onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon']").click()

    apartments_on_this_floor = driver.find_elements(By.XPATH, "//div[@class='apartments__card']//a")
    return apartments_on_this_floor


def get_listings(apartments_on_this_floor):
    main_window = driver.current_window_handle
    listings = []
    try:
        for apartment in apartments_on_this_floor:
            try:
                link = apartment.get_attribute('href')
            except NoSuchElementException:
                continue
            driver.execute_script("window.open('');")
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            apartment_window = driver.window_handles[1]
            driver.switch_to.window(apartment_window)
            driver.get(link)
            beds = (
                (driver.find_element(By.XPATH, "//p[@class='floorplan-modal__info']").text.split('|')[0]).split(' ')[
                    0])
            floor = (driver.find_element(By.XPATH, "//h1[@class='floorplan-modal__title']").text.split('#')[1])[
                    :1]
            if int(beds) > 1 and int(floor) < 3:
                garage_status = False
                garage_status_2 = False
                try:
                    garage_status = driver.find_element(By.XPATH, "//p[contains(text(),'WITH ATTACHED GARAGE')]")
                except NoSuchElementException:
                    garage_found = False
                try:
                    garage_status_2 = driver.find_element(By.XPATH,
                                                          "//p[contains(text(),'With Attached Garage')]")
                except NoSuchElementException:
                    garage_found = False
                garage_found = garage_status or garage_status_2
                try:
                    availability = driver.find_element(By.XPATH,
                                                       "//p//span[contains(text(),'Available starting')]").text
                    start_date = availability.split(' ')[2]
                except NoSuchElementException:
                    start_date = "Available Now"
                if garage_found:
                    apt_with_garages = {"Floor": floor, "Beds": int(beds), "Link": link, "Starting": start_date}
                    listings.append(apt_with_garages)
            driver.close()
            driver.switch_to.window(main_window)
    except NoSuchElementException:
        for items in listings:
            print(items)
    for items in listings:
        print(items)
    return listings


def convert_results(listings):
    df = pd.DataFrame(listings)  # transpose to look just like the sheet above
    df.to_csv('file.csv')
    # df.to_excel('file.xls')
    # send_mail('adila.test.automation@gmail.com', 'sahal.mec@gmail.com', 'Apartment listing at Valley Ranch', 'file.csv')


def send_mail(send_from, send_to, subject, text, files=None,
              server="127.0.0.1"):
    password = 'cmzh pqos hait wudw'
    body = """
    Test mail from python
    """
    em = EmailMessage()
    em['From'] = send_from
    em['To'] = send_to
    em['Subject'] = subject
    em.set_content('body')
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.google.com', 465, context=context) as smtp:
        smtp.login(send_from, password)
        smtp.sendmail(send_from, send_to, em.as_string())


def search():
    launch()
    apartments_available = set_search_criteria()
    results = get_listings(apartments_available)
    convert_results(results)


search()
