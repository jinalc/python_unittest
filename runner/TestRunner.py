from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from test.TestCase1 import AccessGooglePage
from test.TestCase2 import TestCalc

tc1 = TestLoader().loadTestsFromTestCase(AccessGooglePage)
tc2 = TestLoader().loadTestsFromTestCase(TestCalc)

sanityTestSuites = TestSuite([tc1])
funTestSuites = TestSuite([tc2])
masterTestSuites = TestSuite([tc1, tc2])

testRunner = HTMLTestRunner(output='./reports/pyResult.html', report_title='My Report', add_timestamp=True, open_in_browser=True, combine_reports=True)
testRunner.run(masterTestSuites)
