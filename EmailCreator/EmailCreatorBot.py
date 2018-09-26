from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from random import choice, randint
import string
from selenium.webdriver.chrome.options import Options
from time import *

names = ["Jack", "John", "Adam", "Matt", "Mark", "Roman", "Paul", "Stan", "Ted", "Peter", "Robert",
         "Alice", "Celine", "Edith", "Mary", "Natalie", "Nina", "Rose",
         "Rebbeca", "Roxanne", "Nicole", "Sam", "Sandra", "Sophie",
         ]
surnames = ["Smith", "Jones", "Williams", "Brown", "Taylor", "Davies", "Wilson", "Evans", "Thomas", "Roberts", "Johnson",
            "Walker", "Wright", "Robinson", "Robinson", "Hughes", "White", "Edwards", "Hall", "Alden",
            ]



def registration_focus(element, data):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.click();
    actions.send_keys(str(data))
    actions.perform()
    if element.get_attribute("value") == "":
        sleep(1)
        registration_focus(element,data)

def login_passwor_generator():
    alphabet = string.ascii_lowercase
    login = ''
    for i in range(randint(7,12)):
        letter = choice(alphabet)
        login = login + letter
    for i in range(randint(0,3)):
        number = randint(0,9)
        login = login + str(number)
    return login

driver = webdriver.Chrome()
driver.get('https://passport.yandex.com/registration/mail?from=mail&require_'
           'hint=1&origin=hostroot_homer_reg_com&retpath'
           '=\https%3A%2F%2Fmail.yandex.com%2F&backpath='
           'https%3A%2F%2Fmail.yandex.com%3Fnoretpath%3D1')

sleep(4)

driver.find_element_by_xpath("//div[@class='lg-cc__button lg-cc__button_type_action']").click()

registration_focus(driver.find_element_by_xpath("//label[contains(text(),'First name')]"),choice(names))
registration_focus(driver.find_element_by_xpath("//label[contains(text(),'Surname')]"),choice(surnames))
registration_focus(driver.find_element_by_xpath("//input[@id='login']"),login_passwor_generator())

password = login_passwor_generator()

registration_focus(driver.find_element_by_xpath("//input[@id='password']"), password)
registration_focus(driver.find_element_by_xpath("//input[@id='password_confirm']"), password)
registration_focus(driver.find_element_by_xpath("//input[@id='phone']"), "12313123")

