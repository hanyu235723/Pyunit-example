from selenium import webdriver
import unittest
from Scripts.PO.homePage import HomePage
import Library.Old_HTMLTestRunner as my_runner

from Scripts.PO.homePage import *
from Scripts.PO.SearchResultPage import SearchResultsPage

class  my_test(unittest.TestCase):
    def setUp(self):
        print("test script1-set up ")

    def test_search(self):
        print("test script1")
    def tearDown(self):
        print("test script1-teardown")


testcase = unittest.TestLoader().loadTestsFromTestCase(my_test)
testsuite = unittest.TestSuite()
testsuite.addTest(testcase)
report_file= "e:\\result1.html"
with open(report_file, 'w') as report:

    runner = my_runner.HTMLTestRunner(
        stream=report,
        title='My unit test',
        description='This demonstrates the report output by HTMLTestRunner.'
    )

     # run the test
    runner.run(testsuite)

































