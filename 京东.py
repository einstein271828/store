from selenium import webdriver  # 浏览器驱动
import time
# 1.创建一个谷歌驱动
driver = webdriver.Chrome()

# 2.打开京东
driver.get("https://www.jd.com")
time.sleep(2)
driver.maximize_window()

#搜索电脑
driver.find_element_by_class_name("text").send_keys("电脑\n")
driver.implicitly_wait(15)

driver.find_element_by_xpath("//img[@width='220']").click()

data = driver.window_handles
driver.switch_to.window(data[1])
time.sleep(6)

#登录
driver.find_element_by_class_name("link-login").click()
driver.implicitly_wait(5)
driver.find_element_by_link_text("账户登录").click()
driver.find_element_by_id("loginname").send_keys("lc12345622817")
driver.find_element_by_id("nloginpwd").send_keys("qazxsw123456")
driver.find_element_by_id("loginsubmit").click()
driver.implicitly_wait(15)

driver.find_element_by_id("InitCartUrl").click()
time.sleep(5)


driver.quit()