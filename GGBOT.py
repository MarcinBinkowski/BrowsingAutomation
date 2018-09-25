from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *


class GGBot:


    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.roulette_counter = 0

    def log_in(self):
        self.driver.get("http://www.gg.pl")
        self.iframe = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(self.iframe)
        self.elem = self.driver.find_element_by_id("login_input")
        self.elem.send_keys(self.username)
        self.elem = self.driver.find_element_by_id("password")
        self.elem.send_keys(self.password)
        self.driver.find_element_by_xpath("//button[contains(.,'Zaloguj')]").click()

    def start_roulette(self):
        self.driver.get("http://www.gg.pl/#roulette")
        sleep(2)
        self.driver.find_element_by_xpath(
            '/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/label[1]/input[1]').click()

    def roulette_loop(self):
        while True:
            sleep(4)
            self.roulette_counter += 1
            try:
                self.driver.find_element_by_xpath(
                    '/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[8]/div[2]/label[1]/input[1]').click()
            except:
                try:
                    self.driver.find_element_by_xpath(
                        '/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/label[1]/input[1]').click()
                except:
                    None
            if self.roulette_counter > 400:
                self.driver.get("http://www.gg.pl/#roulette")
                self.roulette_counter = 0

