import requests
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def run_test():

	userName = os.environ.get('BROWSERSTACK_USERNAME')
	accessKey = os.environ.get('BROWSERSTACK_ACCESS_KEY')
	app_url = os.environ.get('BROWSERSTACK_APP_ID')

	desired_caps = {
		"os_version" : "10.0",
		"device" : "Samsung Galaxy Note 20",
		"app" : app_url,
		"name" : "Test"
	}
	
	desired_caps['build'] = os.environ.get('BROWSERSTACK_BUILD_NAME')

	driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)

	search_element = WebDriverWait(driver, 30).until(
    	EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.Button"))
	)

	search_element.click()

	

	elem = driver.find_element_by_name("q")
	elem.send_keys("BrowserStack")
	elem.submit()


	driver.quit()

if __name__ == "__main__":
    run_test()
