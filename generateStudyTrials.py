import random
import csv
import time



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




def generateTrials(name1, name2, whichSet):
    stims = [line.rstrip() for line in open('project/all_stims.txt')]
    #for i in range(len(stims)):
        #stims[i] = stims[i] + '_1.png'
    #stims2 = [line.rstrip() for line in open('project/all_stims.txt')]
    #for stim in stims2:
       # stim = stim + '_2.png'
        #stims.append(stim)
    special = [line.rstrip() for line in open('project/special_stims.txt')]
    info = importTrials('project/stimulus_info.csv')
    study_trials = []
    original = []
    i = 0
    for i in range(186):
        stim = stims[i]
        if special.__contains__(stim):
            continue
        else:
            add = stim + '_' + whichSet + '.png'
            study_trials.append(add)
            original.append(stim)
    category = []
    if whichSet == '1':
        for i in range(26):
            category.append(info[i]['category1'] + '_' + whichSet + '.png')
    else:
        for i in range(26):
            category.append(info[i]['category2'] + '_' + whichSet + '.png')
    repeat = []
    i = 0
    while i < 20:
        stim = random.choice(study_trials)
        if repeat.__contains__(stim):
            continue
        elif special.__contains__(stim):
            continue
        else:
            repeat.append(stim)
            i = i + 1
    study_trials.extend(category)
    study_trial = []
    i = 0
    for i in range(160):
        diction = {'img': study_trials[i], 'rep': False}
        study_trial.append(diction)
    i = 0
    for i in range(20):
        diction = {'img': repeat[i], 'rep': True}
        study_trial.append(diction)
    ifRepeat = True
    while ifRepeat:
        random.shuffle(study_trial)
        ifRepeat = False
        i = 0
        for i in range(5):
            if study_trial[i]['rep']:
                ifRepeat = True
        i = 0
        for i in range(179):
            if study_trial[i]['img'] == study_trial[i + 1]['img']:
                ifRepeat = True
    
    with open(name1, 'wb') as f:
        w = csv.writer(f)
        w.writerows([study_trial[0].keys()])
        for trial in study_trial:
            w.writerows([trial.values()])

    i = 0
    test1 = []
    while i < 50:
        rdm = random.choice(range(180))
        if test1.__contains__(study_trial[rdm]):
            continue
        else:
            test1.append(study_trial[rdm])
            i = i + 1
    category2 = []
    if whichSet == '1':
        i = 0
        for i in range(26):
            category2.append(info[i]['category2'] + '_' + whichSet + '.png')
    else:
        i = 0
        for i in range(26):
            category2.append(info[i]['category1'] + '_' + whichSet + '.png')
    for i in range(26):
        diction = {'img': category2[i], 'rep': False}
        test1.append(diction)
    i = 0
    test2 = []
    while i < 24:
        test_stim = random.choice(original)
        if whichSet == '1':
            test_stim = test_stim + '_2.png'
        else:
            test_stim = test_stim + '_1.png'
        if test2.__contains__(test_stim):
            continue
        else:
            diction = {'img': test_stim, 'rep': False}
            test2.append(diction)
            i = i + 1
    test1.extend(test2)
    random.shuffle(test1)
    
    with open(name2, 'wb') as f:
        w = csv.writer(f)
        w.writerows([test1[0].keys()])
        for trial in test1:
            w.writerows([trial.values()])
    
    
        
    


#generateTrials('project/studyTrials.csv', 'project/testTrials.csv', '1')
        
        
        

