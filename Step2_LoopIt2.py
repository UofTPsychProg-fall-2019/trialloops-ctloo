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
import ctypes
from psychopy import visual, core, event, gui, logging
from psychopy.hardware import keyboard
import win32api

# Bring up a window asking for the subject number. Also creates the file name
# Alerts if a file of the same name already exists and asks if overwrite should occur
# Exits process if a number isn't provided
expName = 'PS5'
fileName = ''
while True:
    expInfo = {'subjNum':''}
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    if dlg.OK == False: core.quit()  # user pressed cancel so exit experiment
    fileName = expName + '_' + expInfo['subjNum']+'.csv'
    break


# create a dataframe to hold output
outVars = ['trial', 'image', 'degredation', 'response', 'rt']    
out = pd.DataFrame(columns=outVars)

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='gray', unit='height') 

#some constants
HICHARLOTTE = visual.TextStim(win, alignHoriz = 'center', height = .03, text = 'Hi Charlotte,\nThis is the study phase of a project Im currently running.\n\nThis will randomly sample five trials from a conditions list, so the trials should be different each run through.\n\nThis is an incidental encoding task, so the responses arent checked for accuracy.\n\nPress any space to continue')
BASEINSTRUCTIONS = visual.TextStim(win, alignHoriz = 'center', height = .03, text='You will see a series of images and are required to make a judgement on them.\n\nSome of these items will be partially obsured. Do your best to make your judgements!\n\nPress any key to continue') 
INDOORINSTRUCTIONS = visual.TextStim(win, alignHoriz = 'center', height = .03, text ='For the next set of images, please make the following decision:\n\nIs the following object typically found indoors or outdoors?\n\n\n1 - Indoors\t\t\t\t\t\t2 - Outdoors\n\nPress any key to continue')
ENDINSTRUCTIONS = visual.TextStim(win, alignHoriz = 'center', height = .03, text='Thanks for playing.\n\nIn two seconds this window will close.')
NTRIALS = 5 #The study phase is actually 440 trials, but let's only do 5
ISI = 1 #The inter stimulus interval in seconds
fixation = visual.Circle(win, pos=(0,0), radius=(0.01), lineColor='black', fillColor='black')

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
trialClock = core.Clock() # trial clock
eventClock = core.Clock() # event clock


# make a list or a pd.DataFrame that contains trial-specific info (stimulus, etc)
conditionList = pd.read_csv('Sub-002_conditions_Study.csv')

# randomize trials
conditionList = conditionList.sample(frac=1)
conditionList = conditionList.reset_index()

#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things
# maybe start by making stimulus objects (e.g. myPic = visual.ImageStim(...))

#display instructions until a key is pressed
HICHARLOTTE.draw()
win.flip()
event.waitKeys()

BASEINSTRUCTIONS.draw()
win.flip()
event.waitKeys()

INDOORINSTRUCTIONS.draw()
win.flip()
event.waitKeys()

# make your loop
for t in np.arange(0,NTRIALS) :
    #clear events
    
    event.clearEvents()
    eventClock.reset()
    # include your trial code in your loop but replace anything that should
    # change on each trial with a variable that uses your iterater
    # e.g. thisStimName = stim[t]
    #      thisStim = visual.ImageStim(win, image=thisStimName ...)
    
    out.loc[t,'trial'] = t + 1
    out.loc[t,'image'] = conditionList.loc[t,'Image']
    out.loc[t,'degredation'] = conditionList.loc[t,'Degredation']

    studyPic = visual.ImageStim(win, size = None, pos = (0,0), image= 'Images/'+conditionList.loc[t,'Image'])
    
    while eventClock.getTime() < ISI:
        fixation.draw()
        win.flip()
        #core.wait(.001)
    
    #record study parameters
    
    trialClock.reset()
    studyPic.draw()
    win.flip()
    keys = event.waitKeys(maxWait = 4, keyList = ['1','2'])
    
    # if you're recording responses, be sure to store your responses in a list
    # or DataFrame which also uses your iterater!
    out.loc[t, 'response'] = keys
    out.loc[t, 'rt'] = trialClock.getTime()
    
    


#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

out.to_csv(fileName, index = False)

ENDINSTRUCTIONS.draw()
win.flip()

core.wait(2)
win.close()
