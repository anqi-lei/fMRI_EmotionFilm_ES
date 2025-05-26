# -*- coding: utf-8 -*-
"""
Created on Mon March 3 - pilot run (modified to use an interactive slider)
"""
import os
import sys
import random
from psychopy import core, event, logging, visual, data, sound
from psychopy.sound import microphone
from src.library import *
import time

# bind ESC to quitting immediately
event.globalKeys.add(key='escape', func=core.quit)

# get input for dictionary defining the environment & trials to run
INFO = {
    'Experiment': 'Emotion-Film Watching',  # compulsory: name of program, used for trial definition in ./parameter/~.csv
    'Subject': '001',  # compulsory
    'Version': ['REAL','TEST'],  # no counterbalancing the 2 film orders
    'Run': ['1','2'], # 2 sets of parameters for 2 runs / participant
    'Subtask': ['SliderVerbal'],  # start the task with block for choice from two colors or letter
    'Environment': ['lab'],  # mri version can be tested on a normal stimuli delivery pc
    'ESQuestion': ['ES', 'no ES'], # with or without experience sampling
    }

# set dictionary for instructions in running each trial
instruction_parameter = dict([
        ('inst_size', 24), # size/height of the instruction
        ('inst_color', 'black'), # color of the instruction
        ('inst_font', 'sans'), # color of the instruction
        ])

# set dictionary for parameters in running each trial, anqi: modify
trial_parameter = dict([
        ('StimTxt_size', 44), # size/height of the stimulus text
        ('StimTxt_color', 'black'), # color of the stimulus text
        ('StimTxt_font', 'sans'), # font for the stimulus text
        ('Stim_Video_Type', '.mp4'), # include videos
        ('pos_x_gap', 250), # gap to adjust horizontal position
        ('pos_x_gap_plus', 0), # minor horizontal adjustment
        ('pos_y_gap', 180), # gap to adjust vertical position
        ('pos_y_gap_plus', 0), # minor vertical adjustment
        ('num_stim', 1), # number of stimuli within one trial
        ('resp_stay', 1), # screen stays until response? (0=yes, 1=no)
        ('beep_flag', 0), # beep flag if no response (0=yes, 1=no)
        ])
        
# set the response set for each trial
trial_response = dict([
        ('mri_tr_time', 0),  # mri - time sync with TR time before trial
        ('trialstart_time', 0),  # trial start time
        ('trialend_time', 0),  # trial end time
        ('resp_key', None), # response key
        ('response', 999), # nth response in the response key list, currently set to [yes, none]
        ])

# initialize the output for writing to csv
trial_output = {}

# define whether these stimuli will be displayed together, 0=no display-yet, 1=show
Stim_show = dict([
        (0, 0), # stim1
        ])

def run_continuous_rating(window, movie, timer, slider_params):
    """
    Play a MovieStim instance and collect continuous slider ratings simultaneously.
    Args:
        window: PsychoPy Window
        movie: visual.MovieStim (e.g. cur_stim.display)
        timer: a core.Clock instance
        slider_params: dict with keys 'ticks','labels','granularity','pos','size','color'
    Returns:
        samples: list of {'time': t, 'rating': r}
    """
    # Create the slider in normalized units
    slider = visual.Slider(
        win=window,
        ticks=slider_params.get('ticks', None),
        labels=slider_params.get('labels', []),
        granularity=slider_params.get('granularity', 0.1),
        style='rating', units='norm',
        pos=slider_params.get('pos', (0, -0.8)),
        size=slider_params.get('size', (1.5, 0.1)),
        color=slider_params.get('color', 'LightGray')
    )
    
    # **NEW**: initialize the marker in the center
    ticks = slider.ticks
    mid   = (ticks[0] + ticks[-1]) / 2.0
    slider.markerPos = mid

    samples = []
    start_time = timer.getTime()

    # Start video playback
    movie.noAudio = True
    
    while not movie.isFinished:
        movie.noAudio = False
        # Draw video frame
        movie.draw()
        # Draw slider overlay
        slider.draw()
        # Flip both
        window.flip()
        # Record timestamp and current rating
        t = timer.getTime() - start_time
        rating = slider.getRating() or slider.markerPos
        samples.append({'time': t, 'rating': rating})
        # Allow quitting
        if 'escape' in event.getKeys():
            core.quit()
    # Stop video
    movie.stop()
    return samples

