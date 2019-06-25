from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Scripts.PO.Locators.locators import HomepageLocators
from Scripts.PO.BasePage import  BasePage



class HomePage(BasePage):
    """Home page action methods come here. I.e. Python.org"""
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(HomepageLocators.URL)

    def search_by(self,search_content):
        """Triggers the search"""
        search_icon = self.driver.find_element(*HomepageLocators.SEARCH_BAR)
        search_icon.send_keys(search_content)
        self.driver.find_element(*HomepageLocators.SEARCH_BUTTON).click()








