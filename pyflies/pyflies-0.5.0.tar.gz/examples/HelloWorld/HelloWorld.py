#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple hello world example that will print
10 hello messages in succession and quit.

To generate PsychoPy code call PsychoPy generator
textx generate HelloWorld.pf --target psychopy --overwrite

----

WARNING:
This test was generated by pyFlies (https://github.com/igordejanovic/pyFlies)
on 2020-10-31 11:44:43. The code is partially based on the PsychoPy Builder compiler code and demos.

If you are going to regenerate this file from the pyFlies model again
do not edit it manually or else your manual changes will be lost.

If you publish work using this script the most relevant publication is:

Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
    PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
    https://doi.org/10.3758/s13428-018-01193-y

"""
from __future__ import absolute_import, division

import os  # handy system and path functions
import sys  # to get file system encoding
import re
from random import sample

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle

from psychopy import locale_setup
from psychopy import prefs
from psychopy import gui, visual, sound, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.hardware import keyboard


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = ''
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = os.path.join(_thisDir, u'data',
                        u'%s_%s_%s' % (expInfo['participant'], expName, expInfo['date']))

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=__file__,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=False,
    color='black', units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Hello test
Hello_clock = core.Clock()
Hello_text = visual.TextStim(win=win, name='Hello_text', pos=(0.0, 0.0), height=0.2, color='#ffffff')
Hello_text.model_name = None
Hello_text.cname = 'Hello_text'


Hello_components = [
    Hello_text]


# Trial component settings for Hello test
Hello_1 = [
       # Trial 1
      {'vars': {'order': 1,
            'who': 'Hello, person 1!',
            'repeat_index': 1},
        'ph_exec': [
            {'inst': Hello_text,
                'type': 'visual.text',
                'at': 0.0,
                'duration': 0.4,
                'params': {'text': 'Hello, person 1!'}}]},
       # Trial 2
      {'vars': {'order': 2,
            'who': 'Hello, person 2!',
            'repeat_index': 1},
        'ph_exec': [
            {'inst': Hello_text,
                'type': 'visual.text',
                'at': 0.0,
                'duration': 0.4,
                'params': {'text': 'Hello, person 2!'}}]},
       # Trial 3
      {'vars': {'order': 3,
            'who': 'Hello, person 3!',
            'repeat_index': 1},
        'ph_exec': [
            {'inst': Hello_text,
                'type': 'visual.text',
                'at': 0.0,
                'duration': 0.4,
                'params': {'text': 'Hello, person 3!'}}]},
       # Trial 4
      {'vars': {'order': 4,
            'who': 'Hello, person 4!',
            'repeat_index': 1},
        'ph_exec': [
            {'inst': Hello_text,
                'type': 'visual.text',
                'at': 0.0,
                'duration': 0.4,
                'params': {'text': 'Hello, person 4!'}}]},
       # Trial 5
      {'vars': {'order': 5,
            'who': 'Hello, person 5!',
            'repeat_index': 1},
        'ph_exec': [
            {'inst': Hello_text,
                'type': 'visual.text',
                'at': 0.0,
                'duration': 0.4,
                'params': {'text': 'Hello, person 5!'}}]},
       # Trial 6
      {'vars': {'order': 6,
            'who': 'Hello, person 6!',
            'repeat_index': 1},
        'ph_exec': [
            {'inst': Hello_text,
                'type': 'visual.text',
                'at': 0.0,
                'duration': 0.4,
                'params': {'text': 'Hello, person 6!'}}]},
       # Trial 7
      {'vars': {'order': 7,
            'who': 'Hello, person 7!',
            'repeat_index': 1},
        'ph_exec': [
            {'inst': Hello_text,
                'type': 'visual.text',
                'at': 0.0,
                'duration': 0.4,
                'params': {'text': 'Hello, person 7!'}}]},
       # Trial 8
      {'vars': {'order': 8,
            'who': 'Hello, person 8!',
            'repeat_index': 1},
        'ph_exec': [
            {'inst': Hello_text,
                'type': 'visual.text',
                'at': 0.0,
                'duration': 0.4,
                'params': {'text': 'Hello, person 8!'}}]},
       # Trial 9
      {'vars': {'order': 9,
            'who': 'Hello, person 9!',
            'repeat_index': 1},
        'ph_exec': [
            {'inst': Hello_text,
                'type': 'visual.text',
                'at': 0.0,
                'duration': 0.4,
                'params': {'text': 'Hello, person 9!'}}]},
       # Trial 10
      {'vars': {'order': 10,
            'who': 'Hello, person 10!',
            'repeat_index': 1},
        'ph_exec': [
            {'inst': Hello_text,
                'type': 'visual.text',
                'at': 0.0,
                'duration': 0.4,
                'params': {'text': 'Hello, person 10!'}}]},
]



def unindent(s):
    """
    Remove whitespaces from the beginning of each line of the string s.
    """
    return re.sub(r'\n[\t ]+', r'\n', s)


def get_param(comp, param_name):
    """
    Returns component param for the given name
    """
    try:
        return [v for k, v in comp['params'].items() if k == param_name][0]
    except KeyError:
        return None


def execute_screen(screen, content, duration):
    "Displays the given screen"

    # Calculate font size based on the content number of lines
    screen.setHeight(min(0.5 / len(content.splitlines()), 0.08))

    screen.setText(unindent(content))
    screen.setAutoDraw(True)
    win.flip()

    # Wait for the duration. During wait check for key presses.
    key = event.waitKeys(maxWait=duration if duration > 0 else float('inf'))
    screen.setAutoDraw(False)

    if key in ['escape', 'q']:
        core.quit()


def execute_test(test_trials, test_components, random=False, practice=False):
    """
    Execute given test.  Run components with the given timing and collect
    responses.
    """

    def execute_phase(components, variables=None, should_record=False):
        if not components:
            return
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueTest = True
        correct_response = True

        while continueTest:
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

            # update/draw components on each frame
            for component in components:
                cinst = component['inst']
                ctype = component['type']

                if cinst.status == NOT_STARTED \
                    and tThisFlip >= component['at'] - frameTolerance:
                    # keep track of start time/frame for later
                    cinst.frameNStart = frameN  # exact frame index
                    cinst.tStart = t  # local t and not account for scr refresh
                    cinst.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cinst, 'tStartRefresh')  # time at next scr refresh
                    cinst.status = STARTED

                    # Set component parameters for this trial
                    for pname, pval in component['params'].items():
                        setattr(cinst, pname, pval)

                    # If component is audible start playing
                    if 'audible' in ctype:
                        cinst.play()
                    elif 'mouse' in ctype:
                        cinst.mouseClock.reset()
                        # if button is down already this ISN'T a new click
                        prevButtonState = cinst.getPressed()
                    elif 'keyboard' in ctype:
                        cinst.getKeys()
                        cinst.clock.reset()
                        cinst.start()

                    # Display component on the next flip
                    if 'visual' in ctype:
                        cinst.setAutoDraw(True)

                if 'keyboard' in ctype and cinst.status == STARTED:
                    keys = cinst.getKeys(cinst.valid_keys, waitRelease=False)
                    if 'quit' in keys:
                        core.quit()
                    if keys:
                        correct_keys = get_param(component, 'correct')
                        correct_response = not correct_keys or keys[0].name in correct_keys
                        cinst.key_name = keys[0].name
                        cinst.key_rt = keys[0].rt
                        cinst.key_correct = correct_response
                        continueTest = False

                elif 'mouse' in ctype and cinst.status == STARTED:
                    buttons = cinst.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # If target object(s) are/is defined
                            # check if the mouse was inside our 'clickable' objects
                            # If we don't have targets, then any click is valid
                            x, y = cinst.getPos()
                            gotValidClick = not bool(cinst.targets)
                            for obj in cinst.targets:
                                if obj.contains(x, y):
                                    gotValidClick = True
                                    cinst.clicked_name.append(obj.name)
                            cinst.x.append(x)
                            cinst.y.append(y)
                            buttons = cinst.getPressed()
                            cinst.leftButton.append(buttons[0])
                            cinst.midButton.append(buttons[1])
                            cinst.rightButton.append(buttons[2])
                            cinst.time.append(cinst.mouseClock.getTime())
                            if gotValidClick:  # abort routine on response
                                continueTest = False

                if component['duration'] > 0 and cinst.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cinst.tStartRefresh \
                        + component['duration'] - frameTolerance:
                        # keep track of stop time/frame for later
                        cinst.tStop = t  # not accounting for scr refresh
                        cinst.frameNStop = frameN  # exact frame index
                        cinst.status = FINISHED
                        win.timeOnFlip(cinst, 'tStopRefresh')  # time at next scr refresh

                        # If component is audible stop playing
                        if 'audible' in ctype:
                            cinst.stop()
                        elif 'visual' in ctype:
                            cinst.setAutoDraw(False)

            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            # check if all components have finished
            if not continueTest:
                break
            # will revert to True if at least one component still running
            continueTest = False
            for thisComponent in [c['inst'] for c in components]:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueTest = True
                    # at least one component has not yet finished
                    break

            # refresh the screen
            # don't flip if this test is over or we'll get a blank screen
            if continueTest:
                win.flip()

        # At the end of the phase stop all components
        for component in components:
            cinst = component['inst']
            ctype = component['type']
            if 'visual' in ctype:
                cinst.setAutoDraw(False)
            # If component is audible stop playing
            elif 'audible' in ctype:
                cinst.stop()

        # Register interesting data if not a practice run
        if not practice and should_record:

            # Register trial variables values
            for k, v in variables.items():
                thisExp.addData(k, v) 

            for component in components:
                cinst = component['inst']
                ctype = component['type']

                def datap(attr, name=None):
                    name = attr if name is None else name
                    cname = cinst.model_name if cinst.model_name else cinst.cname
                    col_name = '{}.{}'.format(cname, name)
                    value = getattr(cinst, attr)
                    if type(value) is list:
                        value = value[0]
                    return (col_name, value)

                # component parameters for this trial
                for pname, pval in component['params'].items():
                    cname = cinst.model_name if cinst.model_name else cinst.cname
                    if type(pval) is tuple: pval = str(pval)
                    thisExp.addData('{}.{}'.format(cname, pname), pval)

                if 'keyboard' in ctype:
                    thisExp.addData(*datap('key_name', 'name'))
                    thisExp.addData(*datap('key_rt', 'rt'))
                    thisExp.addData(*datap('key_correct', 'correct'))
                elif 'mouse' in ctype:
                    for dname in ['x', 'y', 'leftButton', 'midButton',
                                  'rightButton', 'time', 'clicked_name']:
                        thisExp.addData(*datap(dname))
                    thisExp.addData(*datap('tStart', 'started'))
                    thisExp.addData(*datap('tStop', 'stopped'))

                elif cinst.model_name is not None:
                    # If we defined name for component in the model we shall record
                    # its start/stop times/frames
                    thisExp.addData(*datap('tStartRefresh', 'started'))
                    thisExp.addData(*datap('frameNStart', 'startFrame'))
                    thisExp.addData(*datap('tStopRefresh', 'stopped'))
                    thisExp.addData(*datap('frameNStop', 'stopFrame'))

            thisExp.nextEntry()

        return correct_response

    # Run trials
    phases = ['ph_fix', 'ph_exec', 'ph_correct', 'ph_error']
    for trial in sample(test_trials, len(test_trials)) if random else test_trials:
        # Initialize components for this trial
        for component in [c for phase in phases for c in trial.get(phase, [])]:
            cinst = component['inst']
            cparams = component['params']
            ctype = component['type']
            cinst.tStart = None
            cinst.tStop = None
            cinst.tStartRefresh = None
            cinst.tStopRefresh = None
            cinst.frameNStart = None
            cinst.frameNStop = None
            if hasattr(cinst, 'status'):
                cinst.status = NOT_STARTED

            # Set component parameters for this trial
            for pname, pval in cparams.items():
                setattr(cinst, pname, pval)

            # If component is audible set duration
            if 'audible' in ctype:
                cinst.secs = component['duration']
            elif 'mouse' in ctype:
                cinst.x = []
                cinst.y = []
                cinst.leftButton = []
                cinst.midButton = []
                cinst.rightButton = []
                cinst.time = []
                cinst.clicked_name = []

        for phase in ['ph_fix', 'ph_exec']:
            if phase in trial:
                correct = execute_phase(trial[phase], trial['vars'], should_record=phase=='ph_exec')

        if correct and 'ph_correct' in trial:
            execute_phase(trial['ph_correct'])
        elif 'ph_error' in trial:
            execute_phase(trial['ph_error'])

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
trialClock = core.Clock()
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# Experiment flow
execute_test(Hello_1, Hello_components)

# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()