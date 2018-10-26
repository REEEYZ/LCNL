import csv
from psychopy import visual, event, core
from generateStudyTrials import *


def importTrials(trialsFilename, colNames=None, separator=','):
    trialsFile = open(trialsFilename, 'rb')

    if colNames is None:
        # Assume the first row contains the column names
        colNames = trialsFile.next().rstrip().split(separator)
    trialsList = []
    for trialStr in trialsFile:
        trialList = trialStr.rstrip().split(separator)
        assert len(trialList) == len(colNames)
        trialDict = dict(zip(colNames, trialList))
        trialsList.append(trialDict)
    return trialsList
    
win = visual.Window([800, 600], color = 'white', units = 'pix')
generateTrials('project/studyTrials.csv')
study_trials = importTrials('project/studyTrials.csv')
pic = visual.ImageStim(win=win, mask=None,interpolate=True)
correctFeedback = visual.TextStim(win=win,text='CORRECT',color="green",height=60)
incorrectFeedback = visual.TextStim(win=win,text='ERROR',color="red",height=60)

for trial in study_trials:
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
                correctFeedback.draw()
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







