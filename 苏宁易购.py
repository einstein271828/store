from selenium import webdriver  # 浏览器驱动
import time
# 1.创建一个谷歌驱动
driver = webdriver.Chrome()

# 2.打开京东
driver.get("https://www.suning.com")
driver.maximize_window()

# 3.
driver.find_element_by_id("searchKeywords").send_keys("苹果11\n")
time.sleep(3)

driver.find_element_by_class_name("btn-xq").click()

data = driver.window_handles
driver.switch_to.window(data[1])

time.sleep(5)

driver.find_element_by_id("addCart").click()


# 5.点击搜索

time.sleep(5)
driver.quit()
