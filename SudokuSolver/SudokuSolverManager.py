import threading
from time import sleep
from SudokuSolverBot import SudokuSolverBot

class Manager:

    def __init__(self):
        self.bots_data = [

        ]
        self.bots_list = []

        for tuple in self.bots_data:
            self.bot = SudokuSolverBot(tuple[0], tuple[1])
            self.bots_list.append(self.bot)

    def threaded(fn):
        def wrapper(*args, **kwargs):
            threading.Thread(target=fn, args=args, kwargs=kwargs).start()
        return wrapper

    @threaded
    def start_bot(self, bot_number, number_of_solutions):
        bot = self.bots_list[bot_number]
        bot.log_in()
        sleep(2) #solving MaxRetriesException
        bot.solve_loop(number_of_solutions)
        bot.driver.close()

    def bot_manager_start(self, number_of_solutions):
        for i in range(len(self.bots_data)):
            self.start_bot(i, number_of_solutions)

if __name__ == "__main__":
    manager = Manager()
    manager.bot_manager_start(150)