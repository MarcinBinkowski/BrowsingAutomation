from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import FakeDataGenerator
from time import sleep
import re


class EmailCreatorBot:

    def __init__(self, name, surname, password, login):
        self.name = name
        self.surname = surname
        self.password = password
        self.login = login
        self.phone_number = ""

        self.driver = webdriver.Chrome()
        self.element = ""
        self.sms = ""

        self.driver.get("https://catchsms.com/")

    def registration_focus(self, element, data):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys(str(data))
        actions.perform()

    def get_phone_number(self):
        sleep(3)
        self.driver.find_element_by_tag_name("body").send_keys(Keys.ESCAPE)
        sleep(1)
        self.phone_number = self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h6[1]").text
        print(self.phone_number)

    def get_sms(self):
        self.driver.find_element_by_xpath("//div[@class='wrap']//div[2]//div[1]//a[1]").click()
        regex_data = self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[2]").text
        self.sms = re.search('\d+|$', regex_data).group()
        print(self.sms)

    def fill_out_forms(self):
        self.driver.execute_script(
            '''window.open("https://passport.yandex.com/registration/mail?from=mail&require\
            _hint=1&origin=hostroot_homer_reg_com&retpath=https%3A%2F%2Fmail.yandex.\
            com%2F&backpath=https%3A%2F%2Fmail.yandex.com%3Fnoretpath%3D1","_blank");''')
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='lg-cc__button lg-cc__button_type_action']")))
        self.element.click()

        self.registration_focus(self.driver.find_element_by_xpath(
            "//label[contains(text(),'First name')]"), self.name)
        self.registration_focus(self.driver.find_element_by_xpath(
            "//label[contains(text(),'Surname')]"), self.surname)
        self.registration_focus(self.driver.find_element_by_xpath(
            "//input[@id='login']"), self.login)
        self.registration_focus(self.driver.find_element_by_xpath(
            "//input[@id='password']"), self.password)
        self.registration_focus(self.driver.find_element_by_xpath(
            "//input[@id='password_confirm']"), self.password)
        self.registration_focus(self.driver.find_element_by_xpath(
            "//input[@id='phone']"), self.phone_number)
        sleep(0.5)
        self.driver.find_element_by_xpath(
            "//div[@class='registration__send-code show-block']//button[@type='button']").click()

    def coordinate(self):
        self.get_phone_number()
        self.fill_out_forms()
        self.driver.switch_to.window(self.driver.window_handles[0])
        sleep(3)
        self.get_sms()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.registration_focus(self.driver.find_element_by_xpath(
            "//input[@id='phoneCode']"), self.sms)
        self.driver.find_element_by_xpath(
            "//div[@class='phone__code-btn']//button[@type='button']").click()
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div/main/div/div/div/form/div[4]/button").click()
    

if __name__ == "__main__":
    data = FakeDataGenerator.FakeDataGenerator().return_data()
    bot = EmailCreatorBot(data["name"], data["surname"], data["password"], data["login"])
    bot.coordinate()