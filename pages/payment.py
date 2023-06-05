from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Payment:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def find_elements_by_css(self, selector):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        element_list = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return element_list

    def find_element_by_css(self, selector):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        return element

    def click_by_css_selector(self, selector):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        element.click()

    def click_by_xpath(self, xpath):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        element.click()

