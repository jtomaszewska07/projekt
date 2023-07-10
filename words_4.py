#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.3),
    on czerwiec 30, 2023, at 23:00
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
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.3'
expName = 'CAL_POWER'  # from the Builder filename that created this script
expInfo = {
    'participant': 'test',
    'define_main_sub_level': '8',
    'refresh_rate': '60',
    'start_training': '1',
}
# --- Show participant info dialog --
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
    originPath='E:\\!!!!!!!!!!!!!!download\\words_4.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
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

# --- Initialize components for Routine "instruction" ---
text_8 = visual.TextStim(win=win, name='text_8',
    text='W zadaniu, które za chwilę wykonasz, na ekranie będą pojawiać się zdania z brakującym ostatnim słowem. Kiedy naciśniesz spację, na bardzo krótko wyświetli się brakujący wyraz. Nie przejmuj się jeśli nie zdążysz go przeczytać - nie wpłynie to negatywnie na wynik eksperymentu. Twoim zadaniem będzie udzielenie odpowiedzi na pytanie dotyczące treści poprzedniego zdania, zgodnie z intuicją. Aby odpowiedzieć TAK, naciśnij klawisz [T], aby odpowiedzieć NIE, naciśnij klawisz [N].\n\nPRZYKŁAD: Jeśli zobaczysz zdanie Jurek lubi … a po nim słowo truskawki, na pytanie Czy Jurek lubi owoce?, powinieneś odpowiedzieć naciśnięciem klawisza [T] dla odpowiedzi TAK.\n\nZanim rozpocznie się sesja eksperymentalna, zostaniesz poddany sesji treningowej, która ułatwi Ci zrozumienie zadania. W trakcie sesji treningowej, po każdej odzielonej odpowiedzi zostaniesz poinformowany o tym, czy Twoja odpowiedź była poprawna czy błędna. Informacja o poprawności nie będzie się pojawiać w sesji eksperymentalnej.\n\nAby przejść dalej naciśnij spację',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()
# Run 'Begin Experiment' code from SETTINGS
import random
maskgen = random.randint(1, 20)
screen_type = int(expInfo['refresh_rate'])
#reps_sub_level = int(expInfo['define_reps_sub_level'])
main_sub_level = int(expInfo['define_main_sub_level'])
training_on = int(expInfo['start_training'])
mask_level = 24
final_mask_level = 8
trial_count = 0
correct_count = 0
result = 999
test = 1
fake_result = 999
rows = ''
fix_dur=(random.uniform(1.3,2.7)) / 2
win.mouseVisible = False
if screen_type == 240:
    frames_calc = 1
else:
    if screen_type == 60:
        frames_calc = 4
    

#LEVELS:
#1 = 4,17 ms;
#2 = 8,34 ms;
#3 = 12,51 ms;
#4 = 16,68 ms; 
#5 = 20,85 ms; 
#6 = 25,02 ms;
#7 = 29,19 ms;
#8 = 33,36 ms;
#24 = 100,08 ms;

# --- Initialize components for Routine "isi_instr" ---
text_18 = visual.TextStim(win=win, name='text_18',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "ISI_wait_training" ---
blank_break = visual.ImageStim(
    win=win,
    name='blank_break', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "pytanie" ---
text_22 = visual.TextStim(win=win, name='text_22',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_29 = visual.TextStim(win=win, name='text_29',
    text='Aby przejść dalej naciśnij spację',
    font='Open Sans',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_22 = keyboard.Keyboard()

# --- Initialize components for Routine "subliminal_phase_power" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',units='cm', 
    size=(0.5, 0.5),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-1.0, interpolate=True)
premask_D = visual.TextStim(win=win, name='premask_D',
    text='',
    font='Arial',
    pos=(0, -0.0025), height=0.066, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sub_D = visual.TextStim(win=win, name='sub_D',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
postmask_D = visual.TextStim(win=win, name='postmask_D',
    text='',
    font='Arial',
    pos=(0, -0.0025), height=0.066, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "visibility_test" ---
question_component = visual.TextStim(win=win, name='question_component',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
response_awareness_test = keyboard.Keyboard()
Q_button_word = visual.TextStim(win=win, name='Q_button_word',
    text='TAK',
    font='Arial',
    pos=(-0.5, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color=[0.004,0.004,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
E_button_nonword = visual.TextStim(win=win, name='E_button_nonword',
    text='NIE',
    font='Arial',
    pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color=[0.004,0.004,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
left_word = visual.TextStim(win=win, name='left_word',
    text='',
    font='Open Sans',
    pos=(-0.3, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
right_word = visual.TextStim(win=win, name='right_word',
    text='',
    font='Open Sans',
    pos=(0.3, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
red_mask = visual.TextStim(win=win, name='red_mask',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "instruction_2" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='Koniec treningu. Naciśnij spację, by rozpocząć główną część zadania.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "ISI_wait_training" ---
blank_break = visual.ImageStim(
    win=win,
    name='blank_break', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "pytanie2" ---
text_23 = visual.TextStim(win=win, name='text_23',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_30 = visual.TextStim(win=win, name='text_30',
    text='Aby przejść dalej naciśnij spację',
    font='Open Sans',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_23 = keyboard.Keyboard()

# --- Initialize components for Routine "subliminal_phase_power" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',units='cm', 
    size=(0.5, 0.5),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-1.0, interpolate=True)
premask_D = visual.TextStim(win=win, name='premask_D',
    text='',
    font='Arial',
    pos=(0, -0.0025), height=0.066, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sub_D = visual.TextStim(win=win, name='sub_D',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
postmask_D = visual.TextStim(win=win, name='postmask_D',
    text='',
    font='Arial',
    pos=(0, -0.0025), height=0.066, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "visibility_test_1" ---
question_component_1 = visual.TextStim(win=win, name='question_component_1',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
response_awareness_test_1 = keyboard.Keyboard()
Q_button_word_1 = visual.TextStim(win=win, name='Q_button_word_1',
    text='TAK',
    font='Arial',
    pos=(-0.5, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.004,0.004,0.004], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-2.0);
E_button_nonword_1 = visual.TextStim(win=win, name='E_button_nonword_1',
    text='NIE',
    font='Arial',
    pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color=[0.004,0.004,0.004], colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-3.0);
left_word_1 = visual.TextStim(win=win, name='left_word_1',
    text='T',
    font='Open Sans',
    pos=(-0.3, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
right_word_1 = visual.TextStim(win=win, name='right_word_1',
    text='N',
    font='Open Sans',
    pos=(0.3, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
red_mask_1 = visual.TextStim(win=win, name='red_mask_1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ISI_wait" ---
blank_start = visual.ImageStim(
    win=win,
    name='blank_start', 
    image=None, mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# --- Initialize components for Routine "instruction3" ---
text_26 = visual.TextStim(win=win, name='text_26',
    text='Koniec tej części.\n\n Naciśnij spację, by rozpocząć następną część zadania.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_26 = keyboard.Keyboard()

# --- Initialize components for Routine "ISI_wait_training" ---
blank_break = visual.ImageStim(
    win=win,
    name='blank_break', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "pytanie3" ---
text_25 = visual.TextStim(win=win, name='text_25',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_31 = visual.TextStim(win=win, name='text_31',
    text='Aby przejść dalej naciśnij spację.',
    font='Open Sans',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_25 = keyboard.Keyboard()

# --- Initialize components for Routine "subliminal_phase_power" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',units='cm', 
    size=(0.5, 0.5),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-1.0, interpolate=True)
premask_D = visual.TextStim(win=win, name='premask_D',
    text='',
    font='Arial',
    pos=(0, -0.0025), height=0.066, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sub_D = visual.TextStim(win=win, name='sub_D',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
postmask_D = visual.TextStim(win=win, name='postmask_D',
    text='',
    font='Arial',
    pos=(0, -0.0025), height=0.066, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "visibility_test" ---
question_component = visual.TextStim(win=win, name='question_component',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
response_awareness_test = keyboard.Keyboard()
Q_button_word = visual.TextStim(win=win, name='Q_button_word',
    text='TAK',
    font='Arial',
    pos=(-0.5, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color=[0.004,0.004,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
E_button_nonword = visual.TextStim(win=win, name='E_button_nonword',
    text='NIE',
    font='Arial',
    pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color=[0.004,0.004,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
left_word = visual.TextStim(win=win, name='left_word',
    text='',
    font='Open Sans',
    pos=(-0.3, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
right_word = visual.TextStim(win=win, name='right_word',
    text='',
    font='Open Sans',
    pos=(0.3, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
red_mask = visual.TextStim(win=win, name='red_mask',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ISI_wait" ---
blank_start = visual.ImageStim(
    win=win,
    name='blank_start', 
    image=None, mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# --- Initialize components for Routine "instruction_3" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "ISI_wait_training" ---
blank_break = visual.ImageStim(
    win=win,
    name='blank_break', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "pytanie4" ---
text_27 = visual.TextStim(win=win, name='text_27',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_32 = visual.TextStim(win=win, name='text_32',
    text='Aby przejść dalej naciśnij spację. ',
    font='Open Sans',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_27 = keyboard.Keyboard()

# --- Initialize components for Routine "subliminal_phase_power" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',units='cm', 
    size=(0.5, 0.5),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-1.0, interpolate=True)
premask_D = visual.TextStim(win=win, name='premask_D',
    text='',
    font='Arial',
    pos=(0, -0.0025), height=0.066, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sub_D = visual.TextStim(win=win, name='sub_D',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
postmask_D = visual.TextStim(win=win, name='postmask_D',
    text='',
    font='Arial',
    pos=(0, -0.0025), height=0.066, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "visibility_test" ---
question_component = visual.TextStim(win=win, name='question_component',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
response_awareness_test = keyboard.Keyboard()
Q_button_word = visual.TextStim(win=win, name='Q_button_word',
    text='TAK',
    font='Arial',
    pos=(-0.5, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color=[0.004,0.004,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
E_button_nonword = visual.TextStim(win=win, name='E_button_nonword',
    text='NIE',
    font='Arial',
    pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color=[0.004,0.004,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
left_word = visual.TextStim(win=win, name='left_word',
    text='',
    font='Open Sans',
    pos=(-0.3, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
right_word = visual.TextStim(win=win, name='right_word',
    text='',
    font='Open Sans',
    pos=(0.3, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
red_mask = visual.TextStim(win=win, name='red_mask',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ISI_wait" ---
blank_start = visual.ImageStim(
    win=win,
    name='blank_start', 
    image=None, mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# --- Initialize components for Routine "instruction_3" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='A teraz warunek zerowy - najprostszy możliwy, w którym bez użycia EEG sprawdzimy, czy słowa są przetwarzane semantycznie.\n\nTym razem zadanie polega na reagowaniu na CZERWONE targety. Należy jak najszybciej nacisnąć Z, gdy zobaczy się czerwone słowo i M, gdy zobaczy się czerwone pseudosłowo.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "ISI_wait_training" ---
blank_break = visual.ImageStim(
    win=win,
    name='blank_break', 
    image=None, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "pytanie5" ---
text_28 = visual.TextStim(win=win, name='text_28',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_33 = visual.TextStim(win=win, name='text_33',
    text='Aby przejść dalej naciśnij spację',
    font='Open Sans',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_28 = keyboard.Keyboard()

# --- Initialize components for Routine "subliminal_phase_power" ---
cross = visual.ShapeStim(
    win=win, name='cross', vertices='cross',units='cm', 
    size=(0.5, 0.5),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=-1.0, interpolate=True)
premask_D = visual.TextStim(win=win, name='premask_D',
    text='',
    font='Arial',
    pos=(0, -0.0025), height=0.066, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
sub_D = visual.TextStim(win=win, name='sub_D',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
postmask_D = visual.TextStim(win=win, name='postmask_D',
    text='',
    font='Arial',
    pos=(0, -0.0025), height=0.066, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "visibility_test" ---
question_component = visual.TextStim(win=win, name='question_component',
    text='',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
response_awareness_test = keyboard.Keyboard()
Q_button_word = visual.TextStim(win=win, name='Q_button_word',
    text='TAK',
    font='Arial',
    pos=(-0.5, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color=[0.004,0.004,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
E_button_nonword = visual.TextStim(win=win, name='E_button_nonword',
    text='NIE',
    font='Arial',
    pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0, 
    color=[0.004,0.004,0.004], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
left_word = visual.TextStim(win=win, name='left_word',
    text='',
    font='Open Sans',
    pos=(-0.3, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
right_word = visual.TextStim(win=win, name='right_word',
    text='',
    font='Open Sans',
    pos=(0.3, -0.15), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
red_mask = visual.TextStim(win=win, name='red_mask',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "ISI_wait" ---
blank_start = visual.ImageStim(
    win=win,
    name='blank_start', 
    image=None, mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# --- Initialize components for Routine "koniec" ---
text_24 = visual.TextStim(win=win, name='text_24',
    text='Koniec Eksperymentu\n\nDziękujemy za udział w badaniu!\n\nAby zakończyć naciśnij spacje',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_24 = keyboard.Keyboard()

# --- Initialize components for Routine "ISI_end" ---
text_13 = visual.TextStim(win=win, name='text_13',
    text='...',
    font='Arial',
    pos=(0, 0.0377), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_20 = keyboard.Keyboard()
mouse_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_3.mouseClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instruction" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
instructionComponents = [text_8, key_resp_8]
for thisComponent in instructionComponents:
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

# --- Run Routine "instruction" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    
    # if text_8 is starting this frame...
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_8.started')
        # update status
        text_8.status = STARTED
        text_8.setAutoDraw(True)
    
    # if text_8 is active this frame...
    if text_8.status == STARTED:
        # update params
        pass
    
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
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            key_resp_8.duration = _key_resp_8_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction" ---
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
    thisExp.addData('key_resp_8.duration', key_resp_8.duration)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "isi_instr" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
isi_instrComponents = [text_18]
for thisComponent in isi_instrComponents:
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

# --- Run Routine "isi_instr" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_18* updates
    
    # if text_18 is starting this frame...
    if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_18.frameNStart = frameN  # exact frame index
        text_18.tStart = t  # local t and not account for scr refresh
        text_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_18.started')
        # update status
        text_18.status = STARTED
        text_18.setAutoDraw(True)
    
    # if text_18 is active this frame...
    if text_18.status == STARTED:
        # update params
        pass
    
    # if text_18 is stopping this frame...
    if text_18.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_18.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text_18.tStop = t  # not accounting for scr refresh
            text_18.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_18.stopped')
            # update status
            text_18.status = FINISHED
            text_18.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in isi_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "isi_instr" ---
for thisComponent in isi_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

# set up handler to look after randomisation of conditions etc
semantic_priming_test = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Users/Michał/Desktop/stimuli_file_cal_power.xlsx', selection='2,4,6,7'),
    seed=None, name='semantic_priming_test')
thisExp.addLoop(semantic_priming_test)  # add the loop to the experiment
thisSemantic_priming_test = semantic_priming_test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSemantic_priming_test.rgb)
if thisSemantic_priming_test != None:
    for paramName in thisSemantic_priming_test:
        exec('{} = thisSemantic_priming_test[paramName]'.format(paramName))

for thisSemantic_priming_test in semantic_priming_test:
    currentLoop = semantic_priming_test
    # abbreviate parameter names if possible (e.g. rgb = thisSemantic_priming_test.rgb)
    if thisSemantic_priming_test != None:
        for paramName in thisSemantic_priming_test:
            exec('{} = thisSemantic_priming_test[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ISI_wait_training" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISI_wait_trainingComponents = [blank_break]
    for thisComponent in ISI_wait_trainingComponents:
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
    
    # --- Run Routine "ISI_wait_training" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_break* updates
        
        # if blank_break is starting this frame...
        if blank_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_break.frameNStart = frameN  # exact frame index
            blank_break.tStart = t  # local t and not account for scr refresh
            blank_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_break, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_break.started')
            # update status
            blank_break.status = STARTED
            blank_break.setAutoDraw(True)
        
        # if blank_break is active this frame...
        if blank_break.status == STARTED:
            # update params
            pass
        
        # if blank_break is stopping this frame...
        if blank_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_break.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_break.tStop = t  # not accounting for scr refresh
                blank_break.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_break.stopped')
                # update status
                blank_break.status = FINISHED
                blank_break.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_wait_trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_wait_training" ---
    for thisComponent in ISI_wait_trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "pytanie" ---
    continueRoutine = True
    # update component parameters for each repeat
    text_22.setText(zdanie)
    key_resp_22.keys = []
    key_resp_22.rt = []
    _key_resp_22_allKeys = []
    # keep track of which components have finished
    pytanieComponents = [text_22, text_29, key_resp_22]
    for thisComponent in pytanieComponents:
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
    
    # --- Run Routine "pytanie" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_22* updates
        
        # if text_22 is starting this frame...
        if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_22.frameNStart = frameN  # exact frame index
            text_22.tStart = t  # local t and not account for scr refresh
            text_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_22.started')
            # update status
            text_22.status = STARTED
            text_22.setAutoDraw(True)
        
        # if text_22 is active this frame...
        if text_22.status == STARTED:
            # update params
            pass
        
        # *text_29* updates
        
        # if text_29 is starting this frame...
        if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_29.frameNStart = frameN  # exact frame index
            text_29.tStart = t  # local t and not account for scr refresh
            text_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_29.started')
            # update status
            text_29.status = STARTED
            text_29.setAutoDraw(True)
        
        # if text_29 is active this frame...
        if text_29.status == STARTED:
            # update params
            pass
        
        # *key_resp_22* updates
        waitOnFlip = False
        
        # if key_resp_22 is starting this frame...
        if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_22.frameNStart = frameN  # exact frame index
            key_resp_22.tStart = t  # local t and not account for scr refresh
            key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_22.started')
            # update status
            key_resp_22.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_22.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_22.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_22_allKeys.extend(theseKeys)
            if len(_key_resp_22_allKeys):
                key_resp_22.keys = _key_resp_22_allKeys[-1].name  # just the last key pressed
                key_resp_22.rt = _key_resp_22_allKeys[-1].rt
                key_resp_22.duration = _key_resp_22_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pytanieComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pytanie" ---
    for thisComponent in pytanieComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_22.keys in ['', [], None]:  # No response was made
        key_resp_22.keys = None
    semantic_priming_test.addData('key_resp_22.keys',key_resp_22.keys)
    if key_resp_22.keys != None:  # we had a response
        semantic_priming_test.addData('key_resp_22.rt', key_resp_22.rt)
        semantic_priming_test.addData('key_resp_22.duration', key_resp_22.duration)
    # the Routine "pytanie" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "subliminal_phase_power" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from mask_version
    if maskgen==1:
        premaskA = mask101
        postmaskA = mask102
        premaskB = mask103
        premaskB = mask104
        premaskC = mask105
        postmaskC = mask106
        premaskD = mask107
        postmaskD = mask108
    else:
        if maskgen==2:
            premaskA = mask102
            postmaskA = mask103
            premaskB = mask104
            premaskB = mask105
            premaskC = mask106
            postmaskC = mask107
            premaskD = mask108
            postmaskD = mask109
        else:
            if maskgen==3:
                premaskA = mask103
                postmaskA = mask104
                premaskB = mask105
                postmaskB = mask106
                premaskC = mask107
                postmaskC = mask108
                premaskD = mask109
                postmaskD = mask110
            else:
                if maskgen==4:
                    premaskA = mask104
                    postmaskA = mask105
                    premaskB = mask106
                    postmaskB = mask107
                    premaskC = mask108
                    postmaskC = mask109
                    premaskD = mask110
                    postmaskD = mask111
    
                else:
                    if maskgen==5:
                        premaskA = mask105
                        postmaskA = mask106
                        premaskB = mask107
                        postmaskB = mask108
                        premaskC = mask109
                        postmaskC = mask110
                        premaskD = mask111
                        postmaskD = mask112
                    else:
                        if maskgen==6:
                            premaskA = mask106
                            postmaskA = mask107
                            premaskB = mask108
                            postmaskB = mask109
                            premaskC = mask110
                            postmaskC = mask111
                            premaskD = mask112
                            postmaskD = mask113
                        else:
                            if maskgen==7:
                                premaskA = mask107
                                postmaskA = mask108
                                premaskB = mask109
                                postmaskB = mask110
                                premaskC = mask111
                                postmaskC = mask112
                                premaskD = mask113
                                postmaskD = mask114
                            else:
                                if maskgen==8:
                                    premaskA = mask108
                                    postmaskA = mask109
                                    premaskB = mask110
                                    postmaskB = mask111
                                    premaskC = mask112
                                    postmaskC = mask113
                                    premaskD = mask114
                                    postmaskD = mask115
                                else:
                                    if maskgen==9:
                                        premaskA = mask109
                                        postmaskA = mask110
                                        premaskB = mask111
                                        postmaskB = mask112
                                        premaskC = mask113
                                        postmaskC = mask114
                                        premaskD = mask115
                                        postmaskD = mask116
                                    else:
                                        if maskgen==10:
                                            premaskA = mask110
                                            postmaskA = mask111
                                            premaskB = mask112
                                            postmaskB = mask113
                                            premaskC = mask114
                                            postmaskC = mask115
                                            premaskD = mask116
                                            postmaskD = mask117
                                        else:
                                            if maskgen==11:
                                                premaskA = mask111
                                                postmaskA = mask112
                                                premaskB = mask113
                                                postmaskB = mask114
                                                premaskC = mask115
                                                postmaskC = mask116
                                                premaskD = mask117
                                                postmaskD = mask118                                      
                                            else:
                                                if maskgen==12:
                                                    premaskA = mask112
                                                    postmaskA = mask113
                                                    premaskB = mask114
                                                    postmaskB = mask115
                                                    premaskC = mask116
                                                    postmaskC = mask117
                                                    premaskD = mask118
                                                    postmaskD = mask119          
                                                else:
                                                    if maskgen==13:
                                                        premaskA = mask113
                                                        postmaskA = mask114
                                                        premaskB = mask115
                                                        postmaskB = mask116
                                                        premaskC = mask117
                                                        postmaskC = mask118
                                                        premaskD = mask119
                                                        postmaskD = mask120  
                                                    else:
                                                        if maskgen==14:
                                                            premaskA = mask114
                                                            postmaskA = mask115
                                                            premaskB = mask116
                                                            postmaskB = mask117
                                                            premaskC = mask118
                                                            postmaskC = mask119
                                                            premaskD = mask120
                                                            postmaskD = mask101  
                                                        else:
                                                            if maskgen==15:
                                                                premaskA = mask115
                                                                postmaskA = mask116
                                                                premaskB = mask117
                                                                postmaskB = mask118
                                                                premaskC = mask119
                                                                postmaskC = mask120
                                                                premaskD = mask101
                                                                postmaskD = mask102    
                                                            else:
                                                                if maskgen==16:
                                                                    premaskA = mask116
                                                                    postmaskA = mask117
                                                                    premaskB = mask118
                                                                    postmaskB = mask119
                                                                    premaskC = mask120
                                                                    postmaskC = mask101
                                                                    premaskD = mask102
                                                                    postmaskD = mask103                                    
                                                                else:
                                                                    if maskgen==17:
                                                                        premaskA = mask117
                                                                        postmaskA = mask118
                                                                        premaskB = mask119
                                                                        postmaskB = mask120
                                                                        premaskC = mask101
                                                                        postmaskC = mask102
                                                                        premaskD = mask103
                                                                        postmaskD = mask104
                                                                    else:
                                                                        if maskgen==18:
                                                                            premaskA = mask118
                                                                            postmaskA = mask119
                                                                            premaskB = mask120
                                                                            postmaskB = mask101
                                                                            premaskC = mask102
                                                                            postmaskC = mask103
                                                                            premaskD = mask104
                                                                            postmaskD = mask105
                                                                        else:
                                                                            if maskgen==19:
                                                                                premaskA = mask119
                                                                                postmaskA = mask120
                                                                                premaskB = mask101
                                                                                postmaskB = mask102
                                                                                premaskC = mask103
                                                                                postmaskC = mask104
                                                                                premaskD = mask105
                                                                                postmaskD = mask106
                                                                            else:
                                                                                if maskgen==20:
                                                                                    premaskA = mask120
                                                                                    postmaskA = mask101
                                                                                    premaskB = mask102
                                                                                    postmaskB = mask103
                                                                                    premaskC = mask104
                                                                                    postmaskC = mask105
                                                                                    premaskD = mask106
                                                                                    postmaskD = mask107                                                                
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
    premask_D.setColor(color, colorSpace='rgb')
    premask_D.setText(premaskD)
    sub_D.setColor(color, colorSpace='rgb')
    sub_D.setText(sub_test)
    postmask_D.setColor(color, colorSpace='rgb')
    postmask_D.setText(postmaskD)
    # keep track of which components have finished
    subliminal_phase_powerComponents = [cross, premask_D, sub_D, postmask_D]
    for thisComponent in subliminal_phase_powerComponents:
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
    
    # --- Run Routine "subliminal_phase_power" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        
        # if cross is starting this frame...
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            # update status
            cross.status = STARTED
            cross.setAutoDraw(True)
        
        # if cross is active this frame...
        if cross.status == STARTED:
            # update params
            pass
        
        # if cross is stopping this frame...
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        
        # *premask_D* updates
        
        # if premask_D is starting this frame...
        if premask_D.status == NOT_STARTED and cross.status==FINISHED:
            # keep track of start time/frame for later
            premask_D.frameNStart = frameN  # exact frame index
            premask_D.tStart = t  # local t and not account for scr refresh
            premask_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(premask_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'premask_D.started')
            # update status
            premask_D.status = STARTED
            premask_D.setAutoDraw(True)
        
        # if premask_D is active this frame...
        if premask_D.status == STARTED:
            # update params
            pass
        
        # if premask_D is stopping this frame...
        if premask_D.status == STARTED:
            if frameN >= (premask_D.frameNStart + mask_level/frames_calc):
                # keep track of stop time/frame for later
                premask_D.tStop = t  # not accounting for scr refresh
                premask_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'premask_D.stopped')
                # update status
                premask_D.status = FINISHED
                premask_D.setAutoDraw(False)
        
        # *sub_D* updates
        
        # if sub_D is starting this frame...
        if sub_D.status == NOT_STARTED and premask_D.status==FINISHED:
            # keep track of start time/frame for later
            sub_D.frameNStart = frameN  # exact frame index
            sub_D.tStart = t  # local t and not account for scr refresh
            sub_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sub_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sub_D.started')
            # update status
            sub_D.status = STARTED
            sub_D.setAutoDraw(True)
        
        # if sub_D is active this frame...
        if sub_D.status == STARTED:
            # update params
            pass
        
        # if sub_D is stopping this frame...
        if sub_D.status == STARTED:
            if frameN >= (sub_D.frameNStart + main_sub_level/frames_calc):
                # keep track of stop time/frame for later
                sub_D.tStop = t  # not accounting for scr refresh
                sub_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sub_D.stopped')
                # update status
                sub_D.status = FINISHED
                sub_D.setAutoDraw(False)
        
        # *postmask_D* updates
        
        # if postmask_D is starting this frame...
        if postmask_D.status == NOT_STARTED and sub_D.status==FINISHED:
            # keep track of start time/frame for later
            postmask_D.frameNStart = frameN  # exact frame index
            postmask_D.tStart = t  # local t and not account for scr refresh
            postmask_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(postmask_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'postmask_D.started')
            # update status
            postmask_D.status = STARTED
            postmask_D.setAutoDraw(True)
        
        # if postmask_D is active this frame...
        if postmask_D.status == STARTED:
            # update params
            pass
        
        # if postmask_D is stopping this frame...
        if postmask_D.status == STARTED:
            if frameN >= (postmask_D.frameNStart + final_mask_level/frames_calc):
                # keep track of stop time/frame for later
                postmask_D.tStop = t  # not accounting for scr refresh
                postmask_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'postmask_D.stopped')
                # update status
                postmask_D.status = FINISHED
                postmask_D.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in subliminal_phase_powerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "subliminal_phase_power" ---
    for thisComponent in subliminal_phase_powerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "subliminal_phase_power" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "visibility_test" ---
    continueRoutine = True
    # update component parameters for each repeat
    question_component.setText(question)
    response_awareness_test.keys = []
    response_awareness_test.rt = []
    _response_awareness_test_allKeys = []
    left_word.setText('T')
    right_word.setText('N')
    red_mask.setText(question_final)
    # keep track of which components have finished
    visibility_testComponents = [question_component, response_awareness_test, Q_button_word, E_button_nonword, left_word, right_word, red_mask]
    for thisComponent in visibility_testComponents:
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
    
    # --- Run Routine "visibility_test" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *question_component* updates
        
        # if question_component is starting this frame...
        if question_component.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_component.frameNStart = frameN  # exact frame index
            question_component.tStart = t  # local t and not account for scr refresh
            question_component.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_component, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'question_component.started')
            # update status
            question_component.status = STARTED
            question_component.setAutoDraw(True)
        
        # if question_component is active this frame...
        if question_component.status == STARTED:
            # update params
            pass
        
        # *response_awareness_test* updates
        waitOnFlip = False
        
        # if response_awareness_test is starting this frame...
        if response_awareness_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_awareness_test.frameNStart = frameN  # exact frame index
            response_awareness_test.tStart = t  # local t and not account for scr refresh
            response_awareness_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_awareness_test, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_awareness_test.started')
            # update status
            response_awareness_test.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_awareness_test.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_awareness_test.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_awareness_test.status == STARTED and not waitOnFlip:
            theseKeys = response_awareness_test.getKeys(keyList=['t', 'n'], waitRelease=False)
            _response_awareness_test_allKeys.extend(theseKeys)
            if len(_response_awareness_test_allKeys):
                response_awareness_test.keys = _response_awareness_test_allKeys[-1].name  # just the last key pressed
                response_awareness_test.rt = _response_awareness_test_allKeys[-1].rt
                response_awareness_test.duration = _response_awareness_test_allKeys[-1].duration
                # was this correct?
                if (response_awareness_test.keys == str(corrAns)) or (response_awareness_test.keys == corrAns):
                    response_awareness_test.corr = 1
                else:
                    response_awareness_test.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Q_button_word* updates
        
        # if Q_button_word is starting this frame...
        if Q_button_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_button_word.frameNStart = frameN  # exact frame index
            Q_button_word.tStart = t  # local t and not account for scr refresh
            Q_button_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_button_word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Q_button_word.started')
            # update status
            Q_button_word.status = STARTED
            Q_button_word.setAutoDraw(True)
        
        # if Q_button_word is active this frame...
        if Q_button_word.status == STARTED:
            # update params
            pass
        
        # *E_button_nonword* updates
        
        # if E_button_nonword is starting this frame...
        if E_button_nonword.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            E_button_nonword.frameNStart = frameN  # exact frame index
            E_button_nonword.tStart = t  # local t and not account for scr refresh
            E_button_nonword.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(E_button_nonword, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'E_button_nonword.started')
            # update status
            E_button_nonword.status = STARTED
            E_button_nonword.setAutoDraw(True)
        
        # if E_button_nonword is active this frame...
        if E_button_nonword.status == STARTED:
            # update params
            pass
        
        # *left_word* updates
        
        # if left_word is starting this frame...
        if left_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_word.frameNStart = frameN  # exact frame index
            left_word.tStart = t  # local t and not account for scr refresh
            left_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_word.started')
            # update status
            left_word.status = STARTED
            left_word.setAutoDraw(True)
        
        # if left_word is active this frame...
        if left_word.status == STARTED:
            # update params
            pass
        
        # *right_word* updates
        
        # if right_word is starting this frame...
        if right_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_word.frameNStart = frameN  # exact frame index
            right_word.tStart = t  # local t and not account for scr refresh
            right_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_word.started')
            # update status
            right_word.status = STARTED
            right_word.setAutoDraw(True)
        
        # if right_word is active this frame...
        if right_word.status == STARTED:
            # update params
            pass
        
        # *red_mask* updates
        
        # if red_mask is starting this frame...
        if red_mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_mask.frameNStart = frameN  # exact frame index
            red_mask.tStart = t  # local t and not account for scr refresh
            red_mask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_mask, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'red_mask.started')
            # update status
            red_mask.status = STARTED
            red_mask.setAutoDraw(True)
        
        # if red_mask is active this frame...
        if red_mask.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in visibility_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "visibility_test" ---
    for thisComponent in visibility_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_awareness_test.keys in ['', [], None]:  # No response was made
        response_awareness_test.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_awareness_test.corr = 1;  # correct non-response
        else:
           response_awareness_test.corr = 0;  # failed to respond (incorrectly)
    # store data for semantic_priming_test (TrialHandler)
    semantic_priming_test.addData('response_awareness_test.keys',response_awareness_test.keys)
    semantic_priming_test.addData('response_awareness_test.corr', response_awareness_test.corr)
    if response_awareness_test.keys != None:  # we had a response
        semantic_priming_test.addData('response_awareness_test.rt', response_awareness_test.rt)
        semantic_priming_test.addData('response_awareness_test.duration', response_awareness_test.duration)
    # the Routine "visibility_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'semantic_priming_test'


# --- Prepare to start Routine "instruction_2" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
instruction_2Components = [text_2, key_resp_2]
for thisComponent in instruction_2Components:
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

# --- Run Routine "instruction_2" ---
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
    
    # *key_resp_2* updates
    waitOnFlip = False
    
    # if key_resp_2 is starting this frame...
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_2.started')
        # update status
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            key_resp_2.duration = _key_resp_2_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_2" ---
for thisComponent in instruction_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.addData('key_resp_2.duration', key_resp_2.duration)
thisExp.nextEntry()
# the Routine "instruction_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Users/Michał/Desktop/stimuli_file_cal_power.xlsx', selection=rows),
    seed=None, name='trials_1')
thisExp.addLoop(trials_1)  # add the loop to the experiment
thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
if thisTrial_1 != None:
    for paramName in thisTrial_1:
        exec('{} = thisTrial_1[paramName]'.format(paramName))

for thisTrial_1 in trials_1:
    currentLoop = trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1:
            exec('{} = thisTrial_1[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ISI_wait_training" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISI_wait_trainingComponents = [blank_break]
    for thisComponent in ISI_wait_trainingComponents:
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
    
    # --- Run Routine "ISI_wait_training" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_break* updates
        
        # if blank_break is starting this frame...
        if blank_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_break.frameNStart = frameN  # exact frame index
            blank_break.tStart = t  # local t and not account for scr refresh
            blank_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_break, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_break.started')
            # update status
            blank_break.status = STARTED
            blank_break.setAutoDraw(True)
        
        # if blank_break is active this frame...
        if blank_break.status == STARTED:
            # update params
            pass
        
        # if blank_break is stopping this frame...
        if blank_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_break.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_break.tStop = t  # not accounting for scr refresh
                blank_break.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_break.stopped')
                # update status
                blank_break.status = FINISHED
                blank_break.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_wait_trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_wait_training" ---
    for thisComponent in ISI_wait_trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "pytanie2" ---
    continueRoutine = True
    # update component parameters for each repeat
    text_23.setText(zdanie)
    key_resp_23.keys = []
    key_resp_23.rt = []
    _key_resp_23_allKeys = []
    # keep track of which components have finished
    pytanie2Components = [text_23, text_30, key_resp_23]
    for thisComponent in pytanie2Components:
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
    
    # --- Run Routine "pytanie2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_23* updates
        
        # if text_23 is starting this frame...
        if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_23.started')
            # update status
            text_23.status = STARTED
            text_23.setAutoDraw(True)
        
        # if text_23 is active this frame...
        if text_23.status == STARTED:
            # update params
            pass
        
        # *text_30* updates
        
        # if text_30 is starting this frame...
        if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_30.frameNStart = frameN  # exact frame index
            text_30.tStart = t  # local t and not account for scr refresh
            text_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_30.started')
            # update status
            text_30.status = STARTED
            text_30.setAutoDraw(True)
        
        # if text_30 is active this frame...
        if text_30.status == STARTED:
            # update params
            pass
        
        # *key_resp_23* updates
        waitOnFlip = False
        
        # if key_resp_23 is starting this frame...
        if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_23.frameNStart = frameN  # exact frame index
            key_resp_23.tStart = t  # local t and not account for scr refresh
            key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_23.started')
            # update status
            key_resp_23.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_23.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_23.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_23_allKeys.extend(theseKeys)
            if len(_key_resp_23_allKeys):
                key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
                key_resp_23.rt = _key_resp_23_allKeys[-1].rt
                key_resp_23.duration = _key_resp_23_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pytanie2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pytanie2" ---
    for thisComponent in pytanie2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_23.keys in ['', [], None]:  # No response was made
        key_resp_23.keys = None
    trials_1.addData('key_resp_23.keys',key_resp_23.keys)
    if key_resp_23.keys != None:  # we had a response
        trials_1.addData('key_resp_23.rt', key_resp_23.rt)
        trials_1.addData('key_resp_23.duration', key_resp_23.duration)
    # the Routine "pytanie2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "subliminal_phase_power" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from mask_version
    if maskgen==1:
        premaskA = mask101
        postmaskA = mask102
        premaskB = mask103
        premaskB = mask104
        premaskC = mask105
        postmaskC = mask106
        premaskD = mask107
        postmaskD = mask108
    else:
        if maskgen==2:
            premaskA = mask102
            postmaskA = mask103
            premaskB = mask104
            premaskB = mask105
            premaskC = mask106
            postmaskC = mask107
            premaskD = mask108
            postmaskD = mask109
        else:
            if maskgen==3:
                premaskA = mask103
                postmaskA = mask104
                premaskB = mask105
                postmaskB = mask106
                premaskC = mask107
                postmaskC = mask108
                premaskD = mask109
                postmaskD = mask110
            else:
                if maskgen==4:
                    premaskA = mask104
                    postmaskA = mask105
                    premaskB = mask106
                    postmaskB = mask107
                    premaskC = mask108
                    postmaskC = mask109
                    premaskD = mask110
                    postmaskD = mask111
    
                else:
                    if maskgen==5:
                        premaskA = mask105
                        postmaskA = mask106
                        premaskB = mask107
                        postmaskB = mask108
                        premaskC = mask109
                        postmaskC = mask110
                        premaskD = mask111
                        postmaskD = mask112
                    else:
                        if maskgen==6:
                            premaskA = mask106
                            postmaskA = mask107
                            premaskB = mask108
                            postmaskB = mask109
                            premaskC = mask110
                            postmaskC = mask111
                            premaskD = mask112
                            postmaskD = mask113
                        else:
                            if maskgen==7:
                                premaskA = mask107
                                postmaskA = mask108
                                premaskB = mask109
                                postmaskB = mask110
                                premaskC = mask111
                                postmaskC = mask112
                                premaskD = mask113
                                postmaskD = mask114
                            else:
                                if maskgen==8:
                                    premaskA = mask108
                                    postmaskA = mask109
                                    premaskB = mask110
                                    postmaskB = mask111
                                    premaskC = mask112
                                    postmaskC = mask113
                                    premaskD = mask114
                                    postmaskD = mask115
                                else:
                                    if maskgen==9:
                                        premaskA = mask109
                                        postmaskA = mask110
                                        premaskB = mask111
                                        postmaskB = mask112
                                        premaskC = mask113
                                        postmaskC = mask114
                                        premaskD = mask115
                                        postmaskD = mask116
                                    else:
                                        if maskgen==10:
                                            premaskA = mask110
                                            postmaskA = mask111
                                            premaskB = mask112
                                            postmaskB = mask113
                                            premaskC = mask114
                                            postmaskC = mask115
                                            premaskD = mask116
                                            postmaskD = mask117
                                        else:
                                            if maskgen==11:
                                                premaskA = mask111
                                                postmaskA = mask112
                                                premaskB = mask113
                                                postmaskB = mask114
                                                premaskC = mask115
                                                postmaskC = mask116
                                                premaskD = mask117
                                                postmaskD = mask118                                      
                                            else:
                                                if maskgen==12:
                                                    premaskA = mask112
                                                    postmaskA = mask113
                                                    premaskB = mask114
                                                    postmaskB = mask115
                                                    premaskC = mask116
                                                    postmaskC = mask117
                                                    premaskD = mask118
                                                    postmaskD = mask119          
                                                else:
                                                    if maskgen==13:
                                                        premaskA = mask113
                                                        postmaskA = mask114
                                                        premaskB = mask115
                                                        postmaskB = mask116
                                                        premaskC = mask117
                                                        postmaskC = mask118
                                                        premaskD = mask119
                                                        postmaskD = mask120  
                                                    else:
                                                        if maskgen==14:
                                                            premaskA = mask114
                                                            postmaskA = mask115
                                                            premaskB = mask116
                                                            postmaskB = mask117
                                                            premaskC = mask118
                                                            postmaskC = mask119
                                                            premaskD = mask120
                                                            postmaskD = mask101  
                                                        else:
                                                            if maskgen==15:
                                                                premaskA = mask115
                                                                postmaskA = mask116
                                                                premaskB = mask117
                                                                postmaskB = mask118
                                                                premaskC = mask119
                                                                postmaskC = mask120
                                                                premaskD = mask101
                                                                postmaskD = mask102    
                                                            else:
                                                                if maskgen==16:
                                                                    premaskA = mask116
                                                                    postmaskA = mask117
                                                                    premaskB = mask118
                                                                    postmaskB = mask119
                                                                    premaskC = mask120
                                                                    postmaskC = mask101
                                                                    premaskD = mask102
                                                                    postmaskD = mask103                                    
                                                                else:
                                                                    if maskgen==17:
                                                                        premaskA = mask117
                                                                        postmaskA = mask118
                                                                        premaskB = mask119
                                                                        postmaskB = mask120
                                                                        premaskC = mask101
                                                                        postmaskC = mask102
                                                                        premaskD = mask103
                                                                        postmaskD = mask104
                                                                    else:
                                                                        if maskgen==18:
                                                                            premaskA = mask118
                                                                            postmaskA = mask119
                                                                            premaskB = mask120
                                                                            postmaskB = mask101
                                                                            premaskC = mask102
                                                                            postmaskC = mask103
                                                                            premaskD = mask104
                                                                            postmaskD = mask105
                                                                        else:
                                                                            if maskgen==19:
                                                                                premaskA = mask119
                                                                                postmaskA = mask120
                                                                                premaskB = mask101
                                                                                postmaskB = mask102
                                                                                premaskC = mask103
                                                                                postmaskC = mask104
                                                                                premaskD = mask105
                                                                                postmaskD = mask106
                                                                            else:
                                                                                if maskgen==20:
                                                                                    premaskA = mask120
                                                                                    postmaskA = mask101
                                                                                    premaskB = mask102
                                                                                    postmaskB = mask103
                                                                                    premaskC = mask104
                                                                                    postmaskC = mask105
                                                                                    premaskD = mask106
                                                                                    postmaskD = mask107                                                                
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
    premask_D.setColor(color, colorSpace='rgb')
    premask_D.setText(premaskD)
    sub_D.setColor(color, colorSpace='rgb')
    sub_D.setText(sub_test)
    postmask_D.setColor(color, colorSpace='rgb')
    postmask_D.setText(postmaskD)
    # keep track of which components have finished
    subliminal_phase_powerComponents = [cross, premask_D, sub_D, postmask_D]
    for thisComponent in subliminal_phase_powerComponents:
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
    
    # --- Run Routine "subliminal_phase_power" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        
        # if cross is starting this frame...
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            # update status
            cross.status = STARTED
            cross.setAutoDraw(True)
        
        # if cross is active this frame...
        if cross.status == STARTED:
            # update params
            pass
        
        # if cross is stopping this frame...
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        
        # *premask_D* updates
        
        # if premask_D is starting this frame...
        if premask_D.status == NOT_STARTED and cross.status==FINISHED:
            # keep track of start time/frame for later
            premask_D.frameNStart = frameN  # exact frame index
            premask_D.tStart = t  # local t and not account for scr refresh
            premask_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(premask_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'premask_D.started')
            # update status
            premask_D.status = STARTED
            premask_D.setAutoDraw(True)
        
        # if premask_D is active this frame...
        if premask_D.status == STARTED:
            # update params
            pass
        
        # if premask_D is stopping this frame...
        if premask_D.status == STARTED:
            if frameN >= (premask_D.frameNStart + mask_level/frames_calc):
                # keep track of stop time/frame for later
                premask_D.tStop = t  # not accounting for scr refresh
                premask_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'premask_D.stopped')
                # update status
                premask_D.status = FINISHED
                premask_D.setAutoDraw(False)
        
        # *sub_D* updates
        
        # if sub_D is starting this frame...
        if sub_D.status == NOT_STARTED and premask_D.status==FINISHED:
            # keep track of start time/frame for later
            sub_D.frameNStart = frameN  # exact frame index
            sub_D.tStart = t  # local t and not account for scr refresh
            sub_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sub_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sub_D.started')
            # update status
            sub_D.status = STARTED
            sub_D.setAutoDraw(True)
        
        # if sub_D is active this frame...
        if sub_D.status == STARTED:
            # update params
            pass
        
        # if sub_D is stopping this frame...
        if sub_D.status == STARTED:
            if frameN >= (sub_D.frameNStart + main_sub_level/frames_calc):
                # keep track of stop time/frame for later
                sub_D.tStop = t  # not accounting for scr refresh
                sub_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sub_D.stopped')
                # update status
                sub_D.status = FINISHED
                sub_D.setAutoDraw(False)
        
        # *postmask_D* updates
        
        # if postmask_D is starting this frame...
        if postmask_D.status == NOT_STARTED and sub_D.status==FINISHED:
            # keep track of start time/frame for later
            postmask_D.frameNStart = frameN  # exact frame index
            postmask_D.tStart = t  # local t and not account for scr refresh
            postmask_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(postmask_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'postmask_D.started')
            # update status
            postmask_D.status = STARTED
            postmask_D.setAutoDraw(True)
        
        # if postmask_D is active this frame...
        if postmask_D.status == STARTED:
            # update params
            pass
        
        # if postmask_D is stopping this frame...
        if postmask_D.status == STARTED:
            if frameN >= (postmask_D.frameNStart + final_mask_level/frames_calc):
                # keep track of stop time/frame for later
                postmask_D.tStop = t  # not accounting for scr refresh
                postmask_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'postmask_D.stopped')
                # update status
                postmask_D.status = FINISHED
                postmask_D.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in subliminal_phase_powerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "subliminal_phase_power" ---
    for thisComponent in subliminal_phase_powerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "subliminal_phase_power" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "visibility_test_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    question_component_1.setText(question)
    response_awareness_test_1.keys = []
    response_awareness_test_1.rt = []
    _response_awareness_test_1_allKeys = []
    red_mask_1.setText(question_final)
    # keep track of which components have finished
    visibility_test_1Components = [question_component_1, response_awareness_test_1, Q_button_word_1, E_button_nonword_1, left_word_1, right_word_1, red_mask_1]
    for thisComponent in visibility_test_1Components:
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
    
    # --- Run Routine "visibility_test_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *question_component_1* updates
        
        # if question_component_1 is starting this frame...
        if question_component_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_component_1.frameNStart = frameN  # exact frame index
            question_component_1.tStart = t  # local t and not account for scr refresh
            question_component_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_component_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'question_component_1.started')
            # update status
            question_component_1.status = STARTED
            question_component_1.setAutoDraw(True)
        
        # if question_component_1 is active this frame...
        if question_component_1.status == STARTED:
            # update params
            pass
        
        # *response_awareness_test_1* updates
        waitOnFlip = False
        
        # if response_awareness_test_1 is starting this frame...
        if response_awareness_test_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_awareness_test_1.frameNStart = frameN  # exact frame index
            response_awareness_test_1.tStart = t  # local t and not account for scr refresh
            response_awareness_test_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_awareness_test_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_awareness_test_1.started')
            # update status
            response_awareness_test_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_awareness_test_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_awareness_test_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_awareness_test_1.status == STARTED and not waitOnFlip:
            theseKeys = response_awareness_test_1.getKeys(keyList=['t', 'n'], waitRelease=False)
            _response_awareness_test_1_allKeys.extend(theseKeys)
            if len(_response_awareness_test_1_allKeys):
                response_awareness_test_1.keys = _response_awareness_test_1_allKeys[-1].name  # just the last key pressed
                response_awareness_test_1.rt = _response_awareness_test_1_allKeys[-1].rt
                response_awareness_test_1.duration = _response_awareness_test_1_allKeys[-1].duration
                # was this correct?
                if (response_awareness_test_1.keys == str(corrAns)) or (response_awareness_test_1.keys == corrAns):
                    response_awareness_test_1.corr = 1
                else:
                    response_awareness_test_1.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Q_button_word_1* updates
        
        # if Q_button_word_1 is starting this frame...
        if Q_button_word_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_button_word_1.frameNStart = frameN  # exact frame index
            Q_button_word_1.tStart = t  # local t and not account for scr refresh
            Q_button_word_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_button_word_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Q_button_word_1.started')
            # update status
            Q_button_word_1.status = STARTED
            Q_button_word_1.setAutoDraw(True)
        
        # if Q_button_word_1 is active this frame...
        if Q_button_word_1.status == STARTED:
            # update params
            pass
        
        # *E_button_nonword_1* updates
        
        # if E_button_nonword_1 is starting this frame...
        if E_button_nonword_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            E_button_nonword_1.frameNStart = frameN  # exact frame index
            E_button_nonword_1.tStart = t  # local t and not account for scr refresh
            E_button_nonword_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(E_button_nonword_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'E_button_nonword_1.started')
            # update status
            E_button_nonword_1.status = STARTED
            E_button_nonword_1.setAutoDraw(True)
        
        # if E_button_nonword_1 is active this frame...
        if E_button_nonword_1.status == STARTED:
            # update params
            pass
        
        # *left_word_1* updates
        
        # if left_word_1 is starting this frame...
        if left_word_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_word_1.frameNStart = frameN  # exact frame index
            left_word_1.tStart = t  # local t and not account for scr refresh
            left_word_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_word_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_word_1.started')
            # update status
            left_word_1.status = STARTED
            left_word_1.setAutoDraw(True)
        
        # if left_word_1 is active this frame...
        if left_word_1.status == STARTED:
            # update params
            pass
        
        # *right_word_1* updates
        
        # if right_word_1 is starting this frame...
        if right_word_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_word_1.frameNStart = frameN  # exact frame index
            right_word_1.tStart = t  # local t and not account for scr refresh
            right_word_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_word_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_word_1.started')
            # update status
            right_word_1.status = STARTED
            right_word_1.setAutoDraw(True)
        
        # if right_word_1 is active this frame...
        if right_word_1.status == STARTED:
            # update params
            pass
        
        # *red_mask_1* updates
        
        # if red_mask_1 is starting this frame...
        if red_mask_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_mask_1.frameNStart = frameN  # exact frame index
            red_mask_1.tStart = t  # local t and not account for scr refresh
            red_mask_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_mask_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'red_mask_1.started')
            # update status
            red_mask_1.status = STARTED
            red_mask_1.setAutoDraw(True)
        
        # if red_mask_1 is active this frame...
        if red_mask_1.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in visibility_test_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "visibility_test_1" ---
    for thisComponent in visibility_test_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_awareness_test_1.keys in ['', [], None]:  # No response was made
        response_awareness_test_1.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_awareness_test_1.corr = 1;  # correct non-response
        else:
           response_awareness_test_1.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_1 (TrialHandler)
    trials_1.addData('response_awareness_test_1.keys',response_awareness_test_1.keys)
    trials_1.addData('response_awareness_test_1.corr', response_awareness_test_1.corr)
    if response_awareness_test_1.keys != None:  # we had a response
        trials_1.addData('response_awareness_test_1.rt', response_awareness_test_1.rt)
        trials_1.addData('response_awareness_test_1.duration', response_awareness_test_1.duration)
    # the Routine "visibility_test_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI_wait" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from trials_counter_after
    trial_count = trial_count + 1
    
    if response_awareness_test.corr:
         correct_count = correct_count + 1
    # keep track of which components have finished
    ISI_waitComponents = [blank_start]
    for thisComponent in ISI_waitComponents:
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
    
    # --- Run Routine "ISI_wait" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_start* updates
        
        # if blank_start is starting this frame...
        if blank_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_start.frameNStart = frameN  # exact frame index
            blank_start.tStart = t  # local t and not account for scr refresh
            blank_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_start, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_start.started')
            # update status
            blank_start.status = STARTED
            blank_start.setAutoDraw(True)
        
        # if blank_start is active this frame...
        if blank_start.status == STARTED:
            # update params
            pass
        
        # if blank_start is stopping this frame...
        if blank_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_start.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_start.tStop = t  # not accounting for scr refresh
                blank_start.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_start.stopped')
                # update status
                blank_start.status = FINISHED
                blank_start.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_wait" ---
    for thisComponent in ISI_waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_1'


# --- Prepare to start Routine "instruction3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_26.keys = []
key_resp_26.rt = []
_key_resp_26_allKeys = []
# keep track of which components have finished
instruction3Components = [text_26, key_resp_26]
for thisComponent in instruction3Components:
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

# --- Run Routine "instruction3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_26* updates
    
    # if text_26 is starting this frame...
    if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_26.frameNStart = frameN  # exact frame index
        text_26.tStart = t  # local t and not account for scr refresh
        text_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_26.started')
        # update status
        text_26.status = STARTED
        text_26.setAutoDraw(True)
    
    # if text_26 is active this frame...
    if text_26.status == STARTED:
        # update params
        pass
    
    # *key_resp_26* updates
    waitOnFlip = False
    
    # if key_resp_26 is starting this frame...
    if key_resp_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_26.frameNStart = frameN  # exact frame index
        key_resp_26.tStart = t  # local t and not account for scr refresh
        key_resp_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_26, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_26.started')
        # update status
        key_resp_26.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_26.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_26.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_26.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_26.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_26_allKeys.extend(theseKeys)
        if len(_key_resp_26_allKeys):
            key_resp_26.keys = _key_resp_26_allKeys[-1].name  # just the last key pressed
            key_resp_26.rt = _key_resp_26_allKeys[-1].rt
            key_resp_26.duration = _key_resp_26_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction3" ---
for thisComponent in instruction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_26.keys in ['', [], None]:  # No response was made
    key_resp_26.keys = None
thisExp.addData('key_resp_26.keys',key_resp_26.keys)
if key_resp_26.keys != None:  # we had a response
    thisExp.addData('key_resp_26.rt', key_resp_26.rt)
    thisExp.addData('key_resp_26.duration', key_resp_26.duration)
thisExp.nextEntry()
# the Routine "instruction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Users/Michał/Desktop/stimuli_file_cal_power.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ISI_wait_training" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISI_wait_trainingComponents = [blank_break]
    for thisComponent in ISI_wait_trainingComponents:
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
    
    # --- Run Routine "ISI_wait_training" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_break* updates
        
        # if blank_break is starting this frame...
        if blank_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_break.frameNStart = frameN  # exact frame index
            blank_break.tStart = t  # local t and not account for scr refresh
            blank_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_break, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_break.started')
            # update status
            blank_break.status = STARTED
            blank_break.setAutoDraw(True)
        
        # if blank_break is active this frame...
        if blank_break.status == STARTED:
            # update params
            pass
        
        # if blank_break is stopping this frame...
        if blank_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_break.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_break.tStop = t  # not accounting for scr refresh
                blank_break.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_break.stopped')
                # update status
                blank_break.status = FINISHED
                blank_break.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_wait_trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_wait_training" ---
    for thisComponent in ISI_wait_trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "pytanie3" ---
    continueRoutine = True
    # update component parameters for each repeat
    text_25.setText(zdanie)
    key_resp_25.keys = []
    key_resp_25.rt = []
    _key_resp_25_allKeys = []
    # keep track of which components have finished
    pytanie3Components = [text_25, text_31, key_resp_25]
    for thisComponent in pytanie3Components:
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
    
    # --- Run Routine "pytanie3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_25* updates
        
        # if text_25 is starting this frame...
        if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_25.frameNStart = frameN  # exact frame index
            text_25.tStart = t  # local t and not account for scr refresh
            text_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_25.started')
            # update status
            text_25.status = STARTED
            text_25.setAutoDraw(True)
        
        # if text_25 is active this frame...
        if text_25.status == STARTED:
            # update params
            pass
        
        # *text_31* updates
        
        # if text_31 is starting this frame...
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_31.started')
            # update status
            text_31.status = STARTED
            text_31.setAutoDraw(True)
        
        # if text_31 is active this frame...
        if text_31.status == STARTED:
            # update params
            pass
        
        # *key_resp_25* updates
        waitOnFlip = False
        
        # if key_resp_25 is starting this frame...
        if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_25.frameNStart = frameN  # exact frame index
            key_resp_25.tStart = t  # local t and not account for scr refresh
            key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_25.started')
            # update status
            key_resp_25.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_25.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_25.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_25_allKeys.extend(theseKeys)
            if len(_key_resp_25_allKeys):
                key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
                key_resp_25.rt = _key_resp_25_allKeys[-1].rt
                key_resp_25.duration = _key_resp_25_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pytanie3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pytanie3" ---
    for thisComponent in pytanie3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_25.keys in ['', [], None]:  # No response was made
        key_resp_25.keys = None
    trials_2.addData('key_resp_25.keys',key_resp_25.keys)
    if key_resp_25.keys != None:  # we had a response
        trials_2.addData('key_resp_25.rt', key_resp_25.rt)
        trials_2.addData('key_resp_25.duration', key_resp_25.duration)
    # the Routine "pytanie3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "subliminal_phase_power" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from mask_version
    if maskgen==1:
        premaskA = mask101
        postmaskA = mask102
        premaskB = mask103
        premaskB = mask104
        premaskC = mask105
        postmaskC = mask106
        premaskD = mask107
        postmaskD = mask108
    else:
        if maskgen==2:
            premaskA = mask102
            postmaskA = mask103
            premaskB = mask104
            premaskB = mask105
            premaskC = mask106
            postmaskC = mask107
            premaskD = mask108
            postmaskD = mask109
        else:
            if maskgen==3:
                premaskA = mask103
                postmaskA = mask104
                premaskB = mask105
                postmaskB = mask106
                premaskC = mask107
                postmaskC = mask108
                premaskD = mask109
                postmaskD = mask110
            else:
                if maskgen==4:
                    premaskA = mask104
                    postmaskA = mask105
                    premaskB = mask106
                    postmaskB = mask107
                    premaskC = mask108
                    postmaskC = mask109
                    premaskD = mask110
                    postmaskD = mask111
    
                else:
                    if maskgen==5:
                        premaskA = mask105
                        postmaskA = mask106
                        premaskB = mask107
                        postmaskB = mask108
                        premaskC = mask109
                        postmaskC = mask110
                        premaskD = mask111
                        postmaskD = mask112
                    else:
                        if maskgen==6:
                            premaskA = mask106
                            postmaskA = mask107
                            premaskB = mask108
                            postmaskB = mask109
                            premaskC = mask110
                            postmaskC = mask111
                            premaskD = mask112
                            postmaskD = mask113
                        else:
                            if maskgen==7:
                                premaskA = mask107
                                postmaskA = mask108
                                premaskB = mask109
                                postmaskB = mask110
                                premaskC = mask111
                                postmaskC = mask112
                                premaskD = mask113
                                postmaskD = mask114
                            else:
                                if maskgen==8:
                                    premaskA = mask108
                                    postmaskA = mask109
                                    premaskB = mask110
                                    postmaskB = mask111
                                    premaskC = mask112
                                    postmaskC = mask113
                                    premaskD = mask114
                                    postmaskD = mask115
                                else:
                                    if maskgen==9:
                                        premaskA = mask109
                                        postmaskA = mask110
                                        premaskB = mask111
                                        postmaskB = mask112
                                        premaskC = mask113
                                        postmaskC = mask114
                                        premaskD = mask115
                                        postmaskD = mask116
                                    else:
                                        if maskgen==10:
                                            premaskA = mask110
                                            postmaskA = mask111
                                            premaskB = mask112
                                            postmaskB = mask113
                                            premaskC = mask114
                                            postmaskC = mask115
                                            premaskD = mask116
                                            postmaskD = mask117
                                        else:
                                            if maskgen==11:
                                                premaskA = mask111
                                                postmaskA = mask112
                                                premaskB = mask113
                                                postmaskB = mask114
                                                premaskC = mask115
                                                postmaskC = mask116
                                                premaskD = mask117
                                                postmaskD = mask118                                      
                                            else:
                                                if maskgen==12:
                                                    premaskA = mask112
                                                    postmaskA = mask113
                                                    premaskB = mask114
                                                    postmaskB = mask115
                                                    premaskC = mask116
                                                    postmaskC = mask117
                                                    premaskD = mask118
                                                    postmaskD = mask119          
                                                else:
                                                    if maskgen==13:
                                                        premaskA = mask113
                                                        postmaskA = mask114
                                                        premaskB = mask115
                                                        postmaskB = mask116
                                                        premaskC = mask117
                                                        postmaskC = mask118
                                                        premaskD = mask119
                                                        postmaskD = mask120  
                                                    else:
                                                        if maskgen==14:
                                                            premaskA = mask114
                                                            postmaskA = mask115
                                                            premaskB = mask116
                                                            postmaskB = mask117
                                                            premaskC = mask118
                                                            postmaskC = mask119
                                                            premaskD = mask120
                                                            postmaskD = mask101  
                                                        else:
                                                            if maskgen==15:
                                                                premaskA = mask115
                                                                postmaskA = mask116
                                                                premaskB = mask117
                                                                postmaskB = mask118
                                                                premaskC = mask119
                                                                postmaskC = mask120
                                                                premaskD = mask101
                                                                postmaskD = mask102    
                                                            else:
                                                                if maskgen==16:
                                                                    premaskA = mask116
                                                                    postmaskA = mask117
                                                                    premaskB = mask118
                                                                    postmaskB = mask119
                                                                    premaskC = mask120
                                                                    postmaskC = mask101
                                                                    premaskD = mask102
                                                                    postmaskD = mask103                                    
                                                                else:
                                                                    if maskgen==17:
                                                                        premaskA = mask117
                                                                        postmaskA = mask118
                                                                        premaskB = mask119
                                                                        postmaskB = mask120
                                                                        premaskC = mask101
                                                                        postmaskC = mask102
                                                                        premaskD = mask103
                                                                        postmaskD = mask104
                                                                    else:
                                                                        if maskgen==18:
                                                                            premaskA = mask118
                                                                            postmaskA = mask119
                                                                            premaskB = mask120
                                                                            postmaskB = mask101
                                                                            premaskC = mask102
                                                                            postmaskC = mask103
                                                                            premaskD = mask104
                                                                            postmaskD = mask105
                                                                        else:
                                                                            if maskgen==19:
                                                                                premaskA = mask119
                                                                                postmaskA = mask120
                                                                                premaskB = mask101
                                                                                postmaskB = mask102
                                                                                premaskC = mask103
                                                                                postmaskC = mask104
                                                                                premaskD = mask105
                                                                                postmaskD = mask106
                                                                            else:
                                                                                if maskgen==20:
                                                                                    premaskA = mask120
                                                                                    postmaskA = mask101
                                                                                    premaskB = mask102
                                                                                    postmaskB = mask103
                                                                                    premaskC = mask104
                                                                                    postmaskC = mask105
                                                                                    premaskD = mask106
                                                                                    postmaskD = mask107                                                                
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
    premask_D.setColor(color, colorSpace='rgb')
    premask_D.setText(premaskD)
    sub_D.setColor(color, colorSpace='rgb')
    sub_D.setText(sub_test)
    postmask_D.setColor(color, colorSpace='rgb')
    postmask_D.setText(postmaskD)
    # keep track of which components have finished
    subliminal_phase_powerComponents = [cross, premask_D, sub_D, postmask_D]
    for thisComponent in subliminal_phase_powerComponents:
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
    
    # --- Run Routine "subliminal_phase_power" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        
        # if cross is starting this frame...
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            # update status
            cross.status = STARTED
            cross.setAutoDraw(True)
        
        # if cross is active this frame...
        if cross.status == STARTED:
            # update params
            pass
        
        # if cross is stopping this frame...
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        
        # *premask_D* updates
        
        # if premask_D is starting this frame...
        if premask_D.status == NOT_STARTED and cross.status==FINISHED:
            # keep track of start time/frame for later
            premask_D.frameNStart = frameN  # exact frame index
            premask_D.tStart = t  # local t and not account for scr refresh
            premask_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(premask_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'premask_D.started')
            # update status
            premask_D.status = STARTED
            premask_D.setAutoDraw(True)
        
        # if premask_D is active this frame...
        if premask_D.status == STARTED:
            # update params
            pass
        
        # if premask_D is stopping this frame...
        if premask_D.status == STARTED:
            if frameN >= (premask_D.frameNStart + mask_level/frames_calc):
                # keep track of stop time/frame for later
                premask_D.tStop = t  # not accounting for scr refresh
                premask_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'premask_D.stopped')
                # update status
                premask_D.status = FINISHED
                premask_D.setAutoDraw(False)
        
        # *sub_D* updates
        
        # if sub_D is starting this frame...
        if sub_D.status == NOT_STARTED and premask_D.status==FINISHED:
            # keep track of start time/frame for later
            sub_D.frameNStart = frameN  # exact frame index
            sub_D.tStart = t  # local t and not account for scr refresh
            sub_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sub_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sub_D.started')
            # update status
            sub_D.status = STARTED
            sub_D.setAutoDraw(True)
        
        # if sub_D is active this frame...
        if sub_D.status == STARTED:
            # update params
            pass
        
        # if sub_D is stopping this frame...
        if sub_D.status == STARTED:
            if frameN >= (sub_D.frameNStart + main_sub_level/frames_calc):
                # keep track of stop time/frame for later
                sub_D.tStop = t  # not accounting for scr refresh
                sub_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sub_D.stopped')
                # update status
                sub_D.status = FINISHED
                sub_D.setAutoDraw(False)
        
        # *postmask_D* updates
        
        # if postmask_D is starting this frame...
        if postmask_D.status == NOT_STARTED and sub_D.status==FINISHED:
            # keep track of start time/frame for later
            postmask_D.frameNStart = frameN  # exact frame index
            postmask_D.tStart = t  # local t and not account for scr refresh
            postmask_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(postmask_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'postmask_D.started')
            # update status
            postmask_D.status = STARTED
            postmask_D.setAutoDraw(True)
        
        # if postmask_D is active this frame...
        if postmask_D.status == STARTED:
            # update params
            pass
        
        # if postmask_D is stopping this frame...
        if postmask_D.status == STARTED:
            if frameN >= (postmask_D.frameNStart + final_mask_level/frames_calc):
                # keep track of stop time/frame for later
                postmask_D.tStop = t  # not accounting for scr refresh
                postmask_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'postmask_D.stopped')
                # update status
                postmask_D.status = FINISHED
                postmask_D.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in subliminal_phase_powerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "subliminal_phase_power" ---
    for thisComponent in subliminal_phase_powerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "subliminal_phase_power" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "visibility_test" ---
    continueRoutine = True
    # update component parameters for each repeat
    question_component.setText(question)
    response_awareness_test.keys = []
    response_awareness_test.rt = []
    _response_awareness_test_allKeys = []
    left_word.setText('T')
    right_word.setText('N')
    red_mask.setText(question_final)
    # keep track of which components have finished
    visibility_testComponents = [question_component, response_awareness_test, Q_button_word, E_button_nonword, left_word, right_word, red_mask]
    for thisComponent in visibility_testComponents:
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
    
    # --- Run Routine "visibility_test" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *question_component* updates
        
        # if question_component is starting this frame...
        if question_component.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_component.frameNStart = frameN  # exact frame index
            question_component.tStart = t  # local t and not account for scr refresh
            question_component.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_component, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'question_component.started')
            # update status
            question_component.status = STARTED
            question_component.setAutoDraw(True)
        
        # if question_component is active this frame...
        if question_component.status == STARTED:
            # update params
            pass
        
        # *response_awareness_test* updates
        waitOnFlip = False
        
        # if response_awareness_test is starting this frame...
        if response_awareness_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_awareness_test.frameNStart = frameN  # exact frame index
            response_awareness_test.tStart = t  # local t and not account for scr refresh
            response_awareness_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_awareness_test, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_awareness_test.started')
            # update status
            response_awareness_test.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_awareness_test.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_awareness_test.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_awareness_test.status == STARTED and not waitOnFlip:
            theseKeys = response_awareness_test.getKeys(keyList=['t', 'n'], waitRelease=False)
            _response_awareness_test_allKeys.extend(theseKeys)
            if len(_response_awareness_test_allKeys):
                response_awareness_test.keys = _response_awareness_test_allKeys[-1].name  # just the last key pressed
                response_awareness_test.rt = _response_awareness_test_allKeys[-1].rt
                response_awareness_test.duration = _response_awareness_test_allKeys[-1].duration
                # was this correct?
                if (response_awareness_test.keys == str(corrAns)) or (response_awareness_test.keys == corrAns):
                    response_awareness_test.corr = 1
                else:
                    response_awareness_test.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Q_button_word* updates
        
        # if Q_button_word is starting this frame...
        if Q_button_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_button_word.frameNStart = frameN  # exact frame index
            Q_button_word.tStart = t  # local t and not account for scr refresh
            Q_button_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_button_word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Q_button_word.started')
            # update status
            Q_button_word.status = STARTED
            Q_button_word.setAutoDraw(True)
        
        # if Q_button_word is active this frame...
        if Q_button_word.status == STARTED:
            # update params
            pass
        
        # *E_button_nonword* updates
        
        # if E_button_nonword is starting this frame...
        if E_button_nonword.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            E_button_nonword.frameNStart = frameN  # exact frame index
            E_button_nonword.tStart = t  # local t and not account for scr refresh
            E_button_nonword.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(E_button_nonword, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'E_button_nonword.started')
            # update status
            E_button_nonword.status = STARTED
            E_button_nonword.setAutoDraw(True)
        
        # if E_button_nonword is active this frame...
        if E_button_nonword.status == STARTED:
            # update params
            pass
        
        # *left_word* updates
        
        # if left_word is starting this frame...
        if left_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_word.frameNStart = frameN  # exact frame index
            left_word.tStart = t  # local t and not account for scr refresh
            left_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_word.started')
            # update status
            left_word.status = STARTED
            left_word.setAutoDraw(True)
        
        # if left_word is active this frame...
        if left_word.status == STARTED:
            # update params
            pass
        
        # *right_word* updates
        
        # if right_word is starting this frame...
        if right_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_word.frameNStart = frameN  # exact frame index
            right_word.tStart = t  # local t and not account for scr refresh
            right_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_word.started')
            # update status
            right_word.status = STARTED
            right_word.setAutoDraw(True)
        
        # if right_word is active this frame...
        if right_word.status == STARTED:
            # update params
            pass
        
        # *red_mask* updates
        
        # if red_mask is starting this frame...
        if red_mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_mask.frameNStart = frameN  # exact frame index
            red_mask.tStart = t  # local t and not account for scr refresh
            red_mask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_mask, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'red_mask.started')
            # update status
            red_mask.status = STARTED
            red_mask.setAutoDraw(True)
        
        # if red_mask is active this frame...
        if red_mask.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in visibility_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "visibility_test" ---
    for thisComponent in visibility_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_awareness_test.keys in ['', [], None]:  # No response was made
        response_awareness_test.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_awareness_test.corr = 1;  # correct non-response
        else:
           response_awareness_test.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('response_awareness_test.keys',response_awareness_test.keys)
    trials_2.addData('response_awareness_test.corr', response_awareness_test.corr)
    if response_awareness_test.keys != None:  # we had a response
        trials_2.addData('response_awareness_test.rt', response_awareness_test.rt)
        trials_2.addData('response_awareness_test.duration', response_awareness_test.duration)
    # the Routine "visibility_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI_wait" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from trials_counter_after
    trial_count = trial_count + 1
    
    if response_awareness_test.corr:
         correct_count = correct_count + 1
    # keep track of which components have finished
    ISI_waitComponents = [blank_start]
    for thisComponent in ISI_waitComponents:
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
    
    # --- Run Routine "ISI_wait" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_start* updates
        
        # if blank_start is starting this frame...
        if blank_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_start.frameNStart = frameN  # exact frame index
            blank_start.tStart = t  # local t and not account for scr refresh
            blank_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_start, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_start.started')
            # update status
            blank_start.status = STARTED
            blank_start.setAutoDraw(True)
        
        # if blank_start is active this frame...
        if blank_start.status == STARTED:
            # update params
            pass
        
        # if blank_start is stopping this frame...
        if blank_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_start.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_start.tStop = t  # not accounting for scr refresh
                blank_start.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_start.stopped')
                # update status
                blank_start.status = FINISHED
                blank_start.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_wait" ---
    for thisComponent in ISI_waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# --- Prepare to start Routine "instruction_3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruction_3Components = [text_3, key_resp_3]
for thisComponent in instruction_3Components:
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

# --- Run Routine "instruction_3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    
    # if text_3 is starting this frame...
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        # update status
        text_3.status = STARTED
        text_3.setAutoDraw(True)
    
    # if text_3 is active this frame...
    if text_3.status == STARTED:
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
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            key_resp_3.duration = _key_resp_3_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_3" ---
for thisComponent in instruction_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
    thisExp.addData('key_resp_3.duration', key_resp_3.duration)
thisExp.nextEntry()
# the Routine "instruction_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Users/Michał/Desktop/stimuli_file_cal_power.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ISI_wait_training" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISI_wait_trainingComponents = [blank_break]
    for thisComponent in ISI_wait_trainingComponents:
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
    
    # --- Run Routine "ISI_wait_training" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_break* updates
        
        # if blank_break is starting this frame...
        if blank_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_break.frameNStart = frameN  # exact frame index
            blank_break.tStart = t  # local t and not account for scr refresh
            blank_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_break, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_break.started')
            # update status
            blank_break.status = STARTED
            blank_break.setAutoDraw(True)
        
        # if blank_break is active this frame...
        if blank_break.status == STARTED:
            # update params
            pass
        
        # if blank_break is stopping this frame...
        if blank_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_break.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_break.tStop = t  # not accounting for scr refresh
                blank_break.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_break.stopped')
                # update status
                blank_break.status = FINISHED
                blank_break.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_wait_trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_wait_training" ---
    for thisComponent in ISI_wait_trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "pytanie4" ---
    continueRoutine = True
    # update component parameters for each repeat
    text_27.setText(zdanie)
    key_resp_27.keys = []
    key_resp_27.rt = []
    _key_resp_27_allKeys = []
    # keep track of which components have finished
    pytanie4Components = [text_27, text_32, key_resp_27]
    for thisComponent in pytanie4Components:
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
    
    # --- Run Routine "pytanie4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_27* updates
        
        # if text_27 is starting this frame...
        if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_27.frameNStart = frameN  # exact frame index
            text_27.tStart = t  # local t and not account for scr refresh
            text_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_27.started')
            # update status
            text_27.status = STARTED
            text_27.setAutoDraw(True)
        
        # if text_27 is active this frame...
        if text_27.status == STARTED:
            # update params
            pass
        
        # *text_32* updates
        
        # if text_32 is starting this frame...
        if text_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_32.frameNStart = frameN  # exact frame index
            text_32.tStart = t  # local t and not account for scr refresh
            text_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_32.started')
            # update status
            text_32.status = STARTED
            text_32.setAutoDraw(True)
        
        # if text_32 is active this frame...
        if text_32.status == STARTED:
            # update params
            pass
        
        # *key_resp_27* updates
        waitOnFlip = False
        
        # if key_resp_27 is starting this frame...
        if key_resp_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_27.frameNStart = frameN  # exact frame index
            key_resp_27.tStart = t  # local t and not account for scr refresh
            key_resp_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_27, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_27.started')
            # update status
            key_resp_27.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_27.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_27.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_27.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_27.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_27_allKeys.extend(theseKeys)
            if len(_key_resp_27_allKeys):
                key_resp_27.keys = _key_resp_27_allKeys[-1].name  # just the last key pressed
                key_resp_27.rt = _key_resp_27_allKeys[-1].rt
                key_resp_27.duration = _key_resp_27_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pytanie4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pytanie4" ---
    for thisComponent in pytanie4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_27.keys in ['', [], None]:  # No response was made
        key_resp_27.keys = None
    trials_3.addData('key_resp_27.keys',key_resp_27.keys)
    if key_resp_27.keys != None:  # we had a response
        trials_3.addData('key_resp_27.rt', key_resp_27.rt)
        trials_3.addData('key_resp_27.duration', key_resp_27.duration)
    # the Routine "pytanie4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "subliminal_phase_power" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from mask_version
    if maskgen==1:
        premaskA = mask101
        postmaskA = mask102
        premaskB = mask103
        premaskB = mask104
        premaskC = mask105
        postmaskC = mask106
        premaskD = mask107
        postmaskD = mask108
    else:
        if maskgen==2:
            premaskA = mask102
            postmaskA = mask103
            premaskB = mask104
            premaskB = mask105
            premaskC = mask106
            postmaskC = mask107
            premaskD = mask108
            postmaskD = mask109
        else:
            if maskgen==3:
                premaskA = mask103
                postmaskA = mask104
                premaskB = mask105
                postmaskB = mask106
                premaskC = mask107
                postmaskC = mask108
                premaskD = mask109
                postmaskD = mask110
            else:
                if maskgen==4:
                    premaskA = mask104
                    postmaskA = mask105
                    premaskB = mask106
                    postmaskB = mask107
                    premaskC = mask108
                    postmaskC = mask109
                    premaskD = mask110
                    postmaskD = mask111
    
                else:
                    if maskgen==5:
                        premaskA = mask105
                        postmaskA = mask106
                        premaskB = mask107
                        postmaskB = mask108
                        premaskC = mask109
                        postmaskC = mask110
                        premaskD = mask111
                        postmaskD = mask112
                    else:
                        if maskgen==6:
                            premaskA = mask106
                            postmaskA = mask107
                            premaskB = mask108
                            postmaskB = mask109
                            premaskC = mask110
                            postmaskC = mask111
                            premaskD = mask112
                            postmaskD = mask113
                        else:
                            if maskgen==7:
                                premaskA = mask107
                                postmaskA = mask108
                                premaskB = mask109
                                postmaskB = mask110
                                premaskC = mask111
                                postmaskC = mask112
                                premaskD = mask113
                                postmaskD = mask114
                            else:
                                if maskgen==8:
                                    premaskA = mask108
                                    postmaskA = mask109
                                    premaskB = mask110
                                    postmaskB = mask111
                                    premaskC = mask112
                                    postmaskC = mask113
                                    premaskD = mask114
                                    postmaskD = mask115
                                else:
                                    if maskgen==9:
                                        premaskA = mask109
                                        postmaskA = mask110
                                        premaskB = mask111
                                        postmaskB = mask112
                                        premaskC = mask113
                                        postmaskC = mask114
                                        premaskD = mask115
                                        postmaskD = mask116
                                    else:
                                        if maskgen==10:
                                            premaskA = mask110
                                            postmaskA = mask111
                                            premaskB = mask112
                                            postmaskB = mask113
                                            premaskC = mask114
                                            postmaskC = mask115
                                            premaskD = mask116
                                            postmaskD = mask117
                                        else:
                                            if maskgen==11:
                                                premaskA = mask111
                                                postmaskA = mask112
                                                premaskB = mask113
                                                postmaskB = mask114
                                                premaskC = mask115
                                                postmaskC = mask116
                                                premaskD = mask117
                                                postmaskD = mask118                                      
                                            else:
                                                if maskgen==12:
                                                    premaskA = mask112
                                                    postmaskA = mask113
                                                    premaskB = mask114
                                                    postmaskB = mask115
                                                    premaskC = mask116
                                                    postmaskC = mask117
                                                    premaskD = mask118
                                                    postmaskD = mask119          
                                                else:
                                                    if maskgen==13:
                                                        premaskA = mask113
                                                        postmaskA = mask114
                                                        premaskB = mask115
                                                        postmaskB = mask116
                                                        premaskC = mask117
                                                        postmaskC = mask118
                                                        premaskD = mask119
                                                        postmaskD = mask120  
                                                    else:
                                                        if maskgen==14:
                                                            premaskA = mask114
                                                            postmaskA = mask115
                                                            premaskB = mask116
                                                            postmaskB = mask117
                                                            premaskC = mask118
                                                            postmaskC = mask119
                                                            premaskD = mask120
                                                            postmaskD = mask101  
                                                        else:
                                                            if maskgen==15:
                                                                premaskA = mask115
                                                                postmaskA = mask116
                                                                premaskB = mask117
                                                                postmaskB = mask118
                                                                premaskC = mask119
                                                                postmaskC = mask120
                                                                premaskD = mask101
                                                                postmaskD = mask102    
                                                            else:
                                                                if maskgen==16:
                                                                    premaskA = mask116
                                                                    postmaskA = mask117
                                                                    premaskB = mask118
                                                                    postmaskB = mask119
                                                                    premaskC = mask120
                                                                    postmaskC = mask101
                                                                    premaskD = mask102
                                                                    postmaskD = mask103                                    
                                                                else:
                                                                    if maskgen==17:
                                                                        premaskA = mask117
                                                                        postmaskA = mask118
                                                                        premaskB = mask119
                                                                        postmaskB = mask120
                                                                        premaskC = mask101
                                                                        postmaskC = mask102
                                                                        premaskD = mask103
                                                                        postmaskD = mask104
                                                                    else:
                                                                        if maskgen==18:
                                                                            premaskA = mask118
                                                                            postmaskA = mask119
                                                                            premaskB = mask120
                                                                            postmaskB = mask101
                                                                            premaskC = mask102
                                                                            postmaskC = mask103
                                                                            premaskD = mask104
                                                                            postmaskD = mask105
                                                                        else:
                                                                            if maskgen==19:
                                                                                premaskA = mask119
                                                                                postmaskA = mask120
                                                                                premaskB = mask101
                                                                                postmaskB = mask102
                                                                                premaskC = mask103
                                                                                postmaskC = mask104
                                                                                premaskD = mask105
                                                                                postmaskD = mask106
                                                                            else:
                                                                                if maskgen==20:
                                                                                    premaskA = mask120
                                                                                    postmaskA = mask101
                                                                                    premaskB = mask102
                                                                                    postmaskB = mask103
                                                                                    premaskC = mask104
                                                                                    postmaskC = mask105
                                                                                    premaskD = mask106
                                                                                    postmaskD = mask107                                                                
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
    premask_D.setColor(color, colorSpace='rgb')
    premask_D.setText(premaskD)
    sub_D.setColor(color, colorSpace='rgb')
    sub_D.setText(sub_test)
    postmask_D.setColor(color, colorSpace='rgb')
    postmask_D.setText(postmaskD)
    # keep track of which components have finished
    subliminal_phase_powerComponents = [cross, premask_D, sub_D, postmask_D]
    for thisComponent in subliminal_phase_powerComponents:
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
    
    # --- Run Routine "subliminal_phase_power" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        
        # if cross is starting this frame...
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            # update status
            cross.status = STARTED
            cross.setAutoDraw(True)
        
        # if cross is active this frame...
        if cross.status == STARTED:
            # update params
            pass
        
        # if cross is stopping this frame...
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        
        # *premask_D* updates
        
        # if premask_D is starting this frame...
        if premask_D.status == NOT_STARTED and cross.status==FINISHED:
            # keep track of start time/frame for later
            premask_D.frameNStart = frameN  # exact frame index
            premask_D.tStart = t  # local t and not account for scr refresh
            premask_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(premask_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'premask_D.started')
            # update status
            premask_D.status = STARTED
            premask_D.setAutoDraw(True)
        
        # if premask_D is active this frame...
        if premask_D.status == STARTED:
            # update params
            pass
        
        # if premask_D is stopping this frame...
        if premask_D.status == STARTED:
            if frameN >= (premask_D.frameNStart + mask_level/frames_calc):
                # keep track of stop time/frame for later
                premask_D.tStop = t  # not accounting for scr refresh
                premask_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'premask_D.stopped')
                # update status
                premask_D.status = FINISHED
                premask_D.setAutoDraw(False)
        
        # *sub_D* updates
        
        # if sub_D is starting this frame...
        if sub_D.status == NOT_STARTED and premask_D.status==FINISHED:
            # keep track of start time/frame for later
            sub_D.frameNStart = frameN  # exact frame index
            sub_D.tStart = t  # local t and not account for scr refresh
            sub_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sub_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sub_D.started')
            # update status
            sub_D.status = STARTED
            sub_D.setAutoDraw(True)
        
        # if sub_D is active this frame...
        if sub_D.status == STARTED:
            # update params
            pass
        
        # if sub_D is stopping this frame...
        if sub_D.status == STARTED:
            if frameN >= (sub_D.frameNStart + main_sub_level/frames_calc):
                # keep track of stop time/frame for later
                sub_D.tStop = t  # not accounting for scr refresh
                sub_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sub_D.stopped')
                # update status
                sub_D.status = FINISHED
                sub_D.setAutoDraw(False)
        
        # *postmask_D* updates
        
        # if postmask_D is starting this frame...
        if postmask_D.status == NOT_STARTED and sub_D.status==FINISHED:
            # keep track of start time/frame for later
            postmask_D.frameNStart = frameN  # exact frame index
            postmask_D.tStart = t  # local t and not account for scr refresh
            postmask_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(postmask_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'postmask_D.started')
            # update status
            postmask_D.status = STARTED
            postmask_D.setAutoDraw(True)
        
        # if postmask_D is active this frame...
        if postmask_D.status == STARTED:
            # update params
            pass
        
        # if postmask_D is stopping this frame...
        if postmask_D.status == STARTED:
            if frameN >= (postmask_D.frameNStart + final_mask_level/frames_calc):
                # keep track of stop time/frame for later
                postmask_D.tStop = t  # not accounting for scr refresh
                postmask_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'postmask_D.stopped')
                # update status
                postmask_D.status = FINISHED
                postmask_D.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in subliminal_phase_powerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "subliminal_phase_power" ---
    for thisComponent in subliminal_phase_powerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "subliminal_phase_power" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "visibility_test" ---
    continueRoutine = True
    # update component parameters for each repeat
    question_component.setText(question)
    response_awareness_test.keys = []
    response_awareness_test.rt = []
    _response_awareness_test_allKeys = []
    left_word.setText('T')
    right_word.setText('N')
    red_mask.setText(question_final)
    # keep track of which components have finished
    visibility_testComponents = [question_component, response_awareness_test, Q_button_word, E_button_nonword, left_word, right_word, red_mask]
    for thisComponent in visibility_testComponents:
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
    
    # --- Run Routine "visibility_test" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *question_component* updates
        
        # if question_component is starting this frame...
        if question_component.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_component.frameNStart = frameN  # exact frame index
            question_component.tStart = t  # local t and not account for scr refresh
            question_component.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_component, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'question_component.started')
            # update status
            question_component.status = STARTED
            question_component.setAutoDraw(True)
        
        # if question_component is active this frame...
        if question_component.status == STARTED:
            # update params
            pass
        
        # *response_awareness_test* updates
        waitOnFlip = False
        
        # if response_awareness_test is starting this frame...
        if response_awareness_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_awareness_test.frameNStart = frameN  # exact frame index
            response_awareness_test.tStart = t  # local t and not account for scr refresh
            response_awareness_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_awareness_test, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_awareness_test.started')
            # update status
            response_awareness_test.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_awareness_test.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_awareness_test.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_awareness_test.status == STARTED and not waitOnFlip:
            theseKeys = response_awareness_test.getKeys(keyList=['t', 'n'], waitRelease=False)
            _response_awareness_test_allKeys.extend(theseKeys)
            if len(_response_awareness_test_allKeys):
                response_awareness_test.keys = _response_awareness_test_allKeys[-1].name  # just the last key pressed
                response_awareness_test.rt = _response_awareness_test_allKeys[-1].rt
                response_awareness_test.duration = _response_awareness_test_allKeys[-1].duration
                # was this correct?
                if (response_awareness_test.keys == str(corrAns)) or (response_awareness_test.keys == corrAns):
                    response_awareness_test.corr = 1
                else:
                    response_awareness_test.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Q_button_word* updates
        
        # if Q_button_word is starting this frame...
        if Q_button_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_button_word.frameNStart = frameN  # exact frame index
            Q_button_word.tStart = t  # local t and not account for scr refresh
            Q_button_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_button_word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Q_button_word.started')
            # update status
            Q_button_word.status = STARTED
            Q_button_word.setAutoDraw(True)
        
        # if Q_button_word is active this frame...
        if Q_button_word.status == STARTED:
            # update params
            pass
        
        # *E_button_nonword* updates
        
        # if E_button_nonword is starting this frame...
        if E_button_nonword.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            E_button_nonword.frameNStart = frameN  # exact frame index
            E_button_nonword.tStart = t  # local t and not account for scr refresh
            E_button_nonword.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(E_button_nonword, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'E_button_nonword.started')
            # update status
            E_button_nonword.status = STARTED
            E_button_nonword.setAutoDraw(True)
        
        # if E_button_nonword is active this frame...
        if E_button_nonword.status == STARTED:
            # update params
            pass
        
        # *left_word* updates
        
        # if left_word is starting this frame...
        if left_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_word.frameNStart = frameN  # exact frame index
            left_word.tStart = t  # local t and not account for scr refresh
            left_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_word.started')
            # update status
            left_word.status = STARTED
            left_word.setAutoDraw(True)
        
        # if left_word is active this frame...
        if left_word.status == STARTED:
            # update params
            pass
        
        # *right_word* updates
        
        # if right_word is starting this frame...
        if right_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_word.frameNStart = frameN  # exact frame index
            right_word.tStart = t  # local t and not account for scr refresh
            right_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_word.started')
            # update status
            right_word.status = STARTED
            right_word.setAutoDraw(True)
        
        # if right_word is active this frame...
        if right_word.status == STARTED:
            # update params
            pass
        
        # *red_mask* updates
        
        # if red_mask is starting this frame...
        if red_mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_mask.frameNStart = frameN  # exact frame index
            red_mask.tStart = t  # local t and not account for scr refresh
            red_mask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_mask, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'red_mask.started')
            # update status
            red_mask.status = STARTED
            red_mask.setAutoDraw(True)
        
        # if red_mask is active this frame...
        if red_mask.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in visibility_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "visibility_test" ---
    for thisComponent in visibility_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_awareness_test.keys in ['', [], None]:  # No response was made
        response_awareness_test.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_awareness_test.corr = 1;  # correct non-response
        else:
           response_awareness_test.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('response_awareness_test.keys',response_awareness_test.keys)
    trials_3.addData('response_awareness_test.corr', response_awareness_test.corr)
    if response_awareness_test.keys != None:  # we had a response
        trials_3.addData('response_awareness_test.rt', response_awareness_test.rt)
        trials_3.addData('response_awareness_test.duration', response_awareness_test.duration)
    # the Routine "visibility_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI_wait" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from trials_counter_after
    trial_count = trial_count + 1
    
    if response_awareness_test.corr:
         correct_count = correct_count + 1
    # keep track of which components have finished
    ISI_waitComponents = [blank_start]
    for thisComponent in ISI_waitComponents:
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
    
    # --- Run Routine "ISI_wait" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_start* updates
        
        # if blank_start is starting this frame...
        if blank_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_start.frameNStart = frameN  # exact frame index
            blank_start.tStart = t  # local t and not account for scr refresh
            blank_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_start, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_start.started')
            # update status
            blank_start.status = STARTED
            blank_start.setAutoDraw(True)
        
        # if blank_start is active this frame...
        if blank_start.status == STARTED:
            # update params
            pass
        
        # if blank_start is stopping this frame...
        if blank_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_start.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_start.tStop = t  # not accounting for scr refresh
                blank_start.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_start.stopped')
                # update status
                blank_start.status = FINISHED
                blank_start.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_wait" ---
    for thisComponent in ISI_waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# --- Prepare to start Routine "instruction_3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instruction_3Components = [text_3, key_resp_3]
for thisComponent in instruction_3Components:
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

# --- Run Routine "instruction_3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    
    # if text_3 is starting this frame...
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        # update status
        text_3.status = STARTED
        text_3.setAutoDraw(True)
    
    # if text_3 is active this frame...
    if text_3.status == STARTED:
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
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            key_resp_3.duration = _key_resp_3_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_3" ---
for thisComponent in instruction_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
    thisExp.addData('key_resp_3.duration', key_resp_3.duration)
thisExp.nextEntry()
# the Routine "instruction_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('C:/Users/Michał/Desktop/stimuli_file_cal_power.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ISI_wait_training" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISI_wait_trainingComponents = [blank_break]
    for thisComponent in ISI_wait_trainingComponents:
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
    
    # --- Run Routine "ISI_wait_training" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_break* updates
        
        # if blank_break is starting this frame...
        if blank_break.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_break.frameNStart = frameN  # exact frame index
            blank_break.tStart = t  # local t and not account for scr refresh
            blank_break.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_break, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_break.started')
            # update status
            blank_break.status = STARTED
            blank_break.setAutoDraw(True)
        
        # if blank_break is active this frame...
        if blank_break.status == STARTED:
            # update params
            pass
        
        # if blank_break is stopping this frame...
        if blank_break.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_break.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_break.tStop = t  # not accounting for scr refresh
                blank_break.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_break.stopped')
                # update status
                blank_break.status = FINISHED
                blank_break.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_wait_trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_wait_training" ---
    for thisComponent in ISI_wait_trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "pytanie5" ---
    continueRoutine = True
    # update component parameters for each repeat
    text_28.setText(zdanie)
    key_resp_28.keys = []
    key_resp_28.rt = []
    _key_resp_28_allKeys = []
    # keep track of which components have finished
    pytanie5Components = [text_28, text_33, key_resp_28]
    for thisComponent in pytanie5Components:
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
    
    # --- Run Routine "pytanie5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_28* updates
        
        # if text_28 is starting this frame...
        if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_28.frameNStart = frameN  # exact frame index
            text_28.tStart = t  # local t and not account for scr refresh
            text_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_28.started')
            # update status
            text_28.status = STARTED
            text_28.setAutoDraw(True)
        
        # if text_28 is active this frame...
        if text_28.status == STARTED:
            # update params
            pass
        
        # *text_33* updates
        
        # if text_33 is starting this frame...
        if text_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_33.frameNStart = frameN  # exact frame index
            text_33.tStart = t  # local t and not account for scr refresh
            text_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_33.started')
            # update status
            text_33.status = STARTED
            text_33.setAutoDraw(True)
        
        # if text_33 is active this frame...
        if text_33.status == STARTED:
            # update params
            pass
        
        # *key_resp_28* updates
        waitOnFlip = False
        
        # if key_resp_28 is starting this frame...
        if key_resp_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_28.frameNStart = frameN  # exact frame index
            key_resp_28.tStart = t  # local t and not account for scr refresh
            key_resp_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_28, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_28.started')
            # update status
            key_resp_28.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_28.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_28.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_28.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_28.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_28_allKeys.extend(theseKeys)
            if len(_key_resp_28_allKeys):
                key_resp_28.keys = _key_resp_28_allKeys[-1].name  # just the last key pressed
                key_resp_28.rt = _key_resp_28_allKeys[-1].rt
                key_resp_28.duration = _key_resp_28_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pytanie5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pytanie5" ---
    for thisComponent in pytanie5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_28.keys in ['', [], None]:  # No response was made
        key_resp_28.keys = None
    trials_4.addData('key_resp_28.keys',key_resp_28.keys)
    if key_resp_28.keys != None:  # we had a response
        trials_4.addData('key_resp_28.rt', key_resp_28.rt)
        trials_4.addData('key_resp_28.duration', key_resp_28.duration)
    # the Routine "pytanie5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "subliminal_phase_power" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from mask_version
    if maskgen==1:
        premaskA = mask101
        postmaskA = mask102
        premaskB = mask103
        premaskB = mask104
        premaskC = mask105
        postmaskC = mask106
        premaskD = mask107
        postmaskD = mask108
    else:
        if maskgen==2:
            premaskA = mask102
            postmaskA = mask103
            premaskB = mask104
            premaskB = mask105
            premaskC = mask106
            postmaskC = mask107
            premaskD = mask108
            postmaskD = mask109
        else:
            if maskgen==3:
                premaskA = mask103
                postmaskA = mask104
                premaskB = mask105
                postmaskB = mask106
                premaskC = mask107
                postmaskC = mask108
                premaskD = mask109
                postmaskD = mask110
            else:
                if maskgen==4:
                    premaskA = mask104
                    postmaskA = mask105
                    premaskB = mask106
                    postmaskB = mask107
                    premaskC = mask108
                    postmaskC = mask109
                    premaskD = mask110
                    postmaskD = mask111
    
                else:
                    if maskgen==5:
                        premaskA = mask105
                        postmaskA = mask106
                        premaskB = mask107
                        postmaskB = mask108
                        premaskC = mask109
                        postmaskC = mask110
                        premaskD = mask111
                        postmaskD = mask112
                    else:
                        if maskgen==6:
                            premaskA = mask106
                            postmaskA = mask107
                            premaskB = mask108
                            postmaskB = mask109
                            premaskC = mask110
                            postmaskC = mask111
                            premaskD = mask112
                            postmaskD = mask113
                        else:
                            if maskgen==7:
                                premaskA = mask107
                                postmaskA = mask108
                                premaskB = mask109
                                postmaskB = mask110
                                premaskC = mask111
                                postmaskC = mask112
                                premaskD = mask113
                                postmaskD = mask114
                            else:
                                if maskgen==8:
                                    premaskA = mask108
                                    postmaskA = mask109
                                    premaskB = mask110
                                    postmaskB = mask111
                                    premaskC = mask112
                                    postmaskC = mask113
                                    premaskD = mask114
                                    postmaskD = mask115
                                else:
                                    if maskgen==9:
                                        premaskA = mask109
                                        postmaskA = mask110
                                        premaskB = mask111
                                        postmaskB = mask112
                                        premaskC = mask113
                                        postmaskC = mask114
                                        premaskD = mask115
                                        postmaskD = mask116
                                    else:
                                        if maskgen==10:
                                            premaskA = mask110
                                            postmaskA = mask111
                                            premaskB = mask112
                                            postmaskB = mask113
                                            premaskC = mask114
                                            postmaskC = mask115
                                            premaskD = mask116
                                            postmaskD = mask117
                                        else:
                                            if maskgen==11:
                                                premaskA = mask111
                                                postmaskA = mask112
                                                premaskB = mask113
                                                postmaskB = mask114
                                                premaskC = mask115
                                                postmaskC = mask116
                                                premaskD = mask117
                                                postmaskD = mask118                                      
                                            else:
                                                if maskgen==12:
                                                    premaskA = mask112
                                                    postmaskA = mask113
                                                    premaskB = mask114
                                                    postmaskB = mask115
                                                    premaskC = mask116
                                                    postmaskC = mask117
                                                    premaskD = mask118
                                                    postmaskD = mask119          
                                                else:
                                                    if maskgen==13:
                                                        premaskA = mask113
                                                        postmaskA = mask114
                                                        premaskB = mask115
                                                        postmaskB = mask116
                                                        premaskC = mask117
                                                        postmaskC = mask118
                                                        premaskD = mask119
                                                        postmaskD = mask120  
                                                    else:
                                                        if maskgen==14:
                                                            premaskA = mask114
                                                            postmaskA = mask115
                                                            premaskB = mask116
                                                            postmaskB = mask117
                                                            premaskC = mask118
                                                            postmaskC = mask119
                                                            premaskD = mask120
                                                            postmaskD = mask101  
                                                        else:
                                                            if maskgen==15:
                                                                premaskA = mask115
                                                                postmaskA = mask116
                                                                premaskB = mask117
                                                                postmaskB = mask118
                                                                premaskC = mask119
                                                                postmaskC = mask120
                                                                premaskD = mask101
                                                                postmaskD = mask102    
                                                            else:
                                                                if maskgen==16:
                                                                    premaskA = mask116
                                                                    postmaskA = mask117
                                                                    premaskB = mask118
                                                                    postmaskB = mask119
                                                                    premaskC = mask120
                                                                    postmaskC = mask101
                                                                    premaskD = mask102
                                                                    postmaskD = mask103                                    
                                                                else:
                                                                    if maskgen==17:
                                                                        premaskA = mask117
                                                                        postmaskA = mask118
                                                                        premaskB = mask119
                                                                        postmaskB = mask120
                                                                        premaskC = mask101
                                                                        postmaskC = mask102
                                                                        premaskD = mask103
                                                                        postmaskD = mask104
                                                                    else:
                                                                        if maskgen==18:
                                                                            premaskA = mask118
                                                                            postmaskA = mask119
                                                                            premaskB = mask120
                                                                            postmaskB = mask101
                                                                            premaskC = mask102
                                                                            postmaskC = mask103
                                                                            premaskD = mask104
                                                                            postmaskD = mask105
                                                                        else:
                                                                            if maskgen==19:
                                                                                premaskA = mask119
                                                                                postmaskA = mask120
                                                                                premaskB = mask101
                                                                                postmaskB = mask102
                                                                                premaskC = mask103
                                                                                postmaskC = mask104
                                                                                premaskD = mask105
                                                                                postmaskD = mask106
                                                                            else:
                                                                                if maskgen==20:
                                                                                    premaskA = mask120
                                                                                    postmaskA = mask101
                                                                                    premaskB = mask102
                                                                                    postmaskB = mask103
                                                                                    premaskC = mask104
                                                                                    postmaskC = mask105
                                                                                    premaskD = mask106
                                                                                    postmaskD = mask107                                                                
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
                                                                    
    premask_D.setColor(color, colorSpace='rgb')
    premask_D.setText(premaskD)
    sub_D.setColor(color, colorSpace='rgb')
    sub_D.setText(sub_test)
    postmask_D.setColor(color, colorSpace='rgb')
    postmask_D.setText(postmaskD)
    # keep track of which components have finished
    subliminal_phase_powerComponents = [cross, premask_D, sub_D, postmask_D]
    for thisComponent in subliminal_phase_powerComponents:
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
    
    # --- Run Routine "subliminal_phase_power" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *cross* updates
        
        # if cross is starting this frame...
        if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            cross.frameNStart = frameN  # exact frame index
            cross.tStart = t  # local t and not account for scr refresh
            cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'cross.started')
            # update status
            cross.status = STARTED
            cross.setAutoDraw(True)
        
        # if cross is active this frame...
        if cross.status == STARTED:
            # update params
            pass
        
        # if cross is stopping this frame...
        if cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > cross.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                cross.tStop = t  # not accounting for scr refresh
                cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross.stopped')
                # update status
                cross.status = FINISHED
                cross.setAutoDraw(False)
        
        # *premask_D* updates
        
        # if premask_D is starting this frame...
        if premask_D.status == NOT_STARTED and cross.status==FINISHED:
            # keep track of start time/frame for later
            premask_D.frameNStart = frameN  # exact frame index
            premask_D.tStart = t  # local t and not account for scr refresh
            premask_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(premask_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'premask_D.started')
            # update status
            premask_D.status = STARTED
            premask_D.setAutoDraw(True)
        
        # if premask_D is active this frame...
        if premask_D.status == STARTED:
            # update params
            pass
        
        # if premask_D is stopping this frame...
        if premask_D.status == STARTED:
            if frameN >= (premask_D.frameNStart + mask_level/frames_calc):
                # keep track of stop time/frame for later
                premask_D.tStop = t  # not accounting for scr refresh
                premask_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'premask_D.stopped')
                # update status
                premask_D.status = FINISHED
                premask_D.setAutoDraw(False)
        
        # *sub_D* updates
        
        # if sub_D is starting this frame...
        if sub_D.status == NOT_STARTED and premask_D.status==FINISHED:
            # keep track of start time/frame for later
            sub_D.frameNStart = frameN  # exact frame index
            sub_D.tStart = t  # local t and not account for scr refresh
            sub_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sub_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sub_D.started')
            # update status
            sub_D.status = STARTED
            sub_D.setAutoDraw(True)
        
        # if sub_D is active this frame...
        if sub_D.status == STARTED:
            # update params
            pass
        
        # if sub_D is stopping this frame...
        if sub_D.status == STARTED:
            if frameN >= (sub_D.frameNStart + main_sub_level/frames_calc):
                # keep track of stop time/frame for later
                sub_D.tStop = t  # not accounting for scr refresh
                sub_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sub_D.stopped')
                # update status
                sub_D.status = FINISHED
                sub_D.setAutoDraw(False)
        
        # *postmask_D* updates
        
        # if postmask_D is starting this frame...
        if postmask_D.status == NOT_STARTED and sub_D.status==FINISHED:
            # keep track of start time/frame for later
            postmask_D.frameNStart = frameN  # exact frame index
            postmask_D.tStart = t  # local t and not account for scr refresh
            postmask_D.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(postmask_D, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'postmask_D.started')
            # update status
            postmask_D.status = STARTED
            postmask_D.setAutoDraw(True)
        
        # if postmask_D is active this frame...
        if postmask_D.status == STARTED:
            # update params
            pass
        
        # if postmask_D is stopping this frame...
        if postmask_D.status == STARTED:
            if frameN >= (postmask_D.frameNStart + final_mask_level/frames_calc):
                # keep track of stop time/frame for later
                postmask_D.tStop = t  # not accounting for scr refresh
                postmask_D.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'postmask_D.stopped')
                # update status
                postmask_D.status = FINISHED
                postmask_D.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in subliminal_phase_powerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "subliminal_phase_power" ---
    for thisComponent in subliminal_phase_powerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "subliminal_phase_power" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "visibility_test" ---
    continueRoutine = True
    # update component parameters for each repeat
    question_component.setText(question)
    response_awareness_test.keys = []
    response_awareness_test.rt = []
    _response_awareness_test_allKeys = []
    left_word.setText('T')
    right_word.setText('N')
    red_mask.setText(question_final)
    # keep track of which components have finished
    visibility_testComponents = [question_component, response_awareness_test, Q_button_word, E_button_nonword, left_word, right_word, red_mask]
    for thisComponent in visibility_testComponents:
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
    
    # --- Run Routine "visibility_test" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *question_component* updates
        
        # if question_component is starting this frame...
        if question_component.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            question_component.frameNStart = frameN  # exact frame index
            question_component.tStart = t  # local t and not account for scr refresh
            question_component.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_component, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'question_component.started')
            # update status
            question_component.status = STARTED
            question_component.setAutoDraw(True)
        
        # if question_component is active this frame...
        if question_component.status == STARTED:
            # update params
            pass
        
        # *response_awareness_test* updates
        waitOnFlip = False
        
        # if response_awareness_test is starting this frame...
        if response_awareness_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            response_awareness_test.frameNStart = frameN  # exact frame index
            response_awareness_test.tStart = t  # local t and not account for scr refresh
            response_awareness_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_awareness_test, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'response_awareness_test.started')
            # update status
            response_awareness_test.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response_awareness_test.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response_awareness_test.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response_awareness_test.status == STARTED and not waitOnFlip:
            theseKeys = response_awareness_test.getKeys(keyList=['t', 'n'], waitRelease=False)
            _response_awareness_test_allKeys.extend(theseKeys)
            if len(_response_awareness_test_allKeys):
                response_awareness_test.keys = _response_awareness_test_allKeys[-1].name  # just the last key pressed
                response_awareness_test.rt = _response_awareness_test_allKeys[-1].rt
                response_awareness_test.duration = _response_awareness_test_allKeys[-1].duration
                # was this correct?
                if (response_awareness_test.keys == str(corrAns)) or (response_awareness_test.keys == corrAns):
                    response_awareness_test.corr = 1
                else:
                    response_awareness_test.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *Q_button_word* updates
        
        # if Q_button_word is starting this frame...
        if Q_button_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Q_button_word.frameNStart = frameN  # exact frame index
            Q_button_word.tStart = t  # local t and not account for scr refresh
            Q_button_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Q_button_word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Q_button_word.started')
            # update status
            Q_button_word.status = STARTED
            Q_button_word.setAutoDraw(True)
        
        # if Q_button_word is active this frame...
        if Q_button_word.status == STARTED:
            # update params
            pass
        
        # *E_button_nonword* updates
        
        # if E_button_nonword is starting this frame...
        if E_button_nonword.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            E_button_nonword.frameNStart = frameN  # exact frame index
            E_button_nonword.tStart = t  # local t and not account for scr refresh
            E_button_nonword.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(E_button_nonword, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'E_button_nonword.started')
            # update status
            E_button_nonword.status = STARTED
            E_button_nonword.setAutoDraw(True)
        
        # if E_button_nonword is active this frame...
        if E_button_nonword.status == STARTED:
            # update params
            pass
        
        # *left_word* updates
        
        # if left_word is starting this frame...
        if left_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            left_word.frameNStart = frameN  # exact frame index
            left_word.tStart = t  # local t and not account for scr refresh
            left_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(left_word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'left_word.started')
            # update status
            left_word.status = STARTED
            left_word.setAutoDraw(True)
        
        # if left_word is active this frame...
        if left_word.status == STARTED:
            # update params
            pass
        
        # *right_word* updates
        
        # if right_word is starting this frame...
        if right_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            right_word.frameNStart = frameN  # exact frame index
            right_word.tStart = t  # local t and not account for scr refresh
            right_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(right_word, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_word.started')
            # update status
            right_word.status = STARTED
            right_word.setAutoDraw(True)
        
        # if right_word is active this frame...
        if right_word.status == STARTED:
            # update params
            pass
        
        # *red_mask* updates
        
        # if red_mask is starting this frame...
        if red_mask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            red_mask.frameNStart = frameN  # exact frame index
            red_mask.tStart = t  # local t and not account for scr refresh
            red_mask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(red_mask, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'red_mask.started')
            # update status
            red_mask.status = STARTED
            red_mask.setAutoDraw(True)
        
        # if red_mask is active this frame...
        if red_mask.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in visibility_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "visibility_test" ---
    for thisComponent in visibility_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response_awareness_test.keys in ['', [], None]:  # No response was made
        response_awareness_test.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           response_awareness_test.corr = 1;  # correct non-response
        else:
           response_awareness_test.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('response_awareness_test.keys',response_awareness_test.keys)
    trials_4.addData('response_awareness_test.corr', response_awareness_test.corr)
    if response_awareness_test.keys != None:  # we had a response
        trials_4.addData('response_awareness_test.rt', response_awareness_test.rt)
        trials_4.addData('response_awareness_test.duration', response_awareness_test.duration)
    # the Routine "visibility_test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ISI_wait" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from trials_counter_after
    trial_count = trial_count + 1
    
    if response_awareness_test.corr:
         correct_count = correct_count + 1
    # keep track of which components have finished
    ISI_waitComponents = [blank_start]
    for thisComponent in ISI_waitComponents:
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
    
    # --- Run Routine "ISI_wait" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank_start* updates
        
        # if blank_start is starting this frame...
        if blank_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank_start.frameNStart = frameN  # exact frame index
            blank_start.tStart = t  # local t and not account for scr refresh
            blank_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank_start, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank_start.started')
            # update status
            blank_start.status = STARTED
            blank_start.setAutoDraw(True)
        
        # if blank_start is active this frame...
        if blank_start.status == STARTED:
            # update params
            pass
        
        # if blank_start is stopping this frame...
        if blank_start.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank_start.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                blank_start.tStop = t  # not accounting for scr refresh
                blank_start.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_start.stopped')
                # update status
                blank_start.status = FINISHED
                blank_start.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISI_waitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI_wait" ---
    for thisComponent in ISI_waitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_4'


# --- Prepare to start Routine "koniec" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
koniecComponents = [text_24, key_resp_24]
for thisComponent in koniecComponents:
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

# --- Run Routine "koniec" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_24* updates
    
    # if text_24 is starting this frame...
    if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_24.frameNStart = frameN  # exact frame index
        text_24.tStart = t  # local t and not account for scr refresh
        text_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_24.started')
        # update status
        text_24.status = STARTED
        text_24.setAutoDraw(True)
    
    # if text_24 is active this frame...
    if text_24.status == STARTED:
        # update params
        pass
    
    # *key_resp_24* updates
    waitOnFlip = False
    
    # if key_resp_24 is starting this frame...
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_24.started')
        # update status
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            key_resp_24.duration = _key_resp_24_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in koniecComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "koniec" ---
for thisComponent in koniecComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
    thisExp.addData('key_resp_24.duration', key_resp_24.duration)
thisExp.nextEntry()
# the Routine "koniec" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "ISI_end" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_20.keys = []
key_resp_20.rt = []
_key_resp_20_allKeys = []
# setup some python lists for storing info about the mouse_3
gotValidClick = False  # until a click is received
# keep track of which components have finished
ISI_endComponents = [text_13, key_resp_20, mouse_3]
for thisComponent in ISI_endComponents:
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

# --- Run Routine "ISI_end" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    
    # if text_13 is starting this frame...
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_13.started')
        # update status
        text_13.status = STARTED
        text_13.setAutoDraw(True)
    
    # if text_13 is active this frame...
    if text_13.status == STARTED:
        # update params
        pass
    
    # *key_resp_20* updates
    waitOnFlip = False
    
    # if key_resp_20 is starting this frame...
    if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.tStart = t  # local t and not account for scr refresh
        key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_20.started')
        # update status
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_20.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_20.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _key_resp_20_allKeys.extend(theseKeys)
        if len(_key_resp_20_allKeys):
            key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
            key_resp_20.rt = _key_resp_20_allKeys[-1].rt
            key_resp_20.duration = _key_resp_20_allKeys[-1].duration
            # a response ends the routine
            continueRoutine = False
    # *mouse_3* updates
    
    # if mouse_3 is starting this frame...
    if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse_3.frameNStart = frameN  # exact frame index
        mouse_3.tStart = t  # local t and not account for scr refresh
        mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('mouse_3.started', t)
        # update status
        mouse_3.status = STARTED
        mouse_3.mouseClock.reset()
        prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
    if mouse_3.status == STARTED:  # only update if started and not finished!
        buttons = mouse_3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # end routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISI_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ISI_end" ---
for thisComponent in ISI_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_20.keys in ['', [], None]:  # No response was made
    key_resp_20.keys = None
thisExp.addData('key_resp_20.keys',key_resp_20.keys)
if key_resp_20.keys != None:  # we had a response
    thisExp.addData('key_resp_20.rt', key_resp_20.rt)
    thisExp.addData('key_resp_20.duration', key_resp_20.duration)
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
x, y = mouse_3.getPos()
buttons = mouse_3.getPressed()
thisExp.addData('mouse_3.x', x)
thisExp.addData('mouse_3.y', y)
thisExp.addData('mouse_3.leftButton', buttons[0])
thisExp.addData('mouse_3.midButton', buttons[1])
thisExp.addData('mouse_3.rightButton', buttons[2])
thisExp.nextEntry()
# the Routine "ISI_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
