from selenium import webdriver
import unittest
from HtmlTestRunner import HTMLTestRunner


from Scripts.PO.homePage import *
from Scripts.PO.SearchResultPage import SearchResultsPage

class  my_test(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

    def test_search(self):
        homepage= HomePage(self.driver)
        homepage.search_by("toy")
        search_results_page=SearchResultsPage(self.driver)

        assert search_results_page.is_results_found()

    def tearDown(self):
        self.driver.quit()


testcase=unittest.TestLoader().loadTestsFromTestCase(my_test)
testsuite = unittest.TestSuite(testcase)

runner = HTMLTestRunner(output='../../Report/', verbosity=3,
         descriptions="unit test resulf amazon", failfast=True, buffer=False,
         report_title="My Test Report", report_name="report name", template=None, resultclass=None,
         add_timestamp=True, open_in_browser=False,
         combine_reports=False, template_args=None)
runner.run(testsuite)

























