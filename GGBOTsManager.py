import GGBOT
import threading

def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper

class GGBOTsManager:

    def __init__(self):
        """
        to add new bot just add new tuple of strings(email, password)
        """
        self.bots_data = [

            ]
        self.bots_list = []

        for tuple in self.bots_data:
            self.bot = GGBOT.GGBot(tuple[0],tuple[1])
            self.bots_list.append(self.bot)

    @threaded
    def start_bot(self, bot_number):
        bot = self.bots_list[bot_number]
        bot.log_in()
        bot.start_roulette()
        bot.roulette_loop()

    def bot_manager_start(self):
        for i in range(len(self.bots_list)):
            self.start_bot(i)


if __name__ == "__main__":
    manager = GGBOTsManager()
    manager.bot_manager_start()
