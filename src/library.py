# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:25:41 2019

@author: nh1037

modified by Anqi Lei, Mar 4th, 2025
"""

from psychopy import core, data, gui, visual, event, logging
#import winsound
from pyglet.window import key
from random import uniform, shuffle
import numpy as np
import random
import os
import codecs
import csv
import re
import stat
from collections import OrderedDict
from psychopy.hardware import keyboard 
# 01/2013 added for monitor TR in mri
from psychopy.iohub.client import launchHubServer


#from src.fileIO import *
#from src.datastructure.datastructure import *
#from src.datastructure.stimulus import tup2str


###################################################
# file locations
instr_path = './instructions/'  # path for instructions
instr_name = '_instr.txt' # filename (preceded by subtask name) for instructions

begin_name = 'begin_instr.txt' # beginning text, 
begin2_name = 'begin_instr2.txt' # beginning text for second run
begin_slider_name = 'slider_instr.txt' # beginning text, 
begin2_slider_name = 'slider_instr2.txt' # beginning text, 
begin3_slider_name = 'slider_instr3.txt' # beginning text, 
start_name = 'start_instr.txt' # beginning text for real run
concept_instr_name = 'concept_instr.txt' # beginning text for real run

ready_name = 'wait_trigger.txt' # instruction: wait trigger screen
exp_end_name = 'taskend_instr.txt' # instruction: wait trigger screen
ESQ_name = 'ESQ_instr.txt'
Verbal_ESQ_name = 'Verbal_ESQ_instr.txt'
end_name = 'end_instr.txt'
trial_setup_path = './parameters/' # path for trial setup
fixed_ESQ_name = './parameters/fixedQuestions.csv' # experience sampling questions - fixed
random_ESQ_name = './parameters/fixedQuestions.csv' # experience sampling questions - random (#anqi modified for testing, feb28)

random_Conceptual_name = './parameters/concept_similarity_Q.csv' # experience sampling questions - random (#anqi modified for testing, feb28)

###################################################
# Base settings that apply to all environments.
# These settings can be overwritten by any of the
# environment settings.
BASE = {
    'test': False,
    'mouse_visible': False,
#    'logging_level': logging.INFO
    'logging_level': logging.ERROR,
}

# Laboratory setting
LAB = {
    'env': 'lab',  # Enviroment name
    #'window_size': 'full_screen',
    #'window_size': (1280, 720),
    #'window_size': (1920, 1080),
    'window_size': (1440, 900), # for my macbook
    'input_method': 'keyboard',
    }

MRI = {
    'env': 'mri',
     #'window_size': (1920, 1080),
    'window_size': (1440, 900),
    #'input_method': 'keyboard',
    'input_method': 'serial',
        }


# experiment specific vesion related setting
VER_TEST = {
        'txt_color': 'black',
        'rec_keys': ['left', 'right' ,'return'],
        'rec_keyans':['left', 'right' ,'return'],
        }
        
# experiment specific vesion related setting
VER_REAL = {
        'txt_color': 'black',
        'rec_keys': ['left', 'right' ,'return'],
        'rec_keyans': ['left', 'right' ,'return'],
        }

VER_TEST_MRI = {
            'rec_keys': ['b', 'y', 'g'],  
            'rec_keyans': ['left', 'right', 'return'],
            'loc_keys': ['1', '2', '3'],
            }
            
VER_REAL_MRI = {
            'rec_keys': ['b', 'y', 'g'],
            'rec_keyans': ['left', 'right', 'return'],
            'loc_keys': ['1', '2', '3'],
            }

sans = ['Arial','Gill Sans MT', 'Helvetica','Verdana'] #use the first font found on this list

# 01/2013 added for monitor TR in mri
#def track_mri_trigger(experiment_code, session_code, version, ESQuestion, run_no):
#
#io=launchHubServer()
#
#return track_status 

def get_trial_generator(subtask, version, ESQuestion, run_no):
#def get_trial_generator(subtask, version):
    '''
    get the list of parameters (stimuli) from the .csv 
    '''
    
    trial_path = trial_setup_path + subtask + '_' + version + str(run_no) + '.csv'   
    trialpool, trialhead = load_trials(trial_path)
    
    #if ESQuestion == 'ES': # anqi uncommented this section, feb28
     #   question2, _ = load_conditions_dict(random_ESQ_name)
      #  exp_sample_generator = stimulus_ExpSample(question2)
        #question1, _ = load_conditions_dict(fixed_ESQ_name)
     #   questions = exp_sample_generator.generate() # anqi: maybe allocate "thought" and "emotion to question 1 and 2 separately
    
    return trialpool, trialhead


def get_settings(env, ver):
    '''Return a dictionary of settings based on
    the specified environment, given by the parameter
    env. Can also specify whether or not to use testing settings.

    Include keypress counter balancing
    '''
    # Start with the base settings
    settings = BASE


    if env == 'lab':
        settings.update(LAB)

        # display and key press counter balancing
        if ver == 'TEST':
            settings.update(VER_TEST)
        elif ver == 'REAL':
            settings.update(VER_REAL)
        else:
            raise ValueError('Version "{0}" not supported.'.format(ver))

    elif env == 'mri':
        settings.update(MRI)
        # display and key press counter balancing
        if ver == 'TEST':
            settings.update(VER_TEST_MRI)
        elif ver == 'REAL':
            settings.update(VER_REAL_MRI)
        else:
            raise ValueError('Version "{0}" not supported.'.format(ver))

    else:
        raise ValueError('Environment "{0}" not supported.'.format(env))

    return settings


##################################################
# experiment
class Paradigm(object):
    '''
    Study paradigm
    '''
    def __init__(self, escape_key='esc', window_size=(1280, 720), color=0, *args, **kwargs): # specifiy fullscreen or not
        self.escape_key = escape_key
        self.trials = []
        self.stims = {}

        if window_size =='full_screen':
            self.window = visual.Window(fullscr=True, color=color, units='pix', *args, **kwargs)
        else:
            self.window = visual.Window(size=window_size, color=color, allowGUI=True, units='pix', *args, **kwargs)


class Display_Text(object):
    '''
    show text in the screen at x,y
    '''
    def __init__(self, window, text, size, color, font, pos_x, pos_y, show_now):
        '''Initialize a text stimulus.
        Args:
        window - The window object
        text - text to display
        size, color, font - attributes of the text
        pos_x, pos_y - x,y position, 0,0 is the centre
        show_now - 0-don't flip, 1-flip
        '''
        self.window = window
        self.text = text
        self.display = visual.TextStim(
                window, text=text, font=font,
                #name='instruction',
                pos=[pos_x, pos_y], height=size, wrapWidth=1100,
                color=color
                ) #object to display instructions
        self.show_now = show_now

    def show(self, clock):
        self.display.draw()
        if self.show_now == 1:
            self.window.flip()
        start_trial = clock.getTime()

        return start_trial
        
        
class Display_Image(object):
    '''
    show image in the screen at x,y
    '''
    def __init__(self, window, image, size_x, size_y, pos_x, pos_y, show_now):
        '''Initialize a text stimulus.
        Args:
        window - The window object
        image - image to display
        size - attributes of the image
        pos_x, pos_y - x,y position, 0,0 is the centre
        show_now - 0-don't flip, 1-flip
        '''
        self.window = window
        #self.window = image
        self.display = visual.ImageStim(self.window, image=image,
                size=[size_x, size_y], pos=[pos_x, pos_y]
                ) #object to display instructions
        self.show_now = show_now
        
    def show(self, clock):
        self.display.draw()
        if self.show_now == 1:
            self.window.flip()
        start_trial = clock.getTime()

        return start_trial
        
# same as Display_Image but using the actual size
class Display_Image_act(object):
    '''
    show image in the screen at x,y
    '''
    def __init__(self, window, image, pos_x, pos_y):
        '''Initialize a text stimulus.
        Args:
        window - The window object
        image - image to display
        size - attributes of the image
        pos_x, pos_y - x,y position, 0,0 is the centre
        '''
        self.window = window
        #self.window = image
        self.display = visual.ImageStim(self.window, image=image,
#                size=[size_x, size_y], 
                pos=[pos_x, pos_y]
                ) #object to display instructions

    def show(self, clock):
        self.display.draw()
        self.window.flip()
        start_trial = clock.getTime()

        return start_trial

# march 4th - anqi adds, not sure if useful though:
# displays
class Display_Video(object):
    '''
    show image in the screen at x,y
    '''
    def __init__(self, window, filename, size_x, size_y, pos_x, pos_y, show_now):
        '''Initialize a stimulus.
        Args:
        window - The window object
        video - video to display
        size - attributes of the videos
        pos_x, pos_y - x,y position, 0,0 is the centre
        '''
        self.window = window
        self.display = visual.MovieStim(self.window, filename=filename,
                size=[size_x, size_y],
                pos=[pos_x, pos_y], loop = False, noAudio = False
                ) #object to display instructions
        self.show_now = show_now

    def show(self, clock):
        
       
       # if self.show_now == 1:
       #    self.window.flip()

        #while True and routineTimer.getTime() > 0:
        while self.display.isFinished != True:
            self.display.play()
            self.display.draw()
            self.window.flip()
        
        self.display.stop()
        #self.window.flip()
        start_trial = clock.getTime()
        
        return start_trial


def Get_Response(clock, duration, respkeylist, keyans, beepflag):
    
    respRT = np.nan
    KeyResp = None
    Resp = None
    KeyPressTime = np.nan

    event.clearEvents() # clear the keyboard buffer
    #myclock = core.Clock() # start a clock for this response trial
    resp_start  = clock.getTime()

    while KeyResp is None and (clock.getTime() <= resp_start + duration):
        
        # get key press and then disappear
        KeyResp, Resp, KeyPressTime = get_keyboard(
            clock, respkeylist, keyans)

    # get reaction time and key press
    if not np.isnan(KeyPressTime):
        respRT = KeyPressTime - resp_start
    else:
        KeyResp, Resp = 'None', 'None'
        #if beepflag == 0:
        #    winsound.Beep(1000, 100)  # make a beep if no response is made
        
    return resp_start, KeyResp, Resp, KeyPressTime, respRT


def get_keyboard(timer, respkeylist, keyans):
    '''
    Get key board response
    '''
    Resp = None
    KeyResp = None
    KeyPressTime = np.nan
    keylist = ['escape'] + respkeylist

    for key, time in event.getKeys(keyList=keylist, timeStamped=timer):
        if key in ['escape']:
            quitEXP(True)
        else:
            KeyResp, KeyPressTime = key, time
    # get what the key press means
    if KeyResp:
        Resp = keyans[respkeylist.index(KeyResp)]
    return KeyResp, Resp, KeyPressTime


def quitEXP(endExpNow):
    if endExpNow:
        print ('user cancel')
        core.quit()


class my_instructions(object):
    '''
    show instruction and wait for trigger
    '''
    def __init__(self, window, settings, instruction_txt, ready_txt, instruction_size, instruction_font, instruction_color, parseflag):
        self.window = window
        self.settings = settings
        self.env = settings['env']
        self.instruction_txt = load_instruction(instruction_txt)
        self.ready_txt = load_instruction(ready_txt)[0]
        self.display = visual.TextStim(
                window, text='default text', font=instruction_font,
                name='instruction',
                pos=[-50,0], height=instruction_size, wrapWidth=1100,
                color=instruction_color, anchorHoriz='center',
                ) #object to display instructions
        self.parseflag = parseflag

    def parse_inst(self):

        for i in range(0, len(self.settings['rec_keys'])):
            if i == 0:
                self.instruction_txt[1] = self.instruction_txt[1].replace(
                        '{key_0}', self.settings['rec_keys'][0])
                self.instruction_txt[1] = self.instruction_txt[1].replace(
                        '{ans_0}', self.settings['rec_keyans'][0])
            elif i == 1:
                self.instruction_txt[1] = self.instruction_txt[1].replace(
                        '{key_1}', self.settings['rec_keys'][1])
                self.instruction_txt[1] = self.instruction_txt[1].replace(
                        '{ans_1}', self.settings['rec_keyans'][1])
            elif i == 2:
                self.instruction_txt[1] = self.instruction_txt[1].replace(
                        '{key_2}', self.settings['rec_keys'][2])
                self.instruction_txt[1] = self.instruction_txt[1].replace(
                        '{ans_2}', self.settings['rec_keyans'][2])
            elif i == 3:
                self.instruction_txt[1] = self.instruction_txt[1].replace(
                        '{key_3}', self.settings['rec_keys'][3])
                self.instruction_txt[1] = self.instruction_txt[1].replace(
                        '{ans_3}', self.settings['rec_keyans'][3])

        return self.instruction_txt

    def show(self, auto_advance_time=None):

        # substitue keys in the instruction text before displaying the instruction        
        if self.parseflag == 1:
            self.parse_inst()
            
        #kb = keyboard.Keyboard()  # Create a keyboard object for key polling
    
        for i, cur in enumerate(self.instruction_txt):
            self.display.setText(cur)
            self.display.draw()
            self.window.flip()
            if i==0 and self.parseflag == 1:
                core.wait(uniform(1.3,1.75))
            elif self.env == 'mri':
                #event.waitKeys(keyList='t')#
                event.waitKeys(keyList=[ '1', '2', '3', '4', 't'])#
                #event.waitKeys(keyList=['y'])
                #event.waitKeys(keyList='g')
            #elif auto_advance_time is not None:
             #   core.wait(auto_advance_time)
            else:
                event.waitKeys(keyList=['return'])

    def waitTrigger(self, trigger_code):
        # wait for trigger in mri environment
        self.display.setText(self.ready_txt)
        self.display.draw()
        self.window.flip()

        if self.env== 'lab':
            core.wait(0)
        elif self.env == 'mri':
            event.waitKeys(keyList=[trigger_code]) 
        else: # not supported
            raise Exception('Unknown environment setting')

def load_instruction(PATH):
    '''
    load and then parse instrucition
    return a list
    '''

    with codecs.open(PATH, 'r', encoding='utf8') as f:
        input_data = f.read()

    text = parse_instructions(input_data)

    return text


def parse_instructions(input_data):
    '''
    parse instruction into pages
    page break is #
    '''

    text = re.findall(r'([^#]+)', input_data) # match any chars except for #

    return text



def subject_info(experiment_info):
    '''
    get subject information
    return a dictionary
    '''
    dlg_title = '{} subject details:'.format(experiment_info['Experiment'])
    infoDlg = gui.DlgFromDict(experiment_info, title=dlg_title)

    experiment_info['Date'] = data.getDateStr()

   
    file_root = ('_').join([experiment_info['Subject'], experiment_info['Run'],
                            experiment_info['Experiment'], experiment_info['Subtask'], 
                            experiment_info['Version'], experiment_info['Date']])

    experiment_info['DataFile'] = 'data' + os.path.sep + file_root + '.csv'
    experiment_info['LogFile'] = 'data' + os.path.sep + file_root + '.log'

    if experiment_info['Environment'] == 'mri':
        experiment_info['MRIFile'] = 'data' + os.path.sep + file_root + '_voltime.csv'

    if infoDlg.OK:
        return experiment_info
    else:
        core.quit()
        print ('User cancelled')

def create_dir(directory):
    '''

    create a directory if it doesn't exist.

    '''
    if not os.path.exists(directory):
        os.makedirs(directory)



def event_logger(logging_level, LogFile):
    '''
    log events
    '''
    directory = os.path.dirname(LogFile)
    create_dir(directory)

    logging.console.setLevel(logging.WARNING)
    logging.LogFile(LogFile, level=logging_level)


def Write_Response(fileName, list_headers, thisTrial):
    '''
    append the data of the current trial to the data file
    if the data file has not been created, this function will create one


    attributes

    fileName: str
        the file name generated when capturing participant info

    list_headers: list
        the headers in a list, will pass on to function create_headers

    thisTrial: list
        list storing
    '''

    full_path = os.path.abspath(fileName)
    directory = os.path.dirname(full_path)
    create_dir(directory)
    fieldnames = create_headers(list_headers)

    if not os.path.isfile(full_path):
        # headers and the first entry
        with codecs.open(full_path, 'ab+', encoding='utf8') as f:
            dw = csv.DictWriter(f, fieldnames=fieldnames)
            dw.writeheader()
            dw.writerow(thisTrial)
    else:
        with codecs.open(full_path, 'ab+', encoding='utf8') as f:
            dw = csv.DictWriter(f, fieldnames=fieldnames)
            dw.writerow(thisTrial)

class stimulus_ExpSample(object):
    '''
    experience sampling stimulus generator
    save features and generate stimuli

    features: list, dictionaries of questions

    '''
    def __init__(self, features):
        '''split questions into two sets'''
        self.q_focus = features[0:1]  # the focus question stays at the top
        self.q_others = features[1:18]
        self.q_emotion = features[18:23]
        self.q_arousal = features[23:]

    def generate(self):
        '''yield self.stimuli'''
        shuffle(self.q_others)
        shuffle(self.q_emotion)
        return self.q_focus + self.q_others + self.q_emotion + self.q_arousal


def load_trials(infile):
    '''
    load each row as a dictionary with the headers as the keys
    save the headers in its original order for data saving
    '''

    with codecs.open(infile, 'r', encoding='utf8') as f:
        reader = csv.DictReader(f)
        trials = []

        for row in reader:
            trials.append(row)

        # save field names as a list in order
        fieldnames = reader.fieldnames

    return trials, fieldnames


def load_conditions_dict(conditionfile):
    '''
    load each row as a dictionary with the headers as the keys
    save the headers in its original order for data saving
    '''

    with codecs.open(conditionfile, 'r', encoding='utf8') as f:
        reader = csv.DictReader(f)
        trials = []

        for row in reader:
            trials.append(row)

        # save field names as a list in order
        fieldnames = reader.fieldnames

    return trials, fieldnames


def create_headers(list_headers):
    '''
    create ordered headers for the output data csv file
    '''

    headers = []

    for header in list_headers:
        headers.append((header, None))

    return OrderedDict(headers)
        
        
def write_csv_rows(fileName, fieldnames, rows):
    '''
    Append multiple rows (each a dict) to a CSV file.
    If the file does not exist, create it with the header.
    added by anqi, March 17
    ''' 
    import codecs, csv, os, stat
    full_path = os.path.abspath(fileName)
    directory = os.path.dirname(full_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_exists = os.path.isfile(full_path)
    with codecs.open(full_path, 'ab+', encoding='utf8') as f:
        dw = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            dw.writeheader()
        for row in rows:
            dw.writerow(row)


def write_csv(fileName, list_headers, thisTrial):
    '''
    append the data of the current trial to the data file
    if the data file has not been created, this function will create one


    attributes

    fileName: str
        the file name generated when capturing participant info

    list_headers: list
        the headers in a list, will pass on to function create_headers

    thisTrial: dict
        a dictionary storing the current trial
    '''

    full_path = os.path.abspath(fileName)
    directory = os.path.dirname(full_path)
    create_dir(directory)
    fieldnames = create_headers(list_headers)

    if not os.path.isfile(full_path):
        # headers and the first entry
        with codecs.open(full_path, 'ab+', encoding='utf8') as f:
            dw = csv.DictWriter(f, fieldnames=fieldnames)
            dw.writeheader()
            dw.writerow(thisTrial)
    else:
        with codecs.open(full_path, 'ab+', encoding='utf8') as f:
            dw = csv.DictWriter(f, fieldnames=fieldnames)
            dw.writerow(thisTrial)

def read_only(path):
    '''
    change the mode to read only
    '''
    os.chmod(path, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    
    
def run_interactive_slider(win, experiment_info, question_text, initial_rating=5, slider_units='norm'):
    """
    Displays an interactive slider that updates in real time based on mouse or keyboard input.
    Uses normalized coordinates so that components appear appropriately sized.
    """
    # Slider parameters
    slider_width = 0.8      # in norm units
    slider_height = 0.1     # slider background height
    slider_ticks = list(range(1, 11))  # rating scale from 1 to 10
    slider_labels = [str(x) for x in slider_ticks]
    slider_granularity = 1  # step size
    slider_decimals = 0     # no decimals displayed
    marker_colour = 'blue'  # marker color

    # Positions for slider components (norm coordinates)
    slider_center = (0, -0.3)
    question_pos = (0, 0.3)
    text_pos = (0, -0.45)

    # Create visual components with explicit units:
    slider_bg = visual.Rect(win, width=slider_width, height=slider_height, pos=slider_center,
                            units=slider_units, fillColor='gray', lineColor='gray')
    slider_bar = visual.Rect(win, width=slider_width, height=slider_height/10, pos=slider_center,
                             units=slider_units, fillColor='black', lineColor='black')
    marker = visual.Circle(win, radius=0.02, pos=slider_center,
                           units=slider_units, fillColor=marker_colour, lineColor=marker_colour)
    question_stim = visual.TextStim(win, text=question_text, pos=question_pos,
                                    height=0.1, units=slider_units, color='white')
    rating_text = visual.TextStim(win, text=str(initial_rating), pos=text_pos,
                                  height=0.08, units=slider_units, color='white')

    # Create tick labels along the slider:
    tick_texts = []
    for i, label in enumerate(slider_labels):
        x_pos = -slider_width/2 + (i / (len(slider_labels) - 1)) * slider_width
        tick = visual.TextStim(win, text=label, pos=(x_pos, slider_center[1] - slider_height),
                               height=0.05, units=slider_units, color='white')
        tick_texts.append(tick)

    # Mapping function: rating -> x-position
    min_rating = slider_ticks[0]
    max_rating = slider_ticks[-1]
    def rating_to_pos(rating):
        proportion = (rating - min_rating) / (max_rating - min_rating)
        return -slider_width/2 + proportion * slider_width

    # Initialize rating and marker position:
    #rating = initial_rating
    rating = random.randint(3,7)
    marker.pos = (rating_to_pos(rating), slider_center[1])

    # Set up keyboard and mouse:
    kb = keyboard.Keyboard()
    mouse = event.Mouse(win=win)

    continueRoutine = True
    while continueRoutine:
        if experiment_info['Environment'] == 'mri':
           keys = kb.getKeys(['b', 'y', 'g'], waitRelease=False) # b: right blue, c: right yellow, g: right green
           for key in keys:
             if key.name == 'b':
                rating = max(min_rating, rating - slider_granularity)
             elif key.name == 'y':
                rating = min(max_rating, rating + slider_granularity)
             elif key.name == 'g':
                continueRoutine = False
        else: # LAB environment
            # Check keyboard input:
            keys = kb.getKeys(['left', 'right', 'return'], waitRelease=False)
            for key in keys:
                if key.name == 'left':
                    rating = max(min_rating, rating - slider_granularity)
                elif key.name == 'right':
                    rating = min(max_rating, rating + slider_granularity)
                elif key.name == 'return':
                    continueRoutine = False

        # Check for escape key:
        if 'escape' in event.getKeys(keyList=['escape']):
            core.quit()

        # Check mouse input: update rating if left-click is pressed within slider_bg
        if slider_bg.contains(mouse):
            if mouse.getPressed()[0]:
                m_pos = mouse.getPos()
                proportion = (m_pos[0] + slider_width/2) / slider_width
                new_rating = min_rating + proportion * (max_rating - min_rating)
                new_rating = round(new_rating / slider_granularity) * slider_granularity
                rating = int(max(min_rating, min(max_rating, new_rating)))

        # Update marker and text:
        marker.pos = (rating_to_pos(rating), slider_center[1])
        rating_text.text = str(rating)

        # Draw components:
        slider_bg.draw()
        slider_bar.draw()
        marker.draw()
        question_stim.draw()
        # Optionally, if you want to show the rating text, draw it here:
        # rating_text.draw()
        
        for tick in tick_texts:
            tick.draw()
        win.flip()
    
    return rating



def run_conceptual_slider(win, experiment_info, question_text, left_text, right_text, initial_rating=5, slider_units='norm'):
    """
    Displays an interactive slider that updates in real time based on mouse or keyboard input.
    Uses normalized coordinates so that components appear appropriately sized.
    """
    # Slider parameters
    slider_width = 0.8      # in norm units
    slider_height = 0.1     # slider background height
    slider_ticks = list(range(1, 11))  # rating scale from 1 to 10
    slider_labels = [str(x) for x in slider_ticks]
    slider_granularity = 1  # step size
    slider_decimals = 0     # no decimals displayed
    marker_colour = 'blue'  # marker color

    # Positions for slider components (norm coordinates)
    slider_center = (0, 0)
    question_pos = (0, 0.6)
    text_pos = (0, 0.05)
    left_text_pos = (-0.3, 0.3)
    right_text_pos = (0.3, 0.3)

    # Create visual components with explicit units:
    slider_bg = visual.Rect(win, width=slider_width, height=slider_height, pos=slider_center,
                            units=slider_units, fillColor='gray', lineColor='gray')
    slider_bar = visual.Rect(win, width=slider_width, height=0.01, pos=slider_center,
                             units=slider_units, fillColor='black', lineColor='black')
    marker = visual.Circle(win, radius=0.02, pos=slider_center,
                           units=slider_units, fillColor=marker_colour, lineColor=marker_colour)
    question_stim = visual.TextStim(win, text=question_text, pos=question_pos,
                                    height=0.1, units=slider_units, color='white')
    rating_text = visual.TextStim(win, text=str(initial_rating), pos=text_pos,
                                  height=0.08, units=slider_units, color='white')
    
    left_label = visual.TextStim(win, text=left_text, pos=left_text_pos,
                                    height=0.08, units=slider_units, color='white')
    
    right_label = visual.TextStim(win, text=right_text, pos=right_text_pos,
                                    height=0.08, units=slider_units, color='white')
    
    dissimilar_label = visual.TextStim(win, text='Dissimilar', pos=(-0.4,0.1),
                                    height=0.05, units=slider_units, color='black')
    
    similar_label = visual.TextStim(win, text='Similar', pos=(0.4,0.1),
                                   height=0.05, units=slider_units, color='black')
    
    
    # Create tick labels along the slider:
    tick_texts = []
    for i, label in enumerate(slider_labels):
        x_pos = -slider_width/2 + (i / (len(slider_labels) - 1)) * slider_width
        tick = visual.TextStim(win, text=label, pos=(x_pos, slider_center[1] - slider_height),
                               height=0.05, units=slider_units, color='white')
        tick_texts.append(tick)

    # Mapping function: rating -> x-position
    min_rating = slider_ticks[0]
    max_rating = slider_ticks[-1]
    def rating_to_pos(rating):
        proportion = (rating - min_rating) / (max_rating - min_rating)
        return -slider_width/2 + proportion * slider_width

    # Initialize rating and marker position:
    #rating = initial_rating
    rating = random.randint(3,7)
    marker.pos = (rating_to_pos(rating), slider_center[1])

    # Set up keyboard and mouse:
    kb = keyboard.Keyboard()
    mouse = event.Mouse(win=win)

    continueRoutine = True
    while continueRoutine:
        if experiment_info['Environment'] == 'mri':
           keys = kb.getKeys(['b', 'y', 'g'], waitRelease=False) # b: right blue, c: right yellow, g: right green
           for key in keys:
             if key.name == 'b':
                rating = max(min_rating, rating - slider_granularity)
             elif key.name == 'y':
                rating = min(max_rating, rating + slider_granularity)
             elif key.name == 'g':
                continueRoutine = False
        else: # LAB environment
            # Check keyboard input:
            keys = kb.getKeys(['left', 'right', 'return'], waitRelease=False)
            for key in keys:
                if key.name == 'left':
                    rating = max(min_rating, rating - slider_granularity)
                elif key.name == 'right':
                    rating = min(max_rating, rating + slider_granularity)
                elif key.name == 'return':
                    continueRoutine = False

        # Check for escape key:
        if 'escape' in event.getKeys(keyList=['escape']):
            core.quit()

        # Check mouse input: update rating if left-click is pressed within slider_bg
        if slider_bg.contains(mouse):
            if mouse.getPressed()[0]:
                m_pos = mouse.getPos()
                proportion = (m_pos[0] + slider_width/2) / slider_width
                new_rating = min_rating + proportion * (max_rating - min_rating)
                new_rating = round(new_rating / slider_granularity) * slider_granularity
                rating = int(max(min_rating, min(max_rating, new_rating)))

        # Update marker and text:
        marker.pos = (rating_to_pos(rating), slider_center[1])
        rating_text.text = str(rating)

        for tick in tick_texts:
            tick.draw()
            
        # Draw components:
        slider_bg.draw()
        slider_bar.draw()
        marker.draw()
        question_stim.draw()
        left_label.draw()
        right_label.draw()
        dissimilar_label.draw()
        similar_label.draw()

        # Optionally, if you want to show the rating text, draw it here:
        # rating_text.draw()
        
        win.flip()
    
    return rating
