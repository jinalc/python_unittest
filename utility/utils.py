from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import configparser
from config import path


class Utils:
    def setUp(self):
        # create a new Chrome session
        caps = webdriver.DesiredCapabilities.CHROME.copy()
        caps['acceptInsecureCerts'] = False
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=caps)
        self.driver.maximize_window()
        configfile = configparser.ConfigParser()
        configfile.read(path.init_file)
        get_url = configfile.get('server', 'base_url')

        # navigate to the application home page
        self.driver.get(get_url)

    def tearDown(self):
        # close the browser window
        self.driver.quit()
