from psychopy import visual, event, core
import random
from generateTrials6 import *



def importTrials(trialsFilename, separator=','):
    trialsFile = open(trialsFilename, 'rb')
    trialsList = []
    for trialStr in trialsFile:
        trialList = trialStr.rstrip().split(separator)
        trialsList.append(trialList)
    print trialsList
    return trialsList




win = visual.Window([800, 600], color = 'black', units = 'pix')
generateTrials('Yuzhe6.csv')
trials = importTrials('Yuzhe6.csv')
correctFeedback = visual.TextStim(win=win,text='CORRECT',color="green",height=60)
incorrectFeedback = visual.TextStim(win=win,text='ERROR',color="red",height=60)

for trial in trials:
    for i in range(len(trial) - 1):
        if trial[i] == 'redcircle':
            circle = visual.Circle(win, size = 20)
            circle.setFillColor('red')
            circle.setLineColor('red')
            circle.setPos([30 * i - 240, 0])
            circle.draw()
        elif trial[i] == 'bluecircle':
            circle = visual.Circle(win, size = 20)
            circle.setFillColor('blue')
            circle.setLineColor('blue')
            circle.setPos([30 * i - 240, 0])
            circle.draw()
        elif trial[i] == 'bluesquare':
            square = visual.Rect(win, size = 40)
            square.setFillColor('blue')
            square.setLineColor('blue')
            square.setPos([30 * i - 240, 0])
            square.draw()
        else:
            square = visual.Rect(win, size = 40)
            square.setFillColor('red')
            square.setLineColor('red')
            square.setPos([30 * i - 240, 0])
            square.draw()
    isFlip = False
    if trial[16] == '1':
        isFlip = True
    win.flip()
    response = event.waitKeys(keyList = ['1', '0'])[0]
    winning = False
    if isFlip:
        if response == '1':
            winning = True
    else:
        if response == '0':
            winning = True
    if winning:
        correctFeedback.draw()
    else:
        incorrectFeedback.draw()
        
    win.flip()
    core.wait(1)
win.close()



    