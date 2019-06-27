from selenium import webdriver
import unittest
from HtmlTestRunner import HTMLTestRunner

from Scripts.PO.homePage import *
from Scripts.PO.SearchResultPage import SearchResultsPage

class  my_test2(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

    def test_search(self):
        homepage= HomePage(self.driver)
        homepage.search_by("swim suit")
        search_results_page=SearchResultsPage(self.driver)

        assert search_results_page.is_results_found()

    def tearDown(self):
        self.driver.quit()

testsuite=unittest.TestLoader().loadTestsFromTestCase(my_test2)

runner = HTMLTestRunner(output='../../Report/', verbosity=3,
        template=None, resultclass=None,
         add_timestamp=True, open_in_browser=True,
         combine_reports=True, template_args=None)
runner.run(testsuite)

























