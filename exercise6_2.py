from psychopy import visual, event, core
import random

win = visual.Window([800, 600], color = 'black', units = 'pix')
locations = [[-15, 0], [15, 0]]
flip = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
flipPoint = random.choice(range(16))
flip[flipPoint] = 1; 
isFlip = True;

for i in range(16):
    if flip[i] == 1:
        isFlip = False
    circle = visual.Circle(win, size = 20)
    circle.setPos(locations[0])
    square = visual.Rect(win, size = 40)
    square.setPos(locations[1])
    
    if i % 2 == 0:
        if isFlip:
            circle.setFillColor('red')
            circle.setLineColor('red')
            circle.setPos([30 * i - 240, 0])
            circle.draw()
        else:
            square.setFillColor('red')
            square.setLineColor('red')
            square.setPos([30 * i - 240, 0])
            square.draw()
    else:
        if isFlip:
            square.setFillColor('blue')
            square.setLineColor('blue')
            square.setPos([30 * i - 240, 0])
            square.draw()
        else:
            circle.setFillColor('blue')
            circle.setLineColor('blue')
            circle.setPos([30 * i - 240, 0])
            circle.draw()

win.flip()
event.waitKeys('q')
win.close()
core.quit()


    