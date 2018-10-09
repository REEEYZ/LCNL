# -*- coding: utf-8 -*-
import random
import csv
import collections

categories = {'Happy':':)', 'Angry':':<', 'Sad':':('}
actors = ['001m', '001w', '002m', '002w', '003m', '003w', '004m', '004w', '005m', '005w']
suffix = '_90_60.jpg'
responseMapping = {1:'w',0:'n'}
numTrials = 40


def randomButNot(l,toExclude):
	chosen = random.choice(l)  
	while toExclude in chosen:
		chosen = random.choice(l)
	return chosen



trials=[]
propMatch  = .6
for i in range(numTrials):
	emotionPrompt = random.choice(categories.keys())
	shownActor = random.choice(actors)
	isMatch = int(random.random()<propMatch)

	if isMatch:
		shownCategory = emotionPrompt
		targetFaceImage = categories[emotionPrompt] 
	else:
		shownCategory = randomButNot(categories.keys(), emotionPrompt)
		targetFaceImage = categories[shownCategory]
        dic = collections.OrderedDict()
        dic['isMatch'] = isMatch
        dic['emotionPrompt'] = emotionPrompt
        dic['shownActor'] = shownActor
        dic['shownCategory'] = shownCategory
        dic['targetFaceImage'] = targetFaceImage
        trials.append(dic)

    

column = ['isMatch', 'emotionPrompt', 'shownActor', 'shownCategory', 'targetFaceImage']
with open('trials.csv','wb') as f:
    w = csv.writer(f)
    w.writerows([data.keys()])
    for data in trials:
        w.writerows([data.values()])
    
    
    #for m in range(len(trials)):
     #    w.writerows(trials[m].values())
    
   

