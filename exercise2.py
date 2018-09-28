# -*- coding: utf-8 -*-
import time
import sys
import random
from psychopy import visual,event,core,gui
count = 0


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
user = raw_input("Enter your name: ")
firstNames.append(user)

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])


while True:
    
    
    
    nameShown = random.choice(firstNames)
    firstNameStim.setText(nameShown)
    firstNameStim.draw()
    win.flip()
    
    core.wait(2)
    start = time.time() 
    if event.getKeys(['x']):
        if nameShown == user:
            end = time.time()
            timeUsed = end - start
            count += 1
            print timeUsed
            print count

    if event.getKeys(['q']):
        break
    
    core.wait(2)

win.close()
sys.exit()


