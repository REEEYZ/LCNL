import random
import csv

def generateTrials(name):
    stims = [line.rstrip() for line in open('project/all_stims.txt')]
    for i in range(len(stims)):
        stims[i] = stims[i] + '_1.png'
    stims2 = [line.rstrip() for line in open('project/all_stims.txt')]
    for stim in stims2:
        stim = stim + '_2.png'
        stims.append(stim)
    study_trials = []
    i = 0
    while i < 160:
        stim = random.choice(stims)
        if study_trials.__contains__(stim):
            continue
        else:
            study_trials.append(stim)
            i = i + 1
    repeat = []
    i = 0
    while i < 20:
        stim = random.choice(study_trials)
        if repeat.__contains__(stim):
            continue
        else:
            repeat.append(stim)
            i = i + 1
    i =  0
    for i in range(20):
        study_trials.append(repeat[i])
    random.shuffle(study_trials)
    
    study_trial = []
    i = 0
    for i in range(180):
        study_trial.append({'img': study_trials[i], 'rep': False})
    check = True
    i= 0
    while check:
        check = False
        for i in range(179):
            if study_trial[i]['img'] == study_trial[i + 1]['img']:
                check = True
                index = random.choice(range(180))
                study_trial[i + 1], study_trial[index] = study_trial[index], study_trial[i + 1]
    i = 0
    for i in range(179):
        j = 0
        for j in range(i + 1):
            if study_trial[j]['img'] == study_trial[i + 1]['img']:
                study_trial[i + 1]['rep'] = True
    
    
    with open(name, 'wb') as f:
        w = csv.writer(f)
        w.writerows([study_trial[0].keys()])
        for trial in study_trial:
            w.writerows([trial.values()])
            
#generateTrials('project/studyTrials.csv')
        
        
        

