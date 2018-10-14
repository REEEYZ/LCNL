from psychopy import visual, core, event, gui
from generateTrials import *
import csv
import time

categories = {'Happy':':)', 'Angry':':<', 'Sad':':('}
actors = ['001m', '001w', '002m', '002w', '003m', '003w', '004m', '004w', '005m', '005w']
suffix = '_90_60.jpg'
responseMapping = {'1':'up','0':'down'}
rows = []




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


dlg = gui.Dlg();
dlg.addText("Enter the name: ");
dlg.addField("name");
dlg.show();

if dlg.OK:
    trialName = dlg.data[0] + '.csv'
    outName = dlg.data[0] + '_data.csv'
else:
    trialName = "trials.csv"
    outName = 'data.csv'


generateTrials(trialName)
trialList = importTrials(trialName)



win = visual.Window([800,600],color="black", units='pix')
prompt = visual.TextStim(win=win,text='',color="white",height=60)
correctFeedback = visual.TextStim(win=win,text='CORRECT',color="green",height=60)
incorrectFeedback = visual.TextStim(win=win,text='ERROR',color="red",height=60)
pic = visual.TextStim(win=win,text='',color="green",height=60)



for curTrial in trialList:
    win.flip()
    core.wait(.25)
    prompt.setText(curTrial['emotionPrompt']+'?')
    prompt.draw()
    win.flip()
    core.wait(.5)
    win.flip()
    core.wait(.1)
    pic.setText(curTrial['targetFaceImage'])
    pic.draw()
    win.flip()
    startTime = time.clock()
    response = event.waitKeys(keyList=responseMapping.values())[0]
    endTime = time.clock()
    total = (endTime - startTime) * 1000
    totalTime = "%.2f" % total
    if response == responseMapping[curTrial['isMatch']]:
        accuracy = 1
        correctFeedback.draw()
    else:
        accuracy = 0
        incorrectFeedback.draw()
    win.flip()
    core.wait(.5)
    row = []
    row.append(dlg.data[0])
    row.append(curTrial['isMatch'])
    row.append(curTrial['emotionPrompt'])
    row.append(curTrial['shownActor'])
    row.append(curTrial['shownCategory'])
    row.append(curTrial['targetFaceImage'])
    row.append(accuracy)
    row.append(totalTime)
    rows.append(row)

with open(outName, 'wb') as f:
    w = csv.writer(f)
    for roww in rows:
        w.writerows([roww])
        
    
    
    
win.close()

