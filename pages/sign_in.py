from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Sign_in:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_by_css_selector(self, selector):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        element = self.driver.find_element(By.CSS_SELECTOR, selector)

        element.click()

    def click_by_xpath(self, xpath):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

    def click_by_class_name(self, class_name):
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
        element = self.driver.find_element(By.CLASS_NAME, class_name)
        element.click()

    def send_keys_by_id(self, id_value, query):
        self.wait.until(EC.presence_of_all_elements_located((By.ID, id_value)))
        element = self.driver.find_element(By.ID, id_value)
        element.send_keys(query)







