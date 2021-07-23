'''
    python自动化刷抖音
'''

from appium  import  webdriver
from appium.webdriver.common.touch_action import TouchAction
import  time



server = "http://127.0.0.1:4723/wd/hub"
param = {
			  "deviceName": "127.0.0.1:62001",
			  "platformName": "Android",
			  "platformVersion": "7.1.2",
			  "appPackage": "com.tencent.mobileqq",
			  "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
            "noReset": "true",


}
# 启动这个软件
driver = webdriver.Remote(server,param)

driver.implicitly_wait(15)
# 自己登录QQ
# TouchAction(driver).tap(x=219, y=1168).perform()
# el1 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
# el1.send_keys("1541254121")
# el2 = driver.find_element_by_accessibility_id("密码 安全")
# el2.send_keys("1541254121")
# TouchAction(driver).tap(x=353, y=459).perform()

el1 = driver.find_element_by_id("com.tencent.mobileqq:id/btn_login")
el1.click()
el2 = driver.find_element_by_accessibility_id("请输入QQ号码或手机或邮箱")
el2.send_keys("12341234")
el3 = driver.find_element_by_accessibility_id("密码 安全")
el3.send_keys("12341234")
el4 = driver.find_element_by_accessibility_id("登录")
el4.click()


time.sleep(12)


driver.quit()































