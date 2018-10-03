import time
import random
from psychopy import visual, core, event,sound
win = visual.Window([800,600],color="black", units='pix')

rect = visual.Rect(win,fillColor="blue")
aspect = {'wide':[200,100], 'narrow':[100,200]}
validKeys = {'wide':'w', 'narrow':'n'}



for curIter in range(20):
    win.flip()
    core.wait(.5)
    curAspect  = random.choice(aspect.values())
    for key, value in aspect.items():
        if curAspect == value:
            typeRec = key
    #typeRec = aspect.keys()[aspect.values().index(curAspect)]
    rect = visual.Rect(win,fillColor="blue", size = curAspect)
    rect.draw()
    win.flip()
    startTime = time.clock()
    resp = event.waitKeys(keyList=validKeys.values())
    endTime = time.clock()
    timer = endTime - startTime
    keyPress = resp[0]
    if keyPress == validKeys[typeRec]:
        print 1, timer
        print "bleep"
    else:
        print 0, timer
        print "buzz"
win.close()

