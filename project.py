import csv
from psychopy import visual, event, core
from generateStudyTrials import *
import time



    
win = visual.Window([1000, 750], color = 'white', units = 'pix')
generateTrials('project/studyTrials.csv', 'project/testTrials.csv', '1')
study_trials = importTrials('project/studyTrials.csv')
test_trials = importTrials('project/testTrials.csv')
pic = visual.ImageStim(win=win, mask=None,interpolate=True)
incorrectFeedback = visual.TextStim(win=win,text='REPEAT MISS',color="red",height=60)
prompt = visual.TextStim(win = win, text = 'Have you seen this exact image in part1?', color = 'red', height = 26)
prompt.setPos([0, -260])
prompt2 = visual.TextStim(win = win, text = 'Definitely Not | 1 2 3 4 5 | Definitely Yes', color = 'red', height = 26)
prompt2.setPos([0, -320])
study_output = []
test_output = []
counter = 0

for trial in study_trials:
    counter += 1
    diction = {'trial number': counter, 'image category': trial['img'][0:len(trial['img']) - 6], 
               'image filename': trial['img'], 'repeat': trial['rep'], 'type': trial['type'], 'response': 'NA',
               'correct': '1', 'reactTime': 0}
    print trial['rep']
    pic.setImage('project/visual/' + trial['img'])
    pic.draw()
    win.flip()
    startTime = time.clock()
    reactTime = 'NA'
    core.wait(1)
    win.flip()
    core.wait(0.5)
    response = event.getKeys(keyList = ['q', 'space'])
    if trial['rep'] == 'True':
        if len(response) != 0:
            diction['response'] = response[0]
            if response[0] == 'q':
                break
            elif response[0] == 'space':
                endTime = time.clock()
                reactTime = endTime - startTime
                print reactTime
                diction['reactTime'] = reactTime
                win.flip()
                core.wait(1)
            else:
                diction['correct'] = '0'
                incorrectFeedback.draw()
                win.flip()
                core.wait(1)
        else:
            diction['correct'] = '0'
            incorrectFeedback.draw()
            win.flip()
            core.wait(1)
    else:
        if len(response) != 0:
            if response[0] == 'q':
                break
        win.flip()
        core.wait(0.5)
    study_output.append(diction)

win.flip()
core.wait(3)
counter = 0
for trial in test_trials:
    counter += 1
    diction = {'trial number': counter, 'image category': trial['img'][0:len(trial['img']) - 6], 
               'image filename': trial['img'], 'neworold': trial['neworold'], 'type': trial['type'], 'response': '0',
               'correct': '0', 'reactTime': 'NA'}
    print trial['rep']
    pic.setImage('project/visual/' + trial['img'])
    pic.draw()
    prompt.draw()
    prompt2.draw()
    win.flip()
    startTime = time.clock()
    reactTime = 'NA'
    response = event.waitKeys(keyList = ['q', '1', '2', '3', '4', '5'])
    if trial['rep'] == 'True':
        if len(response) != 0:
            diction['response'] = response[0]
            if response[0] == 'q':
                break
            elif response[0] == '4' or response[0] == '5':
                endTime = time.clock()
                reactTime = endTime - startTime
                diction['correct'] = '1'
                win.flip()
                core.wait(0.5)
            else:
                win.flip()
                core.wait(0.5)
        else:
            win.flip()
            core.wait(0.5)
    else:
        if len(response) != 0:
            diction['response'] = response[0]
            if response[0] == 'q':
                break
            if response[0] == '1' or response[0] == '2':
                endTime = time.clock()
                reactTime = endTime - startTime
                diction['correct'] = '1'
        win.flip()
        core.wait(0.5)
    test_output.append(diction)
        
with open('project/studyResults.csv', 'wb') as f:
    w = csv.writer(f)
    w.writerows([study_output[0].keys()])
    for trial in study_output:
        w.writerows([trial.values()])

with open('project/testResults.csv', 'wb') as f:
    w = csv.writer(f)
    w.writerows([test_output[0].keys()])
    for trial in test_output:
        w.writerows([trial.values()])


win.close()







