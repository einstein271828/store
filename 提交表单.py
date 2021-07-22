from selenium import webdriver  # 浏览器驱动
import time
from selenium.webdriver.support.select import Select
# 1.创建一个谷歌驱动
driver = webdriver.Chrome()

# 2.打开京东
driver.get(r"D:\pythonZDHCSBJ\automatic\每日作业\day01\练习的html\练习的html\上传文件和下拉列表/autotest.html")
driver.maximize_window()

# 3.
driver.find_element_by_id("accountID").send_keys("刘小丛")

driver.find_element_by_id("passwordID").send_keys("123456")

# driver.find_element_by_id("areaID").send_keys("北京市")

driver.find_element_by_xpath("//input[@id='sexID2']").click()

Select(driver.find_element_by_id("areaID")).select_by_index(3)

driver.find_element_by_xpath("//input[@value='spring']").click()

driver.find_element_by_xpath("//input[@value='summer']").click()

driver.find_element_by_xpath("//input[@value='Auterm']").click()

driver.find_element_by_xpath("//input[@name='file']").send_keys("D:\GITHUB\Git")

driver.find_element_by_xpath("//input[@onclick='return toAlert()']").click()

time.sleep(5)
driver.quit()