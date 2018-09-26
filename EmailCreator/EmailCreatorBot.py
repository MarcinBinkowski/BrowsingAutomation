from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import FakeDataGenerator
from time import sleep


class EmailCreatorBot:

    def __init__(self, name, surname, password, login):
        self.name = name
        self.surname = surname
        self.password = password
        self.login = login
        self.phone_number = "234234"

        self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)
        self.element = ""
        self.regex_data = ""

        # self.driver.get('https://passport.yandex.com/registration/mail?from=mail&require_'
        #            'hint=1&origin=hostroot_homer_reg_com&retpath'
        #            '=\https%3A%2F%2Fmail.yandex.com%2F&backpath='
        #            'https%3A%2F%2Fmail.yandex.com%3Fnoretpath%3D1')
        #self.fill_out_forms()

    def registration_focus(self, element, data):
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(element)
        self.actions.click()
        self.actions.send_keys(str(data))
        self.actions.perform()

    def get_phone_number(self):
        #self.driver.execute_script('''window.open("https://catchsms.com/","_blank");''')
        self.driver.get("https://catchsms.com/")
        sleep(3)
        self.driver.find_element_by_tag_name("body").send_keys(Keys.ESCAPE)
        sleep(1)
        self.phone_number = self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/h6[1]").text
        print(self.phone_number)

    def get_sms(self):
        self.driver.find_element_by_xpath("//div[@class='wrap']//div[2]//div[1]//a[1]").click()
        self.regex_data = self.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[2]").text
        print(self.regex_data)






    def fill_out_forms(self):
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
            "//input[@id='phone']"), "12313123")

if __name__ == "__main__":
    data = FakeDataGenerator.FakeDataGenerator().return_data()
    bot = EmailCreatorBot(data["name"], data["surname"], data["password"], data["login"])
    bot.get_phone_number()
    bot.get_sms()