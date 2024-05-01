class Locator(object):

    #URL = "https://cortland.com/apartments/cortland-at-valley-ranch/"
    #home page
    vr_label_bedrooms = "(//button//span[contains(text(),'Bedrooms')])[1]"
    vr_checkbox_beds = "(//button//span[contains(text(),'Bedrooms')])[1]"
    vr_button_search = "//button[@data-js-hook='filter-form-submit']"
    vr_button_cookie_close = "//button[@class='onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon']"

    #search results page
    vr_apartment_links = "//div[@class='apartments__card']//a"
    vr_text_beds = "//p[@class='floorplan-modal__info']"
    vr_text_floors = "//h1[@class='floorplan-modal__title']"
    vr_text_garage_status = "//p[contains(text(),'WITH ATTACHED GARAGE')]"
    vr_text_garage_status_2 = "//p[contains(text(),'With Attached Garage')]"
    vr_text_availability = "//p//span[contains(text(),'Available starting')]"

    # URL = "https://cortland.com/apartments/cortland-macarthur/"
    ma_label_bedrooms = "(//button[@class='header-2__finder-toggle'])[1]"
    ma_checkbox_beds = "(//button//span[contains(text(),'Bedrooms')])[1]"
    ma_button_search = "//button[@data-js-hook='filter-form-submit']"
    ma_button_cookie_close = "//button[@class='onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon']"

    # search results page
    ma_apartment_links = "//div[@class='apartments__card']//a"
    ma_text_beds = "//p[@class='floorplan-modal__info']"
    ma_text_floors = "//h1[@class='floorplan-modal__title']"
    ma_text_garage_status = "//p[contains(text(),'Attached Garage Select Homes')]"
    ma_text_garage_status_2 = "//p[contains(text(),'ATTACHED GARAGE SELECT HOMES')]"
    ma_text_availability = "//p//span[contains(text(),'Available starting')]"

    # URL = "https://cortland.com/apartments/cortland-north-plano/"
    np_label_bedrooms = "(//button[@class='header-2__finder-toggle'])[1]"
    np_checkbox_beds = "(//button//span[contains(text(),'Bedrooms')])[1]"
    np_button_search = "//button[@data-js-hook='filter-form-submit']"
    np_button_cookie_close = "//button[@class='onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon']"

    # search results page
    np_apartment_links = "//div[@class='apartments__card']//a"
    np_text_beds = "//p[@class='floorplan-modal__info']"
    np_text_floors = "//h1[@class='floorplan-modal__title']"
    np_text_garage_status = "//p[contains(text(),'WITH ATTACHED GARAGE')]"
    np_text_garage_status_2 = "//p[contains(text(),'With Attached Garage')]"
    np_text_availability = "//p//span[contains(text(),'Available starting')]"