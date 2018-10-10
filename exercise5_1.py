from psychopy import visual, core, event
from generateTrials import *

categories = {'Happy':':)', 'Angry':':<', 'Sad':':('}
actors = ['001m', '001w', '002m', '002w', '003m', '003w', '004m', '004w', '005m', '005w']
suffix = '_90_60.jpg'
responseMapping = {'1':'up','0':'down'}




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

generateTrials()

trialList = importTrials('trials.csv')

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
	response = event.waitKeys(keyList=responseMapping.values())[0]
	if response == responseMapping[curTrial['isMatch']]:
		correctFeedback.draw()
	else:
		incorrectFeedback.draw()
	win.flip()
	core.wait(.5)
    
    
win.close()

