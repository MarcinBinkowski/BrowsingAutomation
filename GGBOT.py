from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *

driver = webdriver.Chrome()

user = "xyz@gmail.com"
password = "abc"

driver.get("http://www.gg.pl")
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)

elem = driver.find_element_by_id("login_input")
elem.send_keys(user)
elem = driver.find_element_by_id("password")
elem.send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Zaloguj')]").click()
sleep(50)
driver.close()