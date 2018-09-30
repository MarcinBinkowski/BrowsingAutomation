from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from SudokuSolver import SudokuSolver
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class SudokuSolverBot:

    def __init__(self, username, password):
        self.options = Options() #used with next line to hide head of chrome
        self.options.add_argument("--headless") #comment if u want to see whole process
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(chrome_options=self.options)
        self.solver = SudokuSolver() #instance of class used to get solved sudoku list
        self.dont_click_list = [] # list of fields that are already filled on start
        self.actions = "" # actions to perform
        self.number = 0 # we use this to get board info

    def log_in(self):
        self.driver.get("https://www.sudokukingdom.com//index.php")
        self.driver.find_element_by_xpath("//a[contains(text(),'Log In')]").click()
        self.driver.find_element_by_xpath("//input[@id='login_name']").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@id='member_password']").send_keys(self.password)
        self.driver.find_element_by_xpath("//input[@value='Log In']").click()

    def get_board_info(self):
        for i in range(9):
            for j in range(9):
                self.number = self.driver.find_element_by_xpath("//div[@id='vc_"+ str(i) + "_" + str(j) + "']").text
                if not self.number.isdigit(): # just double checking, without program is not consistent
                    self.number = self.driver.find_element_by_xpath("//div[@id='vc_" + str(i) + "_" + str(j) + "']").text
                if self.number.isdigit():
                    self.dont_click_list.append(str(i)+str(j))
                else:
                    self.number = "-"
                self.solver.add_to_board(j, i, self.number)
        #self.solver.print_board()

    def fill_focus(self, element):
        self.actions = ActionChains(self.driver)
        self.actions.move_to_element(element)
        self.actions.click() # workaround
        sleep(0.08)  
        self.actions.click()
        sleep(0.08) 
        self.actions.perform()

    def fill_blank_spaces(self):
        for i in range(9):
            for j in range(9):
                if str(j) + str(i) not in self.dont_click_list: #workaround 2
                    self.driver.find_element_by_css_selector("#M{}".format(self.solver.board[i][j])).click()
                    sleep(0.08)
                    self.driver.find_element_by_css_selector("#M{}".format(self.solver.board[i][j])).click()
                    sleep(0.08)
                    self.fill_focus(self.driver.find_element_by_xpath(
                            "//div[@id='vc_{}_{}']".format(j,i)))

    def solve_loop(self, number_of_solutions):
        for i in range(number_of_solutions):
            sleep(1) #solving MaxRetriesException
            try:
                self.driver.find_element_by_xpath("//div[@id='g4']").click() #very hard difficulty
            except: #solving MaxRetriesException
                print("Bot {} łączy się ponownie". format(self.username))
                sleep(5)
                self.driver.find_element_by_xpath("//div[@id='g4']").click()
            print("{} Etap I".format(self.username))
            self.dont_click_list = [] # reseting list 
            print("{} Etap II".format(self.username))
            sleep(3) #without this line sometimes program gets wrong board, how to solve?
            self.get_board_info()
            print("{} Etap III".format(self.username))
            self.solver.solve()
            print("{} Etap IV".format(self.username))
            self.fill_blank_spaces()
            print("{} Etap V".format(self.username))
            sleep(5)
        print("Bot {} wykonał zadanie".format(self.username))
