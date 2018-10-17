import random
import csv






def generateTrials(trialName):
    trials = []
    for m in range(10):
        flip = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while True:
            flipPoint = random.choice(range(16))
            if flipPoint == 0:
                continue
            else:
                break
        flip[flipPoint] = 1
        list = []
        repeat = random.choice([0, 1])
        isFlip = True
        for i in range(16):
            if repeat == 1:
                item = ''
                if flip[i] == 1:
                    isFlip = False
                if i % 2 == 0:
                    if isFlip:
                        item = 'redcircle'
                    else:
                        item = 'redsquare'
                    list.append(item)
                else:
                    if isFlip:
                        item = 'bluesquare'
                    else:
                        item = 'bluecircle'
                    list.append(item)
            else:
                item = ''
                if i % 2 == 0:
                    item = 'redcircle'
                    list.append(item)
                else:
                    item = 'bluesquare'
                    list.append(item)
        list.append(repeat)
        trials.append(list)
        
    
    with open(trialName, 'wb') as f:
        w = csv.writer(f)
        for data in trials:
            w.writerows([data])

