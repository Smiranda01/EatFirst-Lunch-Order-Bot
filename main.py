import time
import os
from driver import Driver
from pages.sign_in import Sign_in
from pages.choose_address import ChooseAddress
from pages.choose_day import ChooseDay
from pages.food import FoodOrder
from pages.checkout import Checkout
from pages.payment import Payment
from pages.new_order import NewOrder
from pages.prehome import Pre_home
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
from random import randint


load_dotenv()
driver = Driver(os.getenv("DRIVER_LOC"))
driver = driver.run_driver()
driver.get(
    "https://www.eatfirst.com.au/en-AU/choose-supplier?idAddress=270748&lat=-34.022273&lng=151.1981355&line2=238+Captain+Cook+Drive&city=Kurnell&region=NSW&postalCode=2231&country=Australia")
today = datetime.today()
today_name = today.strftime("%A")
print(today_name)

# Sign in
sign_in_page = Sign_in(driver)
sign_button = sign_in_page.click_by_css_selector(".sub-nav-container button.sds-btn.sds-btn-outline")
time.sleep(1)
#x = sign_in_page.click_by_class_name("iubenda-cs-close-btn")
username_input = sign_in_page.send_keys_by_id("Email", os.getenv("EMAIL"))
password_input = sign_in_page.send_keys_by_id("exampleInputPasswordLogin", os.getenv("PASSWORD"))
sign_in_button = sign_in_page.click_by_css_selector("button.sds-btn.sds-btn-primary")

for i in range(3,5):
    food_random_manager = randint(1, 4)
    print(food_random_manager)
    # Choose address
    choose_address_page = ChooseAddress(driver)
    dropdown_menu = choose_address_page.click_by_css_selector("#chooseSupplier .dropdown-item-container.customselect")
    time.sleep(1)
    address = choose_address_page.click_by_css_selector("#chooseSupplier li[value='0']")
    # Choose day
    choose_day_page = ChooseDay(driver)
    day_elements = choose_day_page.get_day_buttons_by_css_selector(
        ".all-supplier-list .hotspot-info a[style='cursor: pointer;']")
    day_elements_names = [str(day.get_attribute("href")).split("_")[1].replace("-", "") for day in day_elements]
    try:
        print(day_elements_names[i])
        day_elements[i].click()

    except Exception as e:
        print(f"Could not click on the element: {e}")
    time.sleep(1)

    #     Click on the foods we want to order from Food Order page
    food_order_page = FoodOrder(driver)
    if food_random_manager == 1:
        food_order_page.order_chicken_schnitzel_wrap()
    elif food_random_manager == 2:
        food_order_page.order_club_sette_sandwich()
    elif food_random_manager == 3:
        food_order_page.order_poached_chicken_sandwich()
    elif food_random_manager == 4:
        food_order_page.order_southern_fried_wrap()

    time.sleep(2)
    # choose_date_button = food_order_page.click_by_css_selector(".cart-btn .sds-btn.sds-btn-outline")
    try:
        dates = food_order_page.find_elements_by_css("div.react-datepicker__day:not(.react-datepicker__day--disabled)")
        dates_text = [date.text for date in dates]
        print(dates_text)
    except TimeoutException:
        next_month = food_order_page.click_by_css_selector("a.react-datepicker__navigation.react-datepicker__navigation--next")
        dates = food_order_page.find_elements_by_css("div.react-datepicker__day:not(.react-datepicker__day--disabled)")
        dates_text = [date.text for date in dates]
        print(dates_text)

    if today_name == day_elements_names[i]:
        dates[1].click()
    else:
        dates[0].click()

    set_time_bar = food_order_page.click_by_css_selector(".col-md-12.pad0 .dropdown-item")
    hour = food_order_page.click_by_xpath("//a[contains(@class, 'delivery-times-dropdown__link') and contains(text(), '12:00 pm')]")
    proceed_to_cart = food_order_page.click_by_css_selector(".cart-btn button.sds-btn.sds-btn-secondary")
    checkout = food_order_page.click_by_css_selector(".cart-btn button.sds-btn.sds-btn-primary")

    #    Type query and proceed to payment
    checkout_page = Checkout(driver)
    query_box = checkout_page.send_keys_by_id("DeliveryInstructions", ".")
    time.sleep(1)
    continue_to_payment = checkout_page.click_by_css_selector(".button-group .sds-btn.sds-btn-primary")

    #     Choose department and delivery time. Then make payment
    payment_page = Payment(driver)
    dropdown_list = payment_page.find_elements_by_css(
        ".generic-dropdown1 .sds-select.sds-select-single.sds-select-show-arrow")
    payment_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
                                       dropdown_list[0])
    time.sleep(1)
    dropdown_list[0].click()
    time.sleep(1)
    for _ in range(2):
        try:
            departments = payment_page.find_elements_by_css("div.sds-select-item.sds-select-item-option")
            payment_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", departments[3])
            time.sleep(1)
            if i == 2:
                departments[5].click()
        except TimeoutException:
            payment_page.click_by_xpath('//div[contains(@class, "sds-select-item-option-content") and text()="15| IT"]')
            time.sleep(1)

    payment_page.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", dropdown_list[1])
    time.sleep(1)
    dropdown_list[1].click()
    time_lunch = payment_page.click_by_xpath("//div[@class='sds-select-item-option-content' and text()='LUNCH']")
    make_payment = payment_page.click_by_css_selector("button.sds-btn.sds-btn-primary")

    # Press new order button and start again
    new_order_page = NewOrder(driver)
    new_order_page.click_by_css_selector("a.sds-btn.sds-btn-primary")

    # Press SM button to continue the loop
    pre_home_page = Pre_home(driver)
    pre_home_page.click_by_css_selector("button.uppercase.font-bold")

