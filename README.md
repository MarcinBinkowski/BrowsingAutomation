# BrowsingAutomation
Selenium bots to automate some tasks

GGBOT:
  Setup:
  * download GGBOT.py and GGBOTsManager.py
  * download chromedriver.exe http://chromedriver.chromium.org/
  * put chromedriver.exe to the same directory as GGBOT.py and GGBOTsManager.py
  * edit GGBOTsManager.py:

      * in GGBOtsManager class find __init__ method
      * find self.bots_data list
      * add tuple to list with mail and password as strings ("my_email@domain.com", "my_password")
      * save file
  * shift + right click in folder, choose "open command window here"
  * type "python GGBOTsManager.py"
  * ctrl+c to exit
 
  Known bugs:
  
       - exiting program doesn't terminate chromedriver


EmailCreatorBot:
  Setup:
  * download EmailCreatorBot.py, BotManager.py and FakeDataGenerator.py 
  * download chromedriver.exe http://chromedriver.chromium.org/
  * put chromedriver.exe to the same directory as EmailCreatorBot.py, BotManager.py and FakeDataGenerator.py 
  * shift + right click in folder, choose "open command window here"
  * type "python BotManager.py"
  * type how many account you want to create (it's recommended not to create more than 5)
  * wait until emails will be created
  * you can get emails info using database browser (data getter not supported yet)
  
  TODO:
  
      - change phone number if it exceeds max accounts per phone number.
      - rewrite code without using time.sleep()
      - write console script for getting data from database