def run_experiment():
    
    ##########################################
    # collect participant info
    ##########################################
    experiment_info = subject_info(INFO)

    ##########################################
    # Setup
    ##########################################
    settings = get_settings(
                    env=experiment_info['Environment'],
                    ver=experiment_info['Version'])
                    
    # get trial information from parameter file
    trials, headers = get_trial_generator(experiment_info['Subtask'], experiment_info['Version'], experiment_info['ESQuestion'], experiment_info['Run'])
    temp = list(trials[1].items())
    mycount = 0
    for i in range(len(headers)):
        if temp[i][1] != 'NA':
            trial_output[headers[i]] = temp[mycount][1]
        mycount += 1
    trial_output_headers = list(trial_output.keys()) + list(trial_response.keys())
    
    # set log file
    event_logger(settings['logging_level'], experiment_info['LogFile'])
    
    # create experiment window etc.
    Experiment = Paradigm(escape_key='esc', color=0,
                          window_size=settings['window_size'])
 
    # hide mouse cursor
    event.Mouse(visible=True)

    ##########################################
    # Running the experiment
    ##########################################
    for trialcount in range(len(trials)):
        if (trials[trialcount]['Stim_Cond'] == 'INSTR'): # anqi modified, Apr.15
            ##########################################
            # Set & display instructions
            ##########################################
            myparse = 0
            if (trials[trialcount]['Trial_Cond'] == 'begin_exp'):
                instr_txt = instr_path +  begin_slider_name
                    
            elif (trials[trialcount]['Trial_Cond'] == 'begin2'):
                instr_txt = instr_path + begin2_slider_name
            
            elif (trials[trialcount]['Trial_Cond'] == 'begin3'):
                instr_txt = instr_path + begin3_slider_name
            
            ready_txt = instr_path + ready_name
            
            myparse = 1
            instructions_run = my_instructions(
                window=Experiment.window, settings=settings,
                instruction_txt=instr_txt, ready_txt=ready_txt, 
                instruction_size=instruction_parameter['inst_size'], instruction_font=instruction_parameter['inst_font'],
                instruction_color=instruction_parameter['inst_color'], parseflag=myparse)
            
            instructions_run.show()
            timer = core.Clock()

                
        else:
            # update trial_output with trial-specific info
            for key in trial_output_headers:
                if key not in list(trial_response.keys()):
                    trial_output[key] = trials[trialcount][key]
                    
            trial_response['trialstart_time'] = timer.getTime()
            
            trial_stim = [trials[trialcount]['Stim1']]
            trial_size_x = [trials[trialcount]['Size_x']]
            trial_size_y = [trials[trialcount]['Size_y']]
            
            for stimcount in range(trial_parameter['num_stim']):
                mytext = trial_stim[stimcount]
                mypos_x = 0
                mypos_y = 0
                mytext_color = trial_parameter['StimTxt_color']
                
                        
                if trial_parameter['Stim_Video_Type'] in trial_stim[stimcount]:
                    cur_stim = Display_Video2(window=Experiment.window, filename=trial_stim[stimcount], 
                                            size_x=trial_size_x[stimcount], size_y=trial_size_y[stimcount],
                                            pos_x=mypos_x, pos_y=mypos_y, show_now=0, noAudio = False)
                    duration = cur_stim.display.duration
                    rating_samples = run_continuous_rating(Experiment.window, cur_stim.display, timer, 
                        {
                            'ticks': list(range(1, 11)),
                            'labels': [str(x) for x in range(1, 11)],
                            'granularity': 0.1,
                            'pos': (0, -0.4),
                            'size': (1.7, 0.2),
                            'color': 'white'
                        }
                    )
                    write_csv_rows(
                        experiment_info['DataFile'].replace('.csv','_valence.csv'),
                        ['trial','time','rating'],
                        [{'trial': trials[trialcount]['Trial_No'], 'time': s['time'], 'rating': s['rating']} for s in rating_samples]
                    )

                
                elif experiment_info['ESQuestion'] == 'ES' and (trials[trialcount]['Stim_Cond'] == 'VERBAL'):
                    # -------------
                    # Modified ESQ section using interactive slider:
                    ESQ_txt = instr_path + Verbal_ESQ_name
                    ESQ_msg = my_instructions(
                        window=Experiment.window, settings=settings,
                        instruction_txt=ESQ_txt, ready_txt=ready_txt, 
                        instruction_size=instruction_parameter['inst_size'], instruction_font=instruction_parameter['inst_font'],
                        instruction_color=instruction_parameter['inst_color'], parseflag=0)

                  #  Generate a filename for the audio file
                    audio_filename = f"{experiment_info['Subject']}_ESQ_{trials[trialcount]['Trial_Cond']}.wav"
                    file_path = os.path.join('recordings', audio_filename)
                    
                    # Record voice for a fixed duration (e.g., 5 seconds)
                    mic= microphone.Microphone()
                    #print("Recording started...")
                    
                    mic_onset=mic.start()
                    #mic.poll()
                    response_rows = []
                    questionnaire_start = cur_stim.show(timer)
                    done = False
                    
                    kb = keyboard.Keyboard()
                    while not done:
                         # Show the ES instructions
                        ESQ_msg.show() 
                        keys = kb.getKeys(keyList=['return', 'escape'], waitRelease = False)
                        for key in keys:
                            if key.name == 'return':
                               done = True
                               print('stop')
                            elif key.name == 'escape':
                               core.quit()
                   
                    Experiment.window.flip()
                    mic.stop()
                    #print("Recording stopped...")
                    #Experiment.window.flip()
                    #mic.stop()
                    #print("Recording stopped...")

                    audioClip=mic.getRecording()
                    audioClip.save(audio_filename)
                    
                     # INSERT A PART WHERE PARTICIPANTS' SPEECH IS RECORDED, AND A BUTTON PRESS INDICATES THE END OF IT
                    
                    questionnaire_end = cur_stim.show(timer)
                    trial_duration = questionnaire_end - questionnaire_start
                    # Update each row with the end time and duration:
                    for row in response_rows:
                        row['Questionnaire_endTime'] = questionnaire_end
                        row['TrialDuration'] = trial_duration
                    
                    # Define the header order for the CSV file:
                    fieldnames = ['Participant_number', 'Questionnaire_startTime', 'Questionnaire_endTime', 
                                  'TrialDuration', 'question label', 'rating value', 'Trial_No', 'Stim_Cond', 'Trial_Cond']
                    filename = experiment_info['DataFile'].replace('.csv', 'endQs.csv')
                    write_csv_rows(filename, fieldnames, response_rows)
                    # -------------
                    # Skip further stimulus processing in this branch.
                    continue
                
                else:
                    cur_stim = Display_Text(window=Experiment.window, text=mytext, 
                                            size=trial_parameter['StimTxt_size'], color=mytext_color, 
                                            font=trial_parameter['StimTxt_font'], pos_x=mypos_x, pos_y=mypos_y, show_now=Stim_show[stimcount])
                     # Check for escape key:
                    if 'escape' in event.getKeys(keyList=['escape']):
                        core.quit()
                    
                if Stim_show[stimcount] == 1:
                    if stimcount == 0:
                        trial_response['stim_1_start_time'] = timer.getTime()
                        
                mytime = cur_stim.show(timer)
               
               # added for mri - log trigger_code before end of trial
                if experiment_info['Environment'] == 'mri':
                    trial_response['mri_tr_time'] = trial_response['mri_tr_time'] + event.getKeys(keyList=[trigger_code], modifiers=False, timeStamped=timer)
                

                if stimcount == (trial_parameter['num_stim']-1):
                    for key in trial_response:
                        trial_output[key] = trial_response[key]
                    write_csv(experiment_info['DataFile'], trial_output_headers, trial_output)
                     
            
               

    ##########################################
    # Finishing the experiment
    ##########################################
    exp_end_txt = instr_path + exp_end_name
    exp_end_msg = my_instructions(
        window=Experiment.window, settings=settings,
        instruction_txt=exp_end_txt, ready_txt=ready_txt, 
        instruction_size=instruction_parameter['inst_size'], instruction_font=instruction_parameter['inst_font'],
        instruction_color=instruction_parameter['inst_color'], parseflag=0)
    
    exp_end_msg.show()
    logging.flush()
    read_only(experiment_info['DataFile'])
    read_only(experiment_info['LogFile'])
    
if __name__ == "__main__":
    _thisDir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(_thisDir)
    run_experiment() 