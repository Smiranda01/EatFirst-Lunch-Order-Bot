from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Checkout:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_by_css_selector(self, selector):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        element.click()

    def send_keys_by_id(self, id_value, query):
        self.wait.until(EC.presence_of_all_elements_located((By.ID, id_value)))
        element = self.driver.find_element(By.ID, id_value)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        element.send_keys(query)
