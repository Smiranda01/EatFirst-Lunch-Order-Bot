from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ChooseDay:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_day_buttons_by_css_selector(self, selector):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        element_list = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return element_list

    def click_by_css_selector(self, selector):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        element.click()
