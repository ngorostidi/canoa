import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt
from spectralfunctions import getFourier, momentum, AvgStDev, getAveragePeriod
from combocount import comboc 

def create_dictionary(keys, data):
    """  This function creates a dictionary with the provided data and keys. keys is an array containing the str
     that will be the keys and data is a matrix whose columns are the values for each key in the dictionary """

    cont = 0
    pair_list = []
    try:
        for key in keys:
            pair_list.append((key, data[:, cont]))
            cont = cont + 1
    except IndexError:
        for key in keys:
            pair_list.append((key, data[cont]))
            cont = cont + 1
    except TypeError:
        if isinstance(data, (list)):
            for key in keys:
                pair_list.append((key, data[cont]))
                cont = cont + 1

    dictionary = dict(pair_list)

    return dictionary


def read_OpenFAST_output(file):
    if file.endswith(".out"):
        data = pd.read_csv(file, sep="\t", skiprows=6, header=0, skip_blank_lines=False, comment="(")
        keys = np.array(data.columns)
        for i in range(len(np.array(data.columns))):
            keys[i] = keys[i].strip()

        data = create_dictionary(keys, data.to_numpy())

        return data

#data = read_OpenFAST_output('SimResults/sim{0}.out')

proc = int(sys.argv[1])
tot_procs = 8
tot_sims = 216 

with open('SimResults-2022-05-10-15.07/'+str(proc)+'/DNNLibrary.csv', 'w+') as output:
	#output.write('Hs, Tp, V, signal_mean, signal_stdev, period_mean, period_stdev, f_max, m0\n')
	output.close()


for i in range(int((proc-1)*tot_sims/tot_procs), int(proc*tot_sims/tot_procs)):

	data = read_OpenFAST_output('SimResults-2022-05-10-15.07/'+str(proc)+'/SimFiles/sim{'+str(i)+'}.out')
	data = pd.DataFrame(data)
	
	condition = 0
	V, Hs, Tp = comboc('combos.json', index=i)

	surge_mean, surge_stdev = AvgStDev(data['PtfmSurge'])
	sway_mean, sway_stdev = AvgStDev(data['PtfmSway'])
	heave_mean, heave_stdev = AvgStDev(data['PtfmHeave'])
	roll_mean, roll_stdev = AvgStDev(data['PtfmRoll'])
	pitch_mean, pitch_stdev = AvgStDev(data['PtfmPitch'])
	yaw_mean, yaw_stdev = AvgStDev(data['PtfmYaw'])

	freq, psd, surge_flow, surge_fhigh = getFourier(data['Time'], data['PtfmSurge'])
	surge_m0 = momentum(freq, psd)
	freq, psd, sway_flow, sway_fhigh = getFourier(data['Time'], data['PtfmSway'])
	sway_m0 = momentum(freq, psd)
	freq, psd, heave_flow, heave_fhigh = getFourier(data['Time'], data['PtfmHeave'])
	heave_m0 = momentum(freq, psd)
	freq, psd, roll_flow, roll_fhigh = getFourier(data['Time'], data['PtfmRoll'])
	roll_m0 = momentum(freq, psd)
	freq, psd, pitch_flow, pitch_fhigh = getFourier(data['Time'], data['PtfmPitch'])
	pitch_m0 = momentum(freq, psd)
	freq, psd, yaw_flow, yaw_fhigh = getFourier(data['Time'], data['PtfmYaw'])
	yaw_m0 = momentum(freq, psd)
        
	filename = 'SimResults-2022-05-10-15.07/'+str(proc)+'/DNNLibrary.csv'
        
	with open(filename, 'a') as output:

	        output.write('{:.3f}, {:.3f}, {:.3f}, '.format(Hs, Tp, V))
	        output.write('{:.4e}, {:.4e}, {:.4e}, {:.4e}, {:.4e}, '.format(surge_mean, surge_stdev, surge_flow, surge_fhigh, surge_m0))
	        output.write('{:.4e}, {:.4e}, {:.4e}, {:.4e}, {:.4e}, '.format(sway_mean, sway_stdev, sway_flow, sway_fhigh, sway_m0))
	        output.write('{:.4e}, {:.4e}, {:.4e}, {:.4e}, {:.4e}, '.format(heave_mean, heave_stdev, heave_flow, heave_fhigh, heave_m0))
	        output.write('{:.4e}, {:.4e}, {:.4e}, {:.4e}, {:.4e}, '.format(roll_mean, roll_stdev, roll_flow, roll_fhigh, roll_m0))
	        output.write('{:.4e}, {:.4e}, {:.4e}, {:.4e}, {:.4e}, '.format(pitch_mean, pitch_stdev, pitch_flow, pitch_fhigh, pitch_m0))
	        output.write('{:.4e}, {:.4e}, {:.4e}, {:.4e}, {:.4e}, {:.0f}\n'.format(yaw_mean, yaw_stdev, yaw_flow, yaw_fhigh, yaw_m0, condition))
	
	#print('Output written for file sim'+str(i)+'.out file') 
	#print('.............................................................................')
