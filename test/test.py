# simple test case with selenium
# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
  
# instance of Options class allows
# us to configure Headless Chrome
options = Options()
  
# this parameter tells Chrome that
# it should be run without UI (Headless)
options.headless = True
 
# inherit TestCase Class and create a new test class
class PythonOrgSearch(unittest.TestCase):
 
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Chrome(options=options)
 
    # Test case method. It should always start with test_
    def test_empty_input_during_login(self):
         
        # get driver
        driver = self.driver
        # get python.org using selenium
        driver.get("https://web-production-b1d0.up.railway.app/")
 
        # locate element using name
        driver.find_element(By.NAME, "email").send_keys("")
        driver.find_element(By.NAME, "password").send_keys("")
        #click the button
        driver.find_element(By.CSS_SELECTOR, "button").click()
        #wait for 4 seconds
        time.sleep(4)
        #get the text of the error message
        text = driver.find_element(By.CSS_SELECTOR, "#loginMessage").text
        self.assertEqual(text, "Invalid email or password")
 
    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()
 
# execute the script
if __name__ == "__main__":
    unittest.main()