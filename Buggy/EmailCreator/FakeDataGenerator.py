import string
from random import randint, choice


class FakeDataGenerator:
    """
    Class for generating data to use in EmailCreatorBot.
    """
    def __init__(self):
        self.names = ["Jack", "John", "Adam", "Matt", "Mark", "Roman", "Paul", "Stan", "Ted", "Peter", "Robert",
                      "Alice", "Celine", "Edith", "Mary", "Natalie", "Nina", "Rose",
                      "Rebbeca", "Roxanne", "Nicole", "Sam", "Sandra", "Sophie"]
        self.surnames = ["Smith", "Jones", "Williams", "Brown", "Taylor", "Davies", "Wilson", "Evans", "Thomas",
                         "Roberts", "Johnson", "Walker", "Wright", "Robinson", "Robinson", "Hughes", "White",
                         "Edwards", "Hall", "Alden"]
        self.alphabet = string.ascii_lowercase
        self.letter = ""
        self.number = 0
        self.temporary = ""
        self.name = choice(self.names)
        self.surname = choice(self.surnames)
        self.login = self.login_password_generator()
        self.password = self.login_password_generator()


    def login_password_generator(self):
        self.temporary = ""
        for i in range(randint(6, 10)):
            self.letter = choice(self.alphabet)
            self.temporary += self.letter
        for i in range(randint(0, 3)):
            self.number = randint(0, 9)
            self.temporary += str(self.number)
        return  self.temporary

    def return_data(self):
        return{
            "name": self.name,
            "surname": self.surname,
            "login": self.login,
            "password": self.password,
        }

if __name__ == "__main__":
    data = FakeDataGenerator().return_data()
    print(data)