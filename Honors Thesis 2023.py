#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on March 25, 2024, at 14:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import serial 
import pandas as pd
import re

ser = serial.Serial('COM1')
ser.close()
cond_set = pd.read_excel('Stimuli_HT/Honors thesis 2023_rand.xlsx')

def send_trigger(conditions, noises):
    if conditions == '1.0' and noises == 'Clear':
        ser.write((1).to_bytes(1, 'big'))
    elif conditions == '1.0' and noises == 'Noise':
        ser.write((2).to_bytes(1, 'big'))
    elif conditions == '1.5' and noises == 'Clear':
        ser.write((3).to_bytes(1, 'big'))
    elif conditions == '1.5' and noises == 'Noise':
        ser.write((4).to_bytes(1, 'big'))
    elif conditions == '2.0' and noises == 'Clear':
        ser.write((5).to_bytes(1, 'big'))
    elif conditions =='2.0' and noises == 'Noise':
        ser.write((6).to_bytes(1, 'big'))


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Honors Thesis 2023'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Public\\Experiments\\TCSMF\\Honors Thesis 2023.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "CondtionSet"
CondtionSetClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='INSTRUCTOR:\n\nPlease press "Spacebar" to continue!\n\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
myIndices= expInfo['session']

# Initialize components for Routine "Instruction"
InstructionClock = core.Clock()
cond_text = visual.TextStim(win=win, name='cond_text',
    text='',
    font='Open Sans',
    pos=(0.63,0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Inst_text = visual.TextStim(win=win, name='Inst_text',
    text='In this experiment you will listen to 6 lecture audios and after each lecture you will be assessed on the content of the lecture that you just heard.\n\n\nPlease press "Spacebar" to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "T1A"
T1AClock = core.Clock()
sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='Stimuli_HT/FixCross.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "Pre_assement_inst"
Pre_assement_instClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='You are now going to complete 10 multiple choice questions on the audio lecture that you just heard. \n\nPlease try to answer questions based on the lecture you heard and avoid using knowledge you already had.\n\nPress "Spacebar" to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "T1Q1"
T1Q1Clock = core.Clock()
T1I1 = visual.ImageStim(
    win=win,
    name='T1I1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T1Q1R = keyboard.Keyboard()

# Initialize components for Routine "T1Q2"
T1Q2Clock = core.Clock()
T1I2 = visual.ImageStim(
    win=win,
    name='T1I2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T1Q2R = keyboard.Keyboard()

# Initialize components for Routine "T1Q3"
T1Q3Clock = core.Clock()
T1I3 = visual.ImageStim(
    win=win,
    name='T1I3', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T1Q3R = keyboard.Keyboard()

# Initialize components for Routine "T1Q4"
T1Q4Clock = core.Clock()
T1I4 = visual.ImageStim(
    win=win,
    name='T1I4', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T1Q4R = keyboard.Keyboard()

# Initialize components for Routine "T1Q5"
T1Q5Clock = core.Clock()
T1I5 = visual.ImageStim(
    win=win,
    name='T1I5', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T1Q5R = keyboard.Keyboard()

# Initialize components for Routine "T1Q6"
T1Q6Clock = core.Clock()
T1I6 = visual.ImageStim(
    win=win,
    name='T1I6', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T1Q6R = keyboard.Keyboard()

# Initialize components for Routine "T1Q7"
T1Q7Clock = core.Clock()
T1I7 = visual.ImageStim(
    win=win,
    name='T1I7', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T1Q7R = keyboard.Keyboard()

# Initialize components for Routine "T1Q8"
T1Q8Clock = core.Clock()
T1I8 = visual.ImageStim(
    win=win,
    name='T1I8', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T1Q8R = keyboard.Keyboard()

# Initialize components for Routine "T1Q9"
T1Q9Clock = core.Clock()
T1I9 = visual.ImageStim(
    win=win,
    name='T1I9', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T1Q9R = keyboard.Keyboard()

# Initialize components for Routine "T1Q10"
T1Q10Clock = core.Clock()
T1I10 = visual.ImageStim(
    win=win,
    name='T1I10', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T1Q10R = keyboard.Keyboard()

# Initialize components for Routine "Trial_Break"
Trial_BreakClock = core.Clock()
Break_message = visual.TextStim(win=win, name='Break_message',
    text='You can take a break and continue when you are ready.\n\nPlease let the instructor know if you want to leave the booth.\n\nPress "Spacebar" to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "T2A"
T2AClock = core.Clock()
sound_2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Stimuli_HT/FixCross.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "Pre_assement_inst"
Pre_assement_instClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='You are now going to complete 10 multiple choice questions on the audio lecture that you just heard. \n\nPlease try to answer questions based on the lecture you heard and avoid using knowledge you already had.\n\nPress "Spacebar" to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "T2Q1"
T2Q1Clock = core.Clock()
T2I1 = visual.ImageStim(
    win=win,
    name='T2I1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T2Q1R = keyboard.Keyboard()

# Initialize components for Routine "T2Q2"
T2Q2Clock = core.Clock()
T2I2 = visual.ImageStim(
    win=win,
    name='T2I2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T2Q2R = keyboard.Keyboard()

# Initialize components for Routine "T2Q3"
T2Q3Clock = core.Clock()
T2I3 = visual.ImageStim(
    win=win,
    name='T2I3', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T2Q3R = keyboard.Keyboard()

# Initialize components for Routine "T2Q4"
T2Q4Clock = core.Clock()
T2I4 = visual.ImageStim(
    win=win,
    name='T2I4', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T2Q4R = keyboard.Keyboard()

# Initialize components for Routine "T2Q5"
T2Q5Clock = core.Clock()
T2I5 = visual.ImageStim(
    win=win,
    name='T2I5', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T2Q5R = keyboard.Keyboard()

# Initialize components for Routine "T2Q6"
T2Q6Clock = core.Clock()
T2I6 = visual.ImageStim(
    win=win,
    name='T2I6', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T2Q6R = keyboard.Keyboard()

# Initialize components for Routine "T2Q7"
T2Q7Clock = core.Clock()
T2I7 = visual.ImageStim(
    win=win,
    name='T2I7', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T2Q7R = keyboard.Keyboard()

# Initialize components for Routine "T2Q8"
T2Q8Clock = core.Clock()
T2I8 = visual.ImageStim(
    win=win,
    name='T2I8', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T2Q8R = keyboard.Keyboard()

# Initialize components for Routine "T2Q9"
T2Q9Clock = core.Clock()
T2I9 = visual.ImageStim(
    win=win,
    name='T2I9', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T2Q9R = keyboard.Keyboard()

# Initialize components for Routine "T2Q10"
T2Q10Clock = core.Clock()
T2I10 = visual.ImageStim(
    win=win,
    name='T2I10', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T2Q10R = keyboard.Keyboard()

# Initialize components for Routine "Trial_Break"
Trial_BreakClock = core.Clock()
Break_message = visual.TextStim(win=win, name='Break_message',
    text='You can take a break and continue when you are ready.\n\nPlease let the instructor know if you want to leave the booth.\n\nPress "Spacebar" to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "T3A"
T3AClock = core.Clock()
sound_3 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='Stimuli_HT/FixCross.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "Pre_assement_inst"
Pre_assement_instClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='You are now going to complete 10 multiple choice questions on the audio lecture that you just heard. \n\nPlease try to answer questions based on the lecture you heard and avoid using knowledge you already had.\n\nPress "Spacebar" to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "T3Q1"
T3Q1Clock = core.Clock()
T3I1 = visual.ImageStim(
    win=win,
    name='T3I1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T3Q1R = keyboard.Keyboard()

# Initialize components for Routine "T3Q2"
T3Q2Clock = core.Clock()
T3I2 = visual.ImageStim(
    win=win,
    name='T3I2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T3Q2R = keyboard.Keyboard()

# Initialize components for Routine "T3Q3"
T3Q3Clock = core.Clock()
T3I3 = visual.ImageStim(
    win=win,
    name='T3I3', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T3Q3R = keyboard.Keyboard()

# Initialize components for Routine "T3Q4"
T3Q4Clock = core.Clock()
T3I4 = visual.ImageStim(
    win=win,
    name='T3I4', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T3Q4R = keyboard.Keyboard()

# Initialize components for Routine "T3Q5"
T3Q5Clock = core.Clock()
T3I5 = visual.ImageStim(
    win=win,
    name='T3I5', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T3Q5R = keyboard.Keyboard()

# Initialize components for Routine "T3Q6"
T3Q6Clock = core.Clock()
T3I6 = visual.ImageStim(
    win=win,
    name='T3I6', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T3Q6R = keyboard.Keyboard()

# Initialize components for Routine "T3Q7"
T3Q7Clock = core.Clock()
T3I7 = visual.ImageStim(
    win=win,
    name='T3I7', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T3Q7R = keyboard.Keyboard()

# Initialize components for Routine "T3Q8"
T3Q8Clock = core.Clock()
T3I8 = visual.ImageStim(
    win=win,
    name='T3I8', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T3Q8R = keyboard.Keyboard()

# Initialize components for Routine "T3Q9"
T3Q9Clock = core.Clock()
T3I9 = visual.ImageStim(
    win=win,
    name='T3I9', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T3Q9R = keyboard.Keyboard()

# Initialize components for Routine "T3Q10"
T3Q10Clock = core.Clock()
T3I10 = visual.ImageStim(
    win=win,
    name='T3I10', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T3Q10R = keyboard.Keyboard()

# Initialize components for Routine "Trial_Break"
Trial_BreakClock = core.Clock()
Break_message = visual.TextStim(win=win, name='Break_message',
    text='You can take a break and continue when you are ready.\n\nPlease let the instructor know if you want to leave the booth.\n\nPress "Spacebar" to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "T4A"
T4AClock = core.Clock()
sound_4 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_4')
sound_4.setVolume(1.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='Stimuli_HT/FixCross.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "Pre_assement_inst"
Pre_assement_instClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='You are now going to complete 10 multiple choice questions on the audio lecture that you just heard. \n\nPlease try to answer questions based on the lecture you heard and avoid using knowledge you already had.\n\nPress "Spacebar" to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "T4Q1"
T4Q1Clock = core.Clock()
T4I1 = visual.ImageStim(
    win=win,
    name='T4I1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T4Q1R = keyboard.Keyboard()

# Initialize components for Routine "T4Q2"
T4Q2Clock = core.Clock()
T4I2 = visual.ImageStim(
    win=win,
    name='T4I2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T4Q2R = keyboard.Keyboard()

# Initialize components for Routine "T4Q3"
T4Q3Clock = core.Clock()
T4I3 = visual.ImageStim(
    win=win,
    name='T4I3', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T4Q3R = keyboard.Keyboard()

# Initialize components for Routine "T4Q4"
T4Q4Clock = core.Clock()
T4I4 = visual.ImageStim(
    win=win,
    name='T4I4', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T4Q4R = keyboard.Keyboard()

# Initialize components for Routine "T4Q5"
T4Q5Clock = core.Clock()
T4I5 = visual.ImageStim(
    win=win,
    name='T4I5', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T4Q5R = keyboard.Keyboard()

# Initialize components for Routine "T4Q6"
T4Q6Clock = core.Clock()
T4I6 = visual.ImageStim(
    win=win,
    name='T4I6', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T4Q6R = keyboard.Keyboard()

# Initialize components for Routine "T4Q7"
T4Q7Clock = core.Clock()
T4I7 = visual.ImageStim(
    win=win,
    name='T4I7', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T4Q7R = keyboard.Keyboard()

# Initialize components for Routine "T4Q8"
T4Q8Clock = core.Clock()
T4I8 = visual.ImageStim(
    win=win,
    name='T4I8', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T4Q8R = keyboard.Keyboard()

# Initialize components for Routine "T4Q9"
T4Q9Clock = core.Clock()
T4I9 = visual.ImageStim(
    win=win,
    name='T4I9', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T4Q9R = keyboard.Keyboard()

# Initialize components for Routine "T4Q10"
T4Q10Clock = core.Clock()
T4I10 = visual.ImageStim(
    win=win,
    name='T4I10', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T4Q10R = keyboard.Keyboard()

# Initialize components for Routine "Trial_Break"
Trial_BreakClock = core.Clock()
Break_message = visual.TextStim(win=win, name='Break_message',
    text='You can take a break and continue when you are ready.\n\nPlease let the instructor know if you want to leave the booth.\n\nPress "Spacebar" to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "T5A"
T5AClock = core.Clock()
sound_5 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_5')
sound_5.setVolume(1.0)
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='Stimuli_HT/FixCross.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "Pre_assement_inst"
Pre_assement_instClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='You are now going to complete 10 multiple choice questions on the audio lecture that you just heard. \n\nPlease try to answer questions based on the lecture you heard and avoid using knowledge you already had.\n\nPress "Spacebar" to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "T5Q1"
T5Q1Clock = core.Clock()
T5I1 = visual.ImageStim(
    win=win,
    name='T5I1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T5Q1R = keyboard.Keyboard()

# Initialize components for Routine "T5Q2"
T5Q2Clock = core.Clock()
T5I2 = visual.ImageStim(
    win=win,
    name='T5I2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T5Q2R = keyboard.Keyboard()

# Initialize components for Routine "T5Q3"
T5Q3Clock = core.Clock()
T5I3 = visual.ImageStim(
    win=win,
    name='T5I3', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T5Q3R = keyboard.Keyboard()

# Initialize components for Routine "T5Q4"
T5Q4Clock = core.Clock()
T5I4 = visual.ImageStim(
    win=win,
    name='T5I4', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T5Q4R = keyboard.Keyboard()

# Initialize components for Routine "T5Q5"
T5Q5Clock = core.Clock()
T5I5 = visual.ImageStim(
    win=win,
    name='T5I5', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T5Q5R = keyboard.Keyboard()

# Initialize components for Routine "T5Q6"
T5Q6Clock = core.Clock()
T5I6 = visual.ImageStim(
    win=win,
    name='T5I6', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T5Q6R = keyboard.Keyboard()

# Initialize components for Routine "T5Q7"
T5Q7Clock = core.Clock()
T5I7 = visual.ImageStim(
    win=win,
    name='T5I7', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T5Q7R = keyboard.Keyboard()

# Initialize components for Routine "T5Q8"
T5Q8Clock = core.Clock()
T5I8 = visual.ImageStim(
    win=win,
    name='T5I8', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T5Q8R = keyboard.Keyboard()

# Initialize components for Routine "T5Q9"
T5Q9Clock = core.Clock()
T5I9 = visual.ImageStim(
    win=win,
    name='T5I9', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T5Q9R = keyboard.Keyboard()

# Initialize components for Routine "T5Q10"
T5Q10Clock = core.Clock()
T5I10 = visual.ImageStim(
    win=win,
    name='T5I10', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T5Q10R = keyboard.Keyboard()

# Initialize components for Routine "Trial_Break"
Trial_BreakClock = core.Clock()
Break_message = visual.TextStim(win=win, name='Break_message',
    text='You can take a break and continue when you are ready.\n\nPlease let the instructor know if you want to leave the booth.\n\nPress "Spacebar" to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "T6A"
T6AClock = core.Clock()
sound_6 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_6')
sound_6.setVolume(1.0)
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='Stimuli_HT/FixCross.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "Pre_assement_inst"
Pre_assement_instClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='You are now going to complete 10 multiple choice questions on the audio lecture that you just heard. \n\nPlease try to answer questions based on the lecture you heard and avoid using knowledge you already had.\n\nPress "Spacebar" to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "T6Q1"
T6Q1Clock = core.Clock()
T6I1 = visual.ImageStim(
    win=win,
    name='T6I1', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T6Q1R = keyboard.Keyboard()

# Initialize components for Routine "T6Q2"
T6Q2Clock = core.Clock()
T6I2 = visual.ImageStim(
    win=win,
    name='T6I2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T6Q2R = keyboard.Keyboard()

# Initialize components for Routine "T6Q3"
T6Q3Clock = core.Clock()
T6I3 = visual.ImageStim(
    win=win,
    name='T6I3', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T6Q3R = keyboard.Keyboard()

# Initialize components for Routine "T6Q4"
T6Q4Clock = core.Clock()
T6I4 = visual.ImageStim(
    win=win,
    name='T6I4', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T6Q4R = keyboard.Keyboard()

# Initialize components for Routine "T6Q5"
T6Q5Clock = core.Clock()
T6I5 = visual.ImageStim(
    win=win,
    name='T6I5', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T6Q5R = keyboard.Keyboard()

# Initialize components for Routine "T6Q6"
T6Q6Clock = core.Clock()
T6I6 = visual.ImageStim(
    win=win,
    name='T6I6', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T6Q6R = keyboard.Keyboard()

# Initialize components for Routine "T6Q7"
T6Q7Clock = core.Clock()
T6I7 = visual.ImageStim(
    win=win,
    name='T6I7', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T6Q7R = keyboard.Keyboard()

# Initialize components for Routine "T6Q8"
T6Q8Clock = core.Clock()
T6I8 = visual.ImageStim(
    win=win,
    name='T6I8', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T6Q8R = keyboard.Keyboard()

# Initialize components for Routine "T6Q9"
T6Q9Clock = core.Clock()
T6I9 = visual.ImageStim(
    win=win,
    name='T6I9', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T6Q9R = keyboard.Keyboard()

# Initialize components for Routine "T6Q10"
T6Q10Clock = core.Clock()
T6I10 = visual.ImageStim(
    win=win,
    name='T6I10', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.4, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
T6Q10R = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Experiment Ended\n\nPlease wait for the instructor.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "CondtionSet"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
myIndices= expInfo['session']
# keep track of which components have finished
CondtionSetComponents = [text, key_resp]
for thisComponent in CondtionSetComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
CondtionSetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "CondtionSet"-------
while continueRoutine:
    # get current time
    t = CondtionSetClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=CondtionSetClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CondtionSetComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "CondtionSet"-------
for thisComponent in CondtionSetComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
myIndices= expInfo['session']
# the Routine "CondtionSet" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli_HT/Honors thesis 2023_rand.xlsx', selection=myIndices),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Instruction"-------
    continueRoutine = True
    # update component parameters for each repeat
    cond_text.setText(CondCheck)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    InstructionComponents = [cond_text, Inst_text, key_resp_3]
    for thisComponent in InstructionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    InstructionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Instruction"-------
    while continueRoutine:
        # get current time
        t = InstructionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=InstructionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cond_text* updates
        if cond_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cond_text.frameNStart = frameN  # exact frame index
            cond_text.tStart = t  # local t and not account for scr refresh
            cond_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cond_text, 'tStartRefresh')  # time at next scr refresh
            cond_text.setAutoDraw(True)
        
        # *Inst_text* updates
        if Inst_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Inst_text.frameNStart = frameN  # exact frame index
            Inst_text.tStart = t  # local t and not account for scr refresh
            Inst_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Inst_text, 'tStartRefresh')  # time at next scr refresh
            Inst_text.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Instruction"-------
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('cond_text.started', cond_text.tStartRefresh)
    trials.addData('cond_text.stopped', cond_text.tStopRefresh)
    trials.addData('Inst_text.started', Inst_text.tStartRefresh)
    trials.addData('Inst_text.stopped', Inst_text.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    trials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T1A"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_1.setSound(T1A, hamming=True)
    sound_1.setVolume(1.0, log=False)
    cond = expInfo['session']
    cond
    cond_set = pd.read_excel('Stimuli_HT/Honors thesis 2023_rand.xlsx')
    t1 = cond_set[cond_set['Cond'] == cond]['T1A'].values[0]
    cond_speed = re.search(r'(\d+\.\d+)x', t1).group(1)
    cond_noise = re.search(r'(\w+)_Audio', t1).group(1)
    send_trigger(cond_speed, cond_noise)
    key_resp_12.keys = []
    key_resp_12.rt = []
    _key_resp_12_allKeys = []
    # keep track of which components have finished
    T1AComponents = [sound_1, image_2, key_resp_12]
    for thisComponent in T1AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T1AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T1A"-------
    while continueRoutine:
        # get current time
        t = T1AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T1AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play()  # start the sound (it finishes automatically)
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if sound_1.status == FINISHED:
            continueRoutine = False
        
        # *key_resp_12* updates
        waitOnFlip = False
        if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_12.frameNStart = frameN  # exact frame index
            key_resp_12.tStart = t  # local t and not account for scr refresh
            key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
            key_resp_12.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_12.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_12.getKeys(keyList=['z'], waitRelease=False)
            _key_resp_12_allKeys.extend(theseKeys)
            if len(_key_resp_12_allKeys):
                key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T1AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T1A"-------
    for thisComponent in T1AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_1.started', sound_1.tStart)
    trials.addData('sound_1.stopped', sound_1.tStop)
    trials.addData('image_2.started', image_2.tStartRefresh)
    trials.addData('image_2.stopped', image_2.tStopRefresh)
    ser.write((200).to_bytes(1, 'big'))
    # check responses
    if key_resp_12.keys in ['', [], None]:  # No response was made
        key_resp_12.keys = None
    trials.addData('key_resp_12.keys',key_resp_12.keys)
    if key_resp_12.keys != None:  # we had a response
        trials.addData('key_resp_12.rt', key_resp_12.rt)
    trials.addData('key_resp_12.started', key_resp_12.tStartRefresh)
    trials.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
    # the Routine "T1A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pre_assement_inst"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    Pre_assement_instComponents = [text_5, key_resp_5]
    for thisComponent in Pre_assement_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pre_assement_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pre_assement_inst"-------
    while continueRoutine:
        # get current time
        t = Pre_assement_instClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pre_assement_instClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pre_assement_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pre_assement_inst"-------
    for thisComponent in Pre_assement_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_5.started', text_5.tStartRefresh)
    trials.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    trials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    trials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "Pre_assement_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T1Q1"-------
    continueRoutine = True
    # update component parameters for each repeat
    T1I1.setImage(T1Q1)
    T1Q1R.keys = []
    T1Q1R.rt = []
    _T1Q1R_allKeys = []
    # keep track of which components have finished
    T1Q1Components = [T1I1, T1Q1R]
    for thisComponent in T1Q1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T1Q1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T1Q1"-------
    while continueRoutine:
        # get current time
        t = T1Q1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T1Q1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T1I1* updates
        if T1I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1I1.frameNStart = frameN  # exact frame index
            T1I1.tStart = t  # local t and not account for scr refresh
            T1I1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1I1, 'tStartRefresh')  # time at next scr refresh
            T1I1.setAutoDraw(True)
        
        # *T1Q1R* updates
        waitOnFlip = False
        if T1Q1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1Q1R.frameNStart = frameN  # exact frame index
            T1Q1R.tStart = t  # local t and not account for scr refresh
            T1Q1R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1Q1R, 'tStartRefresh')  # time at next scr refresh
            T1Q1R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T1Q1R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T1Q1R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T1Q1R.status == STARTED and not waitOnFlip:
            theseKeys = T1Q1R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T1Q1R_allKeys.extend(theseKeys)
            if len(_T1Q1R_allKeys):
                T1Q1R.keys = _T1Q1R_allKeys[-1].name  # just the last key pressed
                T1Q1R.rt = _T1Q1R_allKeys[-1].rt
                # was this correct?
                if (T1Q1R.keys == str(CorrT1Q1)) or (T1Q1R.keys == CorrT1Q1):
                    T1Q1R.corr = 1
                else:
                    T1Q1R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T1Q1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T1Q1"-------
    for thisComponent in T1Q1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T1I1.started', T1I1.tStartRefresh)
    trials.addData('T1I1.stopped', T1I1.tStopRefresh)
    # check responses
    if T1Q1R.keys in ['', [], None]:  # No response was made
        T1Q1R.keys = None
        # was no response the correct answer?!
        if str(CorrT1Q1).lower() == 'none':
           T1Q1R.corr = 1;  # correct non-response
        else:
           T1Q1R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T1Q1R.keys',T1Q1R.keys)
    trials.addData('T1Q1R.corr', T1Q1R.corr)
    if T1Q1R.keys != None:  # we had a response
        trials.addData('T1Q1R.rt', T1Q1R.rt)
    trials.addData('T1Q1R.started', T1Q1R.tStartRefresh)
    trials.addData('T1Q1R.stopped', T1Q1R.tStopRefresh)
    # the Routine "T1Q1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T1Q2"-------
    continueRoutine = True
    # update component parameters for each repeat
    T1I2.setImage(T1Q2)
    T1Q2R.keys = []
    T1Q2R.rt = []
    _T1Q2R_allKeys = []
    # keep track of which components have finished
    T1Q2Components = [T1I2, T1Q2R]
    for thisComponent in T1Q2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T1Q2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T1Q2"-------
    while continueRoutine:
        # get current time
        t = T1Q2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T1Q2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T1I2* updates
        if T1I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1I2.frameNStart = frameN  # exact frame index
            T1I2.tStart = t  # local t and not account for scr refresh
            T1I2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1I2, 'tStartRefresh')  # time at next scr refresh
            T1I2.setAutoDraw(True)
        
        # *T1Q2R* updates
        waitOnFlip = False
        if T1Q2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1Q2R.frameNStart = frameN  # exact frame index
            T1Q2R.tStart = t  # local t and not account for scr refresh
            T1Q2R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1Q2R, 'tStartRefresh')  # time at next scr refresh
            T1Q2R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T1Q2R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T1Q2R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T1Q2R.status == STARTED and not waitOnFlip:
            theseKeys = T1Q2R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T1Q2R_allKeys.extend(theseKeys)
            if len(_T1Q2R_allKeys):
                T1Q2R.keys = _T1Q2R_allKeys[-1].name  # just the last key pressed
                T1Q2R.rt = _T1Q2R_allKeys[-1].rt
                # was this correct?
                if (T1Q2R.keys == str(CorrT1Q2)) or (T1Q2R.keys == CorrT1Q2):
                    T1Q2R.corr = 1
                else:
                    T1Q2R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T1Q2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T1Q2"-------
    for thisComponent in T1Q2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T1I2.started', T1I2.tStartRefresh)
    trials.addData('T1I2.stopped', T1I2.tStopRefresh)
    # check responses
    if T1Q2R.keys in ['', [], None]:  # No response was made
        T1Q2R.keys = None
        # was no response the correct answer?!
        if str(CorrT1Q2).lower() == 'none':
           T1Q2R.corr = 1;  # correct non-response
        else:
           T1Q2R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T1Q2R.keys',T1Q2R.keys)
    trials.addData('T1Q2R.corr', T1Q2R.corr)
    if T1Q2R.keys != None:  # we had a response
        trials.addData('T1Q2R.rt', T1Q2R.rt)
    trials.addData('T1Q2R.started', T1Q2R.tStartRefresh)
    trials.addData('T1Q2R.stopped', T1Q2R.tStopRefresh)
    # the Routine "T1Q2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T1Q3"-------
    continueRoutine = True
    # update component parameters for each repeat
    T1I3.setImage(T1Q3)
    T1Q3R.keys = []
    T1Q3R.rt = []
    _T1Q3R_allKeys = []
    # keep track of which components have finished
    T1Q3Components = [T1I3, T1Q3R]
    for thisComponent in T1Q3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T1Q3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T1Q3"-------
    while continueRoutine:
        # get current time
        t = T1Q3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T1Q3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T1I3* updates
        if T1I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1I3.frameNStart = frameN  # exact frame index
            T1I3.tStart = t  # local t and not account for scr refresh
            T1I3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1I3, 'tStartRefresh')  # time at next scr refresh
            T1I3.setAutoDraw(True)
        
        # *T1Q3R* updates
        waitOnFlip = False
        if T1Q3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1Q3R.frameNStart = frameN  # exact frame index
            T1Q3R.tStart = t  # local t and not account for scr refresh
            T1Q3R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1Q3R, 'tStartRefresh')  # time at next scr refresh
            T1Q3R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T1Q3R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T1Q3R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T1Q3R.status == STARTED and not waitOnFlip:
            theseKeys = T1Q3R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T1Q3R_allKeys.extend(theseKeys)
            if len(_T1Q3R_allKeys):
                T1Q3R.keys = _T1Q3R_allKeys[-1].name  # just the last key pressed
                T1Q3R.rt = _T1Q3R_allKeys[-1].rt
                # was this correct?
                if (T1Q3R.keys == str(CorrT1Q3)) or (T1Q3R.keys == CorrT1Q3):
                    T1Q3R.corr = 1
                else:
                    T1Q3R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T1Q3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T1Q3"-------
    for thisComponent in T1Q3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T1I3.started', T1I3.tStartRefresh)
    trials.addData('T1I3.stopped', T1I3.tStopRefresh)
    # check responses
    if T1Q3R.keys in ['', [], None]:  # No response was made
        T1Q3R.keys = None
        # was no response the correct answer?!
        if str(CorrT1Q3).lower() == 'none':
           T1Q3R.corr = 1;  # correct non-response
        else:
           T1Q3R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T1Q3R.keys',T1Q3R.keys)
    trials.addData('T1Q3R.corr', T1Q3R.corr)
    if T1Q3R.keys != None:  # we had a response
        trials.addData('T1Q3R.rt', T1Q3R.rt)
    trials.addData('T1Q3R.started', T1Q3R.tStartRefresh)
    trials.addData('T1Q3R.stopped', T1Q3R.tStopRefresh)
    # the Routine "T1Q3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T1Q4"-------
    continueRoutine = True
    # update component parameters for each repeat
    T1I4.setImage(T1Q4)
    T1Q4R.keys = []
    T1Q4R.rt = []
    _T1Q4R_allKeys = []
    # keep track of which components have finished
    T1Q4Components = [T1I4, T1Q4R]
    for thisComponent in T1Q4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T1Q4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T1Q4"-------
    while continueRoutine:
        # get current time
        t = T1Q4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T1Q4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T1I4* updates
        if T1I4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1I4.frameNStart = frameN  # exact frame index
            T1I4.tStart = t  # local t and not account for scr refresh
            T1I4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1I4, 'tStartRefresh')  # time at next scr refresh
            T1I4.setAutoDraw(True)
        
        # *T1Q4R* updates
        waitOnFlip = False
        if T1Q4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1Q4R.frameNStart = frameN  # exact frame index
            T1Q4R.tStart = t  # local t and not account for scr refresh
            T1Q4R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1Q4R, 'tStartRefresh')  # time at next scr refresh
            T1Q4R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T1Q4R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T1Q4R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T1Q4R.status == STARTED and not waitOnFlip:
            theseKeys = T1Q4R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T1Q4R_allKeys.extend(theseKeys)
            if len(_T1Q4R_allKeys):
                T1Q4R.keys = _T1Q4R_allKeys[-1].name  # just the last key pressed
                T1Q4R.rt = _T1Q4R_allKeys[-1].rt
                # was this correct?
                if (T1Q4R.keys == str(CorrT1Q4)) or (T1Q4R.keys == CorrT1Q4):
                    T1Q4R.corr = 1
                else:
                    T1Q4R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T1Q4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T1Q4"-------
    for thisComponent in T1Q4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T1I4.started', T1I4.tStartRefresh)
    trials.addData('T1I4.stopped', T1I4.tStopRefresh)
    # check responses
    if T1Q4R.keys in ['', [], None]:  # No response was made
        T1Q4R.keys = None
        # was no response the correct answer?!
        if str(CorrT1Q4).lower() == 'none':
           T1Q4R.corr = 1;  # correct non-response
        else:
           T1Q4R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T1Q4R.keys',T1Q4R.keys)
    trials.addData('T1Q4R.corr', T1Q4R.corr)
    if T1Q4R.keys != None:  # we had a response
        trials.addData('T1Q4R.rt', T1Q4R.rt)
    trials.addData('T1Q4R.started', T1Q4R.tStartRefresh)
    trials.addData('T1Q4R.stopped', T1Q4R.tStopRefresh)
    # the Routine "T1Q4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T1Q5"-------
    continueRoutine = True
    # update component parameters for each repeat
    T1I5.setImage(T1Q5)
    T1Q5R.keys = []
    T1Q5R.rt = []
    _T1Q5R_allKeys = []
    # keep track of which components have finished
    T1Q5Components = [T1I5, T1Q5R]
    for thisComponent in T1Q5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T1Q5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T1Q5"-------
    while continueRoutine:
        # get current time
        t = T1Q5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T1Q5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T1I5* updates
        if T1I5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1I5.frameNStart = frameN  # exact frame index
            T1I5.tStart = t  # local t and not account for scr refresh
            T1I5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1I5, 'tStartRefresh')  # time at next scr refresh
            T1I5.setAutoDraw(True)
        
        # *T1Q5R* updates
        waitOnFlip = False
        if T1Q5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1Q5R.frameNStart = frameN  # exact frame index
            T1Q5R.tStart = t  # local t and not account for scr refresh
            T1Q5R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1Q5R, 'tStartRefresh')  # time at next scr refresh
            T1Q5R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T1Q5R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T1Q5R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T1Q5R.status == STARTED and not waitOnFlip:
            theseKeys = T1Q5R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T1Q5R_allKeys.extend(theseKeys)
            if len(_T1Q5R_allKeys):
                T1Q5R.keys = _T1Q5R_allKeys[-1].name  # just the last key pressed
                T1Q5R.rt = _T1Q5R_allKeys[-1].rt
                # was this correct?
                if (T1Q5R.keys == str(CorrT1Q5)) or (T1Q5R.keys == CorrT1Q5):
                    T1Q5R.corr = 1
                else:
                    T1Q5R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T1Q5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T1Q5"-------
    for thisComponent in T1Q5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T1I5.started', T1I5.tStartRefresh)
    trials.addData('T1I5.stopped', T1I5.tStopRefresh)
    # check responses
    if T1Q5R.keys in ['', [], None]:  # No response was made
        T1Q5R.keys = None
        # was no response the correct answer?!
        if str(CorrT1Q5).lower() == 'none':
           T1Q5R.corr = 1;  # correct non-response
        else:
           T1Q5R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T1Q5R.keys',T1Q5R.keys)
    trials.addData('T1Q5R.corr', T1Q5R.corr)
    if T1Q5R.keys != None:  # we had a response
        trials.addData('T1Q5R.rt', T1Q5R.rt)
    trials.addData('T1Q5R.started', T1Q5R.tStartRefresh)
    trials.addData('T1Q5R.stopped', T1Q5R.tStopRefresh)
    # the Routine "T1Q5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T1Q6"-------
    continueRoutine = True
    # update component parameters for each repeat
    T1I6.setImage(T1Q6)
    T1Q6R.keys = []
    T1Q6R.rt = []
    _T1Q6R_allKeys = []
    # keep track of which components have finished
    T1Q6Components = [T1I6, T1Q6R]
    for thisComponent in T1Q6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T1Q6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T1Q6"-------
    while continueRoutine:
        # get current time
        t = T1Q6Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T1Q6Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T1I6* updates
        if T1I6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1I6.frameNStart = frameN  # exact frame index
            T1I6.tStart = t  # local t and not account for scr refresh
            T1I6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1I6, 'tStartRefresh')  # time at next scr refresh
            T1I6.setAutoDraw(True)
        
        # *T1Q6R* updates
        waitOnFlip = False
        if T1Q6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1Q6R.frameNStart = frameN  # exact frame index
            T1Q6R.tStart = t  # local t and not account for scr refresh
            T1Q6R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1Q6R, 'tStartRefresh')  # time at next scr refresh
            T1Q6R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T1Q6R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T1Q6R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T1Q6R.status == STARTED and not waitOnFlip:
            theseKeys = T1Q6R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T1Q6R_allKeys.extend(theseKeys)
            if len(_T1Q6R_allKeys):
                T1Q6R.keys = _T1Q6R_allKeys[-1].name  # just the last key pressed
                T1Q6R.rt = _T1Q6R_allKeys[-1].rt
                # was this correct?
                if (T1Q6R.keys == str(CorrT1Q6)) or (T1Q6R.keys == CorrT1Q6):
                    T1Q6R.corr = 1
                else:
                    T1Q6R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T1Q6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T1Q6"-------
    for thisComponent in T1Q6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T1I6.started', T1I6.tStartRefresh)
    trials.addData('T1I6.stopped', T1I6.tStopRefresh)
    # check responses
    if T1Q6R.keys in ['', [], None]:  # No response was made
        T1Q6R.keys = None
        # was no response the correct answer?!
        if str(CorrT1Q6).lower() == 'none':
           T1Q6R.corr = 1;  # correct non-response
        else:
           T1Q6R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T1Q6R.keys',T1Q6R.keys)
    trials.addData('T1Q6R.corr', T1Q6R.corr)
    if T1Q6R.keys != None:  # we had a response
        trials.addData('T1Q6R.rt', T1Q6R.rt)
    trials.addData('T1Q6R.started', T1Q6R.tStartRefresh)
    trials.addData('T1Q6R.stopped', T1Q6R.tStopRefresh)
    # the Routine "T1Q6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T1Q7"-------
    continueRoutine = True
    # update component parameters for each repeat
    T1I7.setImage(T1Q7)
    T1Q7R.keys = []
    T1Q7R.rt = []
    _T1Q7R_allKeys = []
    # keep track of which components have finished
    T1Q7Components = [T1I7, T1Q7R]
    for thisComponent in T1Q7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T1Q7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T1Q7"-------
    while continueRoutine:
        # get current time
        t = T1Q7Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T1Q7Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T1I7* updates
        if T1I7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1I7.frameNStart = frameN  # exact frame index
            T1I7.tStart = t  # local t and not account for scr refresh
            T1I7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1I7, 'tStartRefresh')  # time at next scr refresh
            T1I7.setAutoDraw(True)
        
        # *T1Q7R* updates
        waitOnFlip = False
        if T1Q7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1Q7R.frameNStart = frameN  # exact frame index
            T1Q7R.tStart = t  # local t and not account for scr refresh
            T1Q7R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1Q7R, 'tStartRefresh')  # time at next scr refresh
            T1Q7R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T1Q7R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T1Q7R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T1Q7R.status == STARTED and not waitOnFlip:
            theseKeys = T1Q7R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T1Q7R_allKeys.extend(theseKeys)
            if len(_T1Q7R_allKeys):
                T1Q7R.keys = _T1Q7R_allKeys[-1].name  # just the last key pressed
                T1Q7R.rt = _T1Q7R_allKeys[-1].rt
                # was this correct?
                if (T1Q7R.keys == str(CorrT1Q7)) or (T1Q7R.keys == CorrT1Q7):
                    T1Q7R.corr = 1
                else:
                    T1Q7R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T1Q7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T1Q7"-------
    for thisComponent in T1Q7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T1I7.started', T1I7.tStartRefresh)
    trials.addData('T1I7.stopped', T1I7.tStopRefresh)
    # check responses
    if T1Q7R.keys in ['', [], None]:  # No response was made
        T1Q7R.keys = None
        # was no response the correct answer?!
        if str(CorrT1Q7).lower() == 'none':
           T1Q7R.corr = 1;  # correct non-response
        else:
           T1Q7R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T1Q7R.keys',T1Q7R.keys)
    trials.addData('T1Q7R.corr', T1Q7R.corr)
    if T1Q7R.keys != None:  # we had a response
        trials.addData('T1Q7R.rt', T1Q7R.rt)
    trials.addData('T1Q7R.started', T1Q7R.tStartRefresh)
    trials.addData('T1Q7R.stopped', T1Q7R.tStopRefresh)
    # the Routine "T1Q7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T1Q8"-------
    continueRoutine = True
    # update component parameters for each repeat
    T1I8.setImage(T1Q8)
    T1Q8R.keys = []
    T1Q8R.rt = []
    _T1Q8R_allKeys = []
    # keep track of which components have finished
    T1Q8Components = [T1I8, T1Q8R]
    for thisComponent in T1Q8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T1Q8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T1Q8"-------
    while continueRoutine:
        # get current time
        t = T1Q8Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T1Q8Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T1I8* updates
        if T1I8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1I8.frameNStart = frameN  # exact frame index
            T1I8.tStart = t  # local t and not account for scr refresh
            T1I8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1I8, 'tStartRefresh')  # time at next scr refresh
            T1I8.setAutoDraw(True)
        
        # *T1Q8R* updates
        waitOnFlip = False
        if T1Q8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1Q8R.frameNStart = frameN  # exact frame index
            T1Q8R.tStart = t  # local t and not account for scr refresh
            T1Q8R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1Q8R, 'tStartRefresh')  # time at next scr refresh
            T1Q8R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T1Q8R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T1Q8R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T1Q8R.status == STARTED and not waitOnFlip:
            theseKeys = T1Q8R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T1Q8R_allKeys.extend(theseKeys)
            if len(_T1Q8R_allKeys):
                T1Q8R.keys = _T1Q8R_allKeys[-1].name  # just the last key pressed
                T1Q8R.rt = _T1Q8R_allKeys[-1].rt
                # was this correct?
                if (T1Q8R.keys == str(CorrT1Q8)) or (T1Q8R.keys == CorrT1Q8):
                    T1Q8R.corr = 1
                else:
                    T1Q8R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T1Q8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T1Q8"-------
    for thisComponent in T1Q8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T1I8.started', T1I8.tStartRefresh)
    trials.addData('T1I8.stopped', T1I8.tStopRefresh)
    # check responses
    if T1Q8R.keys in ['', [], None]:  # No response was made
        T1Q8R.keys = None
        # was no response the correct answer?!
        if str(CorrT1Q8).lower() == 'none':
           T1Q8R.corr = 1;  # correct non-response
        else:
           T1Q8R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T1Q8R.keys',T1Q8R.keys)
    trials.addData('T1Q8R.corr', T1Q8R.corr)
    if T1Q8R.keys != None:  # we had a response
        trials.addData('T1Q8R.rt', T1Q8R.rt)
    trials.addData('T1Q8R.started', T1Q8R.tStartRefresh)
    trials.addData('T1Q8R.stopped', T1Q8R.tStopRefresh)
    # the Routine "T1Q8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T1Q9"-------
    continueRoutine = True
    # update component parameters for each repeat
    T1I9.setImage(T1Q9)
    T1Q9R.keys = []
    T1Q9R.rt = []
    _T1Q9R_allKeys = []
    # keep track of which components have finished
    T1Q9Components = [T1I9, T1Q9R]
    for thisComponent in T1Q9Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T1Q9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T1Q9"-------
    while continueRoutine:
        # get current time
        t = T1Q9Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T1Q9Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T1I9* updates
        if T1I9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1I9.frameNStart = frameN  # exact frame index
            T1I9.tStart = t  # local t and not account for scr refresh
            T1I9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1I9, 'tStartRefresh')  # time at next scr refresh
            T1I9.setAutoDraw(True)
        
        # *T1Q9R* updates
        waitOnFlip = False
        if T1Q9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1Q9R.frameNStart = frameN  # exact frame index
            T1Q9R.tStart = t  # local t and not account for scr refresh
            T1Q9R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1Q9R, 'tStartRefresh')  # time at next scr refresh
            T1Q9R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T1Q9R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T1Q9R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T1Q9R.status == STARTED and not waitOnFlip:
            theseKeys = T1Q9R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T1Q9R_allKeys.extend(theseKeys)
            if len(_T1Q9R_allKeys):
                T1Q9R.keys = _T1Q9R_allKeys[-1].name  # just the last key pressed
                T1Q9R.rt = _T1Q9R_allKeys[-1].rt
                # was this correct?
                if (T1Q9R.keys == str(CorrT1Q9)) or (T1Q9R.keys == CorrT1Q9):
                    T1Q9R.corr = 1
                else:
                    T1Q9R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T1Q9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T1Q9"-------
    for thisComponent in T1Q9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T1I9.started', T1I9.tStartRefresh)
    trials.addData('T1I9.stopped', T1I9.tStopRefresh)
    # check responses
    if T1Q9R.keys in ['', [], None]:  # No response was made
        T1Q9R.keys = None
        # was no response the correct answer?!
        if str(CorrT1Q9).lower() == 'none':
           T1Q9R.corr = 1;  # correct non-response
        else:
           T1Q9R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T1Q9R.keys',T1Q9R.keys)
    trials.addData('T1Q9R.corr', T1Q9R.corr)
    if T1Q9R.keys != None:  # we had a response
        trials.addData('T1Q9R.rt', T1Q9R.rt)
    trials.addData('T1Q9R.started', T1Q9R.tStartRefresh)
    trials.addData('T1Q9R.stopped', T1Q9R.tStopRefresh)
    # the Routine "T1Q9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T1Q10"-------
    continueRoutine = True
    # update component parameters for each repeat
    T1I10.setImage(T1Q10)
    T1Q10R.keys = []
    T1Q10R.rt = []
    _T1Q10R_allKeys = []
    # keep track of which components have finished
    T1Q10Components = [T1I10, T1Q10R]
    for thisComponent in T1Q10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T1Q10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T1Q10"-------
    while continueRoutine:
        # get current time
        t = T1Q10Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T1Q10Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T1I10* updates
        if T1I10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1I10.frameNStart = frameN  # exact frame index
            T1I10.tStart = t  # local t and not account for scr refresh
            T1I10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1I10, 'tStartRefresh')  # time at next scr refresh
            T1I10.setAutoDraw(True)
        
        # *T1Q10R* updates
        waitOnFlip = False
        if T1Q10R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T1Q10R.frameNStart = frameN  # exact frame index
            T1Q10R.tStart = t  # local t and not account for scr refresh
            T1Q10R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T1Q10R, 'tStartRefresh')  # time at next scr refresh
            T1Q10R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T1Q10R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T1Q10R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T1Q10R.status == STARTED and not waitOnFlip:
            theseKeys = T1Q10R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T1Q10R_allKeys.extend(theseKeys)
            if len(_T1Q10R_allKeys):
                T1Q10R.keys = _T1Q10R_allKeys[-1].name  # just the last key pressed
                T1Q10R.rt = _T1Q10R_allKeys[-1].rt
                # was this correct?
                if (T1Q10R.keys == str(CorrT1Q10)) or (T1Q10R.keys == CorrT1Q10):
                    T1Q10R.corr = 1
                else:
                    T1Q10R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T1Q10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T1Q10"-------
    for thisComponent in T1Q10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T1I10.started', T1I10.tStartRefresh)
    trials.addData('T1I10.stopped', T1I10.tStopRefresh)
    # check responses
    if T1Q10R.keys in ['', [], None]:  # No response was made
        T1Q10R.keys = None
        # was no response the correct answer?!
        if str(CorrT1Q10).lower() == 'none':
           T1Q10R.corr = 1;  # correct non-response
        else:
           T1Q10R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T1Q10R.keys',T1Q10R.keys)
    trials.addData('T1Q10R.corr', T1Q10R.corr)
    if T1Q10R.keys != None:  # we had a response
        trials.addData('T1Q10R.rt', T1Q10R.rt)
    trials.addData('T1Q10R.started', T1Q10R.tStartRefresh)
    trials.addData('T1Q10R.stopped', T1Q10R.tStopRefresh)
    # the Routine "T1Q10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Trial_Break"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    Trial_BreakComponents = [Break_message, key_resp_4]
    for thisComponent in Trial_BreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Trial_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial_Break"-------
    while continueRoutine:
        # get current time
        t = Trial_BreakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_BreakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Break_message* updates
        if Break_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_message.frameNStart = frameN  # exact frame index
            Break_message.tStart = t  # local t and not account for scr refresh
            Break_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_message, 'tStartRefresh')  # time at next scr refresh
            Break_message.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial_Break"-------
    for thisComponent in Trial_BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Break_message.started', Break_message.tStartRefresh)
    trials.addData('Break_message.stopped', Break_message.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Trial_Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T2A"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_2.setSound(T2A, hamming=True)
    sound_2.setVolume(1.0, log=False)
    
    T2A = cond_set[cond_set['Cond'] == cond]['T2A'].values[0]
    cond_speed = re.search(r'(\d+\.\d+)x', T2A).group(1)
    cond_noise = re.search(r'(\w+)_Audio', T2A).group(1)
    send_trigger(cond_speed, cond_noise)
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # keep track of which components have finished
    T2AComponents = [sound_2, image, key_resp_11]
    for thisComponent in T2AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T2AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T2A"-------
    while continueRoutine:
        # get current time
        t = T2AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T2AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play()  # start the sound (it finishes automatically)
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if sound_2.status == FINISHED:
            continueRoutine = False
        
        # *key_resp_11* updates
        waitOnFlip = False
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['z'], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T2AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T2A"-------
    for thisComponent in T2AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_2.started', sound_2.tStart)
    trials.addData('sound_2.stopped', sound_2.tStop)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    ser.write((200).to_bytes(1, 'big'))
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    trials.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        trials.addData('key_resp_11.rt', key_resp_11.rt)
    trials.addData('key_resp_11.started', key_resp_11.tStartRefresh)
    trials.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
    # the Routine "T2A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pre_assement_inst"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    Pre_assement_instComponents = [text_5, key_resp_5]
    for thisComponent in Pre_assement_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pre_assement_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pre_assement_inst"-------
    while continueRoutine:
        # get current time
        t = Pre_assement_instClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pre_assement_instClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pre_assement_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pre_assement_inst"-------
    for thisComponent in Pre_assement_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_5.started', text_5.tStartRefresh)
    trials.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    trials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    trials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "Pre_assement_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T2Q1"-------
    continueRoutine = True
    # update component parameters for each repeat
    T2I1.setImage(T2Q1)
    T2Q1R.keys = []
    T2Q1R.rt = []
    _T2Q1R_allKeys = []
    # keep track of which components have finished
    T2Q1Components = [T2I1, T2Q1R]
    for thisComponent in T2Q1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T2Q1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T2Q1"-------
    while continueRoutine:
        # get current time
        t = T2Q1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T2Q1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2I1* updates
        if T2I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2I1.frameNStart = frameN  # exact frame index
            T2I1.tStart = t  # local t and not account for scr refresh
            T2I1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2I1, 'tStartRefresh')  # time at next scr refresh
            T2I1.setAutoDraw(True)
        
        # *T2Q1R* updates
        waitOnFlip = False
        if T2Q1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2Q1R.frameNStart = frameN  # exact frame index
            T2Q1R.tStart = t  # local t and not account for scr refresh
            T2Q1R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2Q1R, 'tStartRefresh')  # time at next scr refresh
            T2Q1R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T2Q1R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T2Q1R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T2Q1R.status == STARTED and not waitOnFlip:
            theseKeys = T2Q1R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T2Q1R_allKeys.extend(theseKeys)
            if len(_T2Q1R_allKeys):
                T2Q1R.keys = _T2Q1R_allKeys[-1].name  # just the last key pressed
                T2Q1R.rt = _T2Q1R_allKeys[-1].rt
                # was this correct?
                if (T2Q1R.keys == str(CorrT2Q1)) or (T2Q1R.keys == CorrT2Q1):
                    T2Q1R.corr = 1
                else:
                    T2Q1R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T2Q1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T2Q1"-------
    for thisComponent in T2Q1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T2I1.started', T2I1.tStartRefresh)
    trials.addData('T2I1.stopped', T2I1.tStopRefresh)
    # check responses
    if T2Q1R.keys in ['', [], None]:  # No response was made
        T2Q1R.keys = None
        # was no response the correct answer?!
        if str(CorrT2Q1).lower() == 'none':
           T2Q1R.corr = 1;  # correct non-response
        else:
           T2Q1R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T2Q1R.keys',T2Q1R.keys)
    trials.addData('T2Q1R.corr', T2Q1R.corr)
    if T2Q1R.keys != None:  # we had a response
        trials.addData('T2Q1R.rt', T2Q1R.rt)
    trials.addData('T2Q1R.started', T2Q1R.tStartRefresh)
    trials.addData('T2Q1R.stopped', T2Q1R.tStopRefresh)
    # the Routine "T2Q1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T2Q2"-------
    continueRoutine = True
    # update component parameters for each repeat
    T2I2.setImage(T2Q2)
    T2Q2R.keys = []
    T2Q2R.rt = []
    _T2Q2R_allKeys = []
    # keep track of which components have finished
    T2Q2Components = [T2I2, T2Q2R]
    for thisComponent in T2Q2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T2Q2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T2Q2"-------
    while continueRoutine:
        # get current time
        t = T2Q2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T2Q2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2I2* updates
        if T2I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2I2.frameNStart = frameN  # exact frame index
            T2I2.tStart = t  # local t and not account for scr refresh
            T2I2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2I2, 'tStartRefresh')  # time at next scr refresh
            T2I2.setAutoDraw(True)
        
        # *T2Q2R* updates
        waitOnFlip = False
        if T2Q2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2Q2R.frameNStart = frameN  # exact frame index
            T2Q2R.tStart = t  # local t and not account for scr refresh
            T2Q2R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2Q2R, 'tStartRefresh')  # time at next scr refresh
            T2Q2R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T2Q2R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T2Q2R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T2Q2R.status == STARTED and not waitOnFlip:
            theseKeys = T2Q2R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T2Q2R_allKeys.extend(theseKeys)
            if len(_T2Q2R_allKeys):
                T2Q2R.keys = _T2Q2R_allKeys[-1].name  # just the last key pressed
                T2Q2R.rt = _T2Q2R_allKeys[-1].rt
                # was this correct?
                if (T2Q2R.keys == str(CorrT2Q2)) or (T2Q2R.keys == CorrT2Q2):
                    T2Q2R.corr = 1
                else:
                    T2Q2R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T2Q2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T2Q2"-------
    for thisComponent in T2Q2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T2I2.started', T2I2.tStartRefresh)
    trials.addData('T2I2.stopped', T2I2.tStopRefresh)
    # check responses
    if T2Q2R.keys in ['', [], None]:  # No response was made
        T2Q2R.keys = None
        # was no response the correct answer?!
        if str(CorrT2Q2).lower() == 'none':
           T2Q2R.corr = 1;  # correct non-response
        else:
           T2Q2R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T2Q2R.keys',T2Q2R.keys)
    trials.addData('T2Q2R.corr', T2Q2R.corr)
    if T2Q2R.keys != None:  # we had a response
        trials.addData('T2Q2R.rt', T2Q2R.rt)
    trials.addData('T2Q2R.started', T2Q2R.tStartRefresh)
    trials.addData('T2Q2R.stopped', T2Q2R.tStopRefresh)
    # the Routine "T2Q2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T2Q3"-------
    continueRoutine = True
    # update component parameters for each repeat
    T2I3.setImage(T2Q3)
    T2Q3R.keys = []
    T2Q3R.rt = []
    _T2Q3R_allKeys = []
    # keep track of which components have finished
    T2Q3Components = [T2I3, T2Q3R]
    for thisComponent in T2Q3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T2Q3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T2Q3"-------
    while continueRoutine:
        # get current time
        t = T2Q3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T2Q3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2I3* updates
        if T2I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2I3.frameNStart = frameN  # exact frame index
            T2I3.tStart = t  # local t and not account for scr refresh
            T2I3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2I3, 'tStartRefresh')  # time at next scr refresh
            T2I3.setAutoDraw(True)
        
        # *T2Q3R* updates
        waitOnFlip = False
        if T2Q3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2Q3R.frameNStart = frameN  # exact frame index
            T2Q3R.tStart = t  # local t and not account for scr refresh
            T2Q3R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2Q3R, 'tStartRefresh')  # time at next scr refresh
            T2Q3R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T2Q3R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T2Q3R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T2Q3R.status == STARTED and not waitOnFlip:
            theseKeys = T2Q3R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T2Q3R_allKeys.extend(theseKeys)
            if len(_T2Q3R_allKeys):
                T2Q3R.keys = _T2Q3R_allKeys[-1].name  # just the last key pressed
                T2Q3R.rt = _T2Q3R_allKeys[-1].rt
                # was this correct?
                if (T2Q3R.keys == str(CorrT2Q3)) or (T2Q3R.keys == CorrT2Q3):
                    T2Q3R.corr = 1
                else:
                    T2Q3R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T2Q3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T2Q3"-------
    for thisComponent in T2Q3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T2I3.started', T2I3.tStartRefresh)
    trials.addData('T2I3.stopped', T2I3.tStopRefresh)
    # check responses
    if T2Q3R.keys in ['', [], None]:  # No response was made
        T2Q3R.keys = None
        # was no response the correct answer?!
        if str(CorrT2Q3).lower() == 'none':
           T2Q3R.corr = 1;  # correct non-response
        else:
           T2Q3R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T2Q3R.keys',T2Q3R.keys)
    trials.addData('T2Q3R.corr', T2Q3R.corr)
    if T2Q3R.keys != None:  # we had a response
        trials.addData('T2Q3R.rt', T2Q3R.rt)
    trials.addData('T2Q3R.started', T2Q3R.tStartRefresh)
    trials.addData('T2Q3R.stopped', T2Q3R.tStopRefresh)
    # the Routine "T2Q3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T2Q4"-------
    continueRoutine = True
    # update component parameters for each repeat
    T2I4.setImage(T2Q4)
    T2Q4R.keys = []
    T2Q4R.rt = []
    _T2Q4R_allKeys = []
    # keep track of which components have finished
    T2Q4Components = [T2I4, T2Q4R]
    for thisComponent in T2Q4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T2Q4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T2Q4"-------
    while continueRoutine:
        # get current time
        t = T2Q4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T2Q4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2I4* updates
        if T2I4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2I4.frameNStart = frameN  # exact frame index
            T2I4.tStart = t  # local t and not account for scr refresh
            T2I4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2I4, 'tStartRefresh')  # time at next scr refresh
            T2I4.setAutoDraw(True)
        
        # *T2Q4R* updates
        waitOnFlip = False
        if T2Q4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2Q4R.frameNStart = frameN  # exact frame index
            T2Q4R.tStart = t  # local t and not account for scr refresh
            T2Q4R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2Q4R, 'tStartRefresh')  # time at next scr refresh
            T2Q4R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T2Q4R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T2Q4R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T2Q4R.status == STARTED and not waitOnFlip:
            theseKeys = T2Q4R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T2Q4R_allKeys.extend(theseKeys)
            if len(_T2Q4R_allKeys):
                T2Q4R.keys = _T2Q4R_allKeys[-1].name  # just the last key pressed
                T2Q4R.rt = _T2Q4R_allKeys[-1].rt
                # was this correct?
                if (T2Q4R.keys == str(CorrT2Q4)) or (T2Q4R.keys == CorrT2Q4):
                    T2Q4R.corr = 1
                else:
                    T2Q4R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T2Q4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T2Q4"-------
    for thisComponent in T2Q4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T2I4.started', T2I4.tStartRefresh)
    trials.addData('T2I4.stopped', T2I4.tStopRefresh)
    # check responses
    if T2Q4R.keys in ['', [], None]:  # No response was made
        T2Q4R.keys = None
        # was no response the correct answer?!
        if str(CorrT2Q4).lower() == 'none':
           T2Q4R.corr = 1;  # correct non-response
        else:
           T2Q4R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T2Q4R.keys',T2Q4R.keys)
    trials.addData('T2Q4R.corr', T2Q4R.corr)
    if T2Q4R.keys != None:  # we had a response
        trials.addData('T2Q4R.rt', T2Q4R.rt)
    trials.addData('T2Q4R.started', T2Q4R.tStartRefresh)
    trials.addData('T2Q4R.stopped', T2Q4R.tStopRefresh)
    # the Routine "T2Q4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T2Q5"-------
    continueRoutine = True
    # update component parameters for each repeat
    T2I5.setImage(T2Q5)
    T2Q5R.keys = []
    T2Q5R.rt = []
    _T2Q5R_allKeys = []
    # keep track of which components have finished
    T2Q5Components = [T2I5, T2Q5R]
    for thisComponent in T2Q5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T2Q5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T2Q5"-------
    while continueRoutine:
        # get current time
        t = T2Q5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T2Q5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2I5* updates
        if T2I5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2I5.frameNStart = frameN  # exact frame index
            T2I5.tStart = t  # local t and not account for scr refresh
            T2I5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2I5, 'tStartRefresh')  # time at next scr refresh
            T2I5.setAutoDraw(True)
        
        # *T2Q5R* updates
        waitOnFlip = False
        if T2Q5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2Q5R.frameNStart = frameN  # exact frame index
            T2Q5R.tStart = t  # local t and not account for scr refresh
            T2Q5R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2Q5R, 'tStartRefresh')  # time at next scr refresh
            T2Q5R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T2Q5R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T2Q5R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T2Q5R.status == STARTED and not waitOnFlip:
            theseKeys = T2Q5R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T2Q5R_allKeys.extend(theseKeys)
            if len(_T2Q5R_allKeys):
                T2Q5R.keys = _T2Q5R_allKeys[-1].name  # just the last key pressed
                T2Q5R.rt = _T2Q5R_allKeys[-1].rt
                # was this correct?
                if (T2Q5R.keys == str(CorrT2Q5)) or (T2Q5R.keys == CorrT2Q5):
                    T2Q5R.corr = 1
                else:
                    T2Q5R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T2Q5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T2Q5"-------
    for thisComponent in T2Q5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T2I5.started', T2I5.tStartRefresh)
    trials.addData('T2I5.stopped', T2I5.tStopRefresh)
    # check responses
    if T2Q5R.keys in ['', [], None]:  # No response was made
        T2Q5R.keys = None
        # was no response the correct answer?!
        if str(CorrT2Q5).lower() == 'none':
           T2Q5R.corr = 1;  # correct non-response
        else:
           T2Q5R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T2Q5R.keys',T2Q5R.keys)
    trials.addData('T2Q5R.corr', T2Q5R.corr)
    if T2Q5R.keys != None:  # we had a response
        trials.addData('T2Q5R.rt', T2Q5R.rt)
    trials.addData('T2Q5R.started', T2Q5R.tStartRefresh)
    trials.addData('T2Q5R.stopped', T2Q5R.tStopRefresh)
    # the Routine "T2Q5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T2Q6"-------
    continueRoutine = True
    # update component parameters for each repeat
    T2I6.setImage(T2Q6)
    T2Q6R.keys = []
    T2Q6R.rt = []
    _T2Q6R_allKeys = []
    # keep track of which components have finished
    T2Q6Components = [T2I6, T2Q6R]
    for thisComponent in T2Q6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T2Q6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T2Q6"-------
    while continueRoutine:
        # get current time
        t = T2Q6Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T2Q6Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2I6* updates
        if T2I6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2I6.frameNStart = frameN  # exact frame index
            T2I6.tStart = t  # local t and not account for scr refresh
            T2I6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2I6, 'tStartRefresh')  # time at next scr refresh
            T2I6.setAutoDraw(True)
        
        # *T2Q6R* updates
        waitOnFlip = False
        if T2Q6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2Q6R.frameNStart = frameN  # exact frame index
            T2Q6R.tStart = t  # local t and not account for scr refresh
            T2Q6R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2Q6R, 'tStartRefresh')  # time at next scr refresh
            T2Q6R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T2Q6R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T2Q6R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T2Q6R.status == STARTED and not waitOnFlip:
            theseKeys = T2Q6R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T2Q6R_allKeys.extend(theseKeys)
            if len(_T2Q6R_allKeys):
                T2Q6R.keys = _T2Q6R_allKeys[-1].name  # just the last key pressed
                T2Q6R.rt = _T2Q6R_allKeys[-1].rt
                # was this correct?
                if (T2Q6R.keys == str(CorrT2Q6)) or (T2Q6R.keys == CorrT2Q6):
                    T2Q6R.corr = 1
                else:
                    T2Q6R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T2Q6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T2Q6"-------
    for thisComponent in T2Q6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T2I6.started', T2I6.tStartRefresh)
    trials.addData('T2I6.stopped', T2I6.tStopRefresh)
    # check responses
    if T2Q6R.keys in ['', [], None]:  # No response was made
        T2Q6R.keys = None
        # was no response the correct answer?!
        if str(CorrT2Q6).lower() == 'none':
           T2Q6R.corr = 1;  # correct non-response
        else:
           T2Q6R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T2Q6R.keys',T2Q6R.keys)
    trials.addData('T2Q6R.corr', T2Q6R.corr)
    if T2Q6R.keys != None:  # we had a response
        trials.addData('T2Q6R.rt', T2Q6R.rt)
    trials.addData('T2Q6R.started', T2Q6R.tStartRefresh)
    trials.addData('T2Q6R.stopped', T2Q6R.tStopRefresh)
    # the Routine "T2Q6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T2Q7"-------
    continueRoutine = True
    # update component parameters for each repeat
    T2I7.setImage(T2Q7)
    T2Q7R.keys = []
    T2Q7R.rt = []
    _T2Q7R_allKeys = []
    # keep track of which components have finished
    T2Q7Components = [T2I7, T2Q7R]
    for thisComponent in T2Q7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T2Q7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T2Q7"-------
    while continueRoutine:
        # get current time
        t = T2Q7Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T2Q7Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2I7* updates
        if T2I7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2I7.frameNStart = frameN  # exact frame index
            T2I7.tStart = t  # local t and not account for scr refresh
            T2I7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2I7, 'tStartRefresh')  # time at next scr refresh
            T2I7.setAutoDraw(True)
        
        # *T2Q7R* updates
        waitOnFlip = False
        if T2Q7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2Q7R.frameNStart = frameN  # exact frame index
            T2Q7R.tStart = t  # local t and not account for scr refresh
            T2Q7R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2Q7R, 'tStartRefresh')  # time at next scr refresh
            T2Q7R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T2Q7R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T2Q7R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T2Q7R.status == STARTED and not waitOnFlip:
            theseKeys = T2Q7R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T2Q7R_allKeys.extend(theseKeys)
            if len(_T2Q7R_allKeys):
                T2Q7R.keys = _T2Q7R_allKeys[-1].name  # just the last key pressed
                T2Q7R.rt = _T2Q7R_allKeys[-1].rt
                # was this correct?
                if (T2Q7R.keys == str(CorrT2Q7)) or (T2Q7R.keys == CorrT2Q7):
                    T2Q7R.corr = 1
                else:
                    T2Q7R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T2Q7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T2Q7"-------
    for thisComponent in T2Q7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T2I7.started', T2I7.tStartRefresh)
    trials.addData('T2I7.stopped', T2I7.tStopRefresh)
    # check responses
    if T2Q7R.keys in ['', [], None]:  # No response was made
        T2Q7R.keys = None
        # was no response the correct answer?!
        if str(CorrT2Q7).lower() == 'none':
           T2Q7R.corr = 1;  # correct non-response
        else:
           T2Q7R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T2Q7R.keys',T2Q7R.keys)
    trials.addData('T2Q7R.corr', T2Q7R.corr)
    if T2Q7R.keys != None:  # we had a response
        trials.addData('T2Q7R.rt', T2Q7R.rt)
    trials.addData('T2Q7R.started', T2Q7R.tStartRefresh)
    trials.addData('T2Q7R.stopped', T2Q7R.tStopRefresh)
    # the Routine "T2Q7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T2Q8"-------
    continueRoutine = True
    # update component parameters for each repeat
    T2I8.setImage(T2Q8)
    T2Q8R.keys = []
    T2Q8R.rt = []
    _T2Q8R_allKeys = []
    # keep track of which components have finished
    T2Q8Components = [T2I8, T2Q8R]
    for thisComponent in T2Q8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T2Q8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T2Q8"-------
    while continueRoutine:
        # get current time
        t = T2Q8Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T2Q8Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2I8* updates
        if T2I8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2I8.frameNStart = frameN  # exact frame index
            T2I8.tStart = t  # local t and not account for scr refresh
            T2I8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2I8, 'tStartRefresh')  # time at next scr refresh
            T2I8.setAutoDraw(True)
        
        # *T2Q8R* updates
        waitOnFlip = False
        if T2Q8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2Q8R.frameNStart = frameN  # exact frame index
            T2Q8R.tStart = t  # local t and not account for scr refresh
            T2Q8R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2Q8R, 'tStartRefresh')  # time at next scr refresh
            T2Q8R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T2Q8R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T2Q8R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T2Q8R.status == STARTED and not waitOnFlip:
            theseKeys = T2Q8R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T2Q8R_allKeys.extend(theseKeys)
            if len(_T2Q8R_allKeys):
                T2Q8R.keys = _T2Q8R_allKeys[-1].name  # just the last key pressed
                T2Q8R.rt = _T2Q8R_allKeys[-1].rt
                # was this correct?
                if (T2Q8R.keys == str(CorrT2Q8)) or (T2Q8R.keys == CorrT2Q8):
                    T2Q8R.corr = 1
                else:
                    T2Q8R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T2Q8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T2Q8"-------
    for thisComponent in T2Q8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T2I8.started', T2I8.tStartRefresh)
    trials.addData('T2I8.stopped', T2I8.tStopRefresh)
    # check responses
    if T2Q8R.keys in ['', [], None]:  # No response was made
        T2Q8R.keys = None
        # was no response the correct answer?!
        if str(CorrT2Q8).lower() == 'none':
           T2Q8R.corr = 1;  # correct non-response
        else:
           T2Q8R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T2Q8R.keys',T2Q8R.keys)
    trials.addData('T2Q8R.corr', T2Q8R.corr)
    if T2Q8R.keys != None:  # we had a response
        trials.addData('T2Q8R.rt', T2Q8R.rt)
    trials.addData('T2Q8R.started', T2Q8R.tStartRefresh)
    trials.addData('T2Q8R.stopped', T2Q8R.tStopRefresh)
    # the Routine "T2Q8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T2Q9"-------
    continueRoutine = True
    # update component parameters for each repeat
    T2I9.setImage(T2Q9)
    T2Q9R.keys = []
    T2Q9R.rt = []
    _T2Q9R_allKeys = []
    # keep track of which components have finished
    T2Q9Components = [T2I9, T2Q9R]
    for thisComponent in T2Q9Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T2Q9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T2Q9"-------
    while continueRoutine:
        # get current time
        t = T2Q9Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T2Q9Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2I9* updates
        if T2I9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2I9.frameNStart = frameN  # exact frame index
            T2I9.tStart = t  # local t and not account for scr refresh
            T2I9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2I9, 'tStartRefresh')  # time at next scr refresh
            T2I9.setAutoDraw(True)
        
        # *T2Q9R* updates
        waitOnFlip = False
        if T2Q9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2Q9R.frameNStart = frameN  # exact frame index
            T2Q9R.tStart = t  # local t and not account for scr refresh
            T2Q9R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2Q9R, 'tStartRefresh')  # time at next scr refresh
            T2Q9R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T2Q9R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T2Q9R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T2Q9R.status == STARTED and not waitOnFlip:
            theseKeys = T2Q9R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T2Q9R_allKeys.extend(theseKeys)
            if len(_T2Q9R_allKeys):
                T2Q9R.keys = _T2Q9R_allKeys[-1].name  # just the last key pressed
                T2Q9R.rt = _T2Q9R_allKeys[-1].rt
                # was this correct?
                if (T2Q9R.keys == str(CorrT2Q9)) or (T2Q9R.keys == CorrT2Q9):
                    T2Q9R.corr = 1
                else:
                    T2Q9R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T2Q9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T2Q9"-------
    for thisComponent in T2Q9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T2I9.started', T2I9.tStartRefresh)
    trials.addData('T2I9.stopped', T2I9.tStopRefresh)
    # check responses
    if T2Q9R.keys in ['', [], None]:  # No response was made
        T2Q9R.keys = None
        # was no response the correct answer?!
        if str(CorrT2Q9).lower() == 'none':
           T2Q9R.corr = 1;  # correct non-response
        else:
           T2Q9R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T2Q9R.keys',T2Q9R.keys)
    trials.addData('T2Q9R.corr', T2Q9R.corr)
    if T2Q9R.keys != None:  # we had a response
        trials.addData('T2Q9R.rt', T2Q9R.rt)
    trials.addData('T2Q9R.started', T2Q9R.tStartRefresh)
    trials.addData('T2Q9R.stopped', T2Q9R.tStopRefresh)
    # the Routine "T2Q9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T2Q10"-------
    continueRoutine = True
    # update component parameters for each repeat
    T2I10.setImage(T2Q10)
    T2Q10R.keys = []
    T2Q10R.rt = []
    _T2Q10R_allKeys = []
    # keep track of which components have finished
    T2Q10Components = [T2I10, T2Q10R]
    for thisComponent in T2Q10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T2Q10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T2Q10"-------
    while continueRoutine:
        # get current time
        t = T2Q10Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T2Q10Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T2I10* updates
        if T2I10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2I10.frameNStart = frameN  # exact frame index
            T2I10.tStart = t  # local t and not account for scr refresh
            T2I10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2I10, 'tStartRefresh')  # time at next scr refresh
            T2I10.setAutoDraw(True)
        
        # *T2Q10R* updates
        waitOnFlip = False
        if T2Q10R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T2Q10R.frameNStart = frameN  # exact frame index
            T2Q10R.tStart = t  # local t and not account for scr refresh
            T2Q10R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T2Q10R, 'tStartRefresh')  # time at next scr refresh
            T2Q10R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T2Q10R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T2Q10R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T2Q10R.status == STARTED and not waitOnFlip:
            theseKeys = T2Q10R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T2Q10R_allKeys.extend(theseKeys)
            if len(_T2Q10R_allKeys):
                T2Q10R.keys = _T2Q10R_allKeys[-1].name  # just the last key pressed
                T2Q10R.rt = _T2Q10R_allKeys[-1].rt
                # was this correct?
                if (T2Q10R.keys == str(CorrT2Q10)) or (T2Q10R.keys == CorrT2Q10):
                    T2Q10R.corr = 1
                else:
                    T2Q10R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T2Q10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T2Q10"-------
    for thisComponent in T2Q10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T2I10.started', T2I10.tStartRefresh)
    trials.addData('T2I10.stopped', T2I10.tStopRefresh)
    # check responses
    if T2Q10R.keys in ['', [], None]:  # No response was made
        T2Q10R.keys = None
        # was no response the correct answer?!
        if str(CorrT2Q10).lower() == 'none':
           T2Q10R.corr = 1;  # correct non-response
        else:
           T2Q10R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T2Q10R.keys',T2Q10R.keys)
    trials.addData('T2Q10R.corr', T2Q10R.corr)
    if T2Q10R.keys != None:  # we had a response
        trials.addData('T2Q10R.rt', T2Q10R.rt)
    trials.addData('T2Q10R.started', T2Q10R.tStartRefresh)
    trials.addData('T2Q10R.stopped', T2Q10R.tStopRefresh)
    # the Routine "T2Q10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Trial_Break"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    Trial_BreakComponents = [Break_message, key_resp_4]
    for thisComponent in Trial_BreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Trial_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial_Break"-------
    while continueRoutine:
        # get current time
        t = Trial_BreakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_BreakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Break_message* updates
        if Break_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_message.frameNStart = frameN  # exact frame index
            Break_message.tStart = t  # local t and not account for scr refresh
            Break_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_message, 'tStartRefresh')  # time at next scr refresh
            Break_message.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial_Break"-------
    for thisComponent in Trial_BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Break_message.started', Break_message.tStartRefresh)
    trials.addData('Break_message.stopped', Break_message.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Trial_Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T3A"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_3.setSound(T3A, hamming=True)
    sound_3.setVolume(1.0, log=False)
    
    T3A = cond_set[cond_set['Cond'] == cond]['T3A'].values[0]
    cond_speed = re.search(r'(\d+\.\d+)x', T3A).group(1)
    cond_noise = re.search(r'(\w+)_Audio', T3A).group(1)
    send_trigger(cond_speed, cond_noise)
    key_resp_10.keys = []
    key_resp_10.rt = []
    _key_resp_10_allKeys = []
    # keep track of which components have finished
    T3AComponents = [sound_3, image_3, key_resp_10]
    for thisComponent in T3AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T3AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T3A"-------
    while continueRoutine:
        # get current time
        t = T3AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T3AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_3
        if sound_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.tStart = t  # local t and not account for scr refresh
            sound_3.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3.play()  # start the sound (it finishes automatically)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        if sound_3.status == FINISHED:
            continueRoutine = False
        
        # *key_resp_10* updates
        waitOnFlip = False
        if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.tStart = t  # local t and not account for scr refresh
            key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_10.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_10.getKeys(keyList=['z'], waitRelease=False)
            _key_resp_10_allKeys.extend(theseKeys)
            if len(_key_resp_10_allKeys):
                key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T3AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T3A"-------
    for thisComponent in T3AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_3.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_3.started', sound_3.tStart)
    trials.addData('sound_3.stopped', sound_3.tStop)
    trials.addData('image_3.started', image_3.tStartRefresh)
    trials.addData('image_3.stopped', image_3.tStopRefresh)
    ser.write((200).to_bytes(1, 'big'))
    # check responses
    if key_resp_10.keys in ['', [], None]:  # No response was made
        key_resp_10.keys = None
    trials.addData('key_resp_10.keys',key_resp_10.keys)
    if key_resp_10.keys != None:  # we had a response
        trials.addData('key_resp_10.rt', key_resp_10.rt)
    trials.addData('key_resp_10.started', key_resp_10.tStartRefresh)
    trials.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
    # the Routine "T3A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pre_assement_inst"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    Pre_assement_instComponents = [text_5, key_resp_5]
    for thisComponent in Pre_assement_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pre_assement_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pre_assement_inst"-------
    while continueRoutine:
        # get current time
        t = Pre_assement_instClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pre_assement_instClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pre_assement_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pre_assement_inst"-------
    for thisComponent in Pre_assement_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_5.started', text_5.tStartRefresh)
    trials.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    trials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    trials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "Pre_assement_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T3Q1"-------
    continueRoutine = True
    # update component parameters for each repeat
    T3I1.setImage(T3Q1)
    T3Q1R.keys = []
    T3Q1R.rt = []
    _T3Q1R_allKeys = []
    # keep track of which components have finished
    T3Q1Components = [T3I1, T3Q1R]
    for thisComponent in T3Q1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T3Q1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T3Q1"-------
    while continueRoutine:
        # get current time
        t = T3Q1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T3Q1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T3I1* updates
        if T3I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3I1.frameNStart = frameN  # exact frame index
            T3I1.tStart = t  # local t and not account for scr refresh
            T3I1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3I1, 'tStartRefresh')  # time at next scr refresh
            T3I1.setAutoDraw(True)
        
        # *T3Q1R* updates
        waitOnFlip = False
        if T3Q1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3Q1R.frameNStart = frameN  # exact frame index
            T3Q1R.tStart = t  # local t and not account for scr refresh
            T3Q1R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3Q1R, 'tStartRefresh')  # time at next scr refresh
            T3Q1R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T3Q1R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T3Q1R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T3Q1R.status == STARTED and not waitOnFlip:
            theseKeys = T3Q1R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T3Q1R_allKeys.extend(theseKeys)
            if len(_T3Q1R_allKeys):
                T3Q1R.keys = _T3Q1R_allKeys[-1].name  # just the last key pressed
                T3Q1R.rt = _T3Q1R_allKeys[-1].rt
                # was this correct?
                if (T3Q1R.keys == str(CorrT3Q1)) or (T3Q1R.keys == CorrT3Q1):
                    T3Q1R.corr = 1
                else:
                    T3Q1R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T3Q1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T3Q1"-------
    for thisComponent in T3Q1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T3I1.started', T3I1.tStartRefresh)
    trials.addData('T3I1.stopped', T3I1.tStopRefresh)
    # check responses
    if T3Q1R.keys in ['', [], None]:  # No response was made
        T3Q1R.keys = None
        # was no response the correct answer?!
        if str(CorrT3Q1).lower() == 'none':
           T3Q1R.corr = 1;  # correct non-response
        else:
           T3Q1R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T3Q1R.keys',T3Q1R.keys)
    trials.addData('T3Q1R.corr', T3Q1R.corr)
    if T3Q1R.keys != None:  # we had a response
        trials.addData('T3Q1R.rt', T3Q1R.rt)
    trials.addData('T3Q1R.started', T3Q1R.tStartRefresh)
    trials.addData('T3Q1R.stopped', T3Q1R.tStopRefresh)
    # the Routine "T3Q1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T3Q2"-------
    continueRoutine = True
    # update component parameters for each repeat
    T3I2.setImage(T3Q2)
    T3Q2R.keys = []
    T3Q2R.rt = []
    _T3Q2R_allKeys = []
    # keep track of which components have finished
    T3Q2Components = [T3I2, T3Q2R]
    for thisComponent in T3Q2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T3Q2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T3Q2"-------
    while continueRoutine:
        # get current time
        t = T3Q2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T3Q2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T3I2* updates
        if T3I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3I2.frameNStart = frameN  # exact frame index
            T3I2.tStart = t  # local t and not account for scr refresh
            T3I2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3I2, 'tStartRefresh')  # time at next scr refresh
            T3I2.setAutoDraw(True)
        
        # *T3Q2R* updates
        waitOnFlip = False
        if T3Q2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3Q2R.frameNStart = frameN  # exact frame index
            T3Q2R.tStart = t  # local t and not account for scr refresh
            T3Q2R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3Q2R, 'tStartRefresh')  # time at next scr refresh
            T3Q2R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T3Q2R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T3Q2R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T3Q2R.status == STARTED and not waitOnFlip:
            theseKeys = T3Q2R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T3Q2R_allKeys.extend(theseKeys)
            if len(_T3Q2R_allKeys):
                T3Q2R.keys = _T3Q2R_allKeys[-1].name  # just the last key pressed
                T3Q2R.rt = _T3Q2R_allKeys[-1].rt
                # was this correct?
                if (T3Q2R.keys == str(CorrT3Q2)) or (T3Q2R.keys == CorrT3Q2):
                    T3Q2R.corr = 1
                else:
                    T3Q2R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T3Q2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T3Q2"-------
    for thisComponent in T3Q2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T3I2.started', T3I2.tStartRefresh)
    trials.addData('T3I2.stopped', T3I2.tStopRefresh)
    # check responses
    if T3Q2R.keys in ['', [], None]:  # No response was made
        T3Q2R.keys = None
        # was no response the correct answer?!
        if str(CorrT3Q2).lower() == 'none':
           T3Q2R.corr = 1;  # correct non-response
        else:
           T3Q2R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T3Q2R.keys',T3Q2R.keys)
    trials.addData('T3Q2R.corr', T3Q2R.corr)
    if T3Q2R.keys != None:  # we had a response
        trials.addData('T3Q2R.rt', T3Q2R.rt)
    trials.addData('T3Q2R.started', T3Q2R.tStartRefresh)
    trials.addData('T3Q2R.stopped', T3Q2R.tStopRefresh)
    # the Routine "T3Q2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T3Q3"-------
    continueRoutine = True
    # update component parameters for each repeat
    T3I3.setImage(T3Q3)
    T3Q3R.keys = []
    T3Q3R.rt = []
    _T3Q3R_allKeys = []
    # keep track of which components have finished
    T3Q3Components = [T3I3, T3Q3R]
    for thisComponent in T3Q3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T3Q3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T3Q3"-------
    while continueRoutine:
        # get current time
        t = T3Q3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T3Q3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T3I3* updates
        if T3I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3I3.frameNStart = frameN  # exact frame index
            T3I3.tStart = t  # local t and not account for scr refresh
            T3I3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3I3, 'tStartRefresh')  # time at next scr refresh
            T3I3.setAutoDraw(True)
        
        # *T3Q3R* updates
        waitOnFlip = False
        if T3Q3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3Q3R.frameNStart = frameN  # exact frame index
            T3Q3R.tStart = t  # local t and not account for scr refresh
            T3Q3R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3Q3R, 'tStartRefresh')  # time at next scr refresh
            T3Q3R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T3Q3R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T3Q3R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T3Q3R.status == STARTED and not waitOnFlip:
            theseKeys = T3Q3R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T3Q3R_allKeys.extend(theseKeys)
            if len(_T3Q3R_allKeys):
                T3Q3R.keys = _T3Q3R_allKeys[-1].name  # just the last key pressed
                T3Q3R.rt = _T3Q3R_allKeys[-1].rt
                # was this correct?
                if (T3Q3R.keys == str(CorrT3Q3)) or (T3Q3R.keys == CorrT3Q3):
                    T3Q3R.corr = 1
                else:
                    T3Q3R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T3Q3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T3Q3"-------
    for thisComponent in T3Q3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T3I3.started', T3I3.tStartRefresh)
    trials.addData('T3I3.stopped', T3I3.tStopRefresh)
    # check responses
    if T3Q3R.keys in ['', [], None]:  # No response was made
        T3Q3R.keys = None
        # was no response the correct answer?!
        if str(CorrT3Q3).lower() == 'none':
           T3Q3R.corr = 1;  # correct non-response
        else:
           T3Q3R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T3Q3R.keys',T3Q3R.keys)
    trials.addData('T3Q3R.corr', T3Q3R.corr)
    if T3Q3R.keys != None:  # we had a response
        trials.addData('T3Q3R.rt', T3Q3R.rt)
    trials.addData('T3Q3R.started', T3Q3R.tStartRefresh)
    trials.addData('T3Q3R.stopped', T3Q3R.tStopRefresh)
    # the Routine "T3Q3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T3Q4"-------
    continueRoutine = True
    # update component parameters for each repeat
    T3I4.setImage(T3Q4)
    T3Q4R.keys = []
    T3Q4R.rt = []
    _T3Q4R_allKeys = []
    # keep track of which components have finished
    T3Q4Components = [T3I4, T3Q4R]
    for thisComponent in T3Q4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T3Q4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T3Q4"-------
    while continueRoutine:
        # get current time
        t = T3Q4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T3Q4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T3I4* updates
        if T3I4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3I4.frameNStart = frameN  # exact frame index
            T3I4.tStart = t  # local t and not account for scr refresh
            T3I4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3I4, 'tStartRefresh')  # time at next scr refresh
            T3I4.setAutoDraw(True)
        
        # *T3Q4R* updates
        waitOnFlip = False
        if T3Q4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3Q4R.frameNStart = frameN  # exact frame index
            T3Q4R.tStart = t  # local t and not account for scr refresh
            T3Q4R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3Q4R, 'tStartRefresh')  # time at next scr refresh
            T3Q4R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T3Q4R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T3Q4R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T3Q4R.status == STARTED and not waitOnFlip:
            theseKeys = T3Q4R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T3Q4R_allKeys.extend(theseKeys)
            if len(_T3Q4R_allKeys):
                T3Q4R.keys = _T3Q4R_allKeys[-1].name  # just the last key pressed
                T3Q4R.rt = _T3Q4R_allKeys[-1].rt
                # was this correct?
                if (T3Q4R.keys == str(CorrT3Q4)) or (T3Q4R.keys == CorrT3Q4):
                    T3Q4R.corr = 1
                else:
                    T3Q4R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T3Q4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T3Q4"-------
    for thisComponent in T3Q4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T3I4.started', T3I4.tStartRefresh)
    trials.addData('T3I4.stopped', T3I4.tStopRefresh)
    # check responses
    if T3Q4R.keys in ['', [], None]:  # No response was made
        T3Q4R.keys = None
        # was no response the correct answer?!
        if str(CorrT3Q4).lower() == 'none':
           T3Q4R.corr = 1;  # correct non-response
        else:
           T3Q4R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T3Q4R.keys',T3Q4R.keys)
    trials.addData('T3Q4R.corr', T3Q4R.corr)
    if T3Q4R.keys != None:  # we had a response
        trials.addData('T3Q4R.rt', T3Q4R.rt)
    trials.addData('T3Q4R.started', T3Q4R.tStartRefresh)
    trials.addData('T3Q4R.stopped', T3Q4R.tStopRefresh)
    # the Routine "T3Q4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T3Q5"-------
    continueRoutine = True
    # update component parameters for each repeat
    T3I5.setImage(T3Q5)
    T3Q5R.keys = []
    T3Q5R.rt = []
    _T3Q5R_allKeys = []
    # keep track of which components have finished
    T3Q5Components = [T3I5, T3Q5R]
    for thisComponent in T3Q5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T3Q5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T3Q5"-------
    while continueRoutine:
        # get current time
        t = T3Q5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T3Q5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T3I5* updates
        if T3I5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3I5.frameNStart = frameN  # exact frame index
            T3I5.tStart = t  # local t and not account for scr refresh
            T3I5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3I5, 'tStartRefresh')  # time at next scr refresh
            T3I5.setAutoDraw(True)
        
        # *T3Q5R* updates
        waitOnFlip = False
        if T3Q5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3Q5R.frameNStart = frameN  # exact frame index
            T3Q5R.tStart = t  # local t and not account for scr refresh
            T3Q5R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3Q5R, 'tStartRefresh')  # time at next scr refresh
            T3Q5R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T3Q5R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T3Q5R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T3Q5R.status == STARTED and not waitOnFlip:
            theseKeys = T3Q5R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T3Q5R_allKeys.extend(theseKeys)
            if len(_T3Q5R_allKeys):
                T3Q5R.keys = _T3Q5R_allKeys[-1].name  # just the last key pressed
                T3Q5R.rt = _T3Q5R_allKeys[-1].rt
                # was this correct?
                if (T3Q5R.keys == str(CorrT3Q5)) or (T3Q5R.keys == CorrT3Q5):
                    T3Q5R.corr = 1
                else:
                    T3Q5R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T3Q5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T3Q5"-------
    for thisComponent in T3Q5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T3I5.started', T3I5.tStartRefresh)
    trials.addData('T3I5.stopped', T3I5.tStopRefresh)
    # check responses
    if T3Q5R.keys in ['', [], None]:  # No response was made
        T3Q5R.keys = None
        # was no response the correct answer?!
        if str(CorrT3Q5).lower() == 'none':
           T3Q5R.corr = 1;  # correct non-response
        else:
           T3Q5R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T3Q5R.keys',T3Q5R.keys)
    trials.addData('T3Q5R.corr', T3Q5R.corr)
    if T3Q5R.keys != None:  # we had a response
        trials.addData('T3Q5R.rt', T3Q5R.rt)
    trials.addData('T3Q5R.started', T3Q5R.tStartRefresh)
    trials.addData('T3Q5R.stopped', T3Q5R.tStopRefresh)
    # the Routine "T3Q5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T3Q6"-------
    continueRoutine = True
    # update component parameters for each repeat
    T3I6.setImage(T3Q6)
    T3Q6R.keys = []
    T3Q6R.rt = []
    _T3Q6R_allKeys = []
    # keep track of which components have finished
    T3Q6Components = [T3I6, T3Q6R]
    for thisComponent in T3Q6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T3Q6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T3Q6"-------
    while continueRoutine:
        # get current time
        t = T3Q6Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T3Q6Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T3I6* updates
        if T3I6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3I6.frameNStart = frameN  # exact frame index
            T3I6.tStart = t  # local t and not account for scr refresh
            T3I6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3I6, 'tStartRefresh')  # time at next scr refresh
            T3I6.setAutoDraw(True)
        
        # *T3Q6R* updates
        waitOnFlip = False
        if T3Q6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3Q6R.frameNStart = frameN  # exact frame index
            T3Q6R.tStart = t  # local t and not account for scr refresh
            T3Q6R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3Q6R, 'tStartRefresh')  # time at next scr refresh
            T3Q6R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T3Q6R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T3Q6R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T3Q6R.status == STARTED and not waitOnFlip:
            theseKeys = T3Q6R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T3Q6R_allKeys.extend(theseKeys)
            if len(_T3Q6R_allKeys):
                T3Q6R.keys = _T3Q6R_allKeys[-1].name  # just the last key pressed
                T3Q6R.rt = _T3Q6R_allKeys[-1].rt
                # was this correct?
                if (T3Q6R.keys == str(CorrT3Q6)) or (T3Q6R.keys == CorrT3Q6):
                    T3Q6R.corr = 1
                else:
                    T3Q6R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T3Q6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T3Q6"-------
    for thisComponent in T3Q6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T3I6.started', T3I6.tStartRefresh)
    trials.addData('T3I6.stopped', T3I6.tStopRefresh)
    # check responses
    if T3Q6R.keys in ['', [], None]:  # No response was made
        T3Q6R.keys = None
        # was no response the correct answer?!
        if str(CorrT3Q6).lower() == 'none':
           T3Q6R.corr = 1;  # correct non-response
        else:
           T3Q6R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T3Q6R.keys',T3Q6R.keys)
    trials.addData('T3Q6R.corr', T3Q6R.corr)
    if T3Q6R.keys != None:  # we had a response
        trials.addData('T3Q6R.rt', T3Q6R.rt)
    trials.addData('T3Q6R.started', T3Q6R.tStartRefresh)
    trials.addData('T3Q6R.stopped', T3Q6R.tStopRefresh)
    # the Routine "T3Q6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T3Q7"-------
    continueRoutine = True
    # update component parameters for each repeat
    T3I7.setImage(T3Q7)
    T3Q7R.keys = []
    T3Q7R.rt = []
    _T3Q7R_allKeys = []
    # keep track of which components have finished
    T3Q7Components = [T3I7, T3Q7R]
    for thisComponent in T3Q7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T3Q7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T3Q7"-------
    while continueRoutine:
        # get current time
        t = T3Q7Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T3Q7Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T3I7* updates
        if T3I7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3I7.frameNStart = frameN  # exact frame index
            T3I7.tStart = t  # local t and not account for scr refresh
            T3I7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3I7, 'tStartRefresh')  # time at next scr refresh
            T3I7.setAutoDraw(True)
        
        # *T3Q7R* updates
        waitOnFlip = False
        if T3Q7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3Q7R.frameNStart = frameN  # exact frame index
            T3Q7R.tStart = t  # local t and not account for scr refresh
            T3Q7R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3Q7R, 'tStartRefresh')  # time at next scr refresh
            T3Q7R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T3Q7R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T3Q7R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T3Q7R.status == STARTED and not waitOnFlip:
            theseKeys = T3Q7R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T3Q7R_allKeys.extend(theseKeys)
            if len(_T3Q7R_allKeys):
                T3Q7R.keys = _T3Q7R_allKeys[-1].name  # just the last key pressed
                T3Q7R.rt = _T3Q7R_allKeys[-1].rt
                # was this correct?
                if (T3Q7R.keys == str(CorrT3Q7)) or (T3Q7R.keys == CorrT3Q7):
                    T3Q7R.corr = 1
                else:
                    T3Q7R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T3Q7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T3Q7"-------
    for thisComponent in T3Q7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T3I7.started', T3I7.tStartRefresh)
    trials.addData('T3I7.stopped', T3I7.tStopRefresh)
    # check responses
    if T3Q7R.keys in ['', [], None]:  # No response was made
        T3Q7R.keys = None
        # was no response the correct answer?!
        if str(CorrT3Q7).lower() == 'none':
           T3Q7R.corr = 1;  # correct non-response
        else:
           T3Q7R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T3Q7R.keys',T3Q7R.keys)
    trials.addData('T3Q7R.corr', T3Q7R.corr)
    if T3Q7R.keys != None:  # we had a response
        trials.addData('T3Q7R.rt', T3Q7R.rt)
    trials.addData('T3Q7R.started', T3Q7R.tStartRefresh)
    trials.addData('T3Q7R.stopped', T3Q7R.tStopRefresh)
    # the Routine "T3Q7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T3Q8"-------
    continueRoutine = True
    # update component parameters for each repeat
    T3I8.setImage(T3Q8)
    T3Q8R.keys = []
    T3Q8R.rt = []
    _T3Q8R_allKeys = []
    # keep track of which components have finished
    T3Q8Components = [T3I8, T3Q8R]
    for thisComponent in T3Q8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T3Q8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T3Q8"-------
    while continueRoutine:
        # get current time
        t = T3Q8Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T3Q8Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T3I8* updates
        if T3I8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3I8.frameNStart = frameN  # exact frame index
            T3I8.tStart = t  # local t and not account for scr refresh
            T3I8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3I8, 'tStartRefresh')  # time at next scr refresh
            T3I8.setAutoDraw(True)
        
        # *T3Q8R* updates
        waitOnFlip = False
        if T3Q8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3Q8R.frameNStart = frameN  # exact frame index
            T3Q8R.tStart = t  # local t and not account for scr refresh
            T3Q8R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3Q8R, 'tStartRefresh')  # time at next scr refresh
            T3Q8R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T3Q8R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T3Q8R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T3Q8R.status == STARTED and not waitOnFlip:
            theseKeys = T3Q8R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T3Q8R_allKeys.extend(theseKeys)
            if len(_T3Q8R_allKeys):
                T3Q8R.keys = _T3Q8R_allKeys[-1].name  # just the last key pressed
                T3Q8R.rt = _T3Q8R_allKeys[-1].rt
                # was this correct?
                if (T3Q8R.keys == str(CorrT3Q8)) or (T3Q8R.keys == CorrT3Q8):
                    T3Q8R.corr = 1
                else:
                    T3Q8R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T3Q8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T3Q8"-------
    for thisComponent in T3Q8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T3I8.started', T3I8.tStartRefresh)
    trials.addData('T3I8.stopped', T3I8.tStopRefresh)
    # check responses
    if T3Q8R.keys in ['', [], None]:  # No response was made
        T3Q8R.keys = None
        # was no response the correct answer?!
        if str(CorrT3Q8).lower() == 'none':
           T3Q8R.corr = 1;  # correct non-response
        else:
           T3Q8R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T3Q8R.keys',T3Q8R.keys)
    trials.addData('T3Q8R.corr', T3Q8R.corr)
    if T3Q8R.keys != None:  # we had a response
        trials.addData('T3Q8R.rt', T3Q8R.rt)
    trials.addData('T3Q8R.started', T3Q8R.tStartRefresh)
    trials.addData('T3Q8R.stopped', T3Q8R.tStopRefresh)
    # the Routine "T3Q8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T3Q9"-------
    continueRoutine = True
    # update component parameters for each repeat
    T3I9.setImage(T3Q9)
    T3Q9R.keys = []
    T3Q9R.rt = []
    _T3Q9R_allKeys = []
    # keep track of which components have finished
    T3Q9Components = [T3I9, T3Q9R]
    for thisComponent in T3Q9Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T3Q9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T3Q9"-------
    while continueRoutine:
        # get current time
        t = T3Q9Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T3Q9Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T3I9* updates
        if T3I9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3I9.frameNStart = frameN  # exact frame index
            T3I9.tStart = t  # local t and not account for scr refresh
            T3I9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3I9, 'tStartRefresh')  # time at next scr refresh
            T3I9.setAutoDraw(True)
        
        # *T3Q9R* updates
        waitOnFlip = False
        if T3Q9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3Q9R.frameNStart = frameN  # exact frame index
            T3Q9R.tStart = t  # local t and not account for scr refresh
            T3Q9R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3Q9R, 'tStartRefresh')  # time at next scr refresh
            T3Q9R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T3Q9R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T3Q9R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T3Q9R.status == STARTED and not waitOnFlip:
            theseKeys = T3Q9R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T3Q9R_allKeys.extend(theseKeys)
            if len(_T3Q9R_allKeys):
                T3Q9R.keys = _T3Q9R_allKeys[-1].name  # just the last key pressed
                T3Q9R.rt = _T3Q9R_allKeys[-1].rt
                # was this correct?
                if (T3Q9R.keys == str(CorrT3Q9)) or (T3Q9R.keys == CorrT3Q9):
                    T3Q9R.corr = 1
                else:
                    T3Q9R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T3Q9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T3Q9"-------
    for thisComponent in T3Q9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T3I9.started', T3I9.tStartRefresh)
    trials.addData('T3I9.stopped', T3I9.tStopRefresh)
    # check responses
    if T3Q9R.keys in ['', [], None]:  # No response was made
        T3Q9R.keys = None
        # was no response the correct answer?!
        if str(CorrT3Q9).lower() == 'none':
           T3Q9R.corr = 1;  # correct non-response
        else:
           T3Q9R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T3Q9R.keys',T3Q9R.keys)
    trials.addData('T3Q9R.corr', T3Q9R.corr)
    if T3Q9R.keys != None:  # we had a response
        trials.addData('T3Q9R.rt', T3Q9R.rt)
    trials.addData('T3Q9R.started', T3Q9R.tStartRefresh)
    trials.addData('T3Q9R.stopped', T3Q9R.tStopRefresh)
    # the Routine "T3Q9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T3Q10"-------
    continueRoutine = True
    # update component parameters for each repeat
    T3I10.setImage(T3Q10)
    T3Q10R.keys = []
    T3Q10R.rt = []
    _T3Q10R_allKeys = []
    # keep track of which components have finished
    T3Q10Components = [T3I10, T3Q10R]
    for thisComponent in T3Q10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T3Q10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T3Q10"-------
    while continueRoutine:
        # get current time
        t = T3Q10Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T3Q10Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T3I10* updates
        if T3I10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3I10.frameNStart = frameN  # exact frame index
            T3I10.tStart = t  # local t and not account for scr refresh
            T3I10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3I10, 'tStartRefresh')  # time at next scr refresh
            T3I10.setAutoDraw(True)
        
        # *T3Q10R* updates
        waitOnFlip = False
        if T3Q10R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T3Q10R.frameNStart = frameN  # exact frame index
            T3Q10R.tStart = t  # local t and not account for scr refresh
            T3Q10R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T3Q10R, 'tStartRefresh')  # time at next scr refresh
            T3Q10R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T3Q10R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T3Q10R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T3Q10R.status == STARTED and not waitOnFlip:
            theseKeys = T3Q10R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T3Q10R_allKeys.extend(theseKeys)
            if len(_T3Q10R_allKeys):
                T3Q10R.keys = _T3Q10R_allKeys[-1].name  # just the last key pressed
                T3Q10R.rt = _T3Q10R_allKeys[-1].rt
                # was this correct?
                if (T3Q10R.keys == str(CorrT3Q10)) or (T3Q10R.keys == CorrT3Q10):
                    T3Q10R.corr = 1
                else:
                    T3Q10R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T3Q10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T3Q10"-------
    for thisComponent in T3Q10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T3I10.started', T3I10.tStartRefresh)
    trials.addData('T3I10.stopped', T3I10.tStopRefresh)
    # check responses
    if T3Q10R.keys in ['', [], None]:  # No response was made
        T3Q10R.keys = None
        # was no response the correct answer?!
        if str(CorrT3Q10).lower() == 'none':
           T3Q10R.corr = 1;  # correct non-response
        else:
           T3Q10R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T3Q10R.keys',T3Q10R.keys)
    trials.addData('T3Q10R.corr', T3Q10R.corr)
    if T3Q10R.keys != None:  # we had a response
        trials.addData('T3Q10R.rt', T3Q10R.rt)
    trials.addData('T3Q10R.started', T3Q10R.tStartRefresh)
    trials.addData('T3Q10R.stopped', T3Q10R.tStopRefresh)
    # the Routine "T3Q10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Trial_Break"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    Trial_BreakComponents = [Break_message, key_resp_4]
    for thisComponent in Trial_BreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Trial_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial_Break"-------
    while continueRoutine:
        # get current time
        t = Trial_BreakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_BreakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Break_message* updates
        if Break_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_message.frameNStart = frameN  # exact frame index
            Break_message.tStart = t  # local t and not account for scr refresh
            Break_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_message, 'tStartRefresh')  # time at next scr refresh
            Break_message.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial_Break"-------
    for thisComponent in Trial_BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Break_message.started', Break_message.tStartRefresh)
    trials.addData('Break_message.stopped', Break_message.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Trial_Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T4A"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_4.setSound(T4A, hamming=True)
    sound_4.setVolume(1.0, log=False)
    T4A = cond_set[cond_set['Cond'] == cond]['T4A'].values[0]
    cond_speed = re.search(r'(\d+\.\d+)x', T4A).group(1)
    cond_noise = re.search(r'(\w+)_Audio', T4A).group(1)
    send_trigger(cond_speed, cond_noise)
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    # keep track of which components have finished
    T4AComponents = [sound_4, image_4, key_resp_9]
    for thisComponent in T4AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T4AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T4A"-------
    while continueRoutine:
        # get current time
        t = T4AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T4AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_4
        if sound_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_4.frameNStart = frameN  # exact frame index
            sound_4.tStart = t  # local t and not account for scr refresh
            sound_4.tStartRefresh = tThisFlipGlobal  # on global time
            sound_4.play()  # start the sound (it finishes automatically)
        
        # *image_4* updates
        if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_4.frameNStart = frameN  # exact frame index
            image_4.tStart = t  # local t and not account for scr refresh
            image_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
            image_4.setAutoDraw(True)
        if sound_4.status == FINISHED:
            continueRoutine = False
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['z'], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T4AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T4A"-------
    for thisComponent in T4AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_4.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_4.started', sound_4.tStart)
    trials.addData('sound_4.stopped', sound_4.tStop)
    trials.addData('image_4.started', image_4.tStartRefresh)
    trials.addData('image_4.stopped', image_4.tStopRefresh)
    ser.write((200).to_bytes(1, 'big'))
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    trials.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        trials.addData('key_resp_9.rt', key_resp_9.rt)
    trials.addData('key_resp_9.started', key_resp_9.tStartRefresh)
    trials.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
    # the Routine "T4A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pre_assement_inst"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    Pre_assement_instComponents = [text_5, key_resp_5]
    for thisComponent in Pre_assement_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pre_assement_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pre_assement_inst"-------
    while continueRoutine:
        # get current time
        t = Pre_assement_instClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pre_assement_instClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pre_assement_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pre_assement_inst"-------
    for thisComponent in Pre_assement_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_5.started', text_5.tStartRefresh)
    trials.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    trials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    trials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "Pre_assement_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T4Q1"-------
    continueRoutine = True
    # update component parameters for each repeat
    T4I1.setImage(T4Q1)
    T4Q1R.keys = []
    T4Q1R.rt = []
    _T4Q1R_allKeys = []
    # keep track of which components have finished
    T4Q1Components = [T4I1, T4Q1R]
    for thisComponent in T4Q1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T4Q1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T4Q1"-------
    while continueRoutine:
        # get current time
        t = T4Q1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T4Q1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T4I1* updates
        if T4I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4I1.frameNStart = frameN  # exact frame index
            T4I1.tStart = t  # local t and not account for scr refresh
            T4I1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4I1, 'tStartRefresh')  # time at next scr refresh
            T4I1.setAutoDraw(True)
        
        # *T4Q1R* updates
        waitOnFlip = False
        if T4Q1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4Q1R.frameNStart = frameN  # exact frame index
            T4Q1R.tStart = t  # local t and not account for scr refresh
            T4Q1R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4Q1R, 'tStartRefresh')  # time at next scr refresh
            T4Q1R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T4Q1R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T4Q1R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T4Q1R.status == STARTED and not waitOnFlip:
            theseKeys = T4Q1R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T4Q1R_allKeys.extend(theseKeys)
            if len(_T4Q1R_allKeys):
                T4Q1R.keys = _T4Q1R_allKeys[-1].name  # just the last key pressed
                T4Q1R.rt = _T4Q1R_allKeys[-1].rt
                # was this correct?
                if (T4Q1R.keys == str(CorrT4Q1)) or (T4Q1R.keys == CorrT4Q1):
                    T4Q1R.corr = 1
                else:
                    T4Q1R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T4Q1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T4Q1"-------
    for thisComponent in T4Q1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T4I1.started', T4I1.tStartRefresh)
    trials.addData('T4I1.stopped', T4I1.tStopRefresh)
    # check responses
    if T4Q1R.keys in ['', [], None]:  # No response was made
        T4Q1R.keys = None
        # was no response the correct answer?!
        if str(CorrT4Q1).lower() == 'none':
           T4Q1R.corr = 1;  # correct non-response
        else:
           T4Q1R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T4Q1R.keys',T4Q1R.keys)
    trials.addData('T4Q1R.corr', T4Q1R.corr)
    if T4Q1R.keys != None:  # we had a response
        trials.addData('T4Q1R.rt', T4Q1R.rt)
    trials.addData('T4Q1R.started', T4Q1R.tStartRefresh)
    trials.addData('T4Q1R.stopped', T4Q1R.tStopRefresh)
    # the Routine "T4Q1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T4Q2"-------
    continueRoutine = True
    # update component parameters for each repeat
    T4I2.setImage(T4Q2)
    T4Q2R.keys = []
    T4Q2R.rt = []
    _T4Q2R_allKeys = []
    # keep track of which components have finished
    T4Q2Components = [T4I2, T4Q2R]
    for thisComponent in T4Q2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T4Q2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T4Q2"-------
    while continueRoutine:
        # get current time
        t = T4Q2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T4Q2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T4I2* updates
        if T4I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4I2.frameNStart = frameN  # exact frame index
            T4I2.tStart = t  # local t and not account for scr refresh
            T4I2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4I2, 'tStartRefresh')  # time at next scr refresh
            T4I2.setAutoDraw(True)
        
        # *T4Q2R* updates
        waitOnFlip = False
        if T4Q2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4Q2R.frameNStart = frameN  # exact frame index
            T4Q2R.tStart = t  # local t and not account for scr refresh
            T4Q2R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4Q2R, 'tStartRefresh')  # time at next scr refresh
            T4Q2R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T4Q2R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T4Q2R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T4Q2R.status == STARTED and not waitOnFlip:
            theseKeys = T4Q2R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T4Q2R_allKeys.extend(theseKeys)
            if len(_T4Q2R_allKeys):
                T4Q2R.keys = _T4Q2R_allKeys[-1].name  # just the last key pressed
                T4Q2R.rt = _T4Q2R_allKeys[-1].rt
                # was this correct?
                if (T4Q2R.keys == str(CorrT4Q2)) or (T4Q2R.keys == CorrT4Q2):
                    T4Q2R.corr = 1
                else:
                    T4Q2R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T4Q2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T4Q2"-------
    for thisComponent in T4Q2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T4I2.started', T4I2.tStartRefresh)
    trials.addData('T4I2.stopped', T4I2.tStopRefresh)
    # check responses
    if T4Q2R.keys in ['', [], None]:  # No response was made
        T4Q2R.keys = None
        # was no response the correct answer?!
        if str(CorrT4Q2).lower() == 'none':
           T4Q2R.corr = 1;  # correct non-response
        else:
           T4Q2R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T4Q2R.keys',T4Q2R.keys)
    trials.addData('T4Q2R.corr', T4Q2R.corr)
    if T4Q2R.keys != None:  # we had a response
        trials.addData('T4Q2R.rt', T4Q2R.rt)
    trials.addData('T4Q2R.started', T4Q2R.tStartRefresh)
    trials.addData('T4Q2R.stopped', T4Q2R.tStopRefresh)
    # the Routine "T4Q2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T4Q3"-------
    continueRoutine = True
    # update component parameters for each repeat
    T4I3.setImage(T4Q3)
    T4Q3R.keys = []
    T4Q3R.rt = []
    _T4Q3R_allKeys = []
    # keep track of which components have finished
    T4Q3Components = [T4I3, T4Q3R]
    for thisComponent in T4Q3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T4Q3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T4Q3"-------
    while continueRoutine:
        # get current time
        t = T4Q3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T4Q3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T4I3* updates
        if T4I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4I3.frameNStart = frameN  # exact frame index
            T4I3.tStart = t  # local t and not account for scr refresh
            T4I3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4I3, 'tStartRefresh')  # time at next scr refresh
            T4I3.setAutoDraw(True)
        
        # *T4Q3R* updates
        waitOnFlip = False
        if T4Q3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4Q3R.frameNStart = frameN  # exact frame index
            T4Q3R.tStart = t  # local t and not account for scr refresh
            T4Q3R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4Q3R, 'tStartRefresh')  # time at next scr refresh
            T4Q3R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T4Q3R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T4Q3R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T4Q3R.status == STARTED and not waitOnFlip:
            theseKeys = T4Q3R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T4Q3R_allKeys.extend(theseKeys)
            if len(_T4Q3R_allKeys):
                T4Q3R.keys = _T4Q3R_allKeys[-1].name  # just the last key pressed
                T4Q3R.rt = _T4Q3R_allKeys[-1].rt
                # was this correct?
                if (T4Q3R.keys == str(CorrT4Q3)) or (T4Q3R.keys == CorrT4Q3):
                    T4Q3R.corr = 1
                else:
                    T4Q3R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T4Q3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T4Q3"-------
    for thisComponent in T4Q3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T4I3.started', T4I3.tStartRefresh)
    trials.addData('T4I3.stopped', T4I3.tStopRefresh)
    # check responses
    if T4Q3R.keys in ['', [], None]:  # No response was made
        T4Q3R.keys = None
        # was no response the correct answer?!
        if str(CorrT4Q3).lower() == 'none':
           T4Q3R.corr = 1;  # correct non-response
        else:
           T4Q3R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T4Q3R.keys',T4Q3R.keys)
    trials.addData('T4Q3R.corr', T4Q3R.corr)
    if T4Q3R.keys != None:  # we had a response
        trials.addData('T4Q3R.rt', T4Q3R.rt)
    trials.addData('T4Q3R.started', T4Q3R.tStartRefresh)
    trials.addData('T4Q3R.stopped', T4Q3R.tStopRefresh)
    # the Routine "T4Q3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T4Q4"-------
    continueRoutine = True
    # update component parameters for each repeat
    T4I4.setImage(T4Q4)
    T4Q4R.keys = []
    T4Q4R.rt = []
    _T4Q4R_allKeys = []
    # keep track of which components have finished
    T4Q4Components = [T4I4, T4Q4R]
    for thisComponent in T4Q4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T4Q4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T4Q4"-------
    while continueRoutine:
        # get current time
        t = T4Q4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T4Q4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T4I4* updates
        if T4I4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4I4.frameNStart = frameN  # exact frame index
            T4I4.tStart = t  # local t and not account for scr refresh
            T4I4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4I4, 'tStartRefresh')  # time at next scr refresh
            T4I4.setAutoDraw(True)
        
        # *T4Q4R* updates
        waitOnFlip = False
        if T4Q4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4Q4R.frameNStart = frameN  # exact frame index
            T4Q4R.tStart = t  # local t and not account for scr refresh
            T4Q4R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4Q4R, 'tStartRefresh')  # time at next scr refresh
            T4Q4R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T4Q4R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T4Q4R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T4Q4R.status == STARTED and not waitOnFlip:
            theseKeys = T4Q4R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T4Q4R_allKeys.extend(theseKeys)
            if len(_T4Q4R_allKeys):
                T4Q4R.keys = _T4Q4R_allKeys[-1].name  # just the last key pressed
                T4Q4R.rt = _T4Q4R_allKeys[-1].rt
                # was this correct?
                if (T4Q4R.keys == str(CorrT4Q4)) or (T4Q4R.keys == CorrT4Q4):
                    T4Q4R.corr = 1
                else:
                    T4Q4R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T4Q4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T4Q4"-------
    for thisComponent in T4Q4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T4I4.started', T4I4.tStartRefresh)
    trials.addData('T4I4.stopped', T4I4.tStopRefresh)
    # check responses
    if T4Q4R.keys in ['', [], None]:  # No response was made
        T4Q4R.keys = None
        # was no response the correct answer?!
        if str(CorrT4Q4).lower() == 'none':
           T4Q4R.corr = 1;  # correct non-response
        else:
           T4Q4R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T4Q4R.keys',T4Q4R.keys)
    trials.addData('T4Q4R.corr', T4Q4R.corr)
    if T4Q4R.keys != None:  # we had a response
        trials.addData('T4Q4R.rt', T4Q4R.rt)
    trials.addData('T4Q4R.started', T4Q4R.tStartRefresh)
    trials.addData('T4Q4R.stopped', T4Q4R.tStopRefresh)
    # the Routine "T4Q4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T4Q5"-------
    continueRoutine = True
    # update component parameters for each repeat
    T4I5.setImage(T4Q5)
    T4Q5R.keys = []
    T4Q5R.rt = []
    _T4Q5R_allKeys = []
    # keep track of which components have finished
    T4Q5Components = [T4I5, T4Q5R]
    for thisComponent in T4Q5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T4Q5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T4Q5"-------
    while continueRoutine:
        # get current time
        t = T4Q5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T4Q5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T4I5* updates
        if T4I5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4I5.frameNStart = frameN  # exact frame index
            T4I5.tStart = t  # local t and not account for scr refresh
            T4I5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4I5, 'tStartRefresh')  # time at next scr refresh
            T4I5.setAutoDraw(True)
        
        # *T4Q5R* updates
        waitOnFlip = False
        if T4Q5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4Q5R.frameNStart = frameN  # exact frame index
            T4Q5R.tStart = t  # local t and not account for scr refresh
            T4Q5R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4Q5R, 'tStartRefresh')  # time at next scr refresh
            T4Q5R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T4Q5R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T4Q5R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T4Q5R.status == STARTED and not waitOnFlip:
            theseKeys = T4Q5R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T4Q5R_allKeys.extend(theseKeys)
            if len(_T4Q5R_allKeys):
                T4Q5R.keys = _T4Q5R_allKeys[-1].name  # just the last key pressed
                T4Q5R.rt = _T4Q5R_allKeys[-1].rt
                # was this correct?
                if (T4Q5R.keys == str(CorrT4Q5)) or (T4Q5R.keys == CorrT4Q5):
                    T4Q5R.corr = 1
                else:
                    T4Q5R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T4Q5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T4Q5"-------
    for thisComponent in T4Q5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T4I5.started', T4I5.tStartRefresh)
    trials.addData('T4I5.stopped', T4I5.tStopRefresh)
    # check responses
    if T4Q5R.keys in ['', [], None]:  # No response was made
        T4Q5R.keys = None
        # was no response the correct answer?!
        if str(CorrT4Q5).lower() == 'none':
           T4Q5R.corr = 1;  # correct non-response
        else:
           T4Q5R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T4Q5R.keys',T4Q5R.keys)
    trials.addData('T4Q5R.corr', T4Q5R.corr)
    if T4Q5R.keys != None:  # we had a response
        trials.addData('T4Q5R.rt', T4Q5R.rt)
    trials.addData('T4Q5R.started', T4Q5R.tStartRefresh)
    trials.addData('T4Q5R.stopped', T4Q5R.tStopRefresh)
    # the Routine "T4Q5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T4Q6"-------
    continueRoutine = True
    # update component parameters for each repeat
    T4I6.setImage(T4Q6)
    T4Q6R.keys = []
    T4Q6R.rt = []
    _T4Q6R_allKeys = []
    # keep track of which components have finished
    T4Q6Components = [T4I6, T4Q6R]
    for thisComponent in T4Q6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T4Q6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T4Q6"-------
    while continueRoutine:
        # get current time
        t = T4Q6Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T4Q6Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T4I6* updates
        if T4I6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4I6.frameNStart = frameN  # exact frame index
            T4I6.tStart = t  # local t and not account for scr refresh
            T4I6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4I6, 'tStartRefresh')  # time at next scr refresh
            T4I6.setAutoDraw(True)
        
        # *T4Q6R* updates
        waitOnFlip = False
        if T4Q6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4Q6R.frameNStart = frameN  # exact frame index
            T4Q6R.tStart = t  # local t and not account for scr refresh
            T4Q6R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4Q6R, 'tStartRefresh')  # time at next scr refresh
            T4Q6R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T4Q6R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T4Q6R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T4Q6R.status == STARTED and not waitOnFlip:
            theseKeys = T4Q6R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T4Q6R_allKeys.extend(theseKeys)
            if len(_T4Q6R_allKeys):
                T4Q6R.keys = _T4Q6R_allKeys[-1].name  # just the last key pressed
                T4Q6R.rt = _T4Q6R_allKeys[-1].rt
                # was this correct?
                if (T4Q6R.keys == str(CorrT4Q6)) or (T4Q6R.keys == CorrT4Q6):
                    T4Q6R.corr = 1
                else:
                    T4Q6R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T4Q6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T4Q6"-------
    for thisComponent in T4Q6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T4I6.started', T4I6.tStartRefresh)
    trials.addData('T4I6.stopped', T4I6.tStopRefresh)
    # check responses
    if T4Q6R.keys in ['', [], None]:  # No response was made
        T4Q6R.keys = None
        # was no response the correct answer?!
        if str(CorrT4Q6).lower() == 'none':
           T4Q6R.corr = 1;  # correct non-response
        else:
           T4Q6R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T4Q6R.keys',T4Q6R.keys)
    trials.addData('T4Q6R.corr', T4Q6R.corr)
    if T4Q6R.keys != None:  # we had a response
        trials.addData('T4Q6R.rt', T4Q6R.rt)
    trials.addData('T4Q6R.started', T4Q6R.tStartRefresh)
    trials.addData('T4Q6R.stopped', T4Q6R.tStopRefresh)
    # the Routine "T4Q6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T4Q7"-------
    continueRoutine = True
    # update component parameters for each repeat
    T4I7.setImage(T4Q7)
    T4Q7R.keys = []
    T4Q7R.rt = []
    _T4Q7R_allKeys = []
    # keep track of which components have finished
    T4Q7Components = [T4I7, T4Q7R]
    for thisComponent in T4Q7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T4Q7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T4Q7"-------
    while continueRoutine:
        # get current time
        t = T4Q7Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T4Q7Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T4I7* updates
        if T4I7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4I7.frameNStart = frameN  # exact frame index
            T4I7.tStart = t  # local t and not account for scr refresh
            T4I7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4I7, 'tStartRefresh')  # time at next scr refresh
            T4I7.setAutoDraw(True)
        
        # *T4Q7R* updates
        waitOnFlip = False
        if T4Q7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4Q7R.frameNStart = frameN  # exact frame index
            T4Q7R.tStart = t  # local t and not account for scr refresh
            T4Q7R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4Q7R, 'tStartRefresh')  # time at next scr refresh
            T4Q7R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T4Q7R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T4Q7R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T4Q7R.status == STARTED and not waitOnFlip:
            theseKeys = T4Q7R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T4Q7R_allKeys.extend(theseKeys)
            if len(_T4Q7R_allKeys):
                T4Q7R.keys = _T4Q7R_allKeys[-1].name  # just the last key pressed
                T4Q7R.rt = _T4Q7R_allKeys[-1].rt
                # was this correct?
                if (T4Q7R.keys == str(CorrT4Q7)) or (T4Q7R.keys == CorrT4Q7):
                    T4Q7R.corr = 1
                else:
                    T4Q7R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T4Q7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T4Q7"-------
    for thisComponent in T4Q7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T4I7.started', T4I7.tStartRefresh)
    trials.addData('T4I7.stopped', T4I7.tStopRefresh)
    # check responses
    if T4Q7R.keys in ['', [], None]:  # No response was made
        T4Q7R.keys = None
        # was no response the correct answer?!
        if str(CorrT4Q7).lower() == 'none':
           T4Q7R.corr = 1;  # correct non-response
        else:
           T4Q7R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T4Q7R.keys',T4Q7R.keys)
    trials.addData('T4Q7R.corr', T4Q7R.corr)
    if T4Q7R.keys != None:  # we had a response
        trials.addData('T4Q7R.rt', T4Q7R.rt)
    trials.addData('T4Q7R.started', T4Q7R.tStartRefresh)
    trials.addData('T4Q7R.stopped', T4Q7R.tStopRefresh)
    # the Routine "T4Q7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T4Q8"-------
    continueRoutine = True
    # update component parameters for each repeat
    T4I8.setImage(T4Q8)
    T4Q8R.keys = []
    T4Q8R.rt = []
    _T4Q8R_allKeys = []
    # keep track of which components have finished
    T4Q8Components = [T4I8, T4Q8R]
    for thisComponent in T4Q8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T4Q8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T4Q8"-------
    while continueRoutine:
        # get current time
        t = T4Q8Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T4Q8Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T4I8* updates
        if T4I8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4I8.frameNStart = frameN  # exact frame index
            T4I8.tStart = t  # local t and not account for scr refresh
            T4I8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4I8, 'tStartRefresh')  # time at next scr refresh
            T4I8.setAutoDraw(True)
        
        # *T4Q8R* updates
        waitOnFlip = False
        if T4Q8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4Q8R.frameNStart = frameN  # exact frame index
            T4Q8R.tStart = t  # local t and not account for scr refresh
            T4Q8R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4Q8R, 'tStartRefresh')  # time at next scr refresh
            T4Q8R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T4Q8R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T4Q8R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T4Q8R.status == STARTED and not waitOnFlip:
            theseKeys = T4Q8R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T4Q8R_allKeys.extend(theseKeys)
            if len(_T4Q8R_allKeys):
                T4Q8R.keys = _T4Q8R_allKeys[-1].name  # just the last key pressed
                T4Q8R.rt = _T4Q8R_allKeys[-1].rt
                # was this correct?
                if (T4Q8R.keys == str(CorrT4Q8)) or (T4Q8R.keys == CorrT4Q8):
                    T4Q8R.corr = 1
                else:
                    T4Q8R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T4Q8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T4Q8"-------
    for thisComponent in T4Q8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T4I8.started', T4I8.tStartRefresh)
    trials.addData('T4I8.stopped', T4I8.tStopRefresh)
    # check responses
    if T4Q8R.keys in ['', [], None]:  # No response was made
        T4Q8R.keys = None
        # was no response the correct answer?!
        if str(CorrT4Q8).lower() == 'none':
           T4Q8R.corr = 1;  # correct non-response
        else:
           T4Q8R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T4Q8R.keys',T4Q8R.keys)
    trials.addData('T4Q8R.corr', T4Q8R.corr)
    if T4Q8R.keys != None:  # we had a response
        trials.addData('T4Q8R.rt', T4Q8R.rt)
    trials.addData('T4Q8R.started', T4Q8R.tStartRefresh)
    trials.addData('T4Q8R.stopped', T4Q8R.tStopRefresh)
    # the Routine "T4Q8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T4Q9"-------
    continueRoutine = True
    # update component parameters for each repeat
    T4I9.setImage(T4Q9)
    T4Q9R.keys = []
    T4Q9R.rt = []
    _T4Q9R_allKeys = []
    # keep track of which components have finished
    T4Q9Components = [T4I9, T4Q9R]
    for thisComponent in T4Q9Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T4Q9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T4Q9"-------
    while continueRoutine:
        # get current time
        t = T4Q9Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T4Q9Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T4I9* updates
        if T4I9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4I9.frameNStart = frameN  # exact frame index
            T4I9.tStart = t  # local t and not account for scr refresh
            T4I9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4I9, 'tStartRefresh')  # time at next scr refresh
            T4I9.setAutoDraw(True)
        
        # *T4Q9R* updates
        waitOnFlip = False
        if T4Q9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4Q9R.frameNStart = frameN  # exact frame index
            T4Q9R.tStart = t  # local t and not account for scr refresh
            T4Q9R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4Q9R, 'tStartRefresh')  # time at next scr refresh
            T4Q9R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T4Q9R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T4Q9R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T4Q9R.status == STARTED and not waitOnFlip:
            theseKeys = T4Q9R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T4Q9R_allKeys.extend(theseKeys)
            if len(_T4Q9R_allKeys):
                T4Q9R.keys = _T4Q9R_allKeys[-1].name  # just the last key pressed
                T4Q9R.rt = _T4Q9R_allKeys[-1].rt
                # was this correct?
                if (T4Q9R.keys == str(CorrT4Q9)) or (T4Q9R.keys == CorrT4Q9):
                    T4Q9R.corr = 1
                else:
                    T4Q9R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T4Q9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T4Q9"-------
    for thisComponent in T4Q9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T4I9.started', T4I9.tStartRefresh)
    trials.addData('T4I9.stopped', T4I9.tStopRefresh)
    # check responses
    if T4Q9R.keys in ['', [], None]:  # No response was made
        T4Q9R.keys = None
        # was no response the correct answer?!
        if str(CorrT4Q9).lower() == 'none':
           T4Q9R.corr = 1;  # correct non-response
        else:
           T4Q9R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T4Q9R.keys',T4Q9R.keys)
    trials.addData('T4Q9R.corr', T4Q9R.corr)
    if T4Q9R.keys != None:  # we had a response
        trials.addData('T4Q9R.rt', T4Q9R.rt)
    trials.addData('T4Q9R.started', T4Q9R.tStartRefresh)
    trials.addData('T4Q9R.stopped', T4Q9R.tStopRefresh)
    # the Routine "T4Q9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T4Q10"-------
    continueRoutine = True
    # update component parameters for each repeat
    T4I10.setImage(T4Q10)
    T4Q10R.keys = []
    T4Q10R.rt = []
    _T4Q10R_allKeys = []
    # keep track of which components have finished
    T4Q10Components = [T4I10, T4Q10R]
    for thisComponent in T4Q10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T4Q10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T4Q10"-------
    while continueRoutine:
        # get current time
        t = T4Q10Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T4Q10Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T4I10* updates
        if T4I10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4I10.frameNStart = frameN  # exact frame index
            T4I10.tStart = t  # local t and not account for scr refresh
            T4I10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4I10, 'tStartRefresh')  # time at next scr refresh
            T4I10.setAutoDraw(True)
        
        # *T4Q10R* updates
        waitOnFlip = False
        if T4Q10R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T4Q10R.frameNStart = frameN  # exact frame index
            T4Q10R.tStart = t  # local t and not account for scr refresh
            T4Q10R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T4Q10R, 'tStartRefresh')  # time at next scr refresh
            T4Q10R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T4Q10R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T4Q10R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T4Q10R.status == STARTED and not waitOnFlip:
            theseKeys = T4Q10R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T4Q10R_allKeys.extend(theseKeys)
            if len(_T4Q10R_allKeys):
                T4Q10R.keys = _T4Q10R_allKeys[-1].name  # just the last key pressed
                T4Q10R.rt = _T4Q10R_allKeys[-1].rt
                # was this correct?
                if (T4Q10R.keys == str(CorrT4Q10)) or (T4Q10R.keys == CorrT4Q10):
                    T4Q10R.corr = 1
                else:
                    T4Q10R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T4Q10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T4Q10"-------
    for thisComponent in T4Q10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T4I10.started', T4I10.tStartRefresh)
    trials.addData('T4I10.stopped', T4I10.tStopRefresh)
    # check responses
    if T4Q10R.keys in ['', [], None]:  # No response was made
        T4Q10R.keys = None
        # was no response the correct answer?!
        if str(CorrT4Q10).lower() == 'none':
           T4Q10R.corr = 1;  # correct non-response
        else:
           T4Q10R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T4Q10R.keys',T4Q10R.keys)
    trials.addData('T4Q10R.corr', T4Q10R.corr)
    if T4Q10R.keys != None:  # we had a response
        trials.addData('T4Q10R.rt', T4Q10R.rt)
    trials.addData('T4Q10R.started', T4Q10R.tStartRefresh)
    trials.addData('T4Q10R.stopped', T4Q10R.tStopRefresh)
    # the Routine "T4Q10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Trial_Break"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    Trial_BreakComponents = [Break_message, key_resp_4]
    for thisComponent in Trial_BreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Trial_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial_Break"-------
    while continueRoutine:
        # get current time
        t = Trial_BreakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_BreakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Break_message* updates
        if Break_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_message.frameNStart = frameN  # exact frame index
            Break_message.tStart = t  # local t and not account for scr refresh
            Break_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_message, 'tStartRefresh')  # time at next scr refresh
            Break_message.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial_Break"-------
    for thisComponent in Trial_BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Break_message.started', Break_message.tStartRefresh)
    trials.addData('Break_message.stopped', Break_message.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Trial_Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T5A"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_5.setSound(T5A, hamming=True)
    sound_5.setVolume(1.0, log=False)
    T5A = cond_set[cond_set['Cond'] == cond]['T5A'].values[0]
    cond_speed = re.search(r'(\d+\.\d+)x', T5A).group(1)
    cond_noise = re.search(r'(\w+)_Audio', T5).group(1)
    send_trigger(cond_speed, cond_noise)
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # keep track of which components have finished
    T5AComponents = [sound_5, image_5, key_resp_8]
    for thisComponent in T5AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T5AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T5A"-------
    while continueRoutine:
        # get current time
        t = T5AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T5AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_5
        if sound_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_5.frameNStart = frameN  # exact frame index
            sound_5.tStart = t  # local t and not account for scr refresh
            sound_5.tStartRefresh = tThisFlipGlobal  # on global time
            sound_5.play()  # start the sound (it finishes automatically)
        
        # *image_5* updates
        if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_5.frameNStart = frameN  # exact frame index
            image_5.tStart = t  # local t and not account for scr refresh
            image_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
            image_5.setAutoDraw(True)
        if sound_5.status == FINISHED:
            continueRoutine = False
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['z'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T5AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T5A"-------
    for thisComponent in T5AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_5.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_5.started', sound_5.tStart)
    trials.addData('sound_5.stopped', sound_5.tStop)
    trials.addData('image_5.started', image_5.tStartRefresh)
    trials.addData('image_5.stopped', image_5.tStopRefresh)
    ser.write((200).to_bytes(1, 'big'))
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    trials.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        trials.addData('key_resp_8.rt', key_resp_8.rt)
    trials.addData('key_resp_8.started', key_resp_8.tStartRefresh)
    trials.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
    # the Routine "T5A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pre_assement_inst"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    Pre_assement_instComponents = [text_5, key_resp_5]
    for thisComponent in Pre_assement_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pre_assement_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pre_assement_inst"-------
    while continueRoutine:
        # get current time
        t = Pre_assement_instClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pre_assement_instClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pre_assement_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pre_assement_inst"-------
    for thisComponent in Pre_assement_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_5.started', text_5.tStartRefresh)
    trials.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    trials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    trials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "Pre_assement_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T5Q1"-------
    continueRoutine = True
    # update component parameters for each repeat
    T5I1.setImage(T5Q1)
    T5Q1R.keys = []
    T5Q1R.rt = []
    _T5Q1R_allKeys = []
    # keep track of which components have finished
    T5Q1Components = [T5I1, T5Q1R]
    for thisComponent in T5Q1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T5Q1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T5Q1"-------
    while continueRoutine:
        # get current time
        t = T5Q1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T5Q1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T5I1* updates
        if T5I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5I1.frameNStart = frameN  # exact frame index
            T5I1.tStart = t  # local t and not account for scr refresh
            T5I1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5I1, 'tStartRefresh')  # time at next scr refresh
            T5I1.setAutoDraw(True)
        
        # *T5Q1R* updates
        waitOnFlip = False
        if T5Q1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5Q1R.frameNStart = frameN  # exact frame index
            T5Q1R.tStart = t  # local t and not account for scr refresh
            T5Q1R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5Q1R, 'tStartRefresh')  # time at next scr refresh
            T5Q1R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T5Q1R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T5Q1R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T5Q1R.status == STARTED and not waitOnFlip:
            theseKeys = T5Q1R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T5Q1R_allKeys.extend(theseKeys)
            if len(_T5Q1R_allKeys):
                T5Q1R.keys = _T5Q1R_allKeys[-1].name  # just the last key pressed
                T5Q1R.rt = _T5Q1R_allKeys[-1].rt
                # was this correct?
                if (T5Q1R.keys == str(CorrT5Q1)) or (T5Q1R.keys == CorrT5Q1):
                    T5Q1R.corr = 1
                else:
                    T5Q1R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T5Q1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T5Q1"-------
    for thisComponent in T5Q1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T5I1.started', T5I1.tStartRefresh)
    trials.addData('T5I1.stopped', T5I1.tStopRefresh)
    # check responses
    if T5Q1R.keys in ['', [], None]:  # No response was made
        T5Q1R.keys = None
        # was no response the correct answer?!
        if str(CorrT5Q1).lower() == 'none':
           T5Q1R.corr = 1;  # correct non-response
        else:
           T5Q1R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T5Q1R.keys',T5Q1R.keys)
    trials.addData('T5Q1R.corr', T5Q1R.corr)
    if T5Q1R.keys != None:  # we had a response
        trials.addData('T5Q1R.rt', T5Q1R.rt)
    trials.addData('T5Q1R.started', T5Q1R.tStartRefresh)
    trials.addData('T5Q1R.stopped', T5Q1R.tStopRefresh)
    # the Routine "T5Q1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T5Q2"-------
    continueRoutine = True
    # update component parameters for each repeat
    T5I2.setImage(T5Q2)
    T5Q2R.keys = []
    T5Q2R.rt = []
    _T5Q2R_allKeys = []
    # keep track of which components have finished
    T5Q2Components = [T5I2, T5Q2R]
    for thisComponent in T5Q2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T5Q2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T5Q2"-------
    while continueRoutine:
        # get current time
        t = T5Q2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T5Q2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T5I2* updates
        if T5I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5I2.frameNStart = frameN  # exact frame index
            T5I2.tStart = t  # local t and not account for scr refresh
            T5I2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5I2, 'tStartRefresh')  # time at next scr refresh
            T5I2.setAutoDraw(True)
        
        # *T5Q2R* updates
        waitOnFlip = False
        if T5Q2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5Q2R.frameNStart = frameN  # exact frame index
            T5Q2R.tStart = t  # local t and not account for scr refresh
            T5Q2R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5Q2R, 'tStartRefresh')  # time at next scr refresh
            T5Q2R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T5Q2R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T5Q2R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T5Q2R.status == STARTED and not waitOnFlip:
            theseKeys = T5Q2R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T5Q2R_allKeys.extend(theseKeys)
            if len(_T5Q2R_allKeys):
                T5Q2R.keys = _T5Q2R_allKeys[-1].name  # just the last key pressed
                T5Q2R.rt = _T5Q2R_allKeys[-1].rt
                # was this correct?
                if (T5Q2R.keys == str(CorrT5Q2)) or (T5Q2R.keys == CorrT5Q2):
                    T5Q2R.corr = 1
                else:
                    T5Q2R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T5Q2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T5Q2"-------
    for thisComponent in T5Q2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T5I2.started', T5I2.tStartRefresh)
    trials.addData('T5I2.stopped', T5I2.tStopRefresh)
    # check responses
    if T5Q2R.keys in ['', [], None]:  # No response was made
        T5Q2R.keys = None
        # was no response the correct answer?!
        if str(CorrT5Q2).lower() == 'none':
           T5Q2R.corr = 1;  # correct non-response
        else:
           T5Q2R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T5Q2R.keys',T5Q2R.keys)
    trials.addData('T5Q2R.corr', T5Q2R.corr)
    if T5Q2R.keys != None:  # we had a response
        trials.addData('T5Q2R.rt', T5Q2R.rt)
    trials.addData('T5Q2R.started', T5Q2R.tStartRefresh)
    trials.addData('T5Q2R.stopped', T5Q2R.tStopRefresh)
    # the Routine "T5Q2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T5Q3"-------
    continueRoutine = True
    # update component parameters for each repeat
    T5I3.setImage(T5Q3)
    T5Q3R.keys = []
    T5Q3R.rt = []
    _T5Q3R_allKeys = []
    # keep track of which components have finished
    T5Q3Components = [T5I3, T5Q3R]
    for thisComponent in T5Q3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T5Q3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T5Q3"-------
    while continueRoutine:
        # get current time
        t = T5Q3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T5Q3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T5I3* updates
        if T5I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5I3.frameNStart = frameN  # exact frame index
            T5I3.tStart = t  # local t and not account for scr refresh
            T5I3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5I3, 'tStartRefresh')  # time at next scr refresh
            T5I3.setAutoDraw(True)
        
        # *T5Q3R* updates
        waitOnFlip = False
        if T5Q3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5Q3R.frameNStart = frameN  # exact frame index
            T5Q3R.tStart = t  # local t and not account for scr refresh
            T5Q3R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5Q3R, 'tStartRefresh')  # time at next scr refresh
            T5Q3R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T5Q3R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T5Q3R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T5Q3R.status == STARTED and not waitOnFlip:
            theseKeys = T5Q3R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T5Q3R_allKeys.extend(theseKeys)
            if len(_T5Q3R_allKeys):
                T5Q3R.keys = _T5Q3R_allKeys[-1].name  # just the last key pressed
                T5Q3R.rt = _T5Q3R_allKeys[-1].rt
                # was this correct?
                if (T5Q3R.keys == str(CorrT5Q3)) or (T5Q3R.keys == CorrT5Q3):
                    T5Q3R.corr = 1
                else:
                    T5Q3R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T5Q3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T5Q3"-------
    for thisComponent in T5Q3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T5I3.started', T5I3.tStartRefresh)
    trials.addData('T5I3.stopped', T5I3.tStopRefresh)
    # check responses
    if T5Q3R.keys in ['', [], None]:  # No response was made
        T5Q3R.keys = None
        # was no response the correct answer?!
        if str(CorrT5Q3).lower() == 'none':
           T5Q3R.corr = 1;  # correct non-response
        else:
           T5Q3R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T5Q3R.keys',T5Q3R.keys)
    trials.addData('T5Q3R.corr', T5Q3R.corr)
    if T5Q3R.keys != None:  # we had a response
        trials.addData('T5Q3R.rt', T5Q3R.rt)
    trials.addData('T5Q3R.started', T5Q3R.tStartRefresh)
    trials.addData('T5Q3R.stopped', T5Q3R.tStopRefresh)
    # the Routine "T5Q3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T5Q4"-------
    continueRoutine = True
    # update component parameters for each repeat
    T5I4.setImage(T5Q4)
    T5Q4R.keys = []
    T5Q4R.rt = []
    _T5Q4R_allKeys = []
    # keep track of which components have finished
    T5Q4Components = [T5I4, T5Q4R]
    for thisComponent in T5Q4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T5Q4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T5Q4"-------
    while continueRoutine:
        # get current time
        t = T5Q4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T5Q4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T5I4* updates
        if T5I4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5I4.frameNStart = frameN  # exact frame index
            T5I4.tStart = t  # local t and not account for scr refresh
            T5I4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5I4, 'tStartRefresh')  # time at next scr refresh
            T5I4.setAutoDraw(True)
        
        # *T5Q4R* updates
        waitOnFlip = False
        if T5Q4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5Q4R.frameNStart = frameN  # exact frame index
            T5Q4R.tStart = t  # local t and not account for scr refresh
            T5Q4R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5Q4R, 'tStartRefresh')  # time at next scr refresh
            T5Q4R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T5Q4R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T5Q4R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T5Q4R.status == STARTED and not waitOnFlip:
            theseKeys = T5Q4R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T5Q4R_allKeys.extend(theseKeys)
            if len(_T5Q4R_allKeys):
                T5Q4R.keys = _T5Q4R_allKeys[-1].name  # just the last key pressed
                T5Q4R.rt = _T5Q4R_allKeys[-1].rt
                # was this correct?
                if (T5Q4R.keys == str(CorrT5Q4)) or (T5Q4R.keys == CorrT5Q4):
                    T5Q4R.corr = 1
                else:
                    T5Q4R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T5Q4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T5Q4"-------
    for thisComponent in T5Q4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T5I4.started', T5I4.tStartRefresh)
    trials.addData('T5I4.stopped', T5I4.tStopRefresh)
    # check responses
    if T5Q4R.keys in ['', [], None]:  # No response was made
        T5Q4R.keys = None
        # was no response the correct answer?!
        if str(CorrT5Q4).lower() == 'none':
           T5Q4R.corr = 1;  # correct non-response
        else:
           T5Q4R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T5Q4R.keys',T5Q4R.keys)
    trials.addData('T5Q4R.corr', T5Q4R.corr)
    if T5Q4R.keys != None:  # we had a response
        trials.addData('T5Q4R.rt', T5Q4R.rt)
    trials.addData('T5Q4R.started', T5Q4R.tStartRefresh)
    trials.addData('T5Q4R.stopped', T5Q4R.tStopRefresh)
    # the Routine "T5Q4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T5Q5"-------
    continueRoutine = True
    # update component parameters for each repeat
    T5I5.setImage(T5Q5)
    T5Q5R.keys = []
    T5Q5R.rt = []
    _T5Q5R_allKeys = []
    # keep track of which components have finished
    T5Q5Components = [T5I5, T5Q5R]
    for thisComponent in T5Q5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T5Q5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T5Q5"-------
    while continueRoutine:
        # get current time
        t = T5Q5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T5Q5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T5I5* updates
        if T5I5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5I5.frameNStart = frameN  # exact frame index
            T5I5.tStart = t  # local t and not account for scr refresh
            T5I5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5I5, 'tStartRefresh')  # time at next scr refresh
            T5I5.setAutoDraw(True)
        
        # *T5Q5R* updates
        waitOnFlip = False
        if T5Q5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5Q5R.frameNStart = frameN  # exact frame index
            T5Q5R.tStart = t  # local t and not account for scr refresh
            T5Q5R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5Q5R, 'tStartRefresh')  # time at next scr refresh
            T5Q5R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T5Q5R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T5Q5R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T5Q5R.status == STARTED and not waitOnFlip:
            theseKeys = T5Q5R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T5Q5R_allKeys.extend(theseKeys)
            if len(_T5Q5R_allKeys):
                T5Q5R.keys = _T5Q5R_allKeys[-1].name  # just the last key pressed
                T5Q5R.rt = _T5Q5R_allKeys[-1].rt
                # was this correct?
                if (T5Q5R.keys == str(CorrT5Q5)) or (T5Q5R.keys == CorrT5Q5):
                    T5Q5R.corr = 1
                else:
                    T5Q5R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T5Q5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T5Q5"-------
    for thisComponent in T5Q5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T5I5.started', T5I5.tStartRefresh)
    trials.addData('T5I5.stopped', T5I5.tStopRefresh)
    # check responses
    if T5Q5R.keys in ['', [], None]:  # No response was made
        T5Q5R.keys = None
        # was no response the correct answer?!
        if str(CorrT5Q5).lower() == 'none':
           T5Q5R.corr = 1;  # correct non-response
        else:
           T5Q5R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T5Q5R.keys',T5Q5R.keys)
    trials.addData('T5Q5R.corr', T5Q5R.corr)
    if T5Q5R.keys != None:  # we had a response
        trials.addData('T5Q5R.rt', T5Q5R.rt)
    trials.addData('T5Q5R.started', T5Q5R.tStartRefresh)
    trials.addData('T5Q5R.stopped', T5Q5R.tStopRefresh)
    # the Routine "T5Q5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T5Q6"-------
    continueRoutine = True
    # update component parameters for each repeat
    T5I6.setImage(T5Q6)
    T5Q6R.keys = []
    T5Q6R.rt = []
    _T5Q6R_allKeys = []
    # keep track of which components have finished
    T5Q6Components = [T5I6, T5Q6R]
    for thisComponent in T5Q6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T5Q6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T5Q6"-------
    while continueRoutine:
        # get current time
        t = T5Q6Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T5Q6Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T5I6* updates
        if T5I6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5I6.frameNStart = frameN  # exact frame index
            T5I6.tStart = t  # local t and not account for scr refresh
            T5I6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5I6, 'tStartRefresh')  # time at next scr refresh
            T5I6.setAutoDraw(True)
        
        # *T5Q6R* updates
        waitOnFlip = False
        if T5Q6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5Q6R.frameNStart = frameN  # exact frame index
            T5Q6R.tStart = t  # local t and not account for scr refresh
            T5Q6R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5Q6R, 'tStartRefresh')  # time at next scr refresh
            T5Q6R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T5Q6R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T5Q6R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T5Q6R.status == STARTED and not waitOnFlip:
            theseKeys = T5Q6R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T5Q6R_allKeys.extend(theseKeys)
            if len(_T5Q6R_allKeys):
                T5Q6R.keys = _T5Q6R_allKeys[-1].name  # just the last key pressed
                T5Q6R.rt = _T5Q6R_allKeys[-1].rt
                # was this correct?
                if (T5Q6R.keys == str(CorrT5Q6)) or (T5Q6R.keys == CorrT5Q6):
                    T5Q6R.corr = 1
                else:
                    T5Q6R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T5Q6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T5Q6"-------
    for thisComponent in T5Q6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T5I6.started', T5I6.tStartRefresh)
    trials.addData('T5I6.stopped', T5I6.tStopRefresh)
    # check responses
    if T5Q6R.keys in ['', [], None]:  # No response was made
        T5Q6R.keys = None
        # was no response the correct answer?!
        if str(CorrT5Q6).lower() == 'none':
           T5Q6R.corr = 1;  # correct non-response
        else:
           T5Q6R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T5Q6R.keys',T5Q6R.keys)
    trials.addData('T5Q6R.corr', T5Q6R.corr)
    if T5Q6R.keys != None:  # we had a response
        trials.addData('T5Q6R.rt', T5Q6R.rt)
    trials.addData('T5Q6R.started', T5Q6R.tStartRefresh)
    trials.addData('T5Q6R.stopped', T5Q6R.tStopRefresh)
    # the Routine "T5Q6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T5Q7"-------
    continueRoutine = True
    # update component parameters for each repeat
    T5I7.setImage(T5Q7)
    T5Q7R.keys = []
    T5Q7R.rt = []
    _T5Q7R_allKeys = []
    # keep track of which components have finished
    T5Q7Components = [T5I7, T5Q7R]
    for thisComponent in T5Q7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T5Q7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T5Q7"-------
    while continueRoutine:
        # get current time
        t = T5Q7Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T5Q7Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T5I7* updates
        if T5I7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5I7.frameNStart = frameN  # exact frame index
            T5I7.tStart = t  # local t and not account for scr refresh
            T5I7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5I7, 'tStartRefresh')  # time at next scr refresh
            T5I7.setAutoDraw(True)
        
        # *T5Q7R* updates
        waitOnFlip = False
        if T5Q7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5Q7R.frameNStart = frameN  # exact frame index
            T5Q7R.tStart = t  # local t and not account for scr refresh
            T5Q7R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5Q7R, 'tStartRefresh')  # time at next scr refresh
            T5Q7R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T5Q7R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T5Q7R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T5Q7R.status == STARTED and not waitOnFlip:
            theseKeys = T5Q7R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T5Q7R_allKeys.extend(theseKeys)
            if len(_T5Q7R_allKeys):
                T5Q7R.keys = _T5Q7R_allKeys[-1].name  # just the last key pressed
                T5Q7R.rt = _T5Q7R_allKeys[-1].rt
                # was this correct?
                if (T5Q7R.keys == str(CorrT5Q7)) or (T5Q7R.keys == CorrT5Q7):
                    T5Q7R.corr = 1
                else:
                    T5Q7R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T5Q7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T5Q7"-------
    for thisComponent in T5Q7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T5I7.started', T5I7.tStartRefresh)
    trials.addData('T5I7.stopped', T5I7.tStopRefresh)
    # check responses
    if T5Q7R.keys in ['', [], None]:  # No response was made
        T5Q7R.keys = None
        # was no response the correct answer?!
        if str(CorrT5Q7).lower() == 'none':
           T5Q7R.corr = 1;  # correct non-response
        else:
           T5Q7R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T5Q7R.keys',T5Q7R.keys)
    trials.addData('T5Q7R.corr', T5Q7R.corr)
    if T5Q7R.keys != None:  # we had a response
        trials.addData('T5Q7R.rt', T5Q7R.rt)
    trials.addData('T5Q7R.started', T5Q7R.tStartRefresh)
    trials.addData('T5Q7R.stopped', T5Q7R.tStopRefresh)
    # the Routine "T5Q7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T5Q8"-------
    continueRoutine = True
    # update component parameters for each repeat
    T5I8.setImage(T5Q8)
    T5Q8R.keys = []
    T5Q8R.rt = []
    _T5Q8R_allKeys = []
    # keep track of which components have finished
    T5Q8Components = [T5I8, T5Q8R]
    for thisComponent in T5Q8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T5Q8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T5Q8"-------
    while continueRoutine:
        # get current time
        t = T5Q8Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T5Q8Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T5I8* updates
        if T5I8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5I8.frameNStart = frameN  # exact frame index
            T5I8.tStart = t  # local t and not account for scr refresh
            T5I8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5I8, 'tStartRefresh')  # time at next scr refresh
            T5I8.setAutoDraw(True)
        
        # *T5Q8R* updates
        waitOnFlip = False
        if T5Q8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5Q8R.frameNStart = frameN  # exact frame index
            T5Q8R.tStart = t  # local t and not account for scr refresh
            T5Q8R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5Q8R, 'tStartRefresh')  # time at next scr refresh
            T5Q8R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T5Q8R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T5Q8R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T5Q8R.status == STARTED and not waitOnFlip:
            theseKeys = T5Q8R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T5Q8R_allKeys.extend(theseKeys)
            if len(_T5Q8R_allKeys):
                T5Q8R.keys = _T5Q8R_allKeys[-1].name  # just the last key pressed
                T5Q8R.rt = _T5Q8R_allKeys[-1].rt
                # was this correct?
                if (T5Q8R.keys == str(CorrT5Q8)) or (T5Q8R.keys == CorrT5Q8):
                    T5Q8R.corr = 1
                else:
                    T5Q8R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T5Q8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T5Q8"-------
    for thisComponent in T5Q8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T5I8.started', T5I8.tStartRefresh)
    trials.addData('T5I8.stopped', T5I8.tStopRefresh)
    # check responses
    if T5Q8R.keys in ['', [], None]:  # No response was made
        T5Q8R.keys = None
        # was no response the correct answer?!
        if str(CorrT5Q8).lower() == 'none':
           T5Q8R.corr = 1;  # correct non-response
        else:
           T5Q8R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T5Q8R.keys',T5Q8R.keys)
    trials.addData('T5Q8R.corr', T5Q8R.corr)
    if T5Q8R.keys != None:  # we had a response
        trials.addData('T5Q8R.rt', T5Q8R.rt)
    trials.addData('T5Q8R.started', T5Q8R.tStartRefresh)
    trials.addData('T5Q8R.stopped', T5Q8R.tStopRefresh)
    # the Routine "T5Q8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T5Q9"-------
    continueRoutine = True
    # update component parameters for each repeat
    T5I9.setImage(T5Q9)
    T5Q9R.keys = []
    T5Q9R.rt = []
    _T5Q9R_allKeys = []
    # keep track of which components have finished
    T5Q9Components = [T5I9, T5Q9R]
    for thisComponent in T5Q9Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T5Q9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T5Q9"-------
    while continueRoutine:
        # get current time
        t = T5Q9Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T5Q9Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T5I9* updates
        if T5I9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5I9.frameNStart = frameN  # exact frame index
            T5I9.tStart = t  # local t and not account for scr refresh
            T5I9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5I9, 'tStartRefresh')  # time at next scr refresh
            T5I9.setAutoDraw(True)
        
        # *T5Q9R* updates
        waitOnFlip = False
        if T5Q9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5Q9R.frameNStart = frameN  # exact frame index
            T5Q9R.tStart = t  # local t and not account for scr refresh
            T5Q9R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5Q9R, 'tStartRefresh')  # time at next scr refresh
            T5Q9R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T5Q9R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T5Q9R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T5Q9R.status == STARTED and not waitOnFlip:
            theseKeys = T5Q9R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T5Q9R_allKeys.extend(theseKeys)
            if len(_T5Q9R_allKeys):
                T5Q9R.keys = _T5Q9R_allKeys[-1].name  # just the last key pressed
                T5Q9R.rt = _T5Q9R_allKeys[-1].rt
                # was this correct?
                if (T5Q9R.keys == str(CorrT5Q9)) or (T5Q9R.keys == CorrT5Q9):
                    T5Q9R.corr = 1
                else:
                    T5Q9R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T5Q9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T5Q9"-------
    for thisComponent in T5Q9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T5I9.started', T5I9.tStartRefresh)
    trials.addData('T5I9.stopped', T5I9.tStopRefresh)
    # check responses
    if T5Q9R.keys in ['', [], None]:  # No response was made
        T5Q9R.keys = None
        # was no response the correct answer?!
        if str(CorrT5Q9).lower() == 'none':
           T5Q9R.corr = 1;  # correct non-response
        else:
           T5Q9R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T5Q9R.keys',T5Q9R.keys)
    trials.addData('T5Q9R.corr', T5Q9R.corr)
    if T5Q9R.keys != None:  # we had a response
        trials.addData('T5Q9R.rt', T5Q9R.rt)
    trials.addData('T5Q9R.started', T5Q9R.tStartRefresh)
    trials.addData('T5Q9R.stopped', T5Q9R.tStopRefresh)
    # the Routine "T5Q9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T5Q10"-------
    continueRoutine = True
    # update component parameters for each repeat
    T5I10.setImage(T5Q10)
    T5Q10R.keys = []
    T5Q10R.rt = []
    _T5Q10R_allKeys = []
    # keep track of which components have finished
    T5Q10Components = [T5I10, T5Q10R]
    for thisComponent in T5Q10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T5Q10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T5Q10"-------
    while continueRoutine:
        # get current time
        t = T5Q10Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T5Q10Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T5I10* updates
        if T5I10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5I10.frameNStart = frameN  # exact frame index
            T5I10.tStart = t  # local t and not account for scr refresh
            T5I10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5I10, 'tStartRefresh')  # time at next scr refresh
            T5I10.setAutoDraw(True)
        
        # *T5Q10R* updates
        waitOnFlip = False
        if T5Q10R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T5Q10R.frameNStart = frameN  # exact frame index
            T5Q10R.tStart = t  # local t and not account for scr refresh
            T5Q10R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T5Q10R, 'tStartRefresh')  # time at next scr refresh
            T5Q10R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T5Q10R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T5Q10R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T5Q10R.status == STARTED and not waitOnFlip:
            theseKeys = T5Q10R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T5Q10R_allKeys.extend(theseKeys)
            if len(_T5Q10R_allKeys):
                T5Q10R.keys = _T5Q10R_allKeys[-1].name  # just the last key pressed
                T5Q10R.rt = _T5Q10R_allKeys[-1].rt
                # was this correct?
                if (T5Q10R.keys == str(CorrT5Q10)) or (T5Q10R.keys == CorrT5Q10):
                    T5Q10R.corr = 1
                else:
                    T5Q10R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T5Q10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T5Q10"-------
    for thisComponent in T5Q10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T5I10.started', T5I10.tStartRefresh)
    trials.addData('T5I10.stopped', T5I10.tStopRefresh)
    # check responses
    if T5Q10R.keys in ['', [], None]:  # No response was made
        T5Q10R.keys = None
        # was no response the correct answer?!
        if str(CorrT5Q10).lower() == 'none':
           T5Q10R.corr = 1;  # correct non-response
        else:
           T5Q10R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T5Q10R.keys',T5Q10R.keys)
    trials.addData('T5Q10R.corr', T5Q10R.corr)
    if T5Q10R.keys != None:  # we had a response
        trials.addData('T5Q10R.rt', T5Q10R.rt)
    trials.addData('T5Q10R.started', T5Q10R.tStartRefresh)
    trials.addData('T5Q10R.stopped', T5Q10R.tStopRefresh)
    # the Routine "T5Q10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Trial_Break"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    Trial_BreakComponents = [Break_message, key_resp_4]
    for thisComponent in Trial_BreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Trial_BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial_Break"-------
    while continueRoutine:
        # get current time
        t = Trial_BreakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Trial_BreakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Break_message* updates
        if Break_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_message.frameNStart = frameN  # exact frame index
            Break_message.tStart = t  # local t and not account for scr refresh
            Break_message.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_message, 'tStartRefresh')  # time at next scr refresh
            Break_message.setAutoDraw(True)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Trial_BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Trial_Break"-------
    for thisComponent in Trial_BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Break_message.started', Break_message.tStartRefresh)
    trials.addData('Break_message.stopped', Break_message.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Trial_Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T6A"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_6.setSound(T6A, hamming=True)
    sound_6.setVolume(1.0, log=False)
    T6A = cond_set[cond_set['Cond'] == cond]['T6A'].values[0]
    cond_speed = re.search(r'(\d+\.\d+)x', T6A).group(1)
    cond_noise = re.search(r'(\w+)_Audio', T6A).group(1)
    send_trigger(cond_speed, cond_noise)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    T6AComponents = [sound_6, image_6, key_resp_7]
    for thisComponent in T6AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T6AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T6A"-------
    while continueRoutine:
        # get current time
        t = T6AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T6AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_6
        if sound_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_6.frameNStart = frameN  # exact frame index
            sound_6.tStart = t  # local t and not account for scr refresh
            sound_6.tStartRefresh = tThisFlipGlobal  # on global time
            sound_6.play()  # start the sound (it finishes automatically)
        
        # *image_6* updates
        if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_6.frameNStart = frameN  # exact frame index
            image_6.tStart = t  # local t and not account for scr refresh
            image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
            image_6.setAutoDraw(True)
        if sound_6.status == FINISHED:
            continueRoutine = False
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['z'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T6AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T6A"-------
    for thisComponent in T6AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_6.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_6.started', sound_6.tStart)
    trials.addData('sound_6.stopped', sound_6.tStop)
    trials.addData('image_6.started', image_6.tStartRefresh)
    trials.addData('image_6.stopped', image_6.tStopRefresh)
    ser.write((200).to_bytes(1, 'big'))
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    trials.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        trials.addData('key_resp_7.rt', key_resp_7.rt)
    trials.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    trials.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "T6A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pre_assement_inst"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    Pre_assement_instComponents = [text_5, key_resp_5]
    for thisComponent in Pre_assement_instComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pre_assement_instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pre_assement_inst"-------
    while continueRoutine:
        # get current time
        t = Pre_assement_instClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pre_assement_instClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pre_assement_instComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pre_assement_inst"-------
    for thisComponent in Pre_assement_instComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_5.started', text_5.tStartRefresh)
    trials.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials.addData('key_resp_5.rt', key_resp_5.rt)
    trials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    trials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "Pre_assement_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T6Q1"-------
    continueRoutine = True
    # update component parameters for each repeat
    T6I1.setImage(T6Q1)
    T6Q1R.keys = []
    T6Q1R.rt = []
    _T6Q1R_allKeys = []
    # keep track of which components have finished
    T6Q1Components = [T6I1, T6Q1R]
    for thisComponent in T6Q1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T6Q1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T6Q1"-------
    while continueRoutine:
        # get current time
        t = T6Q1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T6Q1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T6I1* updates
        if T6I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6I1.frameNStart = frameN  # exact frame index
            T6I1.tStart = t  # local t and not account for scr refresh
            T6I1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6I1, 'tStartRefresh')  # time at next scr refresh
            T6I1.setAutoDraw(True)
        
        # *T6Q1R* updates
        waitOnFlip = False
        if T6Q1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6Q1R.frameNStart = frameN  # exact frame index
            T6Q1R.tStart = t  # local t and not account for scr refresh
            T6Q1R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6Q1R, 'tStartRefresh')  # time at next scr refresh
            T6Q1R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T6Q1R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T6Q1R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T6Q1R.status == STARTED and not waitOnFlip:
            theseKeys = T6Q1R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T6Q1R_allKeys.extend(theseKeys)
            if len(_T6Q1R_allKeys):
                T6Q1R.keys = _T6Q1R_allKeys[-1].name  # just the last key pressed
                T6Q1R.rt = _T6Q1R_allKeys[-1].rt
                # was this correct?
                if (T6Q1R.keys == str(CorrT6Q1)) or (T6Q1R.keys == CorrT6Q1):
                    T6Q1R.corr = 1
                else:
                    T6Q1R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T6Q1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T6Q1"-------
    for thisComponent in T6Q1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T6I1.started', T6I1.tStartRefresh)
    trials.addData('T6I1.stopped', T6I1.tStopRefresh)
    # check responses
    if T6Q1R.keys in ['', [], None]:  # No response was made
        T6Q1R.keys = None
        # was no response the correct answer?!
        if str(CorrT6Q1).lower() == 'none':
           T6Q1R.corr = 1;  # correct non-response
        else:
           T6Q1R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T6Q1R.keys',T6Q1R.keys)
    trials.addData('T6Q1R.corr', T6Q1R.corr)
    if T6Q1R.keys != None:  # we had a response
        trials.addData('T6Q1R.rt', T6Q1R.rt)
    trials.addData('T6Q1R.started', T6Q1R.tStartRefresh)
    trials.addData('T6Q1R.stopped', T6Q1R.tStopRefresh)
    # the Routine "T6Q1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T6Q2"-------
    continueRoutine = True
    # update component parameters for each repeat
    T6I2.setImage(T6Q2)
    T6Q2R.keys = []
    T6Q2R.rt = []
    _T6Q2R_allKeys = []
    # keep track of which components have finished
    T6Q2Components = [T6I2, T6Q2R]
    for thisComponent in T6Q2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T6Q2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T6Q2"-------
    while continueRoutine:
        # get current time
        t = T6Q2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T6Q2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T6I2* updates
        if T6I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6I2.frameNStart = frameN  # exact frame index
            T6I2.tStart = t  # local t and not account for scr refresh
            T6I2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6I2, 'tStartRefresh')  # time at next scr refresh
            T6I2.setAutoDraw(True)
        
        # *T6Q2R* updates
        waitOnFlip = False
        if T6Q2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6Q2R.frameNStart = frameN  # exact frame index
            T6Q2R.tStart = t  # local t and not account for scr refresh
            T6Q2R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6Q2R, 'tStartRefresh')  # time at next scr refresh
            T6Q2R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T6Q2R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T6Q2R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T6Q2R.status == STARTED and not waitOnFlip:
            theseKeys = T6Q2R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T6Q2R_allKeys.extend(theseKeys)
            if len(_T6Q2R_allKeys):
                T6Q2R.keys = _T6Q2R_allKeys[-1].name  # just the last key pressed
                T6Q2R.rt = _T6Q2R_allKeys[-1].rt
                # was this correct?
                if (T6Q2R.keys == str(CorrT6Q2)) or (T6Q2R.keys == CorrT6Q2):
                    T6Q2R.corr = 1
                else:
                    T6Q2R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T6Q2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T6Q2"-------
    for thisComponent in T6Q2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T6I2.started', T6I2.tStartRefresh)
    trials.addData('T6I2.stopped', T6I2.tStopRefresh)
    # check responses
    if T6Q2R.keys in ['', [], None]:  # No response was made
        T6Q2R.keys = None
        # was no response the correct answer?!
        if str(CorrT6Q2).lower() == 'none':
           T6Q2R.corr = 1;  # correct non-response
        else:
           T6Q2R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T6Q2R.keys',T6Q2R.keys)
    trials.addData('T6Q2R.corr', T6Q2R.corr)
    if T6Q2R.keys != None:  # we had a response
        trials.addData('T6Q2R.rt', T6Q2R.rt)
    trials.addData('T6Q2R.started', T6Q2R.tStartRefresh)
    trials.addData('T6Q2R.stopped', T6Q2R.tStopRefresh)
    # the Routine "T6Q2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T6Q3"-------
    continueRoutine = True
    # update component parameters for each repeat
    T6I3.setImage(T6Q3)
    T6Q3R.keys = []
    T6Q3R.rt = []
    _T6Q3R_allKeys = []
    # keep track of which components have finished
    T6Q3Components = [T6I3, T6Q3R]
    for thisComponent in T6Q3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T6Q3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T6Q3"-------
    while continueRoutine:
        # get current time
        t = T6Q3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T6Q3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T6I3* updates
        if T6I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6I3.frameNStart = frameN  # exact frame index
            T6I3.tStart = t  # local t and not account for scr refresh
            T6I3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6I3, 'tStartRefresh')  # time at next scr refresh
            T6I3.setAutoDraw(True)
        
        # *T6Q3R* updates
        waitOnFlip = False
        if T6Q3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6Q3R.frameNStart = frameN  # exact frame index
            T6Q3R.tStart = t  # local t and not account for scr refresh
            T6Q3R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6Q3R, 'tStartRefresh')  # time at next scr refresh
            T6Q3R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T6Q3R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T6Q3R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T6Q3R.status == STARTED and not waitOnFlip:
            theseKeys = T6Q3R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T6Q3R_allKeys.extend(theseKeys)
            if len(_T6Q3R_allKeys):
                T6Q3R.keys = _T6Q3R_allKeys[-1].name  # just the last key pressed
                T6Q3R.rt = _T6Q3R_allKeys[-1].rt
                # was this correct?
                if (T6Q3R.keys == str(CorrT6Q3)) or (T6Q3R.keys == CorrT6Q3):
                    T6Q3R.corr = 1
                else:
                    T6Q3R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T6Q3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T6Q3"-------
    for thisComponent in T6Q3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T6I3.started', T6I3.tStartRefresh)
    trials.addData('T6I3.stopped', T6I3.tStopRefresh)
    # check responses
    if T6Q3R.keys in ['', [], None]:  # No response was made
        T6Q3R.keys = None
        # was no response the correct answer?!
        if str(CorrT6Q3).lower() == 'none':
           T6Q3R.corr = 1;  # correct non-response
        else:
           T6Q3R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T6Q3R.keys',T6Q3R.keys)
    trials.addData('T6Q3R.corr', T6Q3R.corr)
    if T6Q3R.keys != None:  # we had a response
        trials.addData('T6Q3R.rt', T6Q3R.rt)
    trials.addData('T6Q3R.started', T6Q3R.tStartRefresh)
    trials.addData('T6Q3R.stopped', T6Q3R.tStopRefresh)
    # the Routine "T6Q3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T6Q4"-------
    continueRoutine = True
    # update component parameters for each repeat
    T6I4.setImage(T6Q4)
    T6Q4R.keys = []
    T6Q4R.rt = []
    _T6Q4R_allKeys = []
    # keep track of which components have finished
    T6Q4Components = [T6I4, T6Q4R]
    for thisComponent in T6Q4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T6Q4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T6Q4"-------
    while continueRoutine:
        # get current time
        t = T6Q4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T6Q4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T6I4* updates
        if T6I4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6I4.frameNStart = frameN  # exact frame index
            T6I4.tStart = t  # local t and not account for scr refresh
            T6I4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6I4, 'tStartRefresh')  # time at next scr refresh
            T6I4.setAutoDraw(True)
        
        # *T6Q4R* updates
        waitOnFlip = False
        if T6Q4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6Q4R.frameNStart = frameN  # exact frame index
            T6Q4R.tStart = t  # local t and not account for scr refresh
            T6Q4R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6Q4R, 'tStartRefresh')  # time at next scr refresh
            T6Q4R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T6Q4R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T6Q4R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T6Q4R.status == STARTED and not waitOnFlip:
            theseKeys = T6Q4R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T6Q4R_allKeys.extend(theseKeys)
            if len(_T6Q4R_allKeys):
                T6Q4R.keys = _T6Q4R_allKeys[-1].name  # just the last key pressed
                T6Q4R.rt = _T6Q4R_allKeys[-1].rt
                # was this correct?
                if (T6Q4R.keys == str(CorrT6Q4)) or (T6Q4R.keys == CorrT6Q4):
                    T6Q4R.corr = 1
                else:
                    T6Q4R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T6Q4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T6Q4"-------
    for thisComponent in T6Q4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T6I4.started', T6I4.tStartRefresh)
    trials.addData('T6I4.stopped', T6I4.tStopRefresh)
    # check responses
    if T6Q4R.keys in ['', [], None]:  # No response was made
        T6Q4R.keys = None
        # was no response the correct answer?!
        if str(CorrT6Q4).lower() == 'none':
           T6Q4R.corr = 1;  # correct non-response
        else:
           T6Q4R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T6Q4R.keys',T6Q4R.keys)
    trials.addData('T6Q4R.corr', T6Q4R.corr)
    if T6Q4R.keys != None:  # we had a response
        trials.addData('T6Q4R.rt', T6Q4R.rt)
    trials.addData('T6Q4R.started', T6Q4R.tStartRefresh)
    trials.addData('T6Q4R.stopped', T6Q4R.tStopRefresh)
    # the Routine "T6Q4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T6Q5"-------
    continueRoutine = True
    # update component parameters for each repeat
    T6I5.setImage(T6Q5)
    T6Q5R.keys = []
    T6Q5R.rt = []
    _T6Q5R_allKeys = []
    # keep track of which components have finished
    T6Q5Components = [T6I5, T6Q5R]
    for thisComponent in T6Q5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T6Q5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T6Q5"-------
    while continueRoutine:
        # get current time
        t = T6Q5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T6Q5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T6I5* updates
        if T6I5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6I5.frameNStart = frameN  # exact frame index
            T6I5.tStart = t  # local t and not account for scr refresh
            T6I5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6I5, 'tStartRefresh')  # time at next scr refresh
            T6I5.setAutoDraw(True)
        
        # *T6Q5R* updates
        waitOnFlip = False
        if T6Q5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6Q5R.frameNStart = frameN  # exact frame index
            T6Q5R.tStart = t  # local t and not account for scr refresh
            T6Q5R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6Q5R, 'tStartRefresh')  # time at next scr refresh
            T6Q5R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T6Q5R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T6Q5R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T6Q5R.status == STARTED and not waitOnFlip:
            theseKeys = T6Q5R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T6Q5R_allKeys.extend(theseKeys)
            if len(_T6Q5R_allKeys):
                T6Q5R.keys = _T6Q5R_allKeys[-1].name  # just the last key pressed
                T6Q5R.rt = _T6Q5R_allKeys[-1].rt
                # was this correct?
                if (T6Q5R.keys == str(CorrT6Q5)) or (T6Q5R.keys == CorrT6Q5):
                    T6Q5R.corr = 1
                else:
                    T6Q5R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T6Q5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T6Q5"-------
    for thisComponent in T6Q5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T6I5.started', T6I5.tStartRefresh)
    trials.addData('T6I5.stopped', T6I5.tStopRefresh)
    # check responses
    if T6Q5R.keys in ['', [], None]:  # No response was made
        T6Q5R.keys = None
        # was no response the correct answer?!
        if str(CorrT6Q5).lower() == 'none':
           T6Q5R.corr = 1;  # correct non-response
        else:
           T6Q5R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T6Q5R.keys',T6Q5R.keys)
    trials.addData('T6Q5R.corr', T6Q5R.corr)
    if T6Q5R.keys != None:  # we had a response
        trials.addData('T6Q5R.rt', T6Q5R.rt)
    trials.addData('T6Q5R.started', T6Q5R.tStartRefresh)
    trials.addData('T6Q5R.stopped', T6Q5R.tStopRefresh)
    # the Routine "T6Q5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T6Q6"-------
    continueRoutine = True
    # update component parameters for each repeat
    T6I6.setImage(T6Q6)
    T6Q6R.keys = []
    T6Q6R.rt = []
    _T6Q6R_allKeys = []
    # keep track of which components have finished
    T6Q6Components = [T6I6, T6Q6R]
    for thisComponent in T6Q6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T6Q6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T6Q6"-------
    while continueRoutine:
        # get current time
        t = T6Q6Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T6Q6Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T6I6* updates
        if T6I6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6I6.frameNStart = frameN  # exact frame index
            T6I6.tStart = t  # local t and not account for scr refresh
            T6I6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6I6, 'tStartRefresh')  # time at next scr refresh
            T6I6.setAutoDraw(True)
        
        # *T6Q6R* updates
        waitOnFlip = False
        if T6Q6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6Q6R.frameNStart = frameN  # exact frame index
            T6Q6R.tStart = t  # local t and not account for scr refresh
            T6Q6R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6Q6R, 'tStartRefresh')  # time at next scr refresh
            T6Q6R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T6Q6R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T6Q6R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T6Q6R.status == STARTED and not waitOnFlip:
            theseKeys = T6Q6R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T6Q6R_allKeys.extend(theseKeys)
            if len(_T6Q6R_allKeys):
                T6Q6R.keys = _T6Q6R_allKeys[-1].name  # just the last key pressed
                T6Q6R.rt = _T6Q6R_allKeys[-1].rt
                # was this correct?
                if (T6Q6R.keys == str(CorrT6Q6)) or (T6Q6R.keys == CorrT6Q6):
                    T6Q6R.corr = 1
                else:
                    T6Q6R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T6Q6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T6Q6"-------
    for thisComponent in T6Q6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T6I6.started', T6I6.tStartRefresh)
    trials.addData('T6I6.stopped', T6I6.tStopRefresh)
    # check responses
    if T6Q6R.keys in ['', [], None]:  # No response was made
        T6Q6R.keys = None
        # was no response the correct answer?!
        if str(CorrT6Q6).lower() == 'none':
           T6Q6R.corr = 1;  # correct non-response
        else:
           T6Q6R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T6Q6R.keys',T6Q6R.keys)
    trials.addData('T6Q6R.corr', T6Q6R.corr)
    if T6Q6R.keys != None:  # we had a response
        trials.addData('T6Q6R.rt', T6Q6R.rt)
    trials.addData('T6Q6R.started', T6Q6R.tStartRefresh)
    trials.addData('T6Q6R.stopped', T6Q6R.tStopRefresh)
    # the Routine "T6Q6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T6Q7"-------
    continueRoutine = True
    # update component parameters for each repeat
    T6I7.setImage(T6Q7)
    T6Q7R.keys = []
    T6Q7R.rt = []
    _T6Q7R_allKeys = []
    # keep track of which components have finished
    T6Q7Components = [T6I7, T6Q7R]
    for thisComponent in T6Q7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T6Q7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T6Q7"-------
    while continueRoutine:
        # get current time
        t = T6Q7Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T6Q7Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T6I7* updates
        if T6I7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6I7.frameNStart = frameN  # exact frame index
            T6I7.tStart = t  # local t and not account for scr refresh
            T6I7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6I7, 'tStartRefresh')  # time at next scr refresh
            T6I7.setAutoDraw(True)
        
        # *T6Q7R* updates
        waitOnFlip = False
        if T6Q7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6Q7R.frameNStart = frameN  # exact frame index
            T6Q7R.tStart = t  # local t and not account for scr refresh
            T6Q7R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6Q7R, 'tStartRefresh')  # time at next scr refresh
            T6Q7R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T6Q7R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T6Q7R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T6Q7R.status == STARTED and not waitOnFlip:
            theseKeys = T6Q7R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T6Q7R_allKeys.extend(theseKeys)
            if len(_T6Q7R_allKeys):
                T6Q7R.keys = _T6Q7R_allKeys[-1].name  # just the last key pressed
                T6Q7R.rt = _T6Q7R_allKeys[-1].rt
                # was this correct?
                if (T6Q7R.keys == str(CorrT6Q7)) or (T6Q7R.keys == CorrT6Q7):
                    T6Q7R.corr = 1
                else:
                    T6Q7R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T6Q7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T6Q7"-------
    for thisComponent in T6Q7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T6I7.started', T6I7.tStartRefresh)
    trials.addData('T6I7.stopped', T6I7.tStopRefresh)
    # check responses
    if T6Q7R.keys in ['', [], None]:  # No response was made
        T6Q7R.keys = None
        # was no response the correct answer?!
        if str(CorrT6Q7).lower() == 'none':
           T6Q7R.corr = 1;  # correct non-response
        else:
           T6Q7R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T6Q7R.keys',T6Q7R.keys)
    trials.addData('T6Q7R.corr', T6Q7R.corr)
    if T6Q7R.keys != None:  # we had a response
        trials.addData('T6Q7R.rt', T6Q7R.rt)
    trials.addData('T6Q7R.started', T6Q7R.tStartRefresh)
    trials.addData('T6Q7R.stopped', T6Q7R.tStopRefresh)
    # the Routine "T6Q7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T6Q8"-------
    continueRoutine = True
    # update component parameters for each repeat
    T6I8.setImage(T6Q8)
    T6Q8R.keys = []
    T6Q8R.rt = []
    _T6Q8R_allKeys = []
    # keep track of which components have finished
    T6Q8Components = [T6I8, T6Q8R]
    for thisComponent in T6Q8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T6Q8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T6Q8"-------
    while continueRoutine:
        # get current time
        t = T6Q8Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T6Q8Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T6I8* updates
        if T6I8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6I8.frameNStart = frameN  # exact frame index
            T6I8.tStart = t  # local t and not account for scr refresh
            T6I8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6I8, 'tStartRefresh')  # time at next scr refresh
            T6I8.setAutoDraw(True)
        
        # *T6Q8R* updates
        waitOnFlip = False
        if T6Q8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6Q8R.frameNStart = frameN  # exact frame index
            T6Q8R.tStart = t  # local t and not account for scr refresh
            T6Q8R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6Q8R, 'tStartRefresh')  # time at next scr refresh
            T6Q8R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T6Q8R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T6Q8R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T6Q8R.status == STARTED and not waitOnFlip:
            theseKeys = T6Q8R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T6Q8R_allKeys.extend(theseKeys)
            if len(_T6Q8R_allKeys):
                T6Q8R.keys = _T6Q8R_allKeys[-1].name  # just the last key pressed
                T6Q8R.rt = _T6Q8R_allKeys[-1].rt
                # was this correct?
                if (T6Q8R.keys == str(CorrT6Q8)) or (T6Q8R.keys == CorrT6Q8):
                    T6Q8R.corr = 1
                else:
                    T6Q8R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T6Q8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T6Q8"-------
    for thisComponent in T6Q8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T6I8.started', T6I8.tStartRefresh)
    trials.addData('T6I8.stopped', T6I8.tStopRefresh)
    # check responses
    if T6Q8R.keys in ['', [], None]:  # No response was made
        T6Q8R.keys = None
        # was no response the correct answer?!
        if str(CorrT6Q8).lower() == 'none':
           T6Q8R.corr = 1;  # correct non-response
        else:
           T6Q8R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T6Q8R.keys',T6Q8R.keys)
    trials.addData('T6Q8R.corr', T6Q8R.corr)
    if T6Q8R.keys != None:  # we had a response
        trials.addData('T6Q8R.rt', T6Q8R.rt)
    trials.addData('T6Q8R.started', T6Q8R.tStartRefresh)
    trials.addData('T6Q8R.stopped', T6Q8R.tStopRefresh)
    # the Routine "T6Q8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T6Q9"-------
    continueRoutine = True
    # update component parameters for each repeat
    T6I9.setImage(T6Q9)
    T6Q9R.keys = []
    T6Q9R.rt = []
    _T6Q9R_allKeys = []
    # keep track of which components have finished
    T6Q9Components = [T6I9, T6Q9R]
    for thisComponent in T6Q9Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T6Q9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T6Q9"-------
    while continueRoutine:
        # get current time
        t = T6Q9Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T6Q9Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T6I9* updates
        if T6I9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6I9.frameNStart = frameN  # exact frame index
            T6I9.tStart = t  # local t and not account for scr refresh
            T6I9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6I9, 'tStartRefresh')  # time at next scr refresh
            T6I9.setAutoDraw(True)
        
        # *T6Q9R* updates
        waitOnFlip = False
        if T6Q9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6Q9R.frameNStart = frameN  # exact frame index
            T6Q9R.tStart = t  # local t and not account for scr refresh
            T6Q9R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6Q9R, 'tStartRefresh')  # time at next scr refresh
            T6Q9R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T6Q9R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T6Q9R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T6Q9R.status == STARTED and not waitOnFlip:
            theseKeys = T6Q9R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T6Q9R_allKeys.extend(theseKeys)
            if len(_T6Q9R_allKeys):
                T6Q9R.keys = _T6Q9R_allKeys[-1].name  # just the last key pressed
                T6Q9R.rt = _T6Q9R_allKeys[-1].rt
                # was this correct?
                if (T6Q9R.keys == str(CorrT6Q9)) or (T6Q9R.keys == CorrT6Q9):
                    T6Q9R.corr = 1
                else:
                    T6Q9R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T6Q9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T6Q9"-------
    for thisComponent in T6Q9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T6I9.started', T6I9.tStartRefresh)
    trials.addData('T6I9.stopped', T6I9.tStopRefresh)
    # check responses
    if T6Q9R.keys in ['', [], None]:  # No response was made
        T6Q9R.keys = None
        # was no response the correct answer?!
        if str(CorrT6Q9).lower() == 'none':
           T6Q9R.corr = 1;  # correct non-response
        else:
           T6Q9R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T6Q9R.keys',T6Q9R.keys)
    trials.addData('T6Q9R.corr', T6Q9R.corr)
    if T6Q9R.keys != None:  # we had a response
        trials.addData('T6Q9R.rt', T6Q9R.rt)
    trials.addData('T6Q9R.started', T6Q9R.tStartRefresh)
    trials.addData('T6Q9R.stopped', T6Q9R.tStopRefresh)
    # the Routine "T6Q9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "T6Q10"-------
    continueRoutine = True
    # update component parameters for each repeat
    T6I10.setImage(T6Q10)
    T6Q10R.keys = []
    T6Q10R.rt = []
    _T6Q10R_allKeys = []
    # keep track of which components have finished
    T6Q10Components = [T6I10, T6Q10R]
    for thisComponent in T6Q10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    T6Q10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "T6Q10"-------
    while continueRoutine:
        # get current time
        t = T6Q10Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=T6Q10Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *T6I10* updates
        if T6I10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6I10.frameNStart = frameN  # exact frame index
            T6I10.tStart = t  # local t and not account for scr refresh
            T6I10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6I10, 'tStartRefresh')  # time at next scr refresh
            T6I10.setAutoDraw(True)
        
        # *T6Q10R* updates
        waitOnFlip = False
        if T6Q10R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            T6Q10R.frameNStart = frameN  # exact frame index
            T6Q10R.tStart = t  # local t and not account for scr refresh
            T6Q10R.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(T6Q10R, 'tStartRefresh')  # time at next scr refresh
            T6Q10R.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(T6Q10R.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(T6Q10R.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if T6Q10R.status == STARTED and not waitOnFlip:
            theseKeys = T6Q10R.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _T6Q10R_allKeys.extend(theseKeys)
            if len(_T6Q10R_allKeys):
                T6Q10R.keys = _T6Q10R_allKeys[-1].name  # just the last key pressed
                T6Q10R.rt = _T6Q10R_allKeys[-1].rt
                # was this correct?
                if (T6Q10R.keys == str(CorrT6Q10)) or (T6Q10R.keys == CorrT6Q10):
                    T6Q10R.corr = 1
                else:
                    T6Q10R.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in T6Q10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "T6Q10"-------
    for thisComponent in T6Q10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('T6I10.started', T6I10.tStartRefresh)
    trials.addData('T6I10.stopped', T6I10.tStopRefresh)
    # check responses
    if T6Q10R.keys in ['', [], None]:  # No response was made
        T6Q10R.keys = None
        # was no response the correct answer?!
        if str(CorrT6Q10).lower() == 'none':
           T6Q10R.corr = 1;  # correct non-response
        else:
           T6Q10R.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('T6Q10R.keys',T6Q10R.keys)
    trials.addData('T6Q10R.corr', T6Q10R.corr)
    if T6Q10R.keys != None:  # we had a response
        trials.addData('T6Q10R.rt', T6Q10R.rt)
    trials.addData('T6Q10R.started', T6Q10R.tStartRefresh)
    trials.addData('T6Q10R.stopped', T6Q10R.tStopRefresh)
    # the Routine "T6Q10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "end"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    endComponents = [text_2, key_resp_6]
    for thisComponent in endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end"-------
    while continueRoutine:
        # get current time
        t = endClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=endClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['z'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end"-------
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_2.started', text_2.tStartRefresh)
    trials.addData('text_2.stopped', text_2.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    trials.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials.addData('key_resp_6.rt', key_resp_6.rt)
    trials.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    trials.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

ser.write((255).to_bytes(1, 'big'))

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
