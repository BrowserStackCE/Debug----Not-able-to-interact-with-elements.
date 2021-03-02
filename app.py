from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def runtest():

	userName = "<BROWSERSTACK_USERNAME>"
	accessKey = "<BROWSERSTACK_ACCESS_KEY>"

	desired_caps = {
		"os_version" : "10.0",
		"device" : "Samsung Galaxy Note 20",
		"app" : "<APP_URL>",
		"build" : "BrowserStack WebView",
		"name" : "Test"
	}

	driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)

	search_element = WebDriverWait(driver, 30).until(
    	EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.Button"))
	)

	search_element.click()

	WebDriverWait(driver, 30).until(lambda d: True if 'WEBVIEW_com.example.browserstackwebview' in d.contexts else False)
	driver.switch_to.context(driver.contexts[1])

	elem = driver.find_element_by_name("q")
	elem.send_keys("BrowserStack")
	elem.submit()


	driver.quit()

if __name__ == "__main__":
    runtest()
