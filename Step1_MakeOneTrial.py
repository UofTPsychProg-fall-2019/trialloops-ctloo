#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 1
Use this template script to present one trial with your desired structure
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='gray', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()

#%% up to you!
# this is where you build a trial that you might actually use one day!
# just try to make one trial ordering your lines of code according to the 
# sequence of events that happen on one trial
# if you're stuck you can use the responseExercise.py answer as a starting point 

# maybe start by making stimulus objects (e.g. myPic = visual.ImageStim(...))
baseInstructions = visual.TextStim(win, alignHoriz = 'center', height = .03, text='You will see a series of images and are required to make a judgement on them.') 
myInstructions = visual.ImageStim(win, size = None, pos = (0,0), image ='indoor_instructions.jpg')
endInstructions = visual.TextStim(win, alignHoriz = 'center', height = .03, text='Thanks for playing') 
myPic = visual.ImageStim(win, size = None, pos = (0,0), image = '001a.jpg')

#display instructions until a key is pressed
baseInstructions.draw()
win.flip()
event.waitKeys()

myInstructions.draw()
win.flip()
event.waitKeys()

  
# then draw all stimuli
myPic.draw()

# then flip your window
win.flip()

# then record your responses
#keys = event.getKeys(keyList=('1','2'))
keys = event.waitKeys(maxWait = 4, keyList = ('1','2'))
print(keys)

# rt as a function of 

endInstructions.draw()
win.flip()

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(2)
win.close()
