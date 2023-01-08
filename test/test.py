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
    def test_invalid_input_during_login(self):
        # get driver
        driver = self.driver
        # get webpage
        driver.get("https://web-production-b1d0.up.railway.app/login")
 
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


    def test_invalid_input_during_register(self):
        # get driver
        driver = self.driver
        # get webpage
        driver.get("https://web-production-b1d0.up.railway.app/register")
 
        # locate element using name
        driver.find_element(By.NAME, "name").send_keys("")
        driver.find_element(By.NAME, "email").send_keys("")
        driver.find_element(By.NAME, "password").send_keys("")
        #click the button
        driver.find_element(By.CSS_SELECTOR, "button").click()
        #wait for 4 seconds
        time.sleep(4)
        #get the text of the error message
        text = driver.find_element(By.CSS_SELECTOR, "#registerMessage").text
        self.assertEqual(text, "User validation failed: name: Path `name` is required., email: Path `email` is required., password: Path `password` is required.")


    def test_duplicate_profile_regestration(self):
        # get driver
        driver = self.driver
        # get webpage
        driver.get("https://web-production-b1d0.up.railway.app/register")
 
        # locate element using name
        driver.find_element(By.NAME, "name").send_keys("someperson")
        driver.find_element(By.NAME, "email").send_keys("myemail1@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("12345678")
        #click the button
        driver.find_element(By.CSS_SELECTOR, "button").click()
        #wait for 4 seconds
        time.sleep(4)
        #get the text of the error message
        text = driver.find_element(By.CSS_SELECTOR, "#registerMessage").text
        self.assertEqual(text, "User already exists. Go to Login Page to Log into the account")


    def test_go_to_login_page(self):
        # get driver
        driver = self.driver
        # get webpage
        driver.get("https://web-production-b1d0.up.railway.app/register")
 
        #click the button
        driver.find_element(By.CSS_SELECTOR, "a").click()
        #wait for 4 seconds
        time.sleep(4)

        text = driver.find_element(By.CSS_SELECTOR, "h1").text
        self.assertEqual(text, "Sign in")


    def test_go_to_register_page(self):
        # get driver
        driver = self.driver
        # get webpage
        driver.get("https://web-production-b1d0.up.railway.app/login")
 
        #click the button
        driver.find_element(By.CSS_SELECTOR, "a").click()
        #wait for 4 seconds
        time.sleep(4)
      
        text = driver.find_element(By.CSS_SELECTOR, "h1").text
        self.assertEqual(text, "Sign Up")


    def test_login_with_credentials(self):
        # get driver
        driver = self.driver
        # get webpage
        driver.get("https://web-production-b1d0.up.railway.app/login")
        driver.find_element(By.NAME, "email").send_keys("myemail1@gmail.com")
        driver.find_element(By.NAME, "password").send_keys("12345678")
        #click the button
        driver.find_element(By.CSS_SELECTOR, "button").click()
        #wait for 4 seconds
        time.sleep(4)
       
        text = driver.find_element(By.CSS_SELECTOR, "#maincontent").text
        self.assertEqual(text, "WELCOME TO HOMEPAGE")
 
    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()
 
# execute the script
if __name__ == "__main__":
    unittest.main()