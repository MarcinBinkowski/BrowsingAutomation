import sqlite3
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
            new_bot.coordinate()
            t = [(str(new_bot.login)+"@yandex.com"), (new_bot.password), ("yandex.com")]

            new_bot.driver.close()
            new_bot.driver.switch_to.window(new_bot.driver.window_handles[0])
            new_bot.driver.close()
            self.cursor.execute('insert into mytable values (?,?,?)', t)
            self.conn.commit()
            print(t)
    def close_database(self):
        sleep(0.2)
        self.conn.close()

if __name__ == "__main__":
    manager = Manager()
    num_of_accounts = input("how many accounts u want to create? (recommended less than 5):")
    manager.make_new_accounts(int(num_of_accounts))
