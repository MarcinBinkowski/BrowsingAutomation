from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *

driver = webdriver.Chrome()

user = "xyz
password = "abc"

driver.get("http://www.gg.pl")
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)

elem = driver.find_element_by_id("login_input")
elem.send_keys(user)
elem = driver.find_element_by_id("password")
elem.send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Zaloguj')]").click()
driver.get("http://www.gg.pl/#roulette")
sleep(2)
driver.find_element_by_xpath(
    '/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/label[1]/input[1]').click()
a = 0
while True:
    sleep(5)
    a+=1
    try:
        driver.find_element_by_xpath(
            '/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[8]/div[2]/label[1]/input[1]').click()
    except:
        try:
            driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/label[1]/input[1]').click()
        except:
            continue
    if a >400:
        driver.get("http://www.gg.pl/#roulette")
        a = 0
driver.close()

