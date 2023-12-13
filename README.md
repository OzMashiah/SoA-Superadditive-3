# Ultra Instinct Analysis

## Introduction
Ultra Instinct is a project from Salomon Lab in the University Of Haifa, Israel.
The project aims to investigate the effects of combinations of various levels of different modalities (temporal alteration, and spatial alteration) on the subjective Sense of Agency.
The Ultra Instinct Analysis repository takes the experiment and modelling outputs and perform statistical analysis and data plotting.
The analysis is done in the Python programming language and is in the Python Notebook format, which can be ran easily using the likes of Jupyter Notebook. 

## Prerequisites
The necessary libraries for this project are:
pandas, matplotlib, seaborn, numpy, scipy, math, statsmodels, os, re, glob.

## Repository Structure

### params.py
Parameter file of paths and alteration levels. This file is used by both preprocess.ipynb and analysis.ipynb. 

### preprocess.ipynb
This script takes the raw data from the "data_dir" parameter , preprocess it, and output the preprocessed data to "preprocessed_output_dir" parameter folder. Running this file is necessary before continuating to the analysis.ipynb script. This script is using the params.py parameter file.

### analysis.ipynb
This script takes the preprocessed data from preprocess.ipynb, performs statistical analysis and data plotting. This script is using the params.m parameter file.

### subnum_to_real_subnum.csv
CSV containing the used sub id and the actual sub id. (e.g, 70011, 1).

### tasknum_to_butterfly_location.csv
CSV containing the setup task number and the corresponding butterfly location.

## Instructions
1) Create the data folder and put the raw data with the same convention it was saved in the lab's google drive where each subject has a folder.
2) Copy and paste the modelling predictions from the Ultra Instinct Modelling repository (https://github.com/OzMashiah/ultra-instinct-modelling) to "models_predictions_dir" parameter folder.
2) Go over the params.py parameter file and make sure the values are as wanted.
3) Run preprocess.ipynb to preprocess the raw data.
4) Run analysis.ipynb.

> [!NOTE]
> Change the value of the 'n' (number of trials) variable in 4th cell that has the parameters for the information criteria calculations in analysis.ipynb to 240 when looking at official experiment data, and 234 when looking at pilot data. :+1: 