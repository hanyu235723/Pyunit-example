
from selenium.webdriver.common.by import  By

class HomepageLocators():
    URL='https://amazon.com'
    SEARCH_BAR = (By.CSS_SELECTOR,'#twotabsearchtextbox')
    SEARCH_BUTTON = (By.CSS_SELECTOR,'#nav-search input[type="submit"] ')

class SearchResultPagelocators():
    SEARCH_RESULT_TEXT = '#search span[]'

