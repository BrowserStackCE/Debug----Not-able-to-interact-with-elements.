import requests
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run_test():

	userName = "arvindr1"
	accessKey = "JNzsLXukmxpiaaCsBhSx"

	response = requests.get('https://api-cloud.browserstack.com/app-automate/recent_apps', auth=(userName,accessKey))
	not_uploaded = False
	json_data = response.json()
	for item in json_data:
		try:
			if item["custom_id"] == "bstack-webview":
				not_uploaded = True
				app_url = item["app_url"]
				break
		except:
			pass
	if not_uploaded == False:
		files = {
	    'data': (None, '{"url": "https://github.com/arvind1998/browserstack-webview/raw/master/bstack-webview.apk","custom_id":"bstack-webview"}'),
		}
		response = requests.post('https://api-cloud.browserstack.com/app-automate/upload', files=files, auth=(userName,accessKey))
		json_data = response.json()
		app_url = json_data["app_url"]

	desired_caps = {
		"os_version" : "10.0",
		"device" : "Samsung Galaxy Note 20",
		"app" : app_url,
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
    run_test()
