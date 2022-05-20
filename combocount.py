# Reading modules
import numpy as np
import pandas as pd
import json
import sys

# Reading combinations from dictionary
with open('combos.json','r') as combodict:
        params = json.load(combodict)
        df = pd.DataFrame(params)

WindVel   = np.linspace(int(df['WindVel']['start']),   int(df['WindVel']['end']),   int(df['WindVel']['n']))
Hs = np.linspace(int(df['Hs']['start']),   int(df['Hs']['end']),   int(df['Hs']['n']))
Tp = np.linspace(int(df['Tp']['start']),   int(df['Tp']['end']),   int(df['Tp']['n']))
# MoorMass  = np.linspace(int(df['MoorMass']['start']),  int(df['MoorMass']['end']),  int(df['MoorMass']['n']))
# MoorStiff = np.linspace(int(df['MoorStiff']['start']), int(df['MoorStiff']['end']), int(df['MoorStiff']['n']))
# MoorDamp  = np.linspace(int(df['MoorDamp']['start']),  int(df['MoorDamp']['end']),  int(df['MoorDamp']['n']))

combos_init = np.array(np.meshgrid(WindVel, Hs, Tp)).T.reshape(-1, 3)

print(len(combos_init)) ## UNCOMMENT WHEN RUNNING BASH SIM SCRIPT


def comboc(jsfile, index):
	with open(jsfile,'r') as combd:
		params = json.load(combd)
		df = pd.DataFrame(params)
	
	
	WindVel   = np.linspace(int(df['WindVel']['start']),   int(df['WindVel']['end']),   int(df['WindVel']['n']))
	Hs = np.linspace(int(df['Hs']['start']),   int(df['Hs']['end']),   int(df['Hs']['n']))
	Tp = np.linspace(int(df['Tp']['start']),   int(df['Tp']['end']),   int(df['Tp']['n']))

	combos_init = np.array(np.meshgrid(WindVel, Hs, Tp)).T.reshape(-1, 3)

	return combos_init[index][0], combos_init[index][1], combos_init[index][2]
