# BrowsingAutomation
Selenium bots, written for educational purposes only!

## GGBOT

  Setup:
  * download ggbot.py and ggbotsmanager.py
  * download chromedriver.exe http://chromedriver.chromium.org/
  * put chromedriver.exe to the same directory as ggbot.py and ggbotsmanager.py
  * edit ggbotsmanager.py:

      * in ggbotsmanager class find __init__ method
      * find self.bots_data list
      * add tuple to list with mail and password as strings ("my_email@domain.com", "my_password")
      * save file
  * shift + right click in folder, choose "open command window here"
  * type "python ggbotsmanager.py"
  * ctrl+c to exit
 
  TODO:
  - [ ] remove known bugs
  - [ ] remove time.sleep() where it's not necessary
  - [ ] change try/except blocks for selenium functions
  
  
  Known bugs:
  
       - exiting program doesn't terminate chromedriver
       
       
       
## SudokuSolverBot
Setup:
  * download sudokusolver.py, sudokusolverBot.py and sudokusolvermanager.py
  * download chromedriver.exe http://chromedriver.chromium.org/
  * put chromedriver.exe to the same directory as sudokusolver.py, sudokusolverbot.py and sudokusolvermanager.py
  * shift + right click in folder, choose "open command window here"
  * type "python sudokusolversanager.py"
  * type how many games u want bots to play
  * wait untill all games are played

  TODO:
  - [x] workaround for "Max retries exceeded with URL"
  - [ ] rewrite parts of program which use double sleep and button clicks (didn't find proper way yet)


## EmailCreatorBot
  *very buggy and unfinished version*
  
  Setup:
  * download EmailCreatorBot.py, BotManager.py and FakeDataGenerator.py 
  * download chromedriver.exe http://chromedriver.chromium.org/
  * put chromedriver.exe to the same directory as EmailCreatorBot.py, BotManager.py and FakeDataGenerator.py 
  * shift + right click in folder, choose "open command window here"
  * type "python BotManager.py"
  * type how many account you want to create (it's recommended not to create more than 5 due to ip ban for creating new accounts)
  * wait until emails will be created
  * you can get emails info using database browser (data getter not supported yet)
  
  TODO:
  - [ ] change phone number if it exceeds max accounts per phone number.
  - [ ] rewrite code without using time.sleep()
  - [ ] write console script for getting data from database
  - possibly find a workaround for ip bans (tor?)
