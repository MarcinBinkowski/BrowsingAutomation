import sqlite3
import sys
from time import sleep
from EmailCreatorBot import EmailCreatorBot
from FakeDataGenerator import FakeDataGenerator


class Manager:

    def __init__(self):
        self.conn = sqlite3.connect("email_password.db")
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute("""CREATE TABLE mytable
                     (email, password, hosting)""")
        except:
            pass

    def make_new_accounts(self, number_of_accounts):
        for i in range(number_of_accounts):
            data = FakeDataGenerator().return_data()
            new_bot = EmailCreatorBot(data["name"], data["surname"], data["password"], data["login"])
            self.coordinate(new_bot)
            t = [(str(new_bot.login)+"@yandex.com"), (new_bot.password), ("yandex.com")]

            new_bot.driver.close()
            new_bot.driver.switch_to.window(new_bot.driver.window_handles[0])
            new_bot.driver.close()
            self.cursor.execute('insert into mytable values (?,?,?)', t)
            self.conn.commit()
            print(t)

    def coordinate(self,bot):
        bot.get_phone_number()
        bot.fill_out_forms()
        if bot.stop == True:
            self.close_database()
            sys.exit("too many accounts for this ip adress")
        sleep(2)
        bot.driver.switch_to.window(bot.driver.window_handles[0])
        sleep(3)
        bot.get_sms()
        bot.driver.switch_to.window(bot.driver.window_handles[1])
        bot.registration_focus(bot.driver.find_element_by_xpath(
            "//input[@id='phoneCode']"), bot.sms)
        sleep(2)
        bot.driver.find_element_by_xpath(
            "//button[@type='submit']").click()
        sleep(2)
        bot.driver.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/button[1]")
        sleep(3)
        bot.eula_focus(bot.driver.find_element_by_css_selector(
            "div.layout:nth-child(1) div.layout-inner div.grid div.main-container main.registration__wrapper,.utilityfocus.registration__wrapper_desktop div.registration__block form.registration__form.registration__form_desktop div.form__submit:nth-child(5) div.eula-popup-wrapper.eula-popup__show div.eula-popup div.t-eula-accept > button.button2.button2_size_m.button2_theme_action.button2_width_max:nth-child(3)"))
        sleep(4)

    def close_database(self):
        sleep(0.2)
        self.conn.close()

if __name__ == "__main__":
    manager = Manager()
    num_of_accounts = input("how many accounts u want to create? (recommended <= 5 [ip gets banned for few hours]):")
    manager.make_new_accounts(int(num_of_accounts))
