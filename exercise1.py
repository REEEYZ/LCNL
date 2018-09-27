# -*- coding: utf-8 -*-
import time
import sys
from psychopy import visual,event,core
 
win = visual.Window([400,400],color="black", units='pix') #open a window
square = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100]) #make a blue square
square.draw() #draw the square to the buffer
win.flip() #make the buffer visible
core.wait(5) #pause for 500 ms (half a second)
square.fillColor = "blue"
square.draw() #draw the square to the buffer
win.flip() #make the buffer visible
core.wait(5) #pause for 500 ms (half a second)
win.close() #close the window -- don't need this if you're running this as a separate file
sys.exit()
