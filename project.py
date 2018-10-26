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

for trial in study_trials:
    win.flip()
    core.wait(0.5)
    pic.setImage('project/visual/' + trial['img'])
    pic.draw()
    win.flip()
    core.wait(1)
    response = event.getKeys(keyList = ['q', '1', '0'])
    print response
    if trial['rep']:
        win.flip()
        break
win.close()







