from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

class OpenPageTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get("file:///Users/maksimevsukov/Documents/Selenium-Test:/test3.html")

	def test_assert(self):
		driver = self.driver
		countriesDropDown = driver.find_element_by_css_selector("select#countriesDropDown > option[value='russia']").click()
		russianText = driver.find_element_by_css_selector("#targetDiv")
		self.assertTrue("Russia is Chosen in the Select Box", russianText.text)

		countriesDropDown = driver.find_element_by_css_selector("select#countriesDropDown > option[value='usa']").click()
		russianText = driver.find_element_by_css_selector("#targetDiv")
		self.assertTrue("USA is Chosen in the Select Box", russianText.text)
		
		countriesDropDown = driver.find_element_by_css_selector("select#countriesDropDown > option[value='uk']").click()
		russianText = driver.find_element_by_css_selector("#targetDiv")
		self.assertTrue("UK is Chosen in the Select Box", russianText.text)

	def tearDown(self):
			self.driver.quit()

if __name__ == '__main__':
    	unittest.main()