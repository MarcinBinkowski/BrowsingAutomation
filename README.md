# BrowsingAutomation
Selenium bots to automate some tasks

GGBOT:
  Setup:
  1) download GGBOT.py and GGBOTsManager.py
  2) download chromedriver.exe http://chromedriver.chromium.org/
  3) put chromedriver.exe to the same directory as GGBOT.py and GGBOTsManager.py
  4) edit GGBOTsManager.py:
    1) in GGBOtsManager class find __init__ method
    2) find self.bots_data list
    3) add tuple to list with mail and password as strings ("my_email@domain.com", "my_password")
    4) save file
  5) shift + right click in folder, choose "open command window here"
  6) write "python GGBOTsManager.py"
  7) ctrl+c to exit
