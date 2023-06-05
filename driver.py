from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service


class Driver:

    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.chrome_options = ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument("--start-maximized")
        self.chrome_service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=self.chrome_service, options=self.chrome_options)

    def run_driver(self):
        return self.driver
