from psychopy import visual, event, core
import random

win = visual.Window([800, 600], color = 'black', units = 'pix')
locations = [[-15, 0], [15, 0]]

for i in range(16):
    circle = visual.Circle(win, size = 20)
    circle.setPos(locations[0])
    circle.setFillColor('red')
    circle.setLineColor('red')
    square = visual.Rect(win, size = 40)
    square.setPos(locations[1])
    square.setFillColor('blue')
    square.setLineColor('blue')
    if i % 2 == 0:
        circle.setPos([30 * i - 240, 0])
        circle.draw()
    else:
        square.setPos([30 * i - 240, 0])
        square.draw()

win.flip()
event.waitKeys('q')
win.close()
core.quit()


    