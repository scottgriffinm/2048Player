# python3
# 2048player.py - randomly makes moves in an online 2048 game and keeps
# track of scores.

'''
Gameplan:
1. go to https://gabrielecirulli.github.io/2048/
2. randomly input up, down, left, and right keys, checking for when
the game is over
3. find the score element and record it in a file with the date and time
4. start new game

'''

import time
from random import randint
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager



print('[Starting...]')
keyList = [ # list of possible keys
    Keys.UP,
    Keys.DOWN,
    Keys.LEFT,
    Keys.RIGHT,
    ]
browser = webdriver.Chrome(ChromeDriverManager().install()) # open chrome browser (with fix for incompatible chrome driver)
browser.get('https://gabrielecirulli.github.io/2048/') # go to website with 2048 game

while True: # new game
    print('[Starting a new game...]')
    elHTML = browser.find_element_by_tag_name('html') # select overall webpage
    while True:
        keySelection = randint(0,3) # random integer
        elHTML.send_keys(keyList[keySelection]) # telling browser to press random key in keyList
        try:
            browser.find_element_by_class_name('game-message.game-over') # if the game has ended
            print('[Game has ended.]')
            break # move on
        except: # game has not ended
            continue
        
    elScore = browser.find_element_by_class_name('score-container') # find score element
    time.sleep(1) # wait so the element doesnt capture a (+{some number})
    score = elScore.text # get the score
    print(f'[Score: {score}]')
    now = datetime.now() # get the date/time
    nowString = now.strftime('%d/%m/%Y %H:%M:%S') # format it so and turn it into a string
    scoreItemList = [score,nowString]
    scoreEntry = ' - '.join(scoreItemList) # join score and date/time together for recording in a text file
    scoreData = open('scores.txt', 'a') # open text file
    scoreData.write(scoreEntry + '\n') # write score/date/time
    scoreData.close() # close text file
    print('[Score recorded.]\n')
    elTryAgain = browser.find_element_by_class_name('restart-button') # find New Game button
    elTryAgain.click() # click New Game button

