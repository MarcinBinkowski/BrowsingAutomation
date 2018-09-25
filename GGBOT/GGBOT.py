from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import *


class GGBot:

    def __init__(self, username, password):
        self.options = Options()
        #self.options.add_argument("--headless") #comment if u want to see whole process
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.roulette_counter = 0
        self.driver.minimize_window()

    def log_in(self):
        try:
            self.driver.get("http://www.gg.pl")
            self.iframe = self.driver.find_element_by_tag_name("iframe")
            self.driver.switch_to.frame(self.iframe)
            self.elem = self.driver.find_element_by_id("login_input")
            self.elem.send_keys(self.username)
            self.elem = self.driver.find_element_by_id("password")
            self.elem.send_keys(self.password)
            self.driver.find_element_by_xpath("//button[contains(.,'Zaloguj')]").click()
        except:
            self.log_in()

    def start_roulette(self):
        try:
            self.driver.get("http://www.gg.pl/#roulette")
            sleep(4)
            self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/label[1]/input[1]').click()
        except:
            self.start_roulette()

    def roulette_loop(self):
        while True:
            print("roulette_loop", self.username)  #comment if you dont want to see emails in the console
            sleep(5)
            self.roulette_counter += 1
            try:
                self.driver.find_element_by_xpath(
                    '/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[8]/div[2]/label[1]/input[1]').click()
            except:
                try:
                    self.driver.find_element_by_xpath(
                        '/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[1]/div[6]/div[1]/label[1]/input[1]').click()
                except:
                    continue
            if self.roulette_counter > 50:  #in case u get message "too many draws, wait a while"
                self.driver.get("http://www.gg.pl/#roulette")
                self.roulette_counter = 0
