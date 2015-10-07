from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

class OpenPageTest(unittest.TestCase):

	def setUp(self):
 		self.driver = webdriver.Firefox()
 		self.driver.get("file:///Users/maksimevsukov/Documents/Selenium-Test:/test2.html")
 
 	def test_assert(self):
 		driver = self.driver
 		i = driver.find_element_by_id("daButton")
 		i.click()
		self.assertIn("Behold the Power of jQuery!", i.text)
 
 	def tearDown(self):
 			self.driver.quit()
 
if __name__ == '__main__':
     	unittest.main()