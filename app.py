from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



userName = "arvindr1"
accessKey = "JNzsLXukmxpiaaCsBhSx"


desired_caps = {
	"os_version" : "10.0",
	"device" : "Samsung Galaxy Note 20",
	"app" : "bs://eb351d25b9b0e86ebe05f9a3c65d65fb5a08be21",
	"build" : "BrowserStack WebView",
	"name" : "ClickMe"
}

driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)



search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.Button"))
)

search_element.click()

WebDriverWait(driver, 30).until(lambda d: True if 'WEBVIEW_com.example.browserstackwebview' in d.contexts else False)


#time.sleep(5)

print(driver.contexts)
# driver.switch_to.context(driver.contexts[1])
# print("switched")

# elem = driver.find_element_by_name("q")
# elem.send_keys("BrowserStack")
# elem.submit()




#WebDriverWait(driver).until(lambda d: True if 'WEBVIEW_Terrace' in d.contexts else False)

# driver.switch_to.context('WEBVIEW_Terrace')
# print("switched")


driver.quit()