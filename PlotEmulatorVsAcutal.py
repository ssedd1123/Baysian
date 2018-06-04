import cPickle as pickle
import pandas as pd
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import math

from Emulator.Emulator import *
from Preprocessor.PipeLine import *
from DataReader.DataLoader import DataLoader
from Utilities.Utilities import *

if len(sys.argv) != 2:
    print('Use this script by entering: python %s Training_file' % (sys.argv[0]))
    sys.exit()


"""
Use trained emulator
"""
with open(sys.argv[1], 'rb') as buff:
    data = pickle.load(buff)

emulator = data['emulator']
training_data = data['data']
scales = data['scales']
nuggets = data['nuggets']

num_run = training_data.sim_data.shape[0]
num_excluded = 5
emulator_results = []
actual_results = []

for validation_run in xrange(0, num_run, num_excluded):

    sim_data = training_data.sim_data
    sim_para = training_data.sim_para
    
    sim_data = np.delete(sim_data, slice(validation_run, validation_run + num_excluded), 0)
    sim_para = np.delete(sim_para, slice(validation_run, validation_run + num_excluded), 0)
    
    exp_result = training_data.sim_data[validation_run:validation_run + num_excluded]
    exp_para = training_data.sim_para[validation_run:validation_run + num_excluded]
    
    emulator.ResetData(sim_para, sim_data)
    #emulator.SetCovariance(squared_exponential)
    emulator.SetScales(scales)
    emulator.SetNuggets(nuggets)
    emulator.StartUp()

    for para in exp_para:
        mean, var = emulator.Emulate(para)
        emulator_results.append(mean.flatten().tolist())
    for data in exp_result:
        actual_results.append(data.tolist())

plt.plot(emulator_results, actual_results, 'ro')
plt.xlabel('Emulator result')
plt.ylabel('Actual results')
plt.show()
