import csv
from psychopy import visual, event, core
from generateStudyTrials import *
import time



    
win = visual.Window([800, 600], color = 'white', units = 'pix')
generateTrials('project/studyTrials.csv', 'project/testTrials.csv', '1')
study_trials = importTrials('project/studyTrials.csv')
test_trials = importTrials('project/testTrials.csv')
pic = visual.ImageStim(win=win, mask=None,interpolate=True)
incorrectFeedback = visual.TextStim(win=win,text='REPEAT MISS',color="red",height=60)
output = []

for trial in study_trials:
    print trial['rep']
    pic.setImage('project/visual/' + trial['img'])
    pic.draw()
    win.flip()
    startTime = time.clock()
    reactTime = 0
    core.wait(1)
    win.flip()
    core.wait(0.5)
    response = event.getKeys(keyList = ['q', 'space'])
    if trial['rep'] == 'True':
        if len(response) != 0:
            if response[0] == 'q':
                break
            elif response[0] == 'space':
                endTime = time.clock()
                reactTime = endTime - startTime
                win.flip()
                core.wait(1)
            else:
                incorrectFeedback.draw()
                win.flip()
                core.wait(1)
        else:
            incorrectFeedback.draw()
            win.flip()
            core.wait(1)
    else:
        if len(response) != 0:
            if response[0] == 'q':
                break
        win.flip()
        core.wait(0.5)

for trial in test_trials:
    print trial['rep']
    pic.setImage('project/visual/' + trial['img'])
    pic.draw()
    win.flip()
    core.wait(1)
    win.flip()
    core.wait(0.5)
    response = event.getKeys(keyList = ['q', 'space'])
    if trial['rep'] == 'True':
        if len(response) != 0:
            if response[0] == 'q':
                break
            elif response[0] == 'space':
                win.flip()
                core.wait(1)
            else:
                incorrectFeedback.draw()
                win.flip()
                core.wait(1)
        else:
            incorrectFeedback.draw()
            win.flip()
            core.wait(1)
    else:
        if len(response) != 0:
            if response[0] == 'q':
                break
        win.flip()
        core.wait(0.5)


win.close()







