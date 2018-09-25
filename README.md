# BrowsingAutomation
Selenium bots to automate some tasks

GGBOT:
  Setup:
  * download GGBOT.py and GGBOTsManager.py
  * download chromedriver.exe http://chromedriver.chromium.org/
  * put chromedriver.exe to the same directory as GGBOT.py and GGBOTsManager.py
  * edit GGBOTsManager.py:
  
    1) in GGBOtsManager class find __init__ method
    2) find self.bots_data list
    3) add tuple to list with mail and password as strings ("my_email@domain.com", "my_password")
    4) save file
  * shift + right click in folder, choose "open command window here"
  * write "python GGBOTsManager.py"
  * ctrl+c to exit
  
  Known bugs:
  
  * exiting program doesn't terminate chromedriver
