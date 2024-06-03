#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on February 07, 2024, at 13:07
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
import serial

# Run 'Before Experiment' code from code_7
import serial
import time

def send_trigger():
    conditions = '1.0x', '1.5x', '2.0x'
    background = 'Clear', 'Noise'
    ser = serial.Serial('COM3', 9600)
    if conditions and background is '1.0x' and 'Clear':
        ser.write(b'1')
    elif conditions and background is '1.0x' and 'Noise':
        ser.write(b'2')
    elif conditions and background is '1.5x' and 'Clear':
        ser.write(b'3')
    elif conditions and background is '1.5x' and 'Noise':
        ser.write(b'4')
    elif conditions and background is '2.0x' and 'Clear':
        ser.write(b'5')
    elif conditions and background is '2.0x' and 'Noise':
        ser.write(b'6')

time.sleep(1)
# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'TCSMF-EEG'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'condition': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\cosmo\\OneDrive\\Desktop\\Experiments\\TCSMF\\Honors Thesis 2023_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=(1024, 768), fullscr=True, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "CondtionSet" ---
    text = visual.TextStim(win=win, name='text',
        text='INSTRUCTOR:\n\nPlease press "Spacebar" to continue!\n\n\n',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    # Run 'Begin Experiment' code from code_1
    myIndices= expInfo['session']
    
    # --- Initialize components for Routine "Instruction" ---
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
    
    # --- Initialize components for Routine "T1A" ---
    sound_1 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
        name='sound_1')
    sound_1.setVolume(1.0)
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', 
        image='Stimuli_HT/FixCross.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_12 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Pre_assement_inst" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='You are now going to complete 10 multiple choice questions on the audio lecture that you just heard. \n\nPlease try to answer questions based on the lecture you heard and avoid using knowledge you already had.\n\nPress "Spacebar" to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T1Q1" ---
    T1I1 = visual.ImageStim(
        win=win,
        name='T1I1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T1Q1R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T1Q2" ---
    T1I2 = visual.ImageStim(
        win=win,
        name='T1I2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T1Q2R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T1Q3" ---
    T1I3 = visual.ImageStim(
        win=win,
        name='T1I3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T1Q3R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T1Q4" ---
    T1I4 = visual.ImageStim(
        win=win,
        name='T1I4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T1Q4R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T1Q5" ---
    T1I5 = visual.ImageStim(
        win=win,
        name='T1I5', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T1Q5R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T1Q6" ---
    T1I6 = visual.ImageStim(
        win=win,
        name='T1I6', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T1Q6R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T1Q7" ---
    T1I7 = visual.ImageStim(
        win=win,
        name='T1I7', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T1Q7R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T1Q8" ---
    T1I8 = visual.ImageStim(
        win=win,
        name='T1I8', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T1Q8R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T1Q9" ---
    T1I9 = visual.ImageStim(
        win=win,
        name='T1I9', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T1Q9R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T1Q10" ---
    T1I10 = visual.ImageStim(
        win=win,
        name='T1I10', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T1Q10R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Trial_Break" ---
    Break_message = visual.TextStim(win=win, name='Break_message',
        text='You can take a break and continue when you are ready.\n\nPlease let the instructor know if you want to leave the booth.\n\nPress "Spacebar" to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard()
    # Create serial object for device at port 'COM3'
    serialCom3 = serial.Serial(
        port='COM3',
        baudrate=9600,
        bytesize=8,
        parity='N',
        stopbits=1,
        timeout=None,
    )
    
    # --- Initialize components for Routine "T2A" ---
    sound_2 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
        name='sound_2')
    sound_2.setVolume(1.0)
    image = visual.ImageStim(
        win=win,
        name='image', 
        image='Stimuli_HT/FixCross.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_11 = keyboard.Keyboard()
    
    # point serialPort_3 to device at port 'COM3' and make sure it's open
    serialPort_3 = serialCom3
    serialPort_3.status = NOT_STARTED
    if not serialPort_3.is_open:
        serialPort_3.open()
    
    # point serialPort_4 to device at port 'COM3' and make sure it's open
    serialPort_4 = serialCom3
    serialPort_4.status = NOT_STARTED
    if not serialPort_4.is_open:
        serialPort_4.open()
    
    # --- Initialize components for Routine "Pre_assement_inst" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='You are now going to complete 10 multiple choice questions on the audio lecture that you just heard. \n\nPlease try to answer questions based on the lecture you heard and avoid using knowledge you already had.\n\nPress "Spacebar" to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T2Q1" ---
    T2I1 = visual.ImageStim(
        win=win,
        name='T2I1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T2Q1R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T2Q2" ---
    T2I2 = visual.ImageStim(
        win=win,
        name='T2I2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T2Q2R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T2Q3" ---
    T2I3 = visual.ImageStim(
        win=win,
        name='T2I3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T2Q3R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T2Q4" ---
    T2I4 = visual.ImageStim(
        win=win,
        name='T2I4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T2Q4R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T2Q5" ---
    T2I5 = visual.ImageStim(
        win=win,
        name='T2I5', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T2Q5R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T2Q6" ---
    T2I6 = visual.ImageStim(
        win=win,
        name='T2I6', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T2Q6R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T2Q7" ---
    T2I7 = visual.ImageStim(
        win=win,
        name='T2I7', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T2Q7R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T2Q8" ---
    T2I8 = visual.ImageStim(
        win=win,
        name='T2I8', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T2Q8R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T2Q9" ---
    T2I9 = visual.ImageStim(
        win=win,
        name='T2I9', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T2Q9R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T2Q10" ---
    T2I10 = visual.ImageStim(
        win=win,
        name='T2I10', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T2Q10R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Trial_Break" ---
    Break_message = visual.TextStim(win=win, name='Break_message',
        text='You can take a break and continue when you are ready.\n\nPlease let the instructor know if you want to leave the booth.\n\nPress "Spacebar" to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T3A" ---
    sound_3 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
        name='sound_3')
    sound_3.setVolume(1.0)
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', 
        image='Stimuli_HT/FixCross.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_10 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Pre_assement_inst" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='You are now going to complete 10 multiple choice questions on the audio lecture that you just heard. \n\nPlease try to answer questions based on the lecture you heard and avoid using knowledge you already had.\n\nPress "Spacebar" to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T3Q1" ---
    T3I1 = visual.ImageStim(
        win=win,
        name='T3I1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T3Q1R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T3Q2" ---
    T3I2 = visual.ImageStim(
        win=win,
        name='T3I2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T3Q2R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T3Q3" ---
    T3I3 = visual.ImageStim(
        win=win,
        name='T3I3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T3Q3R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T3Q4" ---
    T3I4 = visual.ImageStim(
        win=win,
        name='T3I4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T3Q4R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T3Q5" ---
    T3I5 = visual.ImageStim(
        win=win,
        name='T3I5', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T3Q5R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T3Q6" ---
    T3I6 = visual.ImageStim(
        win=win,
        name='T3I6', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T3Q6R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T3Q7" ---
    T3I7 = visual.ImageStim(
        win=win,
        name='T3I7', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T3Q7R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T3Q8" ---
    T3I8 = visual.ImageStim(
        win=win,
        name='T3I8', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T3Q8R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T3Q9" ---
    T3I9 = visual.ImageStim(
        win=win,
        name='T3I9', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T3Q9R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T3Q10" ---
    T3I10 = visual.ImageStim(
        win=win,
        name='T3I10', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T3Q10R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Trial_Break" ---
    Break_message = visual.TextStim(win=win, name='Break_message',
        text='You can take a break and continue when you are ready.\n\nPlease let the instructor know if you want to leave the booth.\n\nPress "Spacebar" to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T4A" ---
    sound_4 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
        name='sound_4')
    sound_4.setVolume(1.0)
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', 
        image='Stimuli_HT/FixCross.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_9 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Pre_assement_inst" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='You are now going to complete 10 multiple choice questions on the audio lecture that you just heard. \n\nPlease try to answer questions based on the lecture you heard and avoid using knowledge you already had.\n\nPress "Spacebar" to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T4Q1" ---
    T4I1 = visual.ImageStim(
        win=win,
        name='T4I1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T4Q1R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T4Q2" ---
    T4I2 = visual.ImageStim(
        win=win,
        name='T4I2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T4Q2R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T4Q3" ---
    T4I3 = visual.ImageStim(
        win=win,
        name='T4I3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T4Q3R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T4Q4" ---
    T4I4 = visual.ImageStim(
        win=win,
        name='T4I4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T4Q4R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T4Q5" ---
    T4I5 = visual.ImageStim(
        win=win,
        name='T4I5', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T4Q5R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T4Q6" ---
    T4I6 = visual.ImageStim(
        win=win,
        name='T4I6', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T4Q6R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T4Q7" ---
    T4I7 = visual.ImageStim(
        win=win,
        name='T4I7', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T4Q7R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T4Q8" ---
    T4I8 = visual.ImageStim(
        win=win,
        name='T4I8', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T4Q8R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T4Q9" ---
    T4I9 = visual.ImageStim(
        win=win,
        name='T4I9', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T4Q9R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T4Q10" ---
    T4I10 = visual.ImageStim(
        win=win,
        name='T4I10', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T4Q10R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Trial_Break" ---
    Break_message = visual.TextStim(win=win, name='Break_message',
        text='You can take a break and continue when you are ready.\n\nPlease let the instructor know if you want to leave the booth.\n\nPress "Spacebar" to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T5A" ---
    sound_5 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
        name='sound_5')
    sound_5.setVolume(1.0)
    image_5 = visual.ImageStim(
        win=win,
        name='image_5', 
        image='Stimuli_HT/FixCross.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_8 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Pre_assement_inst" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='You are now going to complete 10 multiple choice questions on the audio lecture that you just heard. \n\nPlease try to answer questions based on the lecture you heard and avoid using knowledge you already had.\n\nPress "Spacebar" to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T5Q1" ---
    T5I1 = visual.ImageStim(
        win=win,
        name='T5I1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T5Q1R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T5Q2" ---
    T5I2 = visual.ImageStim(
        win=win,
        name='T5I2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T5Q2R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T5Q3" ---
    T5I3 = visual.ImageStim(
        win=win,
        name='T5I3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T5Q3R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T5Q4" ---
    T5I4 = visual.ImageStim(
        win=win,
        name='T5I4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T5Q4R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T5Q5" ---
    T5I5 = visual.ImageStim(
        win=win,
        name='T5I5', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T5Q5R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T5Q6" ---
    T5I6 = visual.ImageStim(
        win=win,
        name='T5I6', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T5Q6R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T5Q7" ---
    T5I7 = visual.ImageStim(
        win=win,
        name='T5I7', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T5Q7R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T5Q8" ---
    T5I8 = visual.ImageStim(
        win=win,
        name='T5I8', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T5Q8R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T5Q9" ---
    T5I9 = visual.ImageStim(
        win=win,
        name='T5I9', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T5Q9R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T5Q10" ---
    T5I10 = visual.ImageStim(
        win=win,
        name='T5I10', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T5Q10R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Trial_Break" ---
    Break_message = visual.TextStim(win=win, name='Break_message',
        text='You can take a break and continue when you are ready.\n\nPlease let the instructor know if you want to leave the booth.\n\nPress "Spacebar" to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T6A" ---
    sound_6 = sound.Sound('A', secs=-1, stereo=True, hamming=True,
        name='sound_6')
    sound_6.setVolume(1.0)
    image_6 = visual.ImageStim(
        win=win,
        name='image_6', 
        image='Stimuli_HT/FixCross.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.4, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp_7 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Pre_assement_inst" ---
    text_5 = visual.TextStim(win=win, name='text_5',
        text='You are now going to complete 10 multiple choice questions on the audio lecture that you just heard. \n\nPlease try to answer questions based on the lecture you heard and avoid using knowledge you already had.\n\nPress "Spacebar" to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_5 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T6Q1" ---
    T6I1 = visual.ImageStim(
        win=win,
        name='T6I1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T6Q1R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T6Q2" ---
    T6I2 = visual.ImageStim(
        win=win,
        name='T6I2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T6Q2R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T6Q3" ---
    T6I3 = visual.ImageStim(
        win=win,
        name='T6I3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T6Q3R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T6Q4" ---
    T6I4 = visual.ImageStim(
        win=win,
        name='T6I4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T6Q4R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T6Q5" ---
    T6I5 = visual.ImageStim(
        win=win,
        name='T6I5', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T6Q5R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T6Q6" ---
    T6I6 = visual.ImageStim(
        win=win,
        name='T6I6', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T6Q6R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T6Q7" ---
    T6I7 = visual.ImageStim(
        win=win,
        name='T6I7', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T6Q7R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T6Q8" ---
    T6I8 = visual.ImageStim(
        win=win,
        name='T6I8', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T6Q8R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T6Q9" ---
    T6I9 = visual.ImageStim(
        win=win,
        name='T6I9', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T6Q9R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "T6Q10" ---
    T6I10 = visual.ImageStim(
        win=win,
        name='T6I10', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.4, 0.7),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    T6Q10R = keyboard.Keyboard()
    
    # --- Initialize components for Routine "end" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='Experiment Ended\n\nPlease wait for the instructor.',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_6 = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "CondtionSet" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('CondtionSet.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # Run 'Begin Routine' code from code_1
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
    frameN = -1
    
    # --- Run Routine "CondtionSet" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CondtionSetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CondtionSet" ---
    for thisComponent in CondtionSetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('CondtionSet.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # Run 'End Routine' code from code_1
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
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "Instruction" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Instruction.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "Instruction" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cond_text* updates
            
            # if cond_text is starting this frame...
            if cond_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cond_text.frameNStart = frameN  # exact frame index
                cond_text.tStart = t  # local t and not account for scr refresh
                cond_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cond_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cond_text.started')
                # update status
                cond_text.status = STARTED
                cond_text.setAutoDraw(True)
            
            # if cond_text is active this frame...
            if cond_text.status == STARTED:
                # update params
                pass
            
            # *Inst_text* updates
            
            # if Inst_text is starting this frame...
            if Inst_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Inst_text.frameNStart = frameN  # exact frame index
                Inst_text.tStart = t  # local t and not account for scr refresh
                Inst_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Inst_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Inst_text.started')
                # update status
                Inst_text.status = STARTED
                Inst_text.setAutoDraw(True)
            
            # if Inst_text is active this frame...
            if Inst_text.status == STARTED:
                # update params
                pass
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InstructionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Instruction" ---
        for thisComponent in InstructionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Instruction.stopped', globalClock.getTime())
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials.addData('key_resp_3.rt', key_resp_3.rt)
            trials.addData('key_resp_3.duration', key_resp_3.duration)
        # the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T1A" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T1A.started', globalClock.getTime())
        sound_1.setSound(T1A, hamming=True)
        sound_1.setVolume(1.0, log=False)
        sound_1.seek(0)
        key_resp_12.keys = []
        key_resp_12.rt = []
        _key_resp_12_allKeys = []
        # Run 'Begin Routine' code from code_8
        
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
        frameN = -1
        
        # --- Run Routine "T1A" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # if sound_1 is starting this frame...
            if sound_1.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.tStart = t  # local t and not account for scr refresh
                sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_1.started', t)
                # update status
                sound_1.status = STARTED
                sound_1.play()  # start the sound (it finishes automatically)
            # update sound_1 status according to whether it's playing
            if sound_1.isPlaying:
                sound_1.status = STARTED
            elif sound_1.isFinished:
                sound_1.status = FINISHED
            
            # *image_2* updates
            
            # if image_2 is starting this frame...
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_2.started')
                # update status
                image_2.status = STARTED
                image_2.setAutoDraw(True)
            
            # if image_2 is active this frame...
            if image_2.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code
            if sound_1.status == FINISHED:
                continueRoutine = False
            
            # *key_resp_12* updates
            waitOnFlip = False
            
            # if key_resp_12 is starting this frame...
            if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_12.frameNStart = frameN  # exact frame index
                key_resp_12.tStart = t  # local t and not account for scr refresh
                key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_12.started')
                # update status
                key_resp_12.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_12.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_12.getKeys(keyList=['z'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_12_allKeys.extend(theseKeys)
                if len(_key_resp_12_allKeys):
                    key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                    key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                    key_resp_12.duration = _key_resp_12_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T1AComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T1A" ---
        for thisComponent in T1AComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T1A.stopped', globalClock.getTime())
        sound_1.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if key_resp_12.keys in ['', [], None]:  # No response was made
            key_resp_12.keys = None
        trials.addData('key_resp_12.keys',key_resp_12.keys)
        if key_resp_12.keys != None:  # we had a response
            trials.addData('key_resp_12.rt', key_resp_12.rt)
            trials.addData('key_resp_12.duration', key_resp_12.duration)
        # Run 'End Routine' code from code_8
        send_bits('Stim Ended!')
        # the Routine "T1A" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Pre_assement_inst" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Pre_assement_inst.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "Pre_assement_inst" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_5* updates
            waitOnFlip = False
            
            # if key_resp_5 is starting this frame...
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                # update status
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pre_assement_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pre_assement_inst" ---
        for thisComponent in Pre_assement_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Pre_assement_inst.stopped', globalClock.getTime())
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        trials.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials.addData('key_resp_5.rt', key_resp_5.rt)
            trials.addData('key_resp_5.duration', key_resp_5.duration)
        # the Routine "Pre_assement_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T1Q1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T1Q1.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T1Q1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T1I1* updates
            
            # if T1I1 is starting this frame...
            if T1I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1I1.frameNStart = frameN  # exact frame index
                T1I1.tStart = t  # local t and not account for scr refresh
                T1I1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1I1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1I1.started')
                # update status
                T1I1.status = STARTED
                T1I1.setAutoDraw(True)
            
            # if T1I1 is active this frame...
            if T1I1.status == STARTED:
                # update params
                pass
            
            # *T1Q1R* updates
            waitOnFlip = False
            
            # if T1Q1R is starting this frame...
            if T1Q1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1Q1R.frameNStart = frameN  # exact frame index
                T1Q1R.tStart = t  # local t and not account for scr refresh
                T1Q1R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1Q1R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1Q1R.started')
                # update status
                T1Q1R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T1Q1R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T1Q1R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T1Q1R.status == STARTED and not waitOnFlip:
                theseKeys = T1Q1R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T1Q1R_allKeys.extend(theseKeys)
                if len(_T1Q1R_allKeys):
                    T1Q1R.keys = _T1Q1R_allKeys[-1].name  # just the last key pressed
                    T1Q1R.rt = _T1Q1R_allKeys[-1].rt
                    T1Q1R.duration = _T1Q1R_allKeys[-1].duration
                    # was this correct?
                    if (T1Q1R.keys == str(CorrT1Q1)) or (T1Q1R.keys == CorrT1Q1):
                        T1Q1R.corr = 1
                    else:
                        T1Q1R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T1Q1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T1Q1" ---
        for thisComponent in T1Q1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T1Q1.stopped', globalClock.getTime())
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
            trials.addData('T1Q1R.duration', T1Q1R.duration)
        # the Routine "T1Q1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T1Q2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T1Q2.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T1Q2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T1I2* updates
            
            # if T1I2 is starting this frame...
            if T1I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1I2.frameNStart = frameN  # exact frame index
                T1I2.tStart = t  # local t and not account for scr refresh
                T1I2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1I2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1I2.started')
                # update status
                T1I2.status = STARTED
                T1I2.setAutoDraw(True)
            
            # if T1I2 is active this frame...
            if T1I2.status == STARTED:
                # update params
                pass
            
            # *T1Q2R* updates
            waitOnFlip = False
            
            # if T1Q2R is starting this frame...
            if T1Q2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1Q2R.frameNStart = frameN  # exact frame index
                T1Q2R.tStart = t  # local t and not account for scr refresh
                T1Q2R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1Q2R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1Q2R.started')
                # update status
                T1Q2R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T1Q2R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T1Q2R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T1Q2R.status == STARTED and not waitOnFlip:
                theseKeys = T1Q2R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T1Q2R_allKeys.extend(theseKeys)
                if len(_T1Q2R_allKeys):
                    T1Q2R.keys = _T1Q2R_allKeys[-1].name  # just the last key pressed
                    T1Q2R.rt = _T1Q2R_allKeys[-1].rt
                    T1Q2R.duration = _T1Q2R_allKeys[-1].duration
                    # was this correct?
                    if (T1Q2R.keys == str(CorrT1Q2)) or (T1Q2R.keys == CorrT1Q2):
                        T1Q2R.corr = 1
                    else:
                        T1Q2R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T1Q2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T1Q2" ---
        for thisComponent in T1Q2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T1Q2.stopped', globalClock.getTime())
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
            trials.addData('T1Q2R.duration', T1Q2R.duration)
        # the Routine "T1Q2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T1Q3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T1Q3.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T1Q3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T1I3* updates
            
            # if T1I3 is starting this frame...
            if T1I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1I3.frameNStart = frameN  # exact frame index
                T1I3.tStart = t  # local t and not account for scr refresh
                T1I3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1I3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1I3.started')
                # update status
                T1I3.status = STARTED
                T1I3.setAutoDraw(True)
            
            # if T1I3 is active this frame...
            if T1I3.status == STARTED:
                # update params
                pass
            
            # *T1Q3R* updates
            waitOnFlip = False
            
            # if T1Q3R is starting this frame...
            if T1Q3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1Q3R.frameNStart = frameN  # exact frame index
                T1Q3R.tStart = t  # local t and not account for scr refresh
                T1Q3R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1Q3R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1Q3R.started')
                # update status
                T1Q3R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T1Q3R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T1Q3R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T1Q3R.status == STARTED and not waitOnFlip:
                theseKeys = T1Q3R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T1Q3R_allKeys.extend(theseKeys)
                if len(_T1Q3R_allKeys):
                    T1Q3R.keys = _T1Q3R_allKeys[-1].name  # just the last key pressed
                    T1Q3R.rt = _T1Q3R_allKeys[-1].rt
                    T1Q3R.duration = _T1Q3R_allKeys[-1].duration
                    # was this correct?
                    if (T1Q3R.keys == str(CorrT1Q3)) or (T1Q3R.keys == CorrT1Q3):
                        T1Q3R.corr = 1
                    else:
                        T1Q3R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T1Q3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T1Q3" ---
        for thisComponent in T1Q3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T1Q3.stopped', globalClock.getTime())
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
            trials.addData('T1Q3R.duration', T1Q3R.duration)
        # the Routine "T1Q3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T1Q4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T1Q4.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T1Q4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T1I4* updates
            
            # if T1I4 is starting this frame...
            if T1I4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1I4.frameNStart = frameN  # exact frame index
                T1I4.tStart = t  # local t and not account for scr refresh
                T1I4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1I4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1I4.started')
                # update status
                T1I4.status = STARTED
                T1I4.setAutoDraw(True)
            
            # if T1I4 is active this frame...
            if T1I4.status == STARTED:
                # update params
                pass
            
            # *T1Q4R* updates
            waitOnFlip = False
            
            # if T1Q4R is starting this frame...
            if T1Q4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1Q4R.frameNStart = frameN  # exact frame index
                T1Q4R.tStart = t  # local t and not account for scr refresh
                T1Q4R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1Q4R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1Q4R.started')
                # update status
                T1Q4R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T1Q4R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T1Q4R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T1Q4R.status == STARTED and not waitOnFlip:
                theseKeys = T1Q4R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T1Q4R_allKeys.extend(theseKeys)
                if len(_T1Q4R_allKeys):
                    T1Q4R.keys = _T1Q4R_allKeys[-1].name  # just the last key pressed
                    T1Q4R.rt = _T1Q4R_allKeys[-1].rt
                    T1Q4R.duration = _T1Q4R_allKeys[-1].duration
                    # was this correct?
                    if (T1Q4R.keys == str(CorrT1Q4)) or (T1Q4R.keys == CorrT1Q4):
                        T1Q4R.corr = 1
                    else:
                        T1Q4R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T1Q4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T1Q4" ---
        for thisComponent in T1Q4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T1Q4.stopped', globalClock.getTime())
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
            trials.addData('T1Q4R.duration', T1Q4R.duration)
        # the Routine "T1Q4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T1Q5" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T1Q5.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T1Q5" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T1I5* updates
            
            # if T1I5 is starting this frame...
            if T1I5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1I5.frameNStart = frameN  # exact frame index
                T1I5.tStart = t  # local t and not account for scr refresh
                T1I5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1I5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1I5.started')
                # update status
                T1I5.status = STARTED
                T1I5.setAutoDraw(True)
            
            # if T1I5 is active this frame...
            if T1I5.status == STARTED:
                # update params
                pass
            
            # *T1Q5R* updates
            waitOnFlip = False
            
            # if T1Q5R is starting this frame...
            if T1Q5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1Q5R.frameNStart = frameN  # exact frame index
                T1Q5R.tStart = t  # local t and not account for scr refresh
                T1Q5R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1Q5R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1Q5R.started')
                # update status
                T1Q5R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T1Q5R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T1Q5R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T1Q5R.status == STARTED and not waitOnFlip:
                theseKeys = T1Q5R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T1Q5R_allKeys.extend(theseKeys)
                if len(_T1Q5R_allKeys):
                    T1Q5R.keys = _T1Q5R_allKeys[-1].name  # just the last key pressed
                    T1Q5R.rt = _T1Q5R_allKeys[-1].rt
                    T1Q5R.duration = _T1Q5R_allKeys[-1].duration
                    # was this correct?
                    if (T1Q5R.keys == str(CorrT1Q5)) or (T1Q5R.keys == CorrT1Q5):
                        T1Q5R.corr = 1
                    else:
                        T1Q5R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T1Q5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T1Q5" ---
        for thisComponent in T1Q5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T1Q5.stopped', globalClock.getTime())
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
            trials.addData('T1Q5R.duration', T1Q5R.duration)
        # the Routine "T1Q5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T1Q6" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T1Q6.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T1Q6" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T1I6* updates
            
            # if T1I6 is starting this frame...
            if T1I6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1I6.frameNStart = frameN  # exact frame index
                T1I6.tStart = t  # local t and not account for scr refresh
                T1I6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1I6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1I6.started')
                # update status
                T1I6.status = STARTED
                T1I6.setAutoDraw(True)
            
            # if T1I6 is active this frame...
            if T1I6.status == STARTED:
                # update params
                pass
            
            # *T1Q6R* updates
            waitOnFlip = False
            
            # if T1Q6R is starting this frame...
            if T1Q6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1Q6R.frameNStart = frameN  # exact frame index
                T1Q6R.tStart = t  # local t and not account for scr refresh
                T1Q6R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1Q6R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1Q6R.started')
                # update status
                T1Q6R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T1Q6R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T1Q6R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T1Q6R.status == STARTED and not waitOnFlip:
                theseKeys = T1Q6R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T1Q6R_allKeys.extend(theseKeys)
                if len(_T1Q6R_allKeys):
                    T1Q6R.keys = _T1Q6R_allKeys[-1].name  # just the last key pressed
                    T1Q6R.rt = _T1Q6R_allKeys[-1].rt
                    T1Q6R.duration = _T1Q6R_allKeys[-1].duration
                    # was this correct?
                    if (T1Q6R.keys == str(CorrT1Q6)) or (T1Q6R.keys == CorrT1Q6):
                        T1Q6R.corr = 1
                    else:
                        T1Q6R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T1Q6Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T1Q6" ---
        for thisComponent in T1Q6Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T1Q6.stopped', globalClock.getTime())
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
            trials.addData('T1Q6R.duration', T1Q6R.duration)
        # the Routine "T1Q6" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T1Q7" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T1Q7.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T1Q7" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T1I7* updates
            
            # if T1I7 is starting this frame...
            if T1I7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1I7.frameNStart = frameN  # exact frame index
                T1I7.tStart = t  # local t and not account for scr refresh
                T1I7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1I7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1I7.started')
                # update status
                T1I7.status = STARTED
                T1I7.setAutoDraw(True)
            
            # if T1I7 is active this frame...
            if T1I7.status == STARTED:
                # update params
                pass
            
            # *T1Q7R* updates
            waitOnFlip = False
            
            # if T1Q7R is starting this frame...
            if T1Q7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1Q7R.frameNStart = frameN  # exact frame index
                T1Q7R.tStart = t  # local t and not account for scr refresh
                T1Q7R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1Q7R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1Q7R.started')
                # update status
                T1Q7R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T1Q7R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T1Q7R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T1Q7R.status == STARTED and not waitOnFlip:
                theseKeys = T1Q7R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T1Q7R_allKeys.extend(theseKeys)
                if len(_T1Q7R_allKeys):
                    T1Q7R.keys = _T1Q7R_allKeys[-1].name  # just the last key pressed
                    T1Q7R.rt = _T1Q7R_allKeys[-1].rt
                    T1Q7R.duration = _T1Q7R_allKeys[-1].duration
                    # was this correct?
                    if (T1Q7R.keys == str(CorrT1Q7)) or (T1Q7R.keys == CorrT1Q7):
                        T1Q7R.corr = 1
                    else:
                        T1Q7R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T1Q7Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T1Q7" ---
        for thisComponent in T1Q7Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T1Q7.stopped', globalClock.getTime())
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
            trials.addData('T1Q7R.duration', T1Q7R.duration)
        # the Routine "T1Q7" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T1Q8" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T1Q8.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T1Q8" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T1I8* updates
            
            # if T1I8 is starting this frame...
            if T1I8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1I8.frameNStart = frameN  # exact frame index
                T1I8.tStart = t  # local t and not account for scr refresh
                T1I8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1I8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1I8.started')
                # update status
                T1I8.status = STARTED
                T1I8.setAutoDraw(True)
            
            # if T1I8 is active this frame...
            if T1I8.status == STARTED:
                # update params
                pass
            
            # *T1Q8R* updates
            waitOnFlip = False
            
            # if T1Q8R is starting this frame...
            if T1Q8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1Q8R.frameNStart = frameN  # exact frame index
                T1Q8R.tStart = t  # local t and not account for scr refresh
                T1Q8R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1Q8R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1Q8R.started')
                # update status
                T1Q8R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T1Q8R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T1Q8R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T1Q8R.status == STARTED and not waitOnFlip:
                theseKeys = T1Q8R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T1Q8R_allKeys.extend(theseKeys)
                if len(_T1Q8R_allKeys):
                    T1Q8R.keys = _T1Q8R_allKeys[-1].name  # just the last key pressed
                    T1Q8R.rt = _T1Q8R_allKeys[-1].rt
                    T1Q8R.duration = _T1Q8R_allKeys[-1].duration
                    # was this correct?
                    if (T1Q8R.keys == str(CorrT1Q8)) or (T1Q8R.keys == CorrT1Q8):
                        T1Q8R.corr = 1
                    else:
                        T1Q8R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T1Q8Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T1Q8" ---
        for thisComponent in T1Q8Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T1Q8.stopped', globalClock.getTime())
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
            trials.addData('T1Q8R.duration', T1Q8R.duration)
        # the Routine "T1Q8" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T1Q9" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T1Q9.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T1Q9" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T1I9* updates
            
            # if T1I9 is starting this frame...
            if T1I9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1I9.frameNStart = frameN  # exact frame index
                T1I9.tStart = t  # local t and not account for scr refresh
                T1I9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1I9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1I9.started')
                # update status
                T1I9.status = STARTED
                T1I9.setAutoDraw(True)
            
            # if T1I9 is active this frame...
            if T1I9.status == STARTED:
                # update params
                pass
            
            # *T1Q9R* updates
            waitOnFlip = False
            
            # if T1Q9R is starting this frame...
            if T1Q9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1Q9R.frameNStart = frameN  # exact frame index
                T1Q9R.tStart = t  # local t and not account for scr refresh
                T1Q9R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1Q9R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1Q9R.started')
                # update status
                T1Q9R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T1Q9R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T1Q9R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T1Q9R.status == STARTED and not waitOnFlip:
                theseKeys = T1Q9R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T1Q9R_allKeys.extend(theseKeys)
                if len(_T1Q9R_allKeys):
                    T1Q9R.keys = _T1Q9R_allKeys[-1].name  # just the last key pressed
                    T1Q9R.rt = _T1Q9R_allKeys[-1].rt
                    T1Q9R.duration = _T1Q9R_allKeys[-1].duration
                    # was this correct?
                    if (T1Q9R.keys == str(CorrT1Q9)) or (T1Q9R.keys == CorrT1Q9):
                        T1Q9R.corr = 1
                    else:
                        T1Q9R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T1Q9Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T1Q9" ---
        for thisComponent in T1Q9Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T1Q9.stopped', globalClock.getTime())
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
            trials.addData('T1Q9R.duration', T1Q9R.duration)
        # the Routine "T1Q9" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T1Q10" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T1Q10.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T1Q10" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T1I10* updates
            
            # if T1I10 is starting this frame...
            if T1I10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1I10.frameNStart = frameN  # exact frame index
                T1I10.tStart = t  # local t and not account for scr refresh
                T1I10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1I10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1I10.started')
                # update status
                T1I10.status = STARTED
                T1I10.setAutoDraw(True)
            
            # if T1I10 is active this frame...
            if T1I10.status == STARTED:
                # update params
                pass
            
            # *T1Q10R* updates
            waitOnFlip = False
            
            # if T1Q10R is starting this frame...
            if T1Q10R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T1Q10R.frameNStart = frameN  # exact frame index
                T1Q10R.tStart = t  # local t and not account for scr refresh
                T1Q10R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T1Q10R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T1Q10R.started')
                # update status
                T1Q10R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T1Q10R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T1Q10R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T1Q10R.status == STARTED and not waitOnFlip:
                theseKeys = T1Q10R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T1Q10R_allKeys.extend(theseKeys)
                if len(_T1Q10R_allKeys):
                    T1Q10R.keys = _T1Q10R_allKeys[-1].name  # just the last key pressed
                    T1Q10R.rt = _T1Q10R_allKeys[-1].rt
                    T1Q10R.duration = _T1Q10R_allKeys[-1].duration
                    # was this correct?
                    if (T1Q10R.keys == str(CorrT1Q10)) or (T1Q10R.keys == CorrT1Q10):
                        T1Q10R.corr = 1
                    else:
                        T1Q10R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T1Q10Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T1Q10" ---
        for thisComponent in T1Q10Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T1Q10.stopped', globalClock.getTime())
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
            trials.addData('T1Q10R.duration', T1Q10R.duration)
        # the Routine "T1Q10" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Trial_Break" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Trial_Break.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "Trial_Break" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Break_message* updates
            
            # if Break_message is starting this frame...
            if Break_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Break_message.frameNStart = frameN  # exact frame index
                Break_message.tStart = t  # local t and not account for scr refresh
                Break_message.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Break_message, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Break_message.started')
                # update status
                Break_message.status = STARTED
                Break_message.setAutoDraw(True)
            
            # if Break_message is active this frame...
            if Break_message.status == STARTED:
                # update params
                pass
            
            # *key_resp_4* updates
            waitOnFlip = False
            
            # if key_resp_4 is starting this frame...
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
                # update status
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_BreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial_Break" ---
        for thisComponent in Trial_BreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Trial_Break.stopped', globalClock.getTime())
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        trials.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials.addData('key_resp_4.rt', key_resp_4.rt)
            trials.addData('key_resp_4.duration', key_resp_4.duration)
        # the Routine "Trial_Break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T2A" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T2A.started', globalClock.getTime())
        sound_2.setSound(T2A, hamming=True)
        sound_2.setVolume(1.0, log=False)
        sound_2.seek(0)
        key_resp_11.keys = []
        key_resp_11.rt = []
        _key_resp_11_allKeys = []
        # keep track of which components have finished
        T2AComponents = [sound_2, image, key_resp_11, serialPort_3, serialPort_4]
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
        frameN = -1
        
        # --- Run Routine "T2A" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # if sound_2 is starting this frame...
            if sound_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_2.frameNStart = frameN  # exact frame index
                sound_2.tStart = t  # local t and not account for scr refresh
                sound_2.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_2.started', t)
                # update status
                sound_2.status = STARTED
                sound_2.play()  # start the sound (it finishes automatically)
            # update sound_2 status according to whether it's playing
            if sound_2.isPlaying:
                sound_2.status = STARTED
            elif sound_2.isFinished:
                sound_2.status = FINISHED
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_2
            if sound_2.status == FINISHED:
                continueRoutine = False
            
            # *key_resp_11* updates
            waitOnFlip = False
            
            # if key_resp_11 is starting this frame...
            if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_11.frameNStart = frameN  # exact frame index
                key_resp_11.tStart = t  # local t and not account for scr refresh
                key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_11.started')
                # update status
                key_resp_11.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_11.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_11.getKeys(keyList=['z'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_11_allKeys.extend(theseKeys)
                if len(_key_resp_11_allKeys):
                    key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                    key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                    key_resp_11.duration = _key_resp_11_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # if serialPort_3 is starting this frame...
            if serialPort_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                serialPort_3.frameNStart = frameN  # exact frame index
                serialPort_3.tStart = t  # local t and not account for scr refresh
                serialPort_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(serialPort_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('serialPort_3.started', t)
                # update status
                serialPort_3.status = STARTED
                serialPort_3.write(bytes('1', 'utf8'))
                serialPort_3.status = STARTED
            
            # if serialPort_3 is stopping this frame...
            if serialPort_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > serialPort_3.tStartRefresh + .1-frameTolerance:
                    # keep track of stop time/frame for later
                    serialPort_3.tStop = t  # not accounting for scr refresh
                    serialPort_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('serialPort_3.stopped', t)
                    # update status
                    serialPort_3.status = FINISHED
                    serialPort_3.write(bytes('0', 'utf8'))
                    serialPort_3.status = FINISHED
            
            # if serialPort_4 is starting this frame...
            if serialPort_4.status == NOT_STARTED and t >= 360-frameTolerance:
                # keep track of start time/frame for later
                serialPort_4.frameNStart = frameN  # exact frame index
                serialPort_4.tStart = t  # local t and not account for scr refresh
                serialPort_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(serialPort_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('serialPort_4.started', t)
                # update status
                serialPort_4.status = STARTED
                serialPort_4.write(bytes('1', 'utf8'))
                serialPort_4.status = STARTED
            
            # if serialPort_4 is stopping this frame...
            if serialPort_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > serialPort_4.tStartRefresh + .1-frameTolerance:
                    # keep track of stop time/frame for later
                    serialPort_4.tStop = t  # not accounting for scr refresh
                    serialPort_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('serialPort_4.stopped', t)
                    # update status
                    serialPort_4.status = FINISHED
                    serialPort_4.write(bytes('0', 'utf8'))
                    serialPort_4.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T2AComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T2A" ---
        for thisComponent in T2AComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T2A.stopped', globalClock.getTime())
        sound_2.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if key_resp_11.keys in ['', [], None]:  # No response was made
            key_resp_11.keys = None
        trials.addData('key_resp_11.keys',key_resp_11.keys)
        if key_resp_11.keys != None:  # we had a response
            trials.addData('key_resp_11.rt', key_resp_11.rt)
            trials.addData('key_resp_11.duration', key_resp_11.duration)
        # the Routine "T2A" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Pre_assement_inst" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Pre_assement_inst.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "Pre_assement_inst" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_5* updates
            waitOnFlip = False
            
            # if key_resp_5 is starting this frame...
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                # update status
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pre_assement_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pre_assement_inst" ---
        for thisComponent in Pre_assement_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Pre_assement_inst.stopped', globalClock.getTime())
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        trials.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials.addData('key_resp_5.rt', key_resp_5.rt)
            trials.addData('key_resp_5.duration', key_resp_5.duration)
        # the Routine "Pre_assement_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T2Q1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T2Q1.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T2Q1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T2I1* updates
            
            # if T2I1 is starting this frame...
            if T2I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2I1.frameNStart = frameN  # exact frame index
                T2I1.tStart = t  # local t and not account for scr refresh
                T2I1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2I1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2I1.started')
                # update status
                T2I1.status = STARTED
                T2I1.setAutoDraw(True)
            
            # if T2I1 is active this frame...
            if T2I1.status == STARTED:
                # update params
                pass
            
            # *T2Q1R* updates
            waitOnFlip = False
            
            # if T2Q1R is starting this frame...
            if T2Q1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2Q1R.frameNStart = frameN  # exact frame index
                T2Q1R.tStart = t  # local t and not account for scr refresh
                T2Q1R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2Q1R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2Q1R.started')
                # update status
                T2Q1R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T2Q1R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T2Q1R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T2Q1R.status == STARTED and not waitOnFlip:
                theseKeys = T2Q1R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T2Q1R_allKeys.extend(theseKeys)
                if len(_T2Q1R_allKeys):
                    T2Q1R.keys = _T2Q1R_allKeys[-1].name  # just the last key pressed
                    T2Q1R.rt = _T2Q1R_allKeys[-1].rt
                    T2Q1R.duration = _T2Q1R_allKeys[-1].duration
                    # was this correct?
                    if (T2Q1R.keys == str(CorrT2Q1)) or (T2Q1R.keys == CorrT2Q1):
                        T2Q1R.corr = 1
                    else:
                        T2Q1R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T2Q1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T2Q1" ---
        for thisComponent in T2Q1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T2Q1.stopped', globalClock.getTime())
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
            trials.addData('T2Q1R.duration', T2Q1R.duration)
        # the Routine "T2Q1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T2Q2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T2Q2.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T2Q2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T2I2* updates
            
            # if T2I2 is starting this frame...
            if T2I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2I2.frameNStart = frameN  # exact frame index
                T2I2.tStart = t  # local t and not account for scr refresh
                T2I2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2I2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2I2.started')
                # update status
                T2I2.status = STARTED
                T2I2.setAutoDraw(True)
            
            # if T2I2 is active this frame...
            if T2I2.status == STARTED:
                # update params
                pass
            
            # *T2Q2R* updates
            waitOnFlip = False
            
            # if T2Q2R is starting this frame...
            if T2Q2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2Q2R.frameNStart = frameN  # exact frame index
                T2Q2R.tStart = t  # local t and not account for scr refresh
                T2Q2R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2Q2R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2Q2R.started')
                # update status
                T2Q2R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T2Q2R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T2Q2R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T2Q2R.status == STARTED and not waitOnFlip:
                theseKeys = T2Q2R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T2Q2R_allKeys.extend(theseKeys)
                if len(_T2Q2R_allKeys):
                    T2Q2R.keys = _T2Q2R_allKeys[-1].name  # just the last key pressed
                    T2Q2R.rt = _T2Q2R_allKeys[-1].rt
                    T2Q2R.duration = _T2Q2R_allKeys[-1].duration
                    # was this correct?
                    if (T2Q2R.keys == str(CorrT2Q2)) or (T2Q2R.keys == CorrT2Q2):
                        T2Q2R.corr = 1
                    else:
                        T2Q2R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T2Q2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T2Q2" ---
        for thisComponent in T2Q2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T2Q2.stopped', globalClock.getTime())
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
            trials.addData('T2Q2R.duration', T2Q2R.duration)
        # the Routine "T2Q2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T2Q3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T2Q3.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T2Q3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T2I3* updates
            
            # if T2I3 is starting this frame...
            if T2I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2I3.frameNStart = frameN  # exact frame index
                T2I3.tStart = t  # local t and not account for scr refresh
                T2I3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2I3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2I3.started')
                # update status
                T2I3.status = STARTED
                T2I3.setAutoDraw(True)
            
            # if T2I3 is active this frame...
            if T2I3.status == STARTED:
                # update params
                pass
            
            # *T2Q3R* updates
            waitOnFlip = False
            
            # if T2Q3R is starting this frame...
            if T2Q3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2Q3R.frameNStart = frameN  # exact frame index
                T2Q3R.tStart = t  # local t and not account for scr refresh
                T2Q3R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2Q3R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2Q3R.started')
                # update status
                T2Q3R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T2Q3R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T2Q3R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T2Q3R.status == STARTED and not waitOnFlip:
                theseKeys = T2Q3R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T2Q3R_allKeys.extend(theseKeys)
                if len(_T2Q3R_allKeys):
                    T2Q3R.keys = _T2Q3R_allKeys[-1].name  # just the last key pressed
                    T2Q3R.rt = _T2Q3R_allKeys[-1].rt
                    T2Q3R.duration = _T2Q3R_allKeys[-1].duration
                    # was this correct?
                    if (T2Q3R.keys == str(CorrT2Q3)) or (T2Q3R.keys == CorrT2Q3):
                        T2Q3R.corr = 1
                    else:
                        T2Q3R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T2Q3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T2Q3" ---
        for thisComponent in T2Q3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T2Q3.stopped', globalClock.getTime())
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
            trials.addData('T2Q3R.duration', T2Q3R.duration)
        # the Routine "T2Q3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T2Q4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T2Q4.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T2Q4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T2I4* updates
            
            # if T2I4 is starting this frame...
            if T2I4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2I4.frameNStart = frameN  # exact frame index
                T2I4.tStart = t  # local t and not account for scr refresh
                T2I4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2I4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2I4.started')
                # update status
                T2I4.status = STARTED
                T2I4.setAutoDraw(True)
            
            # if T2I4 is active this frame...
            if T2I4.status == STARTED:
                # update params
                pass
            
            # *T2Q4R* updates
            waitOnFlip = False
            
            # if T2Q4R is starting this frame...
            if T2Q4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2Q4R.frameNStart = frameN  # exact frame index
                T2Q4R.tStart = t  # local t and not account for scr refresh
                T2Q4R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2Q4R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2Q4R.started')
                # update status
                T2Q4R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T2Q4R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T2Q4R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T2Q4R.status == STARTED and not waitOnFlip:
                theseKeys = T2Q4R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T2Q4R_allKeys.extend(theseKeys)
                if len(_T2Q4R_allKeys):
                    T2Q4R.keys = _T2Q4R_allKeys[-1].name  # just the last key pressed
                    T2Q4R.rt = _T2Q4R_allKeys[-1].rt
                    T2Q4R.duration = _T2Q4R_allKeys[-1].duration
                    # was this correct?
                    if (T2Q4R.keys == str(CorrT2Q4)) or (T2Q4R.keys == CorrT2Q4):
                        T2Q4R.corr = 1
                    else:
                        T2Q4R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T2Q4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T2Q4" ---
        for thisComponent in T2Q4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T2Q4.stopped', globalClock.getTime())
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
            trials.addData('T2Q4R.duration', T2Q4R.duration)
        # the Routine "T2Q4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T2Q5" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T2Q5.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T2Q5" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T2I5* updates
            
            # if T2I5 is starting this frame...
            if T2I5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2I5.frameNStart = frameN  # exact frame index
                T2I5.tStart = t  # local t and not account for scr refresh
                T2I5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2I5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2I5.started')
                # update status
                T2I5.status = STARTED
                T2I5.setAutoDraw(True)
            
            # if T2I5 is active this frame...
            if T2I5.status == STARTED:
                # update params
                pass
            
            # *T2Q5R* updates
            waitOnFlip = False
            
            # if T2Q5R is starting this frame...
            if T2Q5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2Q5R.frameNStart = frameN  # exact frame index
                T2Q5R.tStart = t  # local t and not account for scr refresh
                T2Q5R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2Q5R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2Q5R.started')
                # update status
                T2Q5R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T2Q5R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T2Q5R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T2Q5R.status == STARTED and not waitOnFlip:
                theseKeys = T2Q5R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T2Q5R_allKeys.extend(theseKeys)
                if len(_T2Q5R_allKeys):
                    T2Q5R.keys = _T2Q5R_allKeys[-1].name  # just the last key pressed
                    T2Q5R.rt = _T2Q5R_allKeys[-1].rt
                    T2Q5R.duration = _T2Q5R_allKeys[-1].duration
                    # was this correct?
                    if (T2Q5R.keys == str(CorrT2Q5)) or (T2Q5R.keys == CorrT2Q5):
                        T2Q5R.corr = 1
                    else:
                        T2Q5R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T2Q5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T2Q5" ---
        for thisComponent in T2Q5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T2Q5.stopped', globalClock.getTime())
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
            trials.addData('T2Q5R.duration', T2Q5R.duration)
        # the Routine "T2Q5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T2Q6" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T2Q6.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T2Q6" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T2I6* updates
            
            # if T2I6 is starting this frame...
            if T2I6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2I6.frameNStart = frameN  # exact frame index
                T2I6.tStart = t  # local t and not account for scr refresh
                T2I6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2I6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2I6.started')
                # update status
                T2I6.status = STARTED
                T2I6.setAutoDraw(True)
            
            # if T2I6 is active this frame...
            if T2I6.status == STARTED:
                # update params
                pass
            
            # *T2Q6R* updates
            waitOnFlip = False
            
            # if T2Q6R is starting this frame...
            if T2Q6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2Q6R.frameNStart = frameN  # exact frame index
                T2Q6R.tStart = t  # local t and not account for scr refresh
                T2Q6R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2Q6R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2Q6R.started')
                # update status
                T2Q6R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T2Q6R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T2Q6R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T2Q6R.status == STARTED and not waitOnFlip:
                theseKeys = T2Q6R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T2Q6R_allKeys.extend(theseKeys)
                if len(_T2Q6R_allKeys):
                    T2Q6R.keys = _T2Q6R_allKeys[-1].name  # just the last key pressed
                    T2Q6R.rt = _T2Q6R_allKeys[-1].rt
                    T2Q6R.duration = _T2Q6R_allKeys[-1].duration
                    # was this correct?
                    if (T2Q6R.keys == str(CorrT2Q6)) or (T2Q6R.keys == CorrT2Q6):
                        T2Q6R.corr = 1
                    else:
                        T2Q6R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T2Q6Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T2Q6" ---
        for thisComponent in T2Q6Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T2Q6.stopped', globalClock.getTime())
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
            trials.addData('T2Q6R.duration', T2Q6R.duration)
        # the Routine "T2Q6" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T2Q7" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T2Q7.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T2Q7" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T2I7* updates
            
            # if T2I7 is starting this frame...
            if T2I7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2I7.frameNStart = frameN  # exact frame index
                T2I7.tStart = t  # local t and not account for scr refresh
                T2I7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2I7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2I7.started')
                # update status
                T2I7.status = STARTED
                T2I7.setAutoDraw(True)
            
            # if T2I7 is active this frame...
            if T2I7.status == STARTED:
                # update params
                pass
            
            # *T2Q7R* updates
            waitOnFlip = False
            
            # if T2Q7R is starting this frame...
            if T2Q7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2Q7R.frameNStart = frameN  # exact frame index
                T2Q7R.tStart = t  # local t and not account for scr refresh
                T2Q7R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2Q7R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2Q7R.started')
                # update status
                T2Q7R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T2Q7R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T2Q7R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T2Q7R.status == STARTED and not waitOnFlip:
                theseKeys = T2Q7R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T2Q7R_allKeys.extend(theseKeys)
                if len(_T2Q7R_allKeys):
                    T2Q7R.keys = _T2Q7R_allKeys[-1].name  # just the last key pressed
                    T2Q7R.rt = _T2Q7R_allKeys[-1].rt
                    T2Q7R.duration = _T2Q7R_allKeys[-1].duration
                    # was this correct?
                    if (T2Q7R.keys == str(CorrT2Q7)) or (T2Q7R.keys == CorrT2Q7):
                        T2Q7R.corr = 1
                    else:
                        T2Q7R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T2Q7Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T2Q7" ---
        for thisComponent in T2Q7Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T2Q7.stopped', globalClock.getTime())
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
            trials.addData('T2Q7R.duration', T2Q7R.duration)
        # the Routine "T2Q7" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T2Q8" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T2Q8.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T2Q8" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T2I8* updates
            
            # if T2I8 is starting this frame...
            if T2I8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2I8.frameNStart = frameN  # exact frame index
                T2I8.tStart = t  # local t and not account for scr refresh
                T2I8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2I8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2I8.started')
                # update status
                T2I8.status = STARTED
                T2I8.setAutoDraw(True)
            
            # if T2I8 is active this frame...
            if T2I8.status == STARTED:
                # update params
                pass
            
            # *T2Q8R* updates
            waitOnFlip = False
            
            # if T2Q8R is starting this frame...
            if T2Q8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2Q8R.frameNStart = frameN  # exact frame index
                T2Q8R.tStart = t  # local t and not account for scr refresh
                T2Q8R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2Q8R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2Q8R.started')
                # update status
                T2Q8R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T2Q8R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T2Q8R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T2Q8R.status == STARTED and not waitOnFlip:
                theseKeys = T2Q8R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T2Q8R_allKeys.extend(theseKeys)
                if len(_T2Q8R_allKeys):
                    T2Q8R.keys = _T2Q8R_allKeys[-1].name  # just the last key pressed
                    T2Q8R.rt = _T2Q8R_allKeys[-1].rt
                    T2Q8R.duration = _T2Q8R_allKeys[-1].duration
                    # was this correct?
                    if (T2Q8R.keys == str(CorrT2Q8)) or (T2Q8R.keys == CorrT2Q8):
                        T2Q8R.corr = 1
                    else:
                        T2Q8R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T2Q8Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T2Q8" ---
        for thisComponent in T2Q8Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T2Q8.stopped', globalClock.getTime())
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
            trials.addData('T2Q8R.duration', T2Q8R.duration)
        # the Routine "T2Q8" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T2Q9" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T2Q9.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T2Q9" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T2I9* updates
            
            # if T2I9 is starting this frame...
            if T2I9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2I9.frameNStart = frameN  # exact frame index
                T2I9.tStart = t  # local t and not account for scr refresh
                T2I9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2I9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2I9.started')
                # update status
                T2I9.status = STARTED
                T2I9.setAutoDraw(True)
            
            # if T2I9 is active this frame...
            if T2I9.status == STARTED:
                # update params
                pass
            
            # *T2Q9R* updates
            waitOnFlip = False
            
            # if T2Q9R is starting this frame...
            if T2Q9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2Q9R.frameNStart = frameN  # exact frame index
                T2Q9R.tStart = t  # local t and not account for scr refresh
                T2Q9R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2Q9R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2Q9R.started')
                # update status
                T2Q9R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T2Q9R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T2Q9R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T2Q9R.status == STARTED and not waitOnFlip:
                theseKeys = T2Q9R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T2Q9R_allKeys.extend(theseKeys)
                if len(_T2Q9R_allKeys):
                    T2Q9R.keys = _T2Q9R_allKeys[-1].name  # just the last key pressed
                    T2Q9R.rt = _T2Q9R_allKeys[-1].rt
                    T2Q9R.duration = _T2Q9R_allKeys[-1].duration
                    # was this correct?
                    if (T2Q9R.keys == str(CorrT2Q9)) or (T2Q9R.keys == CorrT2Q9):
                        T2Q9R.corr = 1
                    else:
                        T2Q9R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T2Q9Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T2Q9" ---
        for thisComponent in T2Q9Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T2Q9.stopped', globalClock.getTime())
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
            trials.addData('T2Q9R.duration', T2Q9R.duration)
        # the Routine "T2Q9" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T2Q10" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T2Q10.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T2Q10" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T2I10* updates
            
            # if T2I10 is starting this frame...
            if T2I10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2I10.frameNStart = frameN  # exact frame index
                T2I10.tStart = t  # local t and not account for scr refresh
                T2I10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2I10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2I10.started')
                # update status
                T2I10.status = STARTED
                T2I10.setAutoDraw(True)
            
            # if T2I10 is active this frame...
            if T2I10.status == STARTED:
                # update params
                pass
            
            # *T2Q10R* updates
            waitOnFlip = False
            
            # if T2Q10R is starting this frame...
            if T2Q10R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T2Q10R.frameNStart = frameN  # exact frame index
                T2Q10R.tStart = t  # local t and not account for scr refresh
                T2Q10R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T2Q10R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T2Q10R.started')
                # update status
                T2Q10R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T2Q10R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T2Q10R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T2Q10R.status == STARTED and not waitOnFlip:
                theseKeys = T2Q10R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T2Q10R_allKeys.extend(theseKeys)
                if len(_T2Q10R_allKeys):
                    T2Q10R.keys = _T2Q10R_allKeys[-1].name  # just the last key pressed
                    T2Q10R.rt = _T2Q10R_allKeys[-1].rt
                    T2Q10R.duration = _T2Q10R_allKeys[-1].duration
                    # was this correct?
                    if (T2Q10R.keys == str(CorrT2Q10)) or (T2Q10R.keys == CorrT2Q10):
                        T2Q10R.corr = 1
                    else:
                        T2Q10R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T2Q10Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T2Q10" ---
        for thisComponent in T2Q10Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T2Q10.stopped', globalClock.getTime())
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
            trials.addData('T2Q10R.duration', T2Q10R.duration)
        # the Routine "T2Q10" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Trial_Break" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Trial_Break.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "Trial_Break" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Break_message* updates
            
            # if Break_message is starting this frame...
            if Break_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Break_message.frameNStart = frameN  # exact frame index
                Break_message.tStart = t  # local t and not account for scr refresh
                Break_message.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Break_message, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Break_message.started')
                # update status
                Break_message.status = STARTED
                Break_message.setAutoDraw(True)
            
            # if Break_message is active this frame...
            if Break_message.status == STARTED:
                # update params
                pass
            
            # *key_resp_4* updates
            waitOnFlip = False
            
            # if key_resp_4 is starting this frame...
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
                # update status
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_BreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial_Break" ---
        for thisComponent in Trial_BreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Trial_Break.stopped', globalClock.getTime())
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        trials.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials.addData('key_resp_4.rt', key_resp_4.rt)
            trials.addData('key_resp_4.duration', key_resp_4.duration)
        # the Routine "Trial_Break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T3A" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T3A.started', globalClock.getTime())
        sound_3.setSound(T3A, hamming=True)
        sound_3.setVolume(1.0, log=False)
        sound_3.seek(0)
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
        frameN = -1
        
        # --- Run Routine "T3A" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # if sound_3 is starting this frame...
            if sound_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_3.frameNStart = frameN  # exact frame index
                sound_3.tStart = t  # local t and not account for scr refresh
                sound_3.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_3.started', t)
                # update status
                sound_3.status = STARTED
                sound_3.play()  # start the sound (it finishes automatically)
            # update sound_3 status according to whether it's playing
            if sound_3.isPlaying:
                sound_3.status = STARTED
            elif sound_3.isFinished:
                sound_3.status = FINISHED
            
            # *image_3* updates
            
            # if image_3 is starting this frame...
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_3.started')
                # update status
                image_3.status = STARTED
                image_3.setAutoDraw(True)
            
            # if image_3 is active this frame...
            if image_3.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_3
            if sound_3.status == FINISHED:
                continueRoutine = False
            
            # *key_resp_10* updates
            waitOnFlip = False
            
            # if key_resp_10 is starting this frame...
            if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_10.frameNStart = frameN  # exact frame index
                key_resp_10.tStart = t  # local t and not account for scr refresh
                key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_10.started')
                # update status
                key_resp_10.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_10.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_10.getKeys(keyList=['z'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_10_allKeys.extend(theseKeys)
                if len(_key_resp_10_allKeys):
                    key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                    key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                    key_resp_10.duration = _key_resp_10_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T3AComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T3A" ---
        for thisComponent in T3AComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T3A.stopped', globalClock.getTime())
        sound_3.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if key_resp_10.keys in ['', [], None]:  # No response was made
            key_resp_10.keys = None
        trials.addData('key_resp_10.keys',key_resp_10.keys)
        if key_resp_10.keys != None:  # we had a response
            trials.addData('key_resp_10.rt', key_resp_10.rt)
            trials.addData('key_resp_10.duration', key_resp_10.duration)
        # the Routine "T3A" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Pre_assement_inst" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Pre_assement_inst.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "Pre_assement_inst" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_5* updates
            waitOnFlip = False
            
            # if key_resp_5 is starting this frame...
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                # update status
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pre_assement_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pre_assement_inst" ---
        for thisComponent in Pre_assement_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Pre_assement_inst.stopped', globalClock.getTime())
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        trials.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials.addData('key_resp_5.rt', key_resp_5.rt)
            trials.addData('key_resp_5.duration', key_resp_5.duration)
        # the Routine "Pre_assement_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T3Q1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T3Q1.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T3Q1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T3I1* updates
            
            # if T3I1 is starting this frame...
            if T3I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3I1.frameNStart = frameN  # exact frame index
                T3I1.tStart = t  # local t and not account for scr refresh
                T3I1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3I1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3I1.started')
                # update status
                T3I1.status = STARTED
                T3I1.setAutoDraw(True)
            
            # if T3I1 is active this frame...
            if T3I1.status == STARTED:
                # update params
                pass
            
            # *T3Q1R* updates
            waitOnFlip = False
            
            # if T3Q1R is starting this frame...
            if T3Q1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3Q1R.frameNStart = frameN  # exact frame index
                T3Q1R.tStart = t  # local t and not account for scr refresh
                T3Q1R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3Q1R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3Q1R.started')
                # update status
                T3Q1R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T3Q1R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T3Q1R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T3Q1R.status == STARTED and not waitOnFlip:
                theseKeys = T3Q1R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T3Q1R_allKeys.extend(theseKeys)
                if len(_T3Q1R_allKeys):
                    T3Q1R.keys = _T3Q1R_allKeys[-1].name  # just the last key pressed
                    T3Q1R.rt = _T3Q1R_allKeys[-1].rt
                    T3Q1R.duration = _T3Q1R_allKeys[-1].duration
                    # was this correct?
                    if (T3Q1R.keys == str(CorrT3Q1)) or (T3Q1R.keys == CorrT3Q1):
                        T3Q1R.corr = 1
                    else:
                        T3Q1R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T3Q1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T3Q1" ---
        for thisComponent in T3Q1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T3Q1.stopped', globalClock.getTime())
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
            trials.addData('T3Q1R.duration', T3Q1R.duration)
        # the Routine "T3Q1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T3Q2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T3Q2.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T3Q2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T3I2* updates
            
            # if T3I2 is starting this frame...
            if T3I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3I2.frameNStart = frameN  # exact frame index
                T3I2.tStart = t  # local t and not account for scr refresh
                T3I2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3I2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3I2.started')
                # update status
                T3I2.status = STARTED
                T3I2.setAutoDraw(True)
            
            # if T3I2 is active this frame...
            if T3I2.status == STARTED:
                # update params
                pass
            
            # *T3Q2R* updates
            waitOnFlip = False
            
            # if T3Q2R is starting this frame...
            if T3Q2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3Q2R.frameNStart = frameN  # exact frame index
                T3Q2R.tStart = t  # local t and not account for scr refresh
                T3Q2R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3Q2R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3Q2R.started')
                # update status
                T3Q2R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T3Q2R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T3Q2R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T3Q2R.status == STARTED and not waitOnFlip:
                theseKeys = T3Q2R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T3Q2R_allKeys.extend(theseKeys)
                if len(_T3Q2R_allKeys):
                    T3Q2R.keys = _T3Q2R_allKeys[-1].name  # just the last key pressed
                    T3Q2R.rt = _T3Q2R_allKeys[-1].rt
                    T3Q2R.duration = _T3Q2R_allKeys[-1].duration
                    # was this correct?
                    if (T3Q2R.keys == str(CorrT3Q2)) or (T3Q2R.keys == CorrT3Q2):
                        T3Q2R.corr = 1
                    else:
                        T3Q2R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T3Q2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T3Q2" ---
        for thisComponent in T3Q2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T3Q2.stopped', globalClock.getTime())
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
            trials.addData('T3Q2R.duration', T3Q2R.duration)
        # the Routine "T3Q2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T3Q3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T3Q3.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T3Q3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T3I3* updates
            
            # if T3I3 is starting this frame...
            if T3I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3I3.frameNStart = frameN  # exact frame index
                T3I3.tStart = t  # local t and not account for scr refresh
                T3I3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3I3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3I3.started')
                # update status
                T3I3.status = STARTED
                T3I3.setAutoDraw(True)
            
            # if T3I3 is active this frame...
            if T3I3.status == STARTED:
                # update params
                pass
            
            # *T3Q3R* updates
            waitOnFlip = False
            
            # if T3Q3R is starting this frame...
            if T3Q3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3Q3R.frameNStart = frameN  # exact frame index
                T3Q3R.tStart = t  # local t and not account for scr refresh
                T3Q3R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3Q3R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3Q3R.started')
                # update status
                T3Q3R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T3Q3R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T3Q3R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T3Q3R.status == STARTED and not waitOnFlip:
                theseKeys = T3Q3R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T3Q3R_allKeys.extend(theseKeys)
                if len(_T3Q3R_allKeys):
                    T3Q3R.keys = _T3Q3R_allKeys[-1].name  # just the last key pressed
                    T3Q3R.rt = _T3Q3R_allKeys[-1].rt
                    T3Q3R.duration = _T3Q3R_allKeys[-1].duration
                    # was this correct?
                    if (T3Q3R.keys == str(CorrT3Q3)) or (T3Q3R.keys == CorrT3Q3):
                        T3Q3R.corr = 1
                    else:
                        T3Q3R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T3Q3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T3Q3" ---
        for thisComponent in T3Q3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T3Q3.stopped', globalClock.getTime())
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
            trials.addData('T3Q3R.duration', T3Q3R.duration)
        # the Routine "T3Q3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T3Q4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T3Q4.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T3Q4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T3I4* updates
            
            # if T3I4 is starting this frame...
            if T3I4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3I4.frameNStart = frameN  # exact frame index
                T3I4.tStart = t  # local t and not account for scr refresh
                T3I4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3I4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3I4.started')
                # update status
                T3I4.status = STARTED
                T3I4.setAutoDraw(True)
            
            # if T3I4 is active this frame...
            if T3I4.status == STARTED:
                # update params
                pass
            
            # *T3Q4R* updates
            waitOnFlip = False
            
            # if T3Q4R is starting this frame...
            if T3Q4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3Q4R.frameNStart = frameN  # exact frame index
                T3Q4R.tStart = t  # local t and not account for scr refresh
                T3Q4R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3Q4R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3Q4R.started')
                # update status
                T3Q4R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T3Q4R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T3Q4R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T3Q4R.status == STARTED and not waitOnFlip:
                theseKeys = T3Q4R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T3Q4R_allKeys.extend(theseKeys)
                if len(_T3Q4R_allKeys):
                    T3Q4R.keys = _T3Q4R_allKeys[-1].name  # just the last key pressed
                    T3Q4R.rt = _T3Q4R_allKeys[-1].rt
                    T3Q4R.duration = _T3Q4R_allKeys[-1].duration
                    # was this correct?
                    if (T3Q4R.keys == str(CorrT3Q4)) or (T3Q4R.keys == CorrT3Q4):
                        T3Q4R.corr = 1
                    else:
                        T3Q4R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T3Q4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T3Q4" ---
        for thisComponent in T3Q4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T3Q4.stopped', globalClock.getTime())
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
            trials.addData('T3Q4R.duration', T3Q4R.duration)
        # the Routine "T3Q4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T3Q5" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T3Q5.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T3Q5" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T3I5* updates
            
            # if T3I5 is starting this frame...
            if T3I5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3I5.frameNStart = frameN  # exact frame index
                T3I5.tStart = t  # local t and not account for scr refresh
                T3I5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3I5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3I5.started')
                # update status
                T3I5.status = STARTED
                T3I5.setAutoDraw(True)
            
            # if T3I5 is active this frame...
            if T3I5.status == STARTED:
                # update params
                pass
            
            # *T3Q5R* updates
            waitOnFlip = False
            
            # if T3Q5R is starting this frame...
            if T3Q5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3Q5R.frameNStart = frameN  # exact frame index
                T3Q5R.tStart = t  # local t and not account for scr refresh
                T3Q5R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3Q5R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3Q5R.started')
                # update status
                T3Q5R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T3Q5R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T3Q5R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T3Q5R.status == STARTED and not waitOnFlip:
                theseKeys = T3Q5R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T3Q5R_allKeys.extend(theseKeys)
                if len(_T3Q5R_allKeys):
                    T3Q5R.keys = _T3Q5R_allKeys[-1].name  # just the last key pressed
                    T3Q5R.rt = _T3Q5R_allKeys[-1].rt
                    T3Q5R.duration = _T3Q5R_allKeys[-1].duration
                    # was this correct?
                    if (T3Q5R.keys == str(CorrT3Q5)) or (T3Q5R.keys == CorrT3Q5):
                        T3Q5R.corr = 1
                    else:
                        T3Q5R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T3Q5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T3Q5" ---
        for thisComponent in T3Q5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T3Q5.stopped', globalClock.getTime())
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
            trials.addData('T3Q5R.duration', T3Q5R.duration)
        # the Routine "T3Q5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T3Q6" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T3Q6.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T3Q6" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T3I6* updates
            
            # if T3I6 is starting this frame...
            if T3I6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3I6.frameNStart = frameN  # exact frame index
                T3I6.tStart = t  # local t and not account for scr refresh
                T3I6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3I6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3I6.started')
                # update status
                T3I6.status = STARTED
                T3I6.setAutoDraw(True)
            
            # if T3I6 is active this frame...
            if T3I6.status == STARTED:
                # update params
                pass
            
            # *T3Q6R* updates
            waitOnFlip = False
            
            # if T3Q6R is starting this frame...
            if T3Q6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3Q6R.frameNStart = frameN  # exact frame index
                T3Q6R.tStart = t  # local t and not account for scr refresh
                T3Q6R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3Q6R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3Q6R.started')
                # update status
                T3Q6R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T3Q6R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T3Q6R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T3Q6R.status == STARTED and not waitOnFlip:
                theseKeys = T3Q6R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T3Q6R_allKeys.extend(theseKeys)
                if len(_T3Q6R_allKeys):
                    T3Q6R.keys = _T3Q6R_allKeys[-1].name  # just the last key pressed
                    T3Q6R.rt = _T3Q6R_allKeys[-1].rt
                    T3Q6R.duration = _T3Q6R_allKeys[-1].duration
                    # was this correct?
                    if (T3Q6R.keys == str(CorrT3Q6)) or (T3Q6R.keys == CorrT3Q6):
                        T3Q6R.corr = 1
                    else:
                        T3Q6R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T3Q6Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T3Q6" ---
        for thisComponent in T3Q6Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T3Q6.stopped', globalClock.getTime())
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
            trials.addData('T3Q6R.duration', T3Q6R.duration)
        # the Routine "T3Q6" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T3Q7" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T3Q7.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T3Q7" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T3I7* updates
            
            # if T3I7 is starting this frame...
            if T3I7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3I7.frameNStart = frameN  # exact frame index
                T3I7.tStart = t  # local t and not account for scr refresh
                T3I7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3I7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3I7.started')
                # update status
                T3I7.status = STARTED
                T3I7.setAutoDraw(True)
            
            # if T3I7 is active this frame...
            if T3I7.status == STARTED:
                # update params
                pass
            
            # *T3Q7R* updates
            waitOnFlip = False
            
            # if T3Q7R is starting this frame...
            if T3Q7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3Q7R.frameNStart = frameN  # exact frame index
                T3Q7R.tStart = t  # local t and not account for scr refresh
                T3Q7R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3Q7R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3Q7R.started')
                # update status
                T3Q7R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T3Q7R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T3Q7R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T3Q7R.status == STARTED and not waitOnFlip:
                theseKeys = T3Q7R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T3Q7R_allKeys.extend(theseKeys)
                if len(_T3Q7R_allKeys):
                    T3Q7R.keys = _T3Q7R_allKeys[-1].name  # just the last key pressed
                    T3Q7R.rt = _T3Q7R_allKeys[-1].rt
                    T3Q7R.duration = _T3Q7R_allKeys[-1].duration
                    # was this correct?
                    if (T3Q7R.keys == str(CorrT3Q7)) or (T3Q7R.keys == CorrT3Q7):
                        T3Q7R.corr = 1
                    else:
                        T3Q7R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T3Q7Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T3Q7" ---
        for thisComponent in T3Q7Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T3Q7.stopped', globalClock.getTime())
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
            trials.addData('T3Q7R.duration', T3Q7R.duration)
        # the Routine "T3Q7" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T3Q8" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T3Q8.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T3Q8" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T3I8* updates
            
            # if T3I8 is starting this frame...
            if T3I8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3I8.frameNStart = frameN  # exact frame index
                T3I8.tStart = t  # local t and not account for scr refresh
                T3I8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3I8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3I8.started')
                # update status
                T3I8.status = STARTED
                T3I8.setAutoDraw(True)
            
            # if T3I8 is active this frame...
            if T3I8.status == STARTED:
                # update params
                pass
            
            # *T3Q8R* updates
            waitOnFlip = False
            
            # if T3Q8R is starting this frame...
            if T3Q8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3Q8R.frameNStart = frameN  # exact frame index
                T3Q8R.tStart = t  # local t and not account for scr refresh
                T3Q8R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3Q8R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3Q8R.started')
                # update status
                T3Q8R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T3Q8R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T3Q8R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T3Q8R.status == STARTED and not waitOnFlip:
                theseKeys = T3Q8R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T3Q8R_allKeys.extend(theseKeys)
                if len(_T3Q8R_allKeys):
                    T3Q8R.keys = _T3Q8R_allKeys[-1].name  # just the last key pressed
                    T3Q8R.rt = _T3Q8R_allKeys[-1].rt
                    T3Q8R.duration = _T3Q8R_allKeys[-1].duration
                    # was this correct?
                    if (T3Q8R.keys == str(CorrT3Q8)) or (T3Q8R.keys == CorrT3Q8):
                        T3Q8R.corr = 1
                    else:
                        T3Q8R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T3Q8Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T3Q8" ---
        for thisComponent in T3Q8Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T3Q8.stopped', globalClock.getTime())
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
            trials.addData('T3Q8R.duration', T3Q8R.duration)
        # the Routine "T3Q8" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T3Q9" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T3Q9.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T3Q9" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T3I9* updates
            
            # if T3I9 is starting this frame...
            if T3I9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3I9.frameNStart = frameN  # exact frame index
                T3I9.tStart = t  # local t and not account for scr refresh
                T3I9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3I9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3I9.started')
                # update status
                T3I9.status = STARTED
                T3I9.setAutoDraw(True)
            
            # if T3I9 is active this frame...
            if T3I9.status == STARTED:
                # update params
                pass
            
            # *T3Q9R* updates
            waitOnFlip = False
            
            # if T3Q9R is starting this frame...
            if T3Q9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3Q9R.frameNStart = frameN  # exact frame index
                T3Q9R.tStart = t  # local t and not account for scr refresh
                T3Q9R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3Q9R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3Q9R.started')
                # update status
                T3Q9R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T3Q9R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T3Q9R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T3Q9R.status == STARTED and not waitOnFlip:
                theseKeys = T3Q9R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T3Q9R_allKeys.extend(theseKeys)
                if len(_T3Q9R_allKeys):
                    T3Q9R.keys = _T3Q9R_allKeys[-1].name  # just the last key pressed
                    T3Q9R.rt = _T3Q9R_allKeys[-1].rt
                    T3Q9R.duration = _T3Q9R_allKeys[-1].duration
                    # was this correct?
                    if (T3Q9R.keys == str(CorrT3Q9)) or (T3Q9R.keys == CorrT3Q9):
                        T3Q9R.corr = 1
                    else:
                        T3Q9R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T3Q9Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T3Q9" ---
        for thisComponent in T3Q9Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T3Q9.stopped', globalClock.getTime())
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
            trials.addData('T3Q9R.duration', T3Q9R.duration)
        # the Routine "T3Q9" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T3Q10" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T3Q10.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T3Q10" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T3I10* updates
            
            # if T3I10 is starting this frame...
            if T3I10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3I10.frameNStart = frameN  # exact frame index
                T3I10.tStart = t  # local t and not account for scr refresh
                T3I10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3I10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3I10.started')
                # update status
                T3I10.status = STARTED
                T3I10.setAutoDraw(True)
            
            # if T3I10 is active this frame...
            if T3I10.status == STARTED:
                # update params
                pass
            
            # *T3Q10R* updates
            waitOnFlip = False
            
            # if T3Q10R is starting this frame...
            if T3Q10R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T3Q10R.frameNStart = frameN  # exact frame index
                T3Q10R.tStart = t  # local t and not account for scr refresh
                T3Q10R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T3Q10R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T3Q10R.started')
                # update status
                T3Q10R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T3Q10R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T3Q10R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T3Q10R.status == STARTED and not waitOnFlip:
                theseKeys = T3Q10R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T3Q10R_allKeys.extend(theseKeys)
                if len(_T3Q10R_allKeys):
                    T3Q10R.keys = _T3Q10R_allKeys[-1].name  # just the last key pressed
                    T3Q10R.rt = _T3Q10R_allKeys[-1].rt
                    T3Q10R.duration = _T3Q10R_allKeys[-1].duration
                    # was this correct?
                    if (T3Q10R.keys == str(CorrT3Q10)) or (T3Q10R.keys == CorrT3Q10):
                        T3Q10R.corr = 1
                    else:
                        T3Q10R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T3Q10Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T3Q10" ---
        for thisComponent in T3Q10Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T3Q10.stopped', globalClock.getTime())
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
            trials.addData('T3Q10R.duration', T3Q10R.duration)
        # the Routine "T3Q10" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Trial_Break" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Trial_Break.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "Trial_Break" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Break_message* updates
            
            # if Break_message is starting this frame...
            if Break_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Break_message.frameNStart = frameN  # exact frame index
                Break_message.tStart = t  # local t and not account for scr refresh
                Break_message.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Break_message, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Break_message.started')
                # update status
                Break_message.status = STARTED
                Break_message.setAutoDraw(True)
            
            # if Break_message is active this frame...
            if Break_message.status == STARTED:
                # update params
                pass
            
            # *key_resp_4* updates
            waitOnFlip = False
            
            # if key_resp_4 is starting this frame...
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
                # update status
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_BreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial_Break" ---
        for thisComponent in Trial_BreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Trial_Break.stopped', globalClock.getTime())
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        trials.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials.addData('key_resp_4.rt', key_resp_4.rt)
            trials.addData('key_resp_4.duration', key_resp_4.duration)
        # the Routine "Trial_Break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T4A" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T4A.started', globalClock.getTime())
        sound_4.setSound(T4A, hamming=True)
        sound_4.setVolume(1.0, log=False)
        sound_4.seek(0)
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
        frameN = -1
        
        # --- Run Routine "T4A" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # if sound_4 is starting this frame...
            if sound_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_4.frameNStart = frameN  # exact frame index
                sound_4.tStart = t  # local t and not account for scr refresh
                sound_4.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_4.started', t)
                # update status
                sound_4.status = STARTED
                sound_4.play()  # start the sound (it finishes automatically)
            # update sound_4 status according to whether it's playing
            if sound_4.isPlaying:
                sound_4.status = STARTED
            elif sound_4.isFinished:
                sound_4.status = FINISHED
            
            # *image_4* updates
            
            # if image_4 is starting this frame...
            if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_4.frameNStart = frameN  # exact frame index
                image_4.tStart = t  # local t and not account for scr refresh
                image_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_4.started')
                # update status
                image_4.status = STARTED
                image_4.setAutoDraw(True)
            
            # if image_4 is active this frame...
            if image_4.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_4
            if sound_4.status == FINISHED:
                continueRoutine = False
            
            # *key_resp_9* updates
            waitOnFlip = False
            
            # if key_resp_9 is starting this frame...
            if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_9.frameNStart = frameN  # exact frame index
                key_resp_9.tStart = t  # local t and not account for scr refresh
                key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_9.started')
                # update status
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_9.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_9.getKeys(keyList=['z'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_9_allKeys.extend(theseKeys)
                if len(_key_resp_9_allKeys):
                    key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                    key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                    key_resp_9.duration = _key_resp_9_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T4AComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T4A" ---
        for thisComponent in T4AComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T4A.stopped', globalClock.getTime())
        sound_4.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if key_resp_9.keys in ['', [], None]:  # No response was made
            key_resp_9.keys = None
        trials.addData('key_resp_9.keys',key_resp_9.keys)
        if key_resp_9.keys != None:  # we had a response
            trials.addData('key_resp_9.rt', key_resp_9.rt)
            trials.addData('key_resp_9.duration', key_resp_9.duration)
        # the Routine "T4A" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Pre_assement_inst" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Pre_assement_inst.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "Pre_assement_inst" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_5* updates
            waitOnFlip = False
            
            # if key_resp_5 is starting this frame...
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                # update status
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pre_assement_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pre_assement_inst" ---
        for thisComponent in Pre_assement_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Pre_assement_inst.stopped', globalClock.getTime())
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        trials.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials.addData('key_resp_5.rt', key_resp_5.rt)
            trials.addData('key_resp_5.duration', key_resp_5.duration)
        # the Routine "Pre_assement_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T4Q1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T4Q1.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T4Q1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T4I1* updates
            
            # if T4I1 is starting this frame...
            if T4I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4I1.frameNStart = frameN  # exact frame index
                T4I1.tStart = t  # local t and not account for scr refresh
                T4I1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4I1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4I1.started')
                # update status
                T4I1.status = STARTED
                T4I1.setAutoDraw(True)
            
            # if T4I1 is active this frame...
            if T4I1.status == STARTED:
                # update params
                pass
            
            # *T4Q1R* updates
            waitOnFlip = False
            
            # if T4Q1R is starting this frame...
            if T4Q1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4Q1R.frameNStart = frameN  # exact frame index
                T4Q1R.tStart = t  # local t and not account for scr refresh
                T4Q1R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4Q1R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4Q1R.started')
                # update status
                T4Q1R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T4Q1R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T4Q1R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T4Q1R.status == STARTED and not waitOnFlip:
                theseKeys = T4Q1R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T4Q1R_allKeys.extend(theseKeys)
                if len(_T4Q1R_allKeys):
                    T4Q1R.keys = _T4Q1R_allKeys[-1].name  # just the last key pressed
                    T4Q1R.rt = _T4Q1R_allKeys[-1].rt
                    T4Q1R.duration = _T4Q1R_allKeys[-1].duration
                    # was this correct?
                    if (T4Q1R.keys == str(CorrT4Q1)) or (T4Q1R.keys == CorrT4Q1):
                        T4Q1R.corr = 1
                    else:
                        T4Q1R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T4Q1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T4Q1" ---
        for thisComponent in T4Q1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T4Q1.stopped', globalClock.getTime())
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
            trials.addData('T4Q1R.duration', T4Q1R.duration)
        # the Routine "T4Q1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T4Q2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T4Q2.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T4Q2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T4I2* updates
            
            # if T4I2 is starting this frame...
            if T4I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4I2.frameNStart = frameN  # exact frame index
                T4I2.tStart = t  # local t and not account for scr refresh
                T4I2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4I2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4I2.started')
                # update status
                T4I2.status = STARTED
                T4I2.setAutoDraw(True)
            
            # if T4I2 is active this frame...
            if T4I2.status == STARTED:
                # update params
                pass
            
            # *T4Q2R* updates
            waitOnFlip = False
            
            # if T4Q2R is starting this frame...
            if T4Q2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4Q2R.frameNStart = frameN  # exact frame index
                T4Q2R.tStart = t  # local t and not account for scr refresh
                T4Q2R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4Q2R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4Q2R.started')
                # update status
                T4Q2R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T4Q2R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T4Q2R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T4Q2R.status == STARTED and not waitOnFlip:
                theseKeys = T4Q2R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T4Q2R_allKeys.extend(theseKeys)
                if len(_T4Q2R_allKeys):
                    T4Q2R.keys = _T4Q2R_allKeys[-1].name  # just the last key pressed
                    T4Q2R.rt = _T4Q2R_allKeys[-1].rt
                    T4Q2R.duration = _T4Q2R_allKeys[-1].duration
                    # was this correct?
                    if (T4Q2R.keys == str(CorrT4Q2)) or (T4Q2R.keys == CorrT4Q2):
                        T4Q2R.corr = 1
                    else:
                        T4Q2R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T4Q2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T4Q2" ---
        for thisComponent in T4Q2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T4Q2.stopped', globalClock.getTime())
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
            trials.addData('T4Q2R.duration', T4Q2R.duration)
        # the Routine "T4Q2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T4Q3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T4Q3.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T4Q3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T4I3* updates
            
            # if T4I3 is starting this frame...
            if T4I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4I3.frameNStart = frameN  # exact frame index
                T4I3.tStart = t  # local t and not account for scr refresh
                T4I3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4I3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4I3.started')
                # update status
                T4I3.status = STARTED
                T4I3.setAutoDraw(True)
            
            # if T4I3 is active this frame...
            if T4I3.status == STARTED:
                # update params
                pass
            
            # *T4Q3R* updates
            waitOnFlip = False
            
            # if T4Q3R is starting this frame...
            if T4Q3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4Q3R.frameNStart = frameN  # exact frame index
                T4Q3R.tStart = t  # local t and not account for scr refresh
                T4Q3R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4Q3R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4Q3R.started')
                # update status
                T4Q3R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T4Q3R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T4Q3R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T4Q3R.status == STARTED and not waitOnFlip:
                theseKeys = T4Q3R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T4Q3R_allKeys.extend(theseKeys)
                if len(_T4Q3R_allKeys):
                    T4Q3R.keys = _T4Q3R_allKeys[-1].name  # just the last key pressed
                    T4Q3R.rt = _T4Q3R_allKeys[-1].rt
                    T4Q3R.duration = _T4Q3R_allKeys[-1].duration
                    # was this correct?
                    if (T4Q3R.keys == str(CorrT4Q3)) or (T4Q3R.keys == CorrT4Q3):
                        T4Q3R.corr = 1
                    else:
                        T4Q3R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T4Q3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T4Q3" ---
        for thisComponent in T4Q3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T4Q3.stopped', globalClock.getTime())
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
            trials.addData('T4Q3R.duration', T4Q3R.duration)
        # the Routine "T4Q3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T4Q4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T4Q4.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T4Q4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T4I4* updates
            
            # if T4I4 is starting this frame...
            if T4I4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4I4.frameNStart = frameN  # exact frame index
                T4I4.tStart = t  # local t and not account for scr refresh
                T4I4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4I4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4I4.started')
                # update status
                T4I4.status = STARTED
                T4I4.setAutoDraw(True)
            
            # if T4I4 is active this frame...
            if T4I4.status == STARTED:
                # update params
                pass
            
            # *T4Q4R* updates
            waitOnFlip = False
            
            # if T4Q4R is starting this frame...
            if T4Q4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4Q4R.frameNStart = frameN  # exact frame index
                T4Q4R.tStart = t  # local t and not account for scr refresh
                T4Q4R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4Q4R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4Q4R.started')
                # update status
                T4Q4R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T4Q4R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T4Q4R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T4Q4R.status == STARTED and not waitOnFlip:
                theseKeys = T4Q4R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T4Q4R_allKeys.extend(theseKeys)
                if len(_T4Q4R_allKeys):
                    T4Q4R.keys = _T4Q4R_allKeys[-1].name  # just the last key pressed
                    T4Q4R.rt = _T4Q4R_allKeys[-1].rt
                    T4Q4R.duration = _T4Q4R_allKeys[-1].duration
                    # was this correct?
                    if (T4Q4R.keys == str(CorrT4Q4)) or (T4Q4R.keys == CorrT4Q4):
                        T4Q4R.corr = 1
                    else:
                        T4Q4R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T4Q4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T4Q4" ---
        for thisComponent in T4Q4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T4Q4.stopped', globalClock.getTime())
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
            trials.addData('T4Q4R.duration', T4Q4R.duration)
        # the Routine "T4Q4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T4Q5" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T4Q5.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T4Q5" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T4I5* updates
            
            # if T4I5 is starting this frame...
            if T4I5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4I5.frameNStart = frameN  # exact frame index
                T4I5.tStart = t  # local t and not account for scr refresh
                T4I5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4I5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4I5.started')
                # update status
                T4I5.status = STARTED
                T4I5.setAutoDraw(True)
            
            # if T4I5 is active this frame...
            if T4I5.status == STARTED:
                # update params
                pass
            
            # *T4Q5R* updates
            waitOnFlip = False
            
            # if T4Q5R is starting this frame...
            if T4Q5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4Q5R.frameNStart = frameN  # exact frame index
                T4Q5R.tStart = t  # local t and not account for scr refresh
                T4Q5R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4Q5R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4Q5R.started')
                # update status
                T4Q5R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T4Q5R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T4Q5R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T4Q5R.status == STARTED and not waitOnFlip:
                theseKeys = T4Q5R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T4Q5R_allKeys.extend(theseKeys)
                if len(_T4Q5R_allKeys):
                    T4Q5R.keys = _T4Q5R_allKeys[-1].name  # just the last key pressed
                    T4Q5R.rt = _T4Q5R_allKeys[-1].rt
                    T4Q5R.duration = _T4Q5R_allKeys[-1].duration
                    # was this correct?
                    if (T4Q5R.keys == str(CorrT4Q5)) or (T4Q5R.keys == CorrT4Q5):
                        T4Q5R.corr = 1
                    else:
                        T4Q5R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T4Q5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T4Q5" ---
        for thisComponent in T4Q5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T4Q5.stopped', globalClock.getTime())
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
            trials.addData('T4Q5R.duration', T4Q5R.duration)
        # the Routine "T4Q5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T4Q6" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T4Q6.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T4Q6" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T4I6* updates
            
            # if T4I6 is starting this frame...
            if T4I6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4I6.frameNStart = frameN  # exact frame index
                T4I6.tStart = t  # local t and not account for scr refresh
                T4I6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4I6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4I6.started')
                # update status
                T4I6.status = STARTED
                T4I6.setAutoDraw(True)
            
            # if T4I6 is active this frame...
            if T4I6.status == STARTED:
                # update params
                pass
            
            # *T4Q6R* updates
            waitOnFlip = False
            
            # if T4Q6R is starting this frame...
            if T4Q6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4Q6R.frameNStart = frameN  # exact frame index
                T4Q6R.tStart = t  # local t and not account for scr refresh
                T4Q6R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4Q6R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4Q6R.started')
                # update status
                T4Q6R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T4Q6R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T4Q6R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T4Q6R.status == STARTED and not waitOnFlip:
                theseKeys = T4Q6R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T4Q6R_allKeys.extend(theseKeys)
                if len(_T4Q6R_allKeys):
                    T4Q6R.keys = _T4Q6R_allKeys[-1].name  # just the last key pressed
                    T4Q6R.rt = _T4Q6R_allKeys[-1].rt
                    T4Q6R.duration = _T4Q6R_allKeys[-1].duration
                    # was this correct?
                    if (T4Q6R.keys == str(CorrT4Q6)) or (T4Q6R.keys == CorrT4Q6):
                        T4Q6R.corr = 1
                    else:
                        T4Q6R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T4Q6Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T4Q6" ---
        for thisComponent in T4Q6Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T4Q6.stopped', globalClock.getTime())
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
            trials.addData('T4Q6R.duration', T4Q6R.duration)
        # the Routine "T4Q6" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T4Q7" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T4Q7.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T4Q7" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T4I7* updates
            
            # if T4I7 is starting this frame...
            if T4I7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4I7.frameNStart = frameN  # exact frame index
                T4I7.tStart = t  # local t and not account for scr refresh
                T4I7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4I7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4I7.started')
                # update status
                T4I7.status = STARTED
                T4I7.setAutoDraw(True)
            
            # if T4I7 is active this frame...
            if T4I7.status == STARTED:
                # update params
                pass
            
            # *T4Q7R* updates
            waitOnFlip = False
            
            # if T4Q7R is starting this frame...
            if T4Q7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4Q7R.frameNStart = frameN  # exact frame index
                T4Q7R.tStart = t  # local t and not account for scr refresh
                T4Q7R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4Q7R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4Q7R.started')
                # update status
                T4Q7R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T4Q7R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T4Q7R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T4Q7R.status == STARTED and not waitOnFlip:
                theseKeys = T4Q7R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T4Q7R_allKeys.extend(theseKeys)
                if len(_T4Q7R_allKeys):
                    T4Q7R.keys = _T4Q7R_allKeys[-1].name  # just the last key pressed
                    T4Q7R.rt = _T4Q7R_allKeys[-1].rt
                    T4Q7R.duration = _T4Q7R_allKeys[-1].duration
                    # was this correct?
                    if (T4Q7R.keys == str(CorrT4Q7)) or (T4Q7R.keys == CorrT4Q7):
                        T4Q7R.corr = 1
                    else:
                        T4Q7R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T4Q7Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T4Q7" ---
        for thisComponent in T4Q7Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T4Q7.stopped', globalClock.getTime())
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
            trials.addData('T4Q7R.duration', T4Q7R.duration)
        # the Routine "T4Q7" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T4Q8" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T4Q8.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T4Q8" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T4I8* updates
            
            # if T4I8 is starting this frame...
            if T4I8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4I8.frameNStart = frameN  # exact frame index
                T4I8.tStart = t  # local t and not account for scr refresh
                T4I8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4I8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4I8.started')
                # update status
                T4I8.status = STARTED
                T4I8.setAutoDraw(True)
            
            # if T4I8 is active this frame...
            if T4I8.status == STARTED:
                # update params
                pass
            
            # *T4Q8R* updates
            waitOnFlip = False
            
            # if T4Q8R is starting this frame...
            if T4Q8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4Q8R.frameNStart = frameN  # exact frame index
                T4Q8R.tStart = t  # local t and not account for scr refresh
                T4Q8R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4Q8R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4Q8R.started')
                # update status
                T4Q8R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T4Q8R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T4Q8R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T4Q8R.status == STARTED and not waitOnFlip:
                theseKeys = T4Q8R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T4Q8R_allKeys.extend(theseKeys)
                if len(_T4Q8R_allKeys):
                    T4Q8R.keys = _T4Q8R_allKeys[-1].name  # just the last key pressed
                    T4Q8R.rt = _T4Q8R_allKeys[-1].rt
                    T4Q8R.duration = _T4Q8R_allKeys[-1].duration
                    # was this correct?
                    if (T4Q8R.keys == str(CorrT4Q8)) or (T4Q8R.keys == CorrT4Q8):
                        T4Q8R.corr = 1
                    else:
                        T4Q8R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T4Q8Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T4Q8" ---
        for thisComponent in T4Q8Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T4Q8.stopped', globalClock.getTime())
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
            trials.addData('T4Q8R.duration', T4Q8R.duration)
        # the Routine "T4Q8" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T4Q9" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T4Q9.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T4Q9" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T4I9* updates
            
            # if T4I9 is starting this frame...
            if T4I9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4I9.frameNStart = frameN  # exact frame index
                T4I9.tStart = t  # local t and not account for scr refresh
                T4I9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4I9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4I9.started')
                # update status
                T4I9.status = STARTED
                T4I9.setAutoDraw(True)
            
            # if T4I9 is active this frame...
            if T4I9.status == STARTED:
                # update params
                pass
            
            # *T4Q9R* updates
            waitOnFlip = False
            
            # if T4Q9R is starting this frame...
            if T4Q9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4Q9R.frameNStart = frameN  # exact frame index
                T4Q9R.tStart = t  # local t and not account for scr refresh
                T4Q9R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4Q9R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4Q9R.started')
                # update status
                T4Q9R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T4Q9R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T4Q9R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T4Q9R.status == STARTED and not waitOnFlip:
                theseKeys = T4Q9R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T4Q9R_allKeys.extend(theseKeys)
                if len(_T4Q9R_allKeys):
                    T4Q9R.keys = _T4Q9R_allKeys[-1].name  # just the last key pressed
                    T4Q9R.rt = _T4Q9R_allKeys[-1].rt
                    T4Q9R.duration = _T4Q9R_allKeys[-1].duration
                    # was this correct?
                    if (T4Q9R.keys == str(CorrT4Q9)) or (T4Q9R.keys == CorrT4Q9):
                        T4Q9R.corr = 1
                    else:
                        T4Q9R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T4Q9Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T4Q9" ---
        for thisComponent in T4Q9Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T4Q9.stopped', globalClock.getTime())
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
            trials.addData('T4Q9R.duration', T4Q9R.duration)
        # the Routine "T4Q9" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T4Q10" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T4Q10.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T4Q10" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T4I10* updates
            
            # if T4I10 is starting this frame...
            if T4I10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4I10.frameNStart = frameN  # exact frame index
                T4I10.tStart = t  # local t and not account for scr refresh
                T4I10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4I10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4I10.started')
                # update status
                T4I10.status = STARTED
                T4I10.setAutoDraw(True)
            
            # if T4I10 is active this frame...
            if T4I10.status == STARTED:
                # update params
                pass
            
            # *T4Q10R* updates
            waitOnFlip = False
            
            # if T4Q10R is starting this frame...
            if T4Q10R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T4Q10R.frameNStart = frameN  # exact frame index
                T4Q10R.tStart = t  # local t and not account for scr refresh
                T4Q10R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T4Q10R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T4Q10R.started')
                # update status
                T4Q10R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T4Q10R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T4Q10R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T4Q10R.status == STARTED and not waitOnFlip:
                theseKeys = T4Q10R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T4Q10R_allKeys.extend(theseKeys)
                if len(_T4Q10R_allKeys):
                    T4Q10R.keys = _T4Q10R_allKeys[-1].name  # just the last key pressed
                    T4Q10R.rt = _T4Q10R_allKeys[-1].rt
                    T4Q10R.duration = _T4Q10R_allKeys[-1].duration
                    # was this correct?
                    if (T4Q10R.keys == str(CorrT4Q10)) or (T4Q10R.keys == CorrT4Q10):
                        T4Q10R.corr = 1
                    else:
                        T4Q10R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T4Q10Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T4Q10" ---
        for thisComponent in T4Q10Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T4Q10.stopped', globalClock.getTime())
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
            trials.addData('T4Q10R.duration', T4Q10R.duration)
        # the Routine "T4Q10" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Trial_Break" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Trial_Break.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "Trial_Break" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Break_message* updates
            
            # if Break_message is starting this frame...
            if Break_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Break_message.frameNStart = frameN  # exact frame index
                Break_message.tStart = t  # local t and not account for scr refresh
                Break_message.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Break_message, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Break_message.started')
                # update status
                Break_message.status = STARTED
                Break_message.setAutoDraw(True)
            
            # if Break_message is active this frame...
            if Break_message.status == STARTED:
                # update params
                pass
            
            # *key_resp_4* updates
            waitOnFlip = False
            
            # if key_resp_4 is starting this frame...
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
                # update status
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_BreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial_Break" ---
        for thisComponent in Trial_BreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Trial_Break.stopped', globalClock.getTime())
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        trials.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials.addData('key_resp_4.rt', key_resp_4.rt)
            trials.addData('key_resp_4.duration', key_resp_4.duration)
        # the Routine "Trial_Break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T5A" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T5A.started', globalClock.getTime())
        sound_5.setSound(T5A, hamming=True)
        sound_5.setVolume(1.0, log=False)
        sound_5.seek(0)
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
        frameN = -1
        
        # --- Run Routine "T5A" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # if sound_5 is starting this frame...
            if sound_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_5.frameNStart = frameN  # exact frame index
                sound_5.tStart = t  # local t and not account for scr refresh
                sound_5.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_5.started', t)
                # update status
                sound_5.status = STARTED
                sound_5.play()  # start the sound (it finishes automatically)
            # update sound_5 status according to whether it's playing
            if sound_5.isPlaying:
                sound_5.status = STARTED
            elif sound_5.isFinished:
                sound_5.status = FINISHED
            
            # *image_5* updates
            
            # if image_5 is starting this frame...
            if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_5.frameNStart = frameN  # exact frame index
                image_5.tStart = t  # local t and not account for scr refresh
                image_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_5.started')
                # update status
                image_5.status = STARTED
                image_5.setAutoDraw(True)
            
            # if image_5 is active this frame...
            if image_5.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_5
            if sound_5.status == FINISHED:
                continueRoutine = False
            
            # *key_resp_8* updates
            waitOnFlip = False
            
            # if key_resp_8 is starting this frame...
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_8.started')
                # update status
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['z'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                    key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                    key_resp_8.duration = _key_resp_8_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T5AComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T5A" ---
        for thisComponent in T5AComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T5A.stopped', globalClock.getTime())
        sound_5.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
        trials.addData('key_resp_8.keys',key_resp_8.keys)
        if key_resp_8.keys != None:  # we had a response
            trials.addData('key_resp_8.rt', key_resp_8.rt)
            trials.addData('key_resp_8.duration', key_resp_8.duration)
        # the Routine "T5A" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Pre_assement_inst" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Pre_assement_inst.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "Pre_assement_inst" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_5* updates
            waitOnFlip = False
            
            # if key_resp_5 is starting this frame...
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                # update status
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pre_assement_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pre_assement_inst" ---
        for thisComponent in Pre_assement_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Pre_assement_inst.stopped', globalClock.getTime())
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        trials.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials.addData('key_resp_5.rt', key_resp_5.rt)
            trials.addData('key_resp_5.duration', key_resp_5.duration)
        # the Routine "Pre_assement_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T5Q1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T5Q1.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T5Q1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T5I1* updates
            
            # if T5I1 is starting this frame...
            if T5I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5I1.frameNStart = frameN  # exact frame index
                T5I1.tStart = t  # local t and not account for scr refresh
                T5I1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5I1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5I1.started')
                # update status
                T5I1.status = STARTED
                T5I1.setAutoDraw(True)
            
            # if T5I1 is active this frame...
            if T5I1.status == STARTED:
                # update params
                pass
            
            # *T5Q1R* updates
            waitOnFlip = False
            
            # if T5Q1R is starting this frame...
            if T5Q1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5Q1R.frameNStart = frameN  # exact frame index
                T5Q1R.tStart = t  # local t and not account for scr refresh
                T5Q1R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5Q1R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5Q1R.started')
                # update status
                T5Q1R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T5Q1R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T5Q1R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T5Q1R.status == STARTED and not waitOnFlip:
                theseKeys = T5Q1R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T5Q1R_allKeys.extend(theseKeys)
                if len(_T5Q1R_allKeys):
                    T5Q1R.keys = _T5Q1R_allKeys[-1].name  # just the last key pressed
                    T5Q1R.rt = _T5Q1R_allKeys[-1].rt
                    T5Q1R.duration = _T5Q1R_allKeys[-1].duration
                    # was this correct?
                    if (T5Q1R.keys == str(CorrT5Q1)) or (T5Q1R.keys == CorrT5Q1):
                        T5Q1R.corr = 1
                    else:
                        T5Q1R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T5Q1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T5Q1" ---
        for thisComponent in T5Q1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T5Q1.stopped', globalClock.getTime())
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
            trials.addData('T5Q1R.duration', T5Q1R.duration)
        # the Routine "T5Q1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T5Q2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T5Q2.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T5Q2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T5I2* updates
            
            # if T5I2 is starting this frame...
            if T5I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5I2.frameNStart = frameN  # exact frame index
                T5I2.tStart = t  # local t and not account for scr refresh
                T5I2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5I2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5I2.started')
                # update status
                T5I2.status = STARTED
                T5I2.setAutoDraw(True)
            
            # if T5I2 is active this frame...
            if T5I2.status == STARTED:
                # update params
                pass
            
            # *T5Q2R* updates
            waitOnFlip = False
            
            # if T5Q2R is starting this frame...
            if T5Q2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5Q2R.frameNStart = frameN  # exact frame index
                T5Q2R.tStart = t  # local t and not account for scr refresh
                T5Q2R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5Q2R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5Q2R.started')
                # update status
                T5Q2R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T5Q2R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T5Q2R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T5Q2R.status == STARTED and not waitOnFlip:
                theseKeys = T5Q2R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T5Q2R_allKeys.extend(theseKeys)
                if len(_T5Q2R_allKeys):
                    T5Q2R.keys = _T5Q2R_allKeys[-1].name  # just the last key pressed
                    T5Q2R.rt = _T5Q2R_allKeys[-1].rt
                    T5Q2R.duration = _T5Q2R_allKeys[-1].duration
                    # was this correct?
                    if (T5Q2R.keys == str(CorrT5Q2)) or (T5Q2R.keys == CorrT5Q2):
                        T5Q2R.corr = 1
                    else:
                        T5Q2R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T5Q2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T5Q2" ---
        for thisComponent in T5Q2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T5Q2.stopped', globalClock.getTime())
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
            trials.addData('T5Q2R.duration', T5Q2R.duration)
        # the Routine "T5Q2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T5Q3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T5Q3.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T5Q3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T5I3* updates
            
            # if T5I3 is starting this frame...
            if T5I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5I3.frameNStart = frameN  # exact frame index
                T5I3.tStart = t  # local t and not account for scr refresh
                T5I3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5I3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5I3.started')
                # update status
                T5I3.status = STARTED
                T5I3.setAutoDraw(True)
            
            # if T5I3 is active this frame...
            if T5I3.status == STARTED:
                # update params
                pass
            
            # *T5Q3R* updates
            waitOnFlip = False
            
            # if T5Q3R is starting this frame...
            if T5Q3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5Q3R.frameNStart = frameN  # exact frame index
                T5Q3R.tStart = t  # local t and not account for scr refresh
                T5Q3R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5Q3R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5Q3R.started')
                # update status
                T5Q3R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T5Q3R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T5Q3R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T5Q3R.status == STARTED and not waitOnFlip:
                theseKeys = T5Q3R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T5Q3R_allKeys.extend(theseKeys)
                if len(_T5Q3R_allKeys):
                    T5Q3R.keys = _T5Q3R_allKeys[-1].name  # just the last key pressed
                    T5Q3R.rt = _T5Q3R_allKeys[-1].rt
                    T5Q3R.duration = _T5Q3R_allKeys[-1].duration
                    # was this correct?
                    if (T5Q3R.keys == str(CorrT5Q3)) or (T5Q3R.keys == CorrT5Q3):
                        T5Q3R.corr = 1
                    else:
                        T5Q3R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T5Q3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T5Q3" ---
        for thisComponent in T5Q3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T5Q3.stopped', globalClock.getTime())
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
            trials.addData('T5Q3R.duration', T5Q3R.duration)
        # the Routine "T5Q3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T5Q4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T5Q4.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T5Q4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T5I4* updates
            
            # if T5I4 is starting this frame...
            if T5I4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5I4.frameNStart = frameN  # exact frame index
                T5I4.tStart = t  # local t and not account for scr refresh
                T5I4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5I4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5I4.started')
                # update status
                T5I4.status = STARTED
                T5I4.setAutoDraw(True)
            
            # if T5I4 is active this frame...
            if T5I4.status == STARTED:
                # update params
                pass
            
            # *T5Q4R* updates
            waitOnFlip = False
            
            # if T5Q4R is starting this frame...
            if T5Q4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5Q4R.frameNStart = frameN  # exact frame index
                T5Q4R.tStart = t  # local t and not account for scr refresh
                T5Q4R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5Q4R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5Q4R.started')
                # update status
                T5Q4R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T5Q4R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T5Q4R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T5Q4R.status == STARTED and not waitOnFlip:
                theseKeys = T5Q4R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T5Q4R_allKeys.extend(theseKeys)
                if len(_T5Q4R_allKeys):
                    T5Q4R.keys = _T5Q4R_allKeys[-1].name  # just the last key pressed
                    T5Q4R.rt = _T5Q4R_allKeys[-1].rt
                    T5Q4R.duration = _T5Q4R_allKeys[-1].duration
                    # was this correct?
                    if (T5Q4R.keys == str(CorrT5Q4)) or (T5Q4R.keys == CorrT5Q4):
                        T5Q4R.corr = 1
                    else:
                        T5Q4R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T5Q4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T5Q4" ---
        for thisComponent in T5Q4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T5Q4.stopped', globalClock.getTime())
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
            trials.addData('T5Q4R.duration', T5Q4R.duration)
        # the Routine "T5Q4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T5Q5" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T5Q5.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T5Q5" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T5I5* updates
            
            # if T5I5 is starting this frame...
            if T5I5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5I5.frameNStart = frameN  # exact frame index
                T5I5.tStart = t  # local t and not account for scr refresh
                T5I5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5I5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5I5.started')
                # update status
                T5I5.status = STARTED
                T5I5.setAutoDraw(True)
            
            # if T5I5 is active this frame...
            if T5I5.status == STARTED:
                # update params
                pass
            
            # *T5Q5R* updates
            waitOnFlip = False
            
            # if T5Q5R is starting this frame...
            if T5Q5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5Q5R.frameNStart = frameN  # exact frame index
                T5Q5R.tStart = t  # local t and not account for scr refresh
                T5Q5R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5Q5R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5Q5R.started')
                # update status
                T5Q5R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T5Q5R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T5Q5R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T5Q5R.status == STARTED and not waitOnFlip:
                theseKeys = T5Q5R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T5Q5R_allKeys.extend(theseKeys)
                if len(_T5Q5R_allKeys):
                    T5Q5R.keys = _T5Q5R_allKeys[-1].name  # just the last key pressed
                    T5Q5R.rt = _T5Q5R_allKeys[-1].rt
                    T5Q5R.duration = _T5Q5R_allKeys[-1].duration
                    # was this correct?
                    if (T5Q5R.keys == str(CorrT5Q5)) or (T5Q5R.keys == CorrT5Q5):
                        T5Q5R.corr = 1
                    else:
                        T5Q5R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T5Q5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T5Q5" ---
        for thisComponent in T5Q5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T5Q5.stopped', globalClock.getTime())
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
            trials.addData('T5Q5R.duration', T5Q5R.duration)
        # the Routine "T5Q5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T5Q6" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T5Q6.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T5Q6" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T5I6* updates
            
            # if T5I6 is starting this frame...
            if T5I6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5I6.frameNStart = frameN  # exact frame index
                T5I6.tStart = t  # local t and not account for scr refresh
                T5I6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5I6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5I6.started')
                # update status
                T5I6.status = STARTED
                T5I6.setAutoDraw(True)
            
            # if T5I6 is active this frame...
            if T5I6.status == STARTED:
                # update params
                pass
            
            # *T5Q6R* updates
            waitOnFlip = False
            
            # if T5Q6R is starting this frame...
            if T5Q6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5Q6R.frameNStart = frameN  # exact frame index
                T5Q6R.tStart = t  # local t and not account for scr refresh
                T5Q6R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5Q6R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5Q6R.started')
                # update status
                T5Q6R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T5Q6R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T5Q6R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T5Q6R.status == STARTED and not waitOnFlip:
                theseKeys = T5Q6R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T5Q6R_allKeys.extend(theseKeys)
                if len(_T5Q6R_allKeys):
                    T5Q6R.keys = _T5Q6R_allKeys[-1].name  # just the last key pressed
                    T5Q6R.rt = _T5Q6R_allKeys[-1].rt
                    T5Q6R.duration = _T5Q6R_allKeys[-1].duration
                    # was this correct?
                    if (T5Q6R.keys == str(CorrT5Q6)) or (T5Q6R.keys == CorrT5Q6):
                        T5Q6R.corr = 1
                    else:
                        T5Q6R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T5Q6Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T5Q6" ---
        for thisComponent in T5Q6Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T5Q6.stopped', globalClock.getTime())
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
            trials.addData('T5Q6R.duration', T5Q6R.duration)
        # the Routine "T5Q6" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T5Q7" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T5Q7.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T5Q7" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T5I7* updates
            
            # if T5I7 is starting this frame...
            if T5I7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5I7.frameNStart = frameN  # exact frame index
                T5I7.tStart = t  # local t and not account for scr refresh
                T5I7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5I7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5I7.started')
                # update status
                T5I7.status = STARTED
                T5I7.setAutoDraw(True)
            
            # if T5I7 is active this frame...
            if T5I7.status == STARTED:
                # update params
                pass
            
            # *T5Q7R* updates
            waitOnFlip = False
            
            # if T5Q7R is starting this frame...
            if T5Q7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5Q7R.frameNStart = frameN  # exact frame index
                T5Q7R.tStart = t  # local t and not account for scr refresh
                T5Q7R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5Q7R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5Q7R.started')
                # update status
                T5Q7R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T5Q7R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T5Q7R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T5Q7R.status == STARTED and not waitOnFlip:
                theseKeys = T5Q7R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T5Q7R_allKeys.extend(theseKeys)
                if len(_T5Q7R_allKeys):
                    T5Q7R.keys = _T5Q7R_allKeys[-1].name  # just the last key pressed
                    T5Q7R.rt = _T5Q7R_allKeys[-1].rt
                    T5Q7R.duration = _T5Q7R_allKeys[-1].duration
                    # was this correct?
                    if (T5Q7R.keys == str(CorrT5Q7)) or (T5Q7R.keys == CorrT5Q7):
                        T5Q7R.corr = 1
                    else:
                        T5Q7R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T5Q7Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T5Q7" ---
        for thisComponent in T5Q7Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T5Q7.stopped', globalClock.getTime())
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
            trials.addData('T5Q7R.duration', T5Q7R.duration)
        # the Routine "T5Q7" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T5Q8" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T5Q8.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T5Q8" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T5I8* updates
            
            # if T5I8 is starting this frame...
            if T5I8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5I8.frameNStart = frameN  # exact frame index
                T5I8.tStart = t  # local t and not account for scr refresh
                T5I8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5I8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5I8.started')
                # update status
                T5I8.status = STARTED
                T5I8.setAutoDraw(True)
            
            # if T5I8 is active this frame...
            if T5I8.status == STARTED:
                # update params
                pass
            
            # *T5Q8R* updates
            waitOnFlip = False
            
            # if T5Q8R is starting this frame...
            if T5Q8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5Q8R.frameNStart = frameN  # exact frame index
                T5Q8R.tStart = t  # local t and not account for scr refresh
                T5Q8R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5Q8R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5Q8R.started')
                # update status
                T5Q8R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T5Q8R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T5Q8R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T5Q8R.status == STARTED and not waitOnFlip:
                theseKeys = T5Q8R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T5Q8R_allKeys.extend(theseKeys)
                if len(_T5Q8R_allKeys):
                    T5Q8R.keys = _T5Q8R_allKeys[-1].name  # just the last key pressed
                    T5Q8R.rt = _T5Q8R_allKeys[-1].rt
                    T5Q8R.duration = _T5Q8R_allKeys[-1].duration
                    # was this correct?
                    if (T5Q8R.keys == str(CorrT5Q8)) or (T5Q8R.keys == CorrT5Q8):
                        T5Q8R.corr = 1
                    else:
                        T5Q8R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T5Q8Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T5Q8" ---
        for thisComponent in T5Q8Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T5Q8.stopped', globalClock.getTime())
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
            trials.addData('T5Q8R.duration', T5Q8R.duration)
        # the Routine "T5Q8" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T5Q9" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T5Q9.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T5Q9" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T5I9* updates
            
            # if T5I9 is starting this frame...
            if T5I9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5I9.frameNStart = frameN  # exact frame index
                T5I9.tStart = t  # local t and not account for scr refresh
                T5I9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5I9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5I9.started')
                # update status
                T5I9.status = STARTED
                T5I9.setAutoDraw(True)
            
            # if T5I9 is active this frame...
            if T5I9.status == STARTED:
                # update params
                pass
            
            # *T5Q9R* updates
            waitOnFlip = False
            
            # if T5Q9R is starting this frame...
            if T5Q9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5Q9R.frameNStart = frameN  # exact frame index
                T5Q9R.tStart = t  # local t and not account for scr refresh
                T5Q9R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5Q9R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5Q9R.started')
                # update status
                T5Q9R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T5Q9R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T5Q9R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T5Q9R.status == STARTED and not waitOnFlip:
                theseKeys = T5Q9R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T5Q9R_allKeys.extend(theseKeys)
                if len(_T5Q9R_allKeys):
                    T5Q9R.keys = _T5Q9R_allKeys[-1].name  # just the last key pressed
                    T5Q9R.rt = _T5Q9R_allKeys[-1].rt
                    T5Q9R.duration = _T5Q9R_allKeys[-1].duration
                    # was this correct?
                    if (T5Q9R.keys == str(CorrT5Q9)) or (T5Q9R.keys == CorrT5Q9):
                        T5Q9R.corr = 1
                    else:
                        T5Q9R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T5Q9Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T5Q9" ---
        for thisComponent in T5Q9Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T5Q9.stopped', globalClock.getTime())
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
            trials.addData('T5Q9R.duration', T5Q9R.duration)
        # the Routine "T5Q9" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T5Q10" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T5Q10.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T5Q10" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T5I10* updates
            
            # if T5I10 is starting this frame...
            if T5I10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5I10.frameNStart = frameN  # exact frame index
                T5I10.tStart = t  # local t and not account for scr refresh
                T5I10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5I10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5I10.started')
                # update status
                T5I10.status = STARTED
                T5I10.setAutoDraw(True)
            
            # if T5I10 is active this frame...
            if T5I10.status == STARTED:
                # update params
                pass
            
            # *T5Q10R* updates
            waitOnFlip = False
            
            # if T5Q10R is starting this frame...
            if T5Q10R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T5Q10R.frameNStart = frameN  # exact frame index
                T5Q10R.tStart = t  # local t and not account for scr refresh
                T5Q10R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T5Q10R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T5Q10R.started')
                # update status
                T5Q10R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T5Q10R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T5Q10R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T5Q10R.status == STARTED and not waitOnFlip:
                theseKeys = T5Q10R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T5Q10R_allKeys.extend(theseKeys)
                if len(_T5Q10R_allKeys):
                    T5Q10R.keys = _T5Q10R_allKeys[-1].name  # just the last key pressed
                    T5Q10R.rt = _T5Q10R_allKeys[-1].rt
                    T5Q10R.duration = _T5Q10R_allKeys[-1].duration
                    # was this correct?
                    if (T5Q10R.keys == str(CorrT5Q10)) or (T5Q10R.keys == CorrT5Q10):
                        T5Q10R.corr = 1
                    else:
                        T5Q10R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T5Q10Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T5Q10" ---
        for thisComponent in T5Q10Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T5Q10.stopped', globalClock.getTime())
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
            trials.addData('T5Q10R.duration', T5Q10R.duration)
        # the Routine "T5Q10" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Trial_Break" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Trial_Break.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "Trial_Break" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Break_message* updates
            
            # if Break_message is starting this frame...
            if Break_message.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Break_message.frameNStart = frameN  # exact frame index
                Break_message.tStart = t  # local t and not account for scr refresh
                Break_message.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Break_message, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Break_message.started')
                # update status
                Break_message.status = STARTED
                Break_message.setAutoDraw(True)
            
            # if Break_message is active this frame...
            if Break_message.status == STARTED:
                # update params
                pass
            
            # *key_resp_4* updates
            waitOnFlip = False
            
            # if key_resp_4 is starting this frame...
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
                # update status
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Trial_BreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial_Break" ---
        for thisComponent in Trial_BreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Trial_Break.stopped', globalClock.getTime())
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        trials.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials.addData('key_resp_4.rt', key_resp_4.rt)
            trials.addData('key_resp_4.duration', key_resp_4.duration)
        # the Routine "Trial_Break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T6A" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T6A.started', globalClock.getTime())
        sound_6.setSound(T6A, hamming=True)
        sound_6.setVolume(1.0, log=False)
        sound_6.seek(0)
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
        frameN = -1
        
        # --- Run Routine "T6A" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # if sound_6 is starting this frame...
            if sound_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_6.frameNStart = frameN  # exact frame index
                sound_6.tStart = t  # local t and not account for scr refresh
                sound_6.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_6.started', t)
                # update status
                sound_6.status = STARTED
                sound_6.play()  # start the sound (it finishes automatically)
            # update sound_6 status according to whether it's playing
            if sound_6.isPlaying:
                sound_6.status = STARTED
            elif sound_6.isFinished:
                sound_6.status = FINISHED
            
            # *image_6* updates
            
            # if image_6 is starting this frame...
            if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_6.frameNStart = frameN  # exact frame index
                image_6.tStart = t  # local t and not account for scr refresh
                image_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_6.started')
                # update status
                image_6.status = STARTED
                image_6.setAutoDraw(True)
            
            # if image_6 is active this frame...
            if image_6.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_6
            if sound_6.status == FINISHED:
                continueRoutine = False
            
            # *key_resp_7* updates
            waitOnFlip = False
            
            # if key_resp_7 is starting this frame...
            if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_7.started')
                # update status
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['z'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_7_allKeys.extend(theseKeys)
                if len(_key_resp_7_allKeys):
                    key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                    key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                    key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T6AComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T6A" ---
        for thisComponent in T6AComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T6A.stopped', globalClock.getTime())
        sound_6.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
        trials.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            trials.addData('key_resp_7.rt', key_resp_7.rt)
            trials.addData('key_resp_7.duration', key_resp_7.duration)
        # the Routine "T6A" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "Pre_assement_inst" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Pre_assement_inst.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "Pre_assement_inst" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_5* updates
            waitOnFlip = False
            
            # if key_resp_5 is starting this frame...
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                # update status
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Pre_assement_instComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Pre_assement_inst" ---
        for thisComponent in Pre_assement_instComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Pre_assement_inst.stopped', globalClock.getTime())
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        trials.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials.addData('key_resp_5.rt', key_resp_5.rt)
            trials.addData('key_resp_5.duration', key_resp_5.duration)
        # the Routine "Pre_assement_inst" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T6Q1" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T6Q1.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T6Q1" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T6I1* updates
            
            # if T6I1 is starting this frame...
            if T6I1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6I1.frameNStart = frameN  # exact frame index
                T6I1.tStart = t  # local t and not account for scr refresh
                T6I1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6I1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6I1.started')
                # update status
                T6I1.status = STARTED
                T6I1.setAutoDraw(True)
            
            # if T6I1 is active this frame...
            if T6I1.status == STARTED:
                # update params
                pass
            
            # *T6Q1R* updates
            waitOnFlip = False
            
            # if T6Q1R is starting this frame...
            if T6Q1R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6Q1R.frameNStart = frameN  # exact frame index
                T6Q1R.tStart = t  # local t and not account for scr refresh
                T6Q1R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6Q1R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6Q1R.started')
                # update status
                T6Q1R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T6Q1R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T6Q1R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T6Q1R.status == STARTED and not waitOnFlip:
                theseKeys = T6Q1R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T6Q1R_allKeys.extend(theseKeys)
                if len(_T6Q1R_allKeys):
                    T6Q1R.keys = _T6Q1R_allKeys[-1].name  # just the last key pressed
                    T6Q1R.rt = _T6Q1R_allKeys[-1].rt
                    T6Q1R.duration = _T6Q1R_allKeys[-1].duration
                    # was this correct?
                    if (T6Q1R.keys == str(CorrT6Q1)) or (T6Q1R.keys == CorrT6Q1):
                        T6Q1R.corr = 1
                    else:
                        T6Q1R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T6Q1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T6Q1" ---
        for thisComponent in T6Q1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T6Q1.stopped', globalClock.getTime())
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
            trials.addData('T6Q1R.duration', T6Q1R.duration)
        # the Routine "T6Q1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T6Q2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T6Q2.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T6Q2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T6I2* updates
            
            # if T6I2 is starting this frame...
            if T6I2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6I2.frameNStart = frameN  # exact frame index
                T6I2.tStart = t  # local t and not account for scr refresh
                T6I2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6I2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6I2.started')
                # update status
                T6I2.status = STARTED
                T6I2.setAutoDraw(True)
            
            # if T6I2 is active this frame...
            if T6I2.status == STARTED:
                # update params
                pass
            
            # *T6Q2R* updates
            waitOnFlip = False
            
            # if T6Q2R is starting this frame...
            if T6Q2R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6Q2R.frameNStart = frameN  # exact frame index
                T6Q2R.tStart = t  # local t and not account for scr refresh
                T6Q2R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6Q2R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6Q2R.started')
                # update status
                T6Q2R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T6Q2R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T6Q2R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T6Q2R.status == STARTED and not waitOnFlip:
                theseKeys = T6Q2R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T6Q2R_allKeys.extend(theseKeys)
                if len(_T6Q2R_allKeys):
                    T6Q2R.keys = _T6Q2R_allKeys[-1].name  # just the last key pressed
                    T6Q2R.rt = _T6Q2R_allKeys[-1].rt
                    T6Q2R.duration = _T6Q2R_allKeys[-1].duration
                    # was this correct?
                    if (T6Q2R.keys == str(CorrT6Q2)) or (T6Q2R.keys == CorrT6Q2):
                        T6Q2R.corr = 1
                    else:
                        T6Q2R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T6Q2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T6Q2" ---
        for thisComponent in T6Q2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T6Q2.stopped', globalClock.getTime())
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
            trials.addData('T6Q2R.duration', T6Q2R.duration)
        # the Routine "T6Q2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T6Q3" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T6Q3.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T6Q3" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T6I3* updates
            
            # if T6I3 is starting this frame...
            if T6I3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6I3.frameNStart = frameN  # exact frame index
                T6I3.tStart = t  # local t and not account for scr refresh
                T6I3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6I3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6I3.started')
                # update status
                T6I3.status = STARTED
                T6I3.setAutoDraw(True)
            
            # if T6I3 is active this frame...
            if T6I3.status == STARTED:
                # update params
                pass
            
            # *T6Q3R* updates
            waitOnFlip = False
            
            # if T6Q3R is starting this frame...
            if T6Q3R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6Q3R.frameNStart = frameN  # exact frame index
                T6Q3R.tStart = t  # local t and not account for scr refresh
                T6Q3R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6Q3R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6Q3R.started')
                # update status
                T6Q3R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T6Q3R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T6Q3R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T6Q3R.status == STARTED and not waitOnFlip:
                theseKeys = T6Q3R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T6Q3R_allKeys.extend(theseKeys)
                if len(_T6Q3R_allKeys):
                    T6Q3R.keys = _T6Q3R_allKeys[-1].name  # just the last key pressed
                    T6Q3R.rt = _T6Q3R_allKeys[-1].rt
                    T6Q3R.duration = _T6Q3R_allKeys[-1].duration
                    # was this correct?
                    if (T6Q3R.keys == str(CorrT6Q3)) or (T6Q3R.keys == CorrT6Q3):
                        T6Q3R.corr = 1
                    else:
                        T6Q3R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T6Q3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T6Q3" ---
        for thisComponent in T6Q3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T6Q3.stopped', globalClock.getTime())
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
            trials.addData('T6Q3R.duration', T6Q3R.duration)
        # the Routine "T6Q3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T6Q4" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T6Q4.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T6Q4" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T6I4* updates
            
            # if T6I4 is starting this frame...
            if T6I4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6I4.frameNStart = frameN  # exact frame index
                T6I4.tStart = t  # local t and not account for scr refresh
                T6I4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6I4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6I4.started')
                # update status
                T6I4.status = STARTED
                T6I4.setAutoDraw(True)
            
            # if T6I4 is active this frame...
            if T6I4.status == STARTED:
                # update params
                pass
            
            # *T6Q4R* updates
            waitOnFlip = False
            
            # if T6Q4R is starting this frame...
            if T6Q4R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6Q4R.frameNStart = frameN  # exact frame index
                T6Q4R.tStart = t  # local t and not account for scr refresh
                T6Q4R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6Q4R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6Q4R.started')
                # update status
                T6Q4R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T6Q4R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T6Q4R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T6Q4R.status == STARTED and not waitOnFlip:
                theseKeys = T6Q4R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T6Q4R_allKeys.extend(theseKeys)
                if len(_T6Q4R_allKeys):
                    T6Q4R.keys = _T6Q4R_allKeys[-1].name  # just the last key pressed
                    T6Q4R.rt = _T6Q4R_allKeys[-1].rt
                    T6Q4R.duration = _T6Q4R_allKeys[-1].duration
                    # was this correct?
                    if (T6Q4R.keys == str(CorrT6Q4)) or (T6Q4R.keys == CorrT6Q4):
                        T6Q4R.corr = 1
                    else:
                        T6Q4R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T6Q4Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T6Q4" ---
        for thisComponent in T6Q4Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T6Q4.stopped', globalClock.getTime())
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
            trials.addData('T6Q4R.duration', T6Q4R.duration)
        # the Routine "T6Q4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T6Q5" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T6Q5.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T6Q5" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T6I5* updates
            
            # if T6I5 is starting this frame...
            if T6I5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6I5.frameNStart = frameN  # exact frame index
                T6I5.tStart = t  # local t and not account for scr refresh
                T6I5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6I5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6I5.started')
                # update status
                T6I5.status = STARTED
                T6I5.setAutoDraw(True)
            
            # if T6I5 is active this frame...
            if T6I5.status == STARTED:
                # update params
                pass
            
            # *T6Q5R* updates
            waitOnFlip = False
            
            # if T6Q5R is starting this frame...
            if T6Q5R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6Q5R.frameNStart = frameN  # exact frame index
                T6Q5R.tStart = t  # local t and not account for scr refresh
                T6Q5R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6Q5R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6Q5R.started')
                # update status
                T6Q5R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T6Q5R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T6Q5R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T6Q5R.status == STARTED and not waitOnFlip:
                theseKeys = T6Q5R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T6Q5R_allKeys.extend(theseKeys)
                if len(_T6Q5R_allKeys):
                    T6Q5R.keys = _T6Q5R_allKeys[-1].name  # just the last key pressed
                    T6Q5R.rt = _T6Q5R_allKeys[-1].rt
                    T6Q5R.duration = _T6Q5R_allKeys[-1].duration
                    # was this correct?
                    if (T6Q5R.keys == str(CorrT6Q5)) or (T6Q5R.keys == CorrT6Q5):
                        T6Q5R.corr = 1
                    else:
                        T6Q5R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T6Q5Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T6Q5" ---
        for thisComponent in T6Q5Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T6Q5.stopped', globalClock.getTime())
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
            trials.addData('T6Q5R.duration', T6Q5R.duration)
        # the Routine "T6Q5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T6Q6" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T6Q6.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T6Q6" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T6I6* updates
            
            # if T6I6 is starting this frame...
            if T6I6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6I6.frameNStart = frameN  # exact frame index
                T6I6.tStart = t  # local t and not account for scr refresh
                T6I6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6I6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6I6.started')
                # update status
                T6I6.status = STARTED
                T6I6.setAutoDraw(True)
            
            # if T6I6 is active this frame...
            if T6I6.status == STARTED:
                # update params
                pass
            
            # *T6Q6R* updates
            waitOnFlip = False
            
            # if T6Q6R is starting this frame...
            if T6Q6R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6Q6R.frameNStart = frameN  # exact frame index
                T6Q6R.tStart = t  # local t and not account for scr refresh
                T6Q6R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6Q6R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6Q6R.started')
                # update status
                T6Q6R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T6Q6R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T6Q6R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T6Q6R.status == STARTED and not waitOnFlip:
                theseKeys = T6Q6R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T6Q6R_allKeys.extend(theseKeys)
                if len(_T6Q6R_allKeys):
                    T6Q6R.keys = _T6Q6R_allKeys[-1].name  # just the last key pressed
                    T6Q6R.rt = _T6Q6R_allKeys[-1].rt
                    T6Q6R.duration = _T6Q6R_allKeys[-1].duration
                    # was this correct?
                    if (T6Q6R.keys == str(CorrT6Q6)) or (T6Q6R.keys == CorrT6Q6):
                        T6Q6R.corr = 1
                    else:
                        T6Q6R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T6Q6Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T6Q6" ---
        for thisComponent in T6Q6Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T6Q6.stopped', globalClock.getTime())
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
            trials.addData('T6Q6R.duration', T6Q6R.duration)
        # the Routine "T6Q6" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T6Q7" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T6Q7.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T6Q7" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T6I7* updates
            
            # if T6I7 is starting this frame...
            if T6I7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6I7.frameNStart = frameN  # exact frame index
                T6I7.tStart = t  # local t and not account for scr refresh
                T6I7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6I7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6I7.started')
                # update status
                T6I7.status = STARTED
                T6I7.setAutoDraw(True)
            
            # if T6I7 is active this frame...
            if T6I7.status == STARTED:
                # update params
                pass
            
            # *T6Q7R* updates
            waitOnFlip = False
            
            # if T6Q7R is starting this frame...
            if T6Q7R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6Q7R.frameNStart = frameN  # exact frame index
                T6Q7R.tStart = t  # local t and not account for scr refresh
                T6Q7R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6Q7R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6Q7R.started')
                # update status
                T6Q7R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T6Q7R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T6Q7R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T6Q7R.status == STARTED and not waitOnFlip:
                theseKeys = T6Q7R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T6Q7R_allKeys.extend(theseKeys)
                if len(_T6Q7R_allKeys):
                    T6Q7R.keys = _T6Q7R_allKeys[-1].name  # just the last key pressed
                    T6Q7R.rt = _T6Q7R_allKeys[-1].rt
                    T6Q7R.duration = _T6Q7R_allKeys[-1].duration
                    # was this correct?
                    if (T6Q7R.keys == str(CorrT6Q7)) or (T6Q7R.keys == CorrT6Q7):
                        T6Q7R.corr = 1
                    else:
                        T6Q7R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T6Q7Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T6Q7" ---
        for thisComponent in T6Q7Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T6Q7.stopped', globalClock.getTime())
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
            trials.addData('T6Q7R.duration', T6Q7R.duration)
        # the Routine "T6Q7" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T6Q8" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T6Q8.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T6Q8" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T6I8* updates
            
            # if T6I8 is starting this frame...
            if T6I8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6I8.frameNStart = frameN  # exact frame index
                T6I8.tStart = t  # local t and not account for scr refresh
                T6I8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6I8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6I8.started')
                # update status
                T6I8.status = STARTED
                T6I8.setAutoDraw(True)
            
            # if T6I8 is active this frame...
            if T6I8.status == STARTED:
                # update params
                pass
            
            # *T6Q8R* updates
            waitOnFlip = False
            
            # if T6Q8R is starting this frame...
            if T6Q8R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6Q8R.frameNStart = frameN  # exact frame index
                T6Q8R.tStart = t  # local t and not account for scr refresh
                T6Q8R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6Q8R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6Q8R.started')
                # update status
                T6Q8R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T6Q8R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T6Q8R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T6Q8R.status == STARTED and not waitOnFlip:
                theseKeys = T6Q8R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T6Q8R_allKeys.extend(theseKeys)
                if len(_T6Q8R_allKeys):
                    T6Q8R.keys = _T6Q8R_allKeys[-1].name  # just the last key pressed
                    T6Q8R.rt = _T6Q8R_allKeys[-1].rt
                    T6Q8R.duration = _T6Q8R_allKeys[-1].duration
                    # was this correct?
                    if (T6Q8R.keys == str(CorrT6Q8)) or (T6Q8R.keys == CorrT6Q8):
                        T6Q8R.corr = 1
                    else:
                        T6Q8R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T6Q8Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T6Q8" ---
        for thisComponent in T6Q8Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T6Q8.stopped', globalClock.getTime())
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
            trials.addData('T6Q8R.duration', T6Q8R.duration)
        # the Routine "T6Q8" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T6Q9" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T6Q9.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T6Q9" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T6I9* updates
            
            # if T6I9 is starting this frame...
            if T6I9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6I9.frameNStart = frameN  # exact frame index
                T6I9.tStart = t  # local t and not account for scr refresh
                T6I9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6I9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6I9.started')
                # update status
                T6I9.status = STARTED
                T6I9.setAutoDraw(True)
            
            # if T6I9 is active this frame...
            if T6I9.status == STARTED:
                # update params
                pass
            
            # *T6Q9R* updates
            waitOnFlip = False
            
            # if T6Q9R is starting this frame...
            if T6Q9R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6Q9R.frameNStart = frameN  # exact frame index
                T6Q9R.tStart = t  # local t and not account for scr refresh
                T6Q9R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6Q9R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6Q9R.started')
                # update status
                T6Q9R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T6Q9R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T6Q9R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T6Q9R.status == STARTED and not waitOnFlip:
                theseKeys = T6Q9R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T6Q9R_allKeys.extend(theseKeys)
                if len(_T6Q9R_allKeys):
                    T6Q9R.keys = _T6Q9R_allKeys[-1].name  # just the last key pressed
                    T6Q9R.rt = _T6Q9R_allKeys[-1].rt
                    T6Q9R.duration = _T6Q9R_allKeys[-1].duration
                    # was this correct?
                    if (T6Q9R.keys == str(CorrT6Q9)) or (T6Q9R.keys == CorrT6Q9):
                        T6Q9R.corr = 1
                    else:
                        T6Q9R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T6Q9Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T6Q9" ---
        for thisComponent in T6Q9Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T6Q9.stopped', globalClock.getTime())
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
            trials.addData('T6Q9R.duration', T6Q9R.duration)
        # the Routine "T6Q9" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "T6Q10" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('T6Q10.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "T6Q10" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *T6I10* updates
            
            # if T6I10 is starting this frame...
            if T6I10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6I10.frameNStart = frameN  # exact frame index
                T6I10.tStart = t  # local t and not account for scr refresh
                T6I10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6I10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6I10.started')
                # update status
                T6I10.status = STARTED
                T6I10.setAutoDraw(True)
            
            # if T6I10 is active this frame...
            if T6I10.status == STARTED:
                # update params
                pass
            
            # *T6Q10R* updates
            waitOnFlip = False
            
            # if T6Q10R is starting this frame...
            if T6Q10R.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                T6Q10R.frameNStart = frameN  # exact frame index
                T6Q10R.tStart = t  # local t and not account for scr refresh
                T6Q10R.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(T6Q10R, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'T6Q10R.started')
                # update status
                T6Q10R.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(T6Q10R.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(T6Q10R.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if T6Q10R.status == STARTED and not waitOnFlip:
                theseKeys = T6Q10R.getKeys(keyList=['1', '2', '3', '4','5'], ignoreKeys=["escape"], waitRelease=False)
                _T6Q10R_allKeys.extend(theseKeys)
                if len(_T6Q10R_allKeys):
                    T6Q10R.keys = _T6Q10R_allKeys[-1].name  # just the last key pressed
                    T6Q10R.rt = _T6Q10R_allKeys[-1].rt
                    T6Q10R.duration = _T6Q10R_allKeys[-1].duration
                    # was this correct?
                    if (T6Q10R.keys == str(CorrT6Q10)) or (T6Q10R.keys == CorrT6Q10):
                        T6Q10R.corr = 1
                    else:
                        T6Q10R.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in T6Q10Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "T6Q10" ---
        for thisComponent in T6Q10Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('T6Q10.stopped', globalClock.getTime())
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
            trials.addData('T6Q10R.duration', T6Q10R.duration)
        # the Routine "T6Q10" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "end" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('end.started', globalClock.getTime())
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
        frameN = -1
        
        # --- Run Routine "end" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_6* updates
            waitOnFlip = False
            
            # if key_resp_6 is starting this frame...
            if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_6.started')
                # update status
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['z'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                    key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in endComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "end" ---
        for thisComponent in endComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('end.stopped', globalClock.getTime())
        # check responses
        if key_resp_6.keys in ['', [], None]:  # No response was made
            key_resp_6.keys = None
        trials.addData('key_resp_6.keys',key_resp_6.keys)
        if key_resp_6.keys != None:  # we had a response
            trials.addData('key_resp_6.rt', key_resp_6.rt)
            trials.addData('key_resp_6.duration', key_resp_6.duration)
        # the Routine "end" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    # Close serialPort_4
    if serialPort_4.is_open:
        serialPort_4.close()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
