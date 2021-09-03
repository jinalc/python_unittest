import unittest
from selenium.common.exceptions import NoSuchElementException
from utility.utils import Utils
from logs.log import logger


class AccessGooglePage(unittest.TestCase):

    @classmethod
    def setUp(cls):
        Utils.setUp(cls)

    @classmethod
    def tearDown(cls):
        Utils.tearDown(cls)

    def test_something(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("Selenium WebDriver Interview questions")
        self.search_field.submit()

    def test_take_screenshot(self):
        try:
            self.gmail_link = self.driver.find_element_by_xpath("//a[contains(text(),'Gmail')]")
            self.gmail_link.is_displayed()
            logger.debug(self.gmail_link.text)
            self.gmail_link.click()
        except:
            NoSuchElementException
        self.driver.save_screenshot("gmail_page.png")


if __name__ == '__main__':
    unittest.main()

# testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\pythontestautomation\reports')
