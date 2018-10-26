import random
import csv


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
    study_trial.append([study_trials[i]])

with open('project/studyTrials.csv', 'wb') as f:
    w = csv.writer(f)
    for trial in study_trial:
        w.writerows([trial])
        
        
        

