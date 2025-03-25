# -*- coding: utf-8 -*-
"""
Created on Mon March 3 - pilot run (modified to use an interactive slider)
"""
import os
import sys
import random
from psychopy import core, event, logging, visual, data
from src.library import *


# get input for dictionary defining the environment & trials to run
INFO = {
    'Experiment': 'Emotion-Film Watching',  # compulsory: name of program, used for trial definition in ./parameter/~.csv
    'Subject': '001',  # compulsory
    'Version': ['TEST', 'REAL'],  # no counterbalancing the 2 film orders
    'Run': ['1', '2'], # 2 sets of parameters for 2 runs / participant
    'Subtask': ['Exp'],  # start the task with block for choice from two colors or letter
    'Environment': ['lab', 'mri'],  # mri version can be tested on a normal stimuli delivery pc
    'ESQuestion': ['ES','No ES'], # with or without experience sampling
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


def run_experiment():
    
    ##########################################
    # collect participant info
    ##########################################
    experiment_info = subject_info(INFO)

    # MRI related settings
    if experiment_info['Environment'] in ['mri']:
        dummy_vol = 0
        tr = 2
        trigger_code = 't'

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
    event.Mouse(visible=False)

    ##########################################
    # Running the experiment
    ##########################################
    for trialcount in range(len(trials)):
        if (trials[trialcount]['Stim_Cond'] == 'INSTR'):
            ##########################################
            # Set & display instructions
            ##########################################
            myparse = 0
            if experiment_info['Run'] == '1' and (trials[trialcount]['Trial_Cond'] == 'begin'):
                instr_txt = instr_path +  begin_name
                    
            elif experiment_info['Run'] == '2':
                instr_txt = instr_path + begin2_name
            else:
                instr_txt = instr_path + start_name
            
            ready_txt = instr_path + ready_name
            
            myparse = 1
            instructions_run = my_instructions(
                window=Experiment.window, settings=settings,
                instruction_txt=instr_txt, ready_txt=ready_txt, 
                instruction_size=instruction_parameter['inst_size'], instruction_font=instruction_parameter['inst_font'],
                instruction_color=instruction_parameter['inst_color'], parseflag=myparse)
            
            instructions_run.show()
            timer = core.Clock()
            
             # 1/2023 - added for mri - log trigger_code before each trial (other than instructions)
            if experiment_info['Environment'] == 'mri':
                # the following is used if each trial is to be aligned with TR
                # Experiment.window.flip()  # clear the window
                #event.waitKeys(keyList=[trigger_code])
                #trial_response['mri_tr_time'] = timer.getTime()
                # the following is used if only need to log each TR
                mri_start_time = event.waitKeys(keyList=[trigger_code], modifiers=False, timeStamped=timer, clearEvents=True)
                mri_start_time = mri_start_time + event.waitKeys(keyList=[trigger_code], modifiers=False, timeStamped=timer, clearEvents=True)
                
        else:
            # update trial_output with trial-specific info
            for key in trial_output_headers:
                if key not in list(trial_response.keys()):
                    trial_output[key] = trials[trialcount][key]
                    
            if experiment_info['Environment'] == 'mri':
                if trialcount == 1:
                    trial_response['mri_tr_time'] = mri_start_time + event.getKeys(keyList=[trigger_code], modifiers=False, timeStamped=timer)
                else:
                    trial_response['mri_tr_time'] = event.getKeys(keyList=[trigger_code], modifiers=False, timeStamped=timer)
            else:
                trial_response['mri_tr_time'] = 0

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
                    cur_stim = Display_Video(window=Experiment.window, filename=trial_stim[stimcount], 
                                            size_x=trial_size_x[stimcount], size_y=trial_size_y[stimcount],
                                            pos_x=mypos_x, pos_y=mypos_y, show_now=Stim_show[stimcount])
                    if 'escape' in event.getKeys(keyList=['escape']):
                        break
                    trial_response['trialend_time'] = cur_stim.show(timer)
                
                elif experiment_info['ESQuestion'] == 'ES' and (trials[trialcount]['Stim_Cond'] == 'ESQ'):
                    # -------------
                    # Modified ESQ section using interactive slider:
                    ESQ_txt = instr_path + ESQ_name
                    ESQ_msg = my_instructions(
                        window=Experiment.window, settings=settings,
                        instruction_txt=ESQ_txt, ready_txt=ready_txt, 
                        instruction_size=instruction_parameter['inst_size'], instruction_font=instruction_parameter['inst_font'],
                        instruction_color=instruction_parameter['inst_color'], parseflag=0)
                    #ESQ_msg.show(auto_advance_time = 2)  # Show the ES instructions
                    
                    # Load ES questions from conditions files
                    random_question, _ = load_conditions_dict(random_ESQ_name)
                    exp_sample_instance = stimulus_ExpSample(random_question)
                    questions = exp_sample_instance.generate()

                    # Create a list to store one row per question response.
                    response_rows = []
                    # Log questionnaire start time:
                    questionnaire_start = cur_stim.show(timer)
                    
                    # Loop over each question and get a rating using the interactive slider:
                    for question in questions:
                        #if experiment_info['Environment'] in ['lab']:
                        rating = run_interactive_slider(Experiment.window,experiment_info, question['Questions'], initial_rating=5)
                       # elif experiment_info['Environment'] in ['mri']:
                        #    rating = run_MRI_slider(Experiment.window, question['Questions'], initial_rating=5)
                        # Create a row for this question:
                        row = {
                            'Participant_number': experiment_info['Subject'],
                            'Questionnaire_startTime': questionnaire_start,
                            'Questionnaire_endTime': None,  # will update later
                            'TrialDuration': None,          # will update later
                            'question label': question['Label'],
                            'rating value': rating,
                            'Stim_Cond': trials[trialcount].get('Stim_Cond', ''),
                            'Trial_Cond': trials[trialcount].get('Trial_Cond', ''),
                            'Trial_No': trials[trialcount].get('Trial_No', ''),
                        }
                        response_rows.append(row)
                    
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
               
               # dded for mri - log trigger_code before end of trial
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
    