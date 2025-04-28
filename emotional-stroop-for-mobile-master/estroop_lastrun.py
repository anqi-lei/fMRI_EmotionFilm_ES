#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on Sat Apr 26 17:33:00 2025
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
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
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

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'estroop'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '',
    'id': '',
    'group': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = [1440, 900]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
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
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
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
        originPath='/Users/christylei/Documents/GitHub/fMRI_EmotionFilm_ES/emotional-stroop-for-mobile-master/estroop_lastrun.py',
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
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
        )
    
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
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
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
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('Response') is None:
        # initialise Response
        Response = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Response',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
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
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
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
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
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
    
    # --- Initialize components for Routine "start" ---
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    # Run 'Begin Experiment' code from code
    colours = [['red','d'],['blue','f'],['yellow','j'],['green','k']]
    shuffle(colours)
    buttonSize=.2
    buttonGap=.2
    buttonOffset=.3
    touchscreen=0
    nBlocks = 3
    #https://run.pavlovia.org/Wake/emotional-stroop/html/?participant=${e://Field/participant}&id=${e://Field/ResponseID}&group=${e://Field/group}&researcher=${e://Field/researcher}
    if expInfo['group']=='1':
        ivLevels=['Practice','Neutral','Negative','Positive']
        block_selection = [['45:75','Positive',2],['75:105','Negative',3]]
    else:
        ivLevels=['Practice','Neutral','Positive','Negative']
        block_selection = [['75:105','Negative',3],['45:75','Positive',2]]      
    block_selection.append(['15:45','Neutral',1])
    block_selection.append(['0:15','Practice',0])
    weblink='https://brookeshls.co1.qualtrics.com/jfe/preview/SV_4GFvF9AAzBNbO5M?Q_CHL=preview&Q_SurveyVersionID=current&'
    nBlocks=4
    thisIndex=0
    #shuffle(block_selection)
    #count, score, RT
    block_results = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    showFeedback = 1
    weblink+='participant='+expInfo['participant']+'&id='+expInfo['id']+'&researcher='+expInfo['researcher']
    
    instructions = visual.TextStim(win=win, name='instructions',
        text=' ',
        font='Arial',
        pos=(0, .2), draggable=False, height=0.06, wrapWidth=1.2, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    rec = visual.Rect(
        win=win, name='rec',
        width=(0.5, 0.09)[0], height=(0.5, 0.09)[1],
        ori=0, pos=(0, -.45), draggable=False, anchor='center',
        lineWidth=5,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[0.2,0.2,.2],
        opacity=1, depth=-3.0, interpolate=True)
    start_button = visual.TextStim(win=win, name='start_button',
        text='Start',
        font='Arial',
        pos=(0, -.45), draggable=False, height=0.08, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "preBlock" ---
    
    # --- Initialize components for Routine "stroop" ---
    fixation = visual.TextStim(win=win, name='fixation',
        text='+',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.15, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    stroop_text = visual.TextStim(win=win, name='stroop_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.15, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    Response = keyboard.Keyboard(deviceName='Response')
    button1 = visual.Polygon(
        win=win, name='button1',
        edges=72, size=buttonSize,
        ori=0, pos=(-buttonGap, -buttonOffset+buttonGap), draggable=False, anchor='center',
        lineWidth=5,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=colours[0][0],
        opacity=1, depth=-4.0, interpolate=True)
    button2 = visual.Polygon(
        win=win, name='button2',
        edges=72, size=buttonSize,
        ori=0, pos=(buttonGap, -buttonOffset+buttonGap), draggable=False, anchor='center',
        lineWidth=5,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=colours[1][0],
        opacity=1, depth=-5.0, interpolate=True)
    button3 = visual.Polygon(
        win=win, name='button3',
        edges=72, size=buttonSize,
        ori=0, pos=(-buttonGap, -buttonOffset-buttonGap), draggable=False, anchor='center',
        lineWidth=5,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=colours[2][0],
        opacity=1, depth=-6.0, interpolate=True)
    button4 = visual.Polygon(
        win=win, name='button4',
        edges=72, size=buttonSize,
        ori=0, pos=(buttonGap, -buttonOffset-buttonGap), draggable=False, anchor='center',
        lineWidth=5,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=colours[3][0],
        opacity=1, depth=-7.0, interpolate=True)
    
    # --- Initialize components for Routine "feedback" ---
    image = visual.ImageStim(
        win=win,
        name='image', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), draggable=False, size=(.3, .3),
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    button1_2 = visual.Polygon(
        win=win, name='button1_2',
        edges=72, size=buttonSize,
        ori=0, pos=(-buttonGap, -buttonOffset+buttonGap), draggable=False, anchor='center',
        lineWidth=5,
        colorSpace='rgb', lineColor='white', fillColor=colours[0][0],
        opacity=1, depth=-1.0, interpolate=True)
    button2_2 = visual.Polygon(
        win=win, name='button2_2',
        edges=72, size=buttonSize,
        ori=0, pos=(buttonGap, -buttonOffset+buttonGap), draggable=False, anchor='center',
        lineWidth=5,
        colorSpace='rgb', lineColor='white', fillColor=colours[1][0],
        opacity=1, depth=-2.0, interpolate=True)
    button3_2 = visual.Polygon(
        win=win, name='button3_2',
        edges=72, size=buttonSize,
        ori=0, pos=(-buttonGap, -buttonOffset-buttonGap), draggable=False, anchor='center',
        lineWidth=5,
        colorSpace='rgb', lineColor='white', fillColor=colours[2][0],
        opacity=1, depth=-3.0, interpolate=True)
    button4_2 = visual.Polygon(
        win=win, name='button4_2',
        edges=72, size=buttonSize,
        ori=0, pos=(buttonGap, -buttonOffset-buttonGap), draggable=False, anchor='center',
        lineWidth=5,
        colorSpace='rgb', lineColor='white', fillColor=colours[3][0],
        opacity=1, depth=-4.0, interpolate=True)
    
    # --- Initialize components for Routine "postBlock" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text=' ',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    text_4 = visual.TextStim(win=win, name='text_4',
        text=' ',
        font='Arial',
        pos=(0, -.45), draggable=False, height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    rec_2 = visual.Rect(
        win=win, name='rec_2',
        width=(0.5, 0.09)[0], height=(0.5, 0.09)[1],
        ori=0, pos=(0, -.45), draggable=False, anchor='center',
        lineWidth=5,
        colorSpace='rgb', lineColor=[1,1,1], fillColor=[0.2,0.2,.2],
        opacity=1, depth=-4.0, interpolate=True)
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "start" ---
    # create an object to store info about Routine start
    start = data.Routine(
        name='start',
        components=[mouse, instructions, rec, start_button],
    )
    start.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    # Run 'Begin Routine' code from code
    mouserec = mouse.getPos()
    instructions.text='This experiment consists of a Stroop task.\n\nIn this task you will be presented with a series of words.\nEach screen will show a single word, these words will appear in different colours (green, yellow, blue and red).\nYour job is to indicate the colour that the word is printed in as quickly and as accurately as possible. \nClick the button on the screen that corresponds to that colour. \n\nTouch Start if you  understand the instructions and are ready to begin.'
    
    # store start times for start
    start.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    start.tStart = globalClock.getTime(format='float')
    start.status = STARTED
    thisExp.addData('start.started', start.tStart)
    start.maxDuration = None
    # keep track of which components have finished
    startComponents = start.components
    for thisComponent in start.components:
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
    
    # --- Run Routine "start" ---
    start.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        # Run 'Each Frame' code from code
        mouseloc = mouse.getPos()
        if mouseloc[0]==mouserec[0] and mouseloc[1]==mouserec[1]:
            pass
        elif rec.contains(mouse):
            touchscreen=1
            fixation.setPos([0,.3])
            stroop_text.setPos([0,.3])
            image.setPos([0,.3])
            continueRoutine = False
        
        # *instructions* updates
        
        # if instructions is starting this frame...
        if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions.frameNStart = frameN  # exact frame index
            instructions.tStart = t  # local t and not account for scr refresh
            instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
            # update status
            instructions.status = STARTED
            instructions.setAutoDraw(True)
        
        # if instructions is active this frame...
        if instructions.status == STARTED:
            # update params
            pass
        
        # *rec* updates
        
        # if rec is starting this frame...
        if rec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rec.frameNStart = frameN  # exact frame index
            rec.tStart = t  # local t and not account for scr refresh
            rec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rec, 'tStartRefresh')  # time at next scr refresh
            # update status
            rec.status = STARTED
            rec.setAutoDraw(True)
        
        # if rec is active this frame...
        if rec.status == STARTED:
            # update params
            pass
        
        # *start_button* updates
        
        # if start_button is starting this frame...
        if start_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_button.frameNStart = frameN  # exact frame index
            start_button.tStart = t  # local t and not account for scr refresh
            start_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_button, 'tStartRefresh')  # time at next scr refresh
            # update status
            start_button.status = STARTED
            start_button.setAutoDraw(True)
        
        # if start_button is active this frame...
        if start_button.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            start.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start" ---
    for thisComponent in start.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for start
    start.tStop = globalClock.getTime(format='float')
    start.tStopRefresh = tThisFlipGlobal
    thisExp.addData('start.stopped', start.tStop)
    # store data for thisExp (ExperimentHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    thisExp.addData('mouse.x', x)
    thisExp.addData('mouse.y', y)
    thisExp.addData('mouse.leftButton', buttons[0])
    thisExp.addData('mouse.midButton', buttons[1])
    thisExp.addData('mouse.rightButton', buttons[2])
    # Run 'End Routine' code from code
    if touchscreen == 0:
        button1.setOpacity(0)
        button2.setOpacity(0)
        button3.setOpacity(0)
        button4.setOpacity(0)
        button1_2.setOpacity(0)
        button2_2.setOpacity(0)
        button3_2.setOpacity(0)
        button4_2.setOpacity(0)
        rec_2.setOpacity(0)
    thisExp.nextEntry()
    # the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    outer_loop = data.TrialHandler2(
        name='outer_loop',
        nReps=nBlocks, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(outer_loop)  # add the loop to the experiment
    thisOuter_loop = outer_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOuter_loop.rgb)
    if thisOuter_loop != None:
        for paramName in thisOuter_loop:
            globals()[paramName] = thisOuter_loop[paramName]
    
    for thisOuter_loop in outer_loop:
        currentLoop = outer_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisOuter_loop.rgb)
        if thisOuter_loop != None:
            for paramName in thisOuter_loop:
                globals()[paramName] = thisOuter_loop[paramName]
        
        # --- Prepare to start Routine "preBlock" ---
        # create an object to store info about Routine preBlock
        preBlock = data.Routine(
            name='preBlock',
            components=[],
        )
        preBlock.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        thisBlock=block_selection.pop()
        useRows=str(thisBlock[0])
        rtList=[]
        # Run 'Begin Routine' code from code_both2
        useColours=[0, 1, 2, 3] * 10
        shuffle(useColours)
        # store start times for preBlock
        preBlock.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        preBlock.tStart = globalClock.getTime(format='float')
        preBlock.status = STARTED
        thisExp.addData('preBlock.started', preBlock.tStart)
        preBlock.maxDuration = None
        # keep track of which components have finished
        preBlockComponents = preBlock.components
        for thisComponent in preBlock.components:
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
        
        # --- Run Routine "preBlock" ---
        # if trial has changed, end Routine now
        if isinstance(outer_loop, data.TrialHandler2) and thisOuter_loop.thisN != outer_loop.thisTrial.thisN:
            continueRoutine = False
        preBlock.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                preBlock.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in preBlock.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "preBlock" ---
        for thisComponent in preBlock.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for preBlock
        preBlock.tStop = globalClock.getTime(format='float')
        preBlock.tStopRefresh = tThisFlipGlobal
        thisExp.addData('preBlock.stopped', preBlock.tStop)
        # the Routine "preBlock" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler2(
            name='trials',
            nReps=1, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions(
            'estroop.xlsx', 
            selection=useRows
        )
        , 
            seed=None, 
        )
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial in trials:
            currentLoop = trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            # --- Prepare to start Routine "stroop" ---
            # create an object to store info about Routine stroop
            stroop = data.Routine(
                name='stroop',
                components=[fixation, stroop_text, Response, button1, button2, button3, button4],
            )
            stroop.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from stroop_code
            thisColour=useColours.pop()
            thisExp.addData('Colour',colours[thisColour][0])
            thisExp.addData('Answer',colours[thisColour][1])
            response=99
            Score=0
            butcol1='white'
            butcol2='white'
            butcol3='white'
            butcol4='white'
            
            stroop_text.setColor(colours[thisColour][0], colorSpace='rgb')
            stroop_text.setText(Word)
            # create starting attributes for Response
            Response.keys = []
            Response.rt = []
            _Response_allKeys = []
            # store start times for stroop
            stroop.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            stroop.tStart = globalClock.getTime(format='float')
            stroop.status = STARTED
            thisExp.addData('stroop.started', stroop.tStart)
            stroop.maxDuration = None
            # keep track of which components have finished
            stroopComponents = stroop.components
            for thisComponent in stroop.components:
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
            
            # --- Run Routine "stroop" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            stroop.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation* updates
                
                # if fixation is starting this frame...
                if fixation.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation.frameNStart = frameN  # exact frame index
                    fixation.tStart = t  # local t and not account for scr refresh
                    fixation.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.started')
                    # update status
                    fixation.status = STARTED
                    fixation.setAutoDraw(True)
                
                # if fixation is active this frame...
                if fixation.status == STARTED:
                    # update params
                    pass
                
                # if fixation is stopping this frame...
                if fixation.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation.tStop = t  # not accounting for scr refresh
                        fixation.tStopRefresh = tThisFlipGlobal  # on global time
                        fixation.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation.stopped')
                        # update status
                        fixation.status = FINISHED
                        fixation.setAutoDraw(False)
                # Run 'Each Frame' code from stroop_code
                if t < .5:
                    mouserec = mouse.getPos()
                else:
                    mouseloc = mouse.getPos()
                    if mouseloc[0]==mouserec[0] and mouseloc[1]==mouserec[1]:
                        pass
                    elif button1.contains(mouse):
                        response=0
                        butcol1='yellow'
                    elif button2.contains(mouse):
                        response=1
                        butcol2='yellow'
                    elif button3.contains(mouse):
                        response=2
                        butcol3='yellow'
                    elif button4.contains(mouse):
                        response=3
                        butcol4='yellow'
                    if response < 99:
                        if response==thisColour:
                            Score = 1
                        continueRoutine=False
                
                # *stroop_text* updates
                
                # if stroop_text is starting this frame...
                if stroop_text.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    stroop_text.frameNStart = frameN  # exact frame index
                    stroop_text.tStart = t  # local t and not account for scr refresh
                    stroop_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stroop_text, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    stroop_text.status = STARTED
                    stroop_text.setAutoDraw(True)
                
                # if stroop_text is active this frame...
                if stroop_text.status == STARTED:
                    # update params
                    pass
                
                # *Response* updates
                waitOnFlip = False
                
                # if Response is starting this frame...
                if Response.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                    # keep track of start time/frame for later
                    Response.frameNStart = frameN  # exact frame index
                    Response.tStart = t  # local t and not account for scr refresh
                    Response.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Response, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    Response.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Response.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Response.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Response.status == STARTED and not waitOnFlip:
                    theseKeys = Response.getKeys(keyList=['d','f','j','k'], ignoreKeys=["escape"], waitRelease=False)
                    _Response_allKeys.extend(theseKeys)
                    if len(_Response_allKeys):
                        Response.keys = _Response_allKeys[-1].name  # just the last key pressed
                        Response.rt = _Response_allKeys[-1].rt
                        Response.duration = _Response_allKeys[-1].duration
                        # was this correct?
                        if (Response.keys == str(colours[0][1])) or (Response.keys == colours[0][1]):
                            Response.corr = 1
                        else:
                            Response.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *button1* updates
                
                # if button1 is starting this frame...
                if button1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    button1.frameNStart = frameN  # exact frame index
                    button1.tStart = t  # local t and not account for scr refresh
                    button1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button1, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button1.status = STARTED
                    button1.setAutoDraw(True)
                
                # if button1 is active this frame...
                if button1.status == STARTED:
                    # update params
                    pass
                
                # *button2* updates
                
                # if button2 is starting this frame...
                if button2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    button2.frameNStart = frameN  # exact frame index
                    button2.tStart = t  # local t and not account for scr refresh
                    button2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button2.status = STARTED
                    button2.setAutoDraw(True)
                
                # if button2 is active this frame...
                if button2.status == STARTED:
                    # update params
                    pass
                
                # *button3* updates
                
                # if button3 is starting this frame...
                if button3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    button3.frameNStart = frameN  # exact frame index
                    button3.tStart = t  # local t and not account for scr refresh
                    button3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button3, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button3.status = STARTED
                    button3.setAutoDraw(True)
                
                # if button3 is active this frame...
                if button3.status == STARTED:
                    # update params
                    pass
                
                # *button4* updates
                
                # if button4 is starting this frame...
                if button4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    button4.frameNStart = frameN  # exact frame index
                    button4.tStart = t  # local t and not account for scr refresh
                    button4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button4, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button4.status = STARTED
                    button4.setAutoDraw(True)
                
                # if button4 is active this frame...
                if button4.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    stroop.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stroop.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stroop" ---
            for thisComponent in stroop.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for stroop
            stroop.tStop = globalClock.getTime(format='float')
            stroop.tStopRefresh = tThisFlipGlobal
            thisExp.addData('stroop.stopped', stroop.tStop)
            # Run 'End Routine' code from stroop_code
            block_results[thisBlock[2]][0]+=1
            if Response.corr == 1 or Score == 1:
                block_results[thisBlock[2]][1]+=1
                rtList.append(round(t*1000)-500)
                feedbackImage='tick_white.png'
            else:
                feedbackImage='cross_white.png'
                
            if thisBlock[2] > 0:
                showFeedback = 0
             
            # check responses
            if Response.keys in ['', [], None]:  # No response was made
                Response.keys = None
                # was no response the correct answer?!
                if str(colours[0][1]).lower() == 'none':
                   Response.corr = 1;  # correct non-response
                else:
                   Response.corr = 0;  # failed to respond (incorrectly)
            # store data for trials (TrialHandler)
            trials.addData('Response.keys',Response.keys)
            trials.addData('Response.corr', Response.corr)
            if Response.keys != None:  # we had a response
                trials.addData('Response.rt', Response.rt)
                trials.addData('Response.duration', Response.duration)
            # the Routine "stroop" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback" ---
            # create an object to store info about Routine feedback
            feedback = data.Routine(
                name='feedback',
                components=[image, button1_2, button2_2, button3_2, button4_2],
            )
            feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image.setOpacity(showFeedback)
            image.setImage(feedbackImage)
            button1_2.setLineColor(butcol1)
            button2_2.setLineColor(butcol2)
            button3_2.setLineColor(butcol3)
            button4_2.setLineColor(butcol4)
            # store start times for feedback
            feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            feedback.tStart = globalClock.getTime(format='float')
            feedback.status = STARTED
            thisExp.addData('feedback.started', feedback.tStart)
            feedback.maxDuration = None
            # keep track of which components have finished
            feedbackComponents = feedback.components
            for thisComponent in feedback.components:
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
            
            # --- Run Routine "feedback" ---
            # if trial has changed, end Routine now
            if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
                continueRoutine = False
            feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
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
                
                # if image is stopping this frame...
                if image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        image.tStop = t  # not accounting for scr refresh
                        image.tStopRefresh = tThisFlipGlobal  # on global time
                        image.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image.stopped')
                        # update status
                        image.status = FINISHED
                        image.setAutoDraw(False)
                
                # *button1_2* updates
                
                # if button1_2 is starting this frame...
                if button1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    button1_2.frameNStart = frameN  # exact frame index
                    button1_2.tStart = t  # local t and not account for scr refresh
                    button1_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button1_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button1_2.status = STARTED
                    button1_2.setAutoDraw(True)
                
                # if button1_2 is active this frame...
                if button1_2.status == STARTED:
                    # update params
                    pass
                
                # if button1_2 is stopping this frame...
                if button1_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > button1_2.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        button1_2.tStop = t  # not accounting for scr refresh
                        button1_2.tStopRefresh = tThisFlipGlobal  # on global time
                        button1_2.frameNStop = frameN  # exact frame index
                        # update status
                        button1_2.status = FINISHED
                        button1_2.setAutoDraw(False)
                
                # *button2_2* updates
                
                # if button2_2 is starting this frame...
                if button2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    button2_2.frameNStart = frameN  # exact frame index
                    button2_2.tStart = t  # local t and not account for scr refresh
                    button2_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button2_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button2_2.status = STARTED
                    button2_2.setAutoDraw(True)
                
                # if button2_2 is active this frame...
                if button2_2.status == STARTED:
                    # update params
                    pass
                
                # if button2_2 is stopping this frame...
                if button2_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > button2_2.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        button2_2.tStop = t  # not accounting for scr refresh
                        button2_2.tStopRefresh = tThisFlipGlobal  # on global time
                        button2_2.frameNStop = frameN  # exact frame index
                        # update status
                        button2_2.status = FINISHED
                        button2_2.setAutoDraw(False)
                
                # *button3_2* updates
                
                # if button3_2 is starting this frame...
                if button3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    button3_2.frameNStart = frameN  # exact frame index
                    button3_2.tStart = t  # local t and not account for scr refresh
                    button3_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button3_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button3_2.status = STARTED
                    button3_2.setAutoDraw(True)
                
                # if button3_2 is active this frame...
                if button3_2.status == STARTED:
                    # update params
                    pass
                
                # if button3_2 is stopping this frame...
                if button3_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > button3_2.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        button3_2.tStop = t  # not accounting for scr refresh
                        button3_2.tStopRefresh = tThisFlipGlobal  # on global time
                        button3_2.frameNStop = frameN  # exact frame index
                        # update status
                        button3_2.status = FINISHED
                        button3_2.setAutoDraw(False)
                
                # *button4_2* updates
                
                # if button4_2 is starting this frame...
                if button4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    button4_2.frameNStart = frameN  # exact frame index
                    button4_2.tStart = t  # local t and not account for scr refresh
                    button4_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(button4_2, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    button4_2.status = STARTED
                    button4_2.setAutoDraw(True)
                
                # if button4_2 is active this frame...
                if button4_2.status == STARTED:
                    # update params
                    pass
                
                # if button4_2 is stopping this frame...
                if button4_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > button4_2.tStartRefresh + .5-frameTolerance:
                        # keep track of stop time/frame for later
                        button4_2.tStop = t  # not accounting for scr refresh
                        button4_2.tStopRefresh = tThisFlipGlobal  # on global time
                        button4_2.frameNStop = frameN  # exact frame index
                        # update status
                        button4_2.status = FINISHED
                        button4_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    feedback.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback" ---
            for thisComponent in feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for feedback
            feedback.tStop = globalClock.getTime(format='float')
            feedback.tStopRefresh = tThisFlipGlobal
            thisExp.addData('feedback.stopped', feedback.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if feedback.maxDurationReached:
                routineTimer.addTime(-feedback.maxDuration)
            elif feedback.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.500000)
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "postBlock" ---
        # create an object to store info about Routine postBlock
        postBlock = data.Routine(
            name='postBlock',
            components=[text_3, text_4, key_resp, rec_2],
        )
        postBlock.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_3
        sort(rtList)
        rtMid = (len(rtList)+1)/2
        
        if rtMid == round(rtMid):
            block_results[thisBlock[2]][2]=rtList[int(rtMid)]
        else:
            block_results[thisBlock[2]][2]=(rtList[int(rtMid-.5)]+rtList[int(rtMid+.5)])/2
        
        if thisBlock[2] == 0:
            text_3.text='That was the end of the practice trials.\n\nYou scored '+str(block_results[thisBlock[2]][1])+' out of '+str(block_results[thisBlock[2]][0])
            text_4.text='Please wait for 10 seconds before starting the first block'
            waitTime = 10
        elif thisBlock[2] == 1:
            text_3.text='That was the end of the first block.'
            text_4.text='Please wait for 30 seconds before starting the second block'
            waitTime = 30
        elif thisBlock[2] == 2 and nBlocks==4:
            text_3.text='That was the end of the second block.'
            text_4.text='Please wait for 30 seconds before starting the third block'
            waitTime = 30
        else:
            text_3.text='Thank you for taking part.'
            text_4.text='Please submit your data and then wait for the green \"Thank you for your patience\" message.'
            waitTime = 2
        pressSpace=0
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # store start times for postBlock
        postBlock.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        postBlock.tStart = globalClock.getTime(format='float')
        postBlock.status = STARTED
        thisExp.addData('postBlock.started', postBlock.tStart)
        postBlock.maxDuration = None
        # keep track of which components have finished
        postBlockComponents = postBlock.components
        for thisComponent in postBlock.components:
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
        
        # --- Run Routine "postBlock" ---
        # if trial has changed, end Routine now
        if isinstance(outer_loop, data.TrialHandler2) and thisOuter_loop.thisN != outer_loop.thisTrial.thisN:
            continueRoutine = False
        postBlock.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code_3
            if t > waitTime and pressSpace==0:
                if touchscreen == 1:
                    text_4.text='Continue'
                    mouserec = mouse.getPos()
                else:
                    text_4.text='Press space to continue'
                pressSpace=1
            elif pressSpace==1 and touchscreen == 1:
                mouseloc = mouse.getPos()
                if mouseloc[0]==mouserec[0] and mouseloc[1]==mouserec[1]:
                    pass
                elif rec_2.contains(mouse):
                    continueRoutine=False
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # *text_4* updates
            
            # if text_4 is starting this frame...
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # update status
                text_4.status = STARTED
                text_4.setAutoDraw(True)
            
            # if text_4 is active this frame...
            if text_4.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= waitTime-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *rec_2* updates
            
            # if rec_2 is starting this frame...
            if rec_2.status == NOT_STARTED and tThisFlip >= waitTime-frameTolerance:
                # keep track of start time/frame for later
                rec_2.frameNStart = frameN  # exact frame index
                rec_2.tStart = t  # local t and not account for scr refresh
                rec_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rec_2, 'tStartRefresh')  # time at next scr refresh
                # update status
                rec_2.status = STARTED
                rec_2.setAutoDraw(True)
            
            # if rec_2 is active this frame...
            if rec_2.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                postBlock.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in postBlock.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "postBlock" ---
        for thisComponent in postBlock.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for postBlock
        postBlock.tStop = globalClock.getTime(format='float')
        postBlock.tStopRefresh = tThisFlipGlobal
        thisExp.addData('postBlock.stopped', postBlock.tStop)
        # the Routine "postBlock" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed nBlocks repeats of 'outer_loop'
    
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


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


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
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
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
