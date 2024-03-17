from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FoodOrder:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_by_css_selector(self, selector):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        element.click()

    def click_by_xpath(self, xpath):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        element.click()

    def click_by_id(self, id_value):
        self.wait.until(EC.element_to_be_clickable((By.ID, id_value)))
        element = self.driver.find_element(By.ID, id_value)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        element.click()

    def find_elements_by_css(self, selector):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        element_list = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return element_list

    def order_chicken_schnitzel_wrap(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[6]/div[2]/div[11]/div[1]/div')))
        element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[6]/div[2]/div[11]/div[1]/div')
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        element.click()
        self.click_by_css_selector("div.sds-select.sds-select-filled.sds-select-single.sds-select-show-arrow")
        self.click_by_xpath("//div[contains(text(), '1 guest')]")
        self.click_by_css_selector("label[for='subItem112467_1'")
        self.click_by_css_selector("label[for='subItem112460_1'")
        self.click_by_css_selector("label[for='subItem112461_1'")
        self.click_by_css_selector(".modal-footer.modal__cart-review button.sds-btn.sds-btn-primary")

    def order_deconstructed_burger_beef(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[6]/div[2]/div[40]")))
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[6]/div[2]/div[40]")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        element.click()
        self.click_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div[3]/div/div/div[1]/div/div")
        self.click_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]")
        self.click_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div/button")

    def order_deconstructed_burger_chicken(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[6]/div[2]/div[40]")))
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[6]/div[2]/div[40]")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        element.click()
        self.click_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div")
        self.click_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]")
        self.click_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div/button")

    def order_southern_fried_wrap(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[6]/div[2]/div[4]/div[1]")))
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[6]/div[2]/div[4]/div[1]")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        element.click()
        self.click_by_css_selector("div.sds-select.sds-select-filled.sds-select-single.sds-select-show-arrow")
        self.click_by_xpath("//div[contains(text(), '1 guest')]")
        self.click_by_css_selector("label[for='subItem112467_1'")
        self.click_by_css_selector("label[for='subItem112460_1'")
        self.click_by_css_selector("label[for='subItem112461_1'")
        self.click_by_css_selector(".modal-footer.modal__cart-review button.sds-btn.sds-btn-primary")

    def order_fruit(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[7]/div[2]/div[2]")))
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[7]/div[2]/div[2]")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        element.click()
        self.click_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div/div[1]")
        self.click_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]")
        self.click_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div/button")

    def order_breakfast(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div[2]/div")))
        element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div[2]/div")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        element.click()
        self.click_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div[3]/div/div/div[1]/div/div")
        self.click_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div")
        self.click_by_xpath("/html/body/div[4]/div/div[2]/div/div[2]/div/div[2]/div/button")

