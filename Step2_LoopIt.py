#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
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
from psychopy.hardware import keyboard

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='gray', unit='height') 
kb = keyboard.Keyboard()

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()


#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things
# maybe start by making stimulus objects (e.g. myPic = visual.ImageStim(...))
baseInstructions = visual.TextStim(win, alignHoriz = 'center', height = .03, text='You will see a series of images and are required to make a judgement on them.\n\nSome of these items will be partially obsured. Do your best to make your judgements') 
myInstructions = visual.ImageStim(win, size = None, pos = (0,0), image ='indoor_instructions.jpg')
endInstructions = visual.TextStim(win, alignHoriz = 'center', height = .03, text='Thanks for playing') 

# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
# e.g. stim = ['1.jpg','2.jpg','3.jpg']
stim = ['001a.jpg', '002a.jpg', '003a.jpg']

#display instructions until a key is pressed
baseInstructions.draw()
win.flip()
event.waitKeys()

myInstructions.draw()
win.flip()
event.waitKeys()
# make your loop
for t in stim :
    #clear events
    
    event.clearEvents()
    
    # include your trial code in your loop but replace anything that should
    # change on each trial with a variable that uses your iterater
    # e.g. thisStimName = stim[t]
    #      thisStim = visual.ImageStim(win, image=thisStimName ...)
    
    myPic = visual.ImageStim(win, size = None, pos = (0,0), image=t)
    myPic.draw()
    win.flip()
    keys = event.waitKeys(maxWait = 4, keyList = ['1','2'])
    print(keys) 
    
    
    # if you're recording responses, be sure to store your responses in a list
    # or DataFrame which also uses your iterater!


#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

endInstructions.draw()
win.flip()

core.wait(2)
win.close()
