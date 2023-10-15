#!/usr/bin/env python
# coding: utf-8

import pandas as pd

# Parameters - make sure to adjust before a new running environment/experiment!
data_dir = "Data/" # Specify where is the subjects data directory 
data_dir_pattern = r'Sub(\d+)' # Specify the pattern of the naming for the results directories, used as regular expression.
trials_file_pattern = r'Trials_sub*' # Specify the pattern of the naming for the trials files, used as regular expression.
preprocessed_output_dir = 'Preprocessed/' # The output folder where you want the preprocessed csvs to be.
models_predictions_dir = 'Models_pred/' # The folder with the models predictions mat files.
spatial_alteration_levels = [0.1583, 0.2125, 0.2679] # Specify the levels of spatial alteration, only positive of each level.
temporal_alteration_levels = [0.05, 0.072, 0.094] # Specify the levels of temporal alteration.
subnum_translator_file = 'subnum_to_real_subnum.csv' # CSV containing the used sub id and the actual sub id. (e.g, 70011, 1)
butterfly_location_translator_file = 'tasknum_to_butterfly_location.csv' # CSV containing setup task num and the butterfly loc.

part1_results_path = "/Part1/"  + "/Sub-*_Plan*" + "/Answers*.csv"
part2_results_path = "/Part2/"  + "/Sub-*_Plan*" + "/Answers*.csv"
part3_results_path = "/Part3/"  + "/Sub-*_Plan*" + "/Answers*.csv"
part1_trials_path = "/Part1/"  + "/Sub-*_Plan*" + "/UsedPlan/" + trials_file_pattern
part2_trials_path = "/Part2/"  + "/Sub-*_Plan*" + "/UsedPlan/" + trials_file_pattern
part3_trials_path = "/Part3/"  + "/Sub-*_Plan*" + "/UsedPlan/" + trials_file_pattern

# Set up a dictionary to translate used subject number (70012) to real subject number (1) using subnum_translator_file
subnum_translation = pd.read_csv(subnum_translator_file)
subnum_translator = dict()
for i in range(0,len(subnum_translation['Real Subject Number'])):
    key = subnum_translation['Used Subject Number'][i]
    value = subnum_translation['Real Subject Number'][i]
    subnum_translator[key] = value
    
# Set up a dictionary to translate setup task number to butterfly location using butterfly_location_translator_file.
tasknum_translation = pd.read_csv(butterfly_location_translator_file)
tasknum_translator = dict()
for i in range(0,len(tasknum_translation['Setup Task Number'])):
    key = tasknum_translation['Setup Task Number'][i]
    value = tasknum_translation['Butterfly Location'][i]
    tasknum_translator[key] = value

