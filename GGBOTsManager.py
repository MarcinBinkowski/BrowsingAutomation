import GGBOT

class GGBOTsManager:

    def __init__(self):
        """
        to add new bot just add new tuple of strings(email, password)
        """
        self.bots_data = [

            ]
        self.bots_list = []

        for tuple in self.bots_data:
            bot = GGBOT.GGBot(tuple[0],tuple[1])
            self.bots_list.append(bot)

    def start_bot(self, bot):
        bot.log_in()
        bot.start_roulette()
        bot.roulette_loop()


    def bot_manager_start(self):
        for bot in self.bots_list:
            self.start_bot(bot)



if __name__ == "__main__":
    manager = GGBOTsManager()
    manager.bot_manager_start()

