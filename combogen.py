import pandas as pd
import numpy as np
import json
import sys

in1 = int(sys.argv[1])
tot_sims = 216
tot_procs = 8

#co = co-(in1-1)*tot_sims/tot_procs

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
df_combos = pd.DataFrame(combos_init)
df_combos.columns = ['WindVel', 'Hs', 'Tp']

#dh = df_combos[int((in1-1)*tot_sims/tot_procs) : int(in1*tot_sims/tot_procs)]
#co = int(co-(in1-1)*tot_sims/tot_procs)

def ChangeParams(c, l, WindVel=10, Hs=6, Tp=10, MoorMass=113.35, MoorStiff=3e6, MoorDamp=3e5):

    with open('NRELOffshrBsline5MW_InflowWind_Steady8mps.dat', 'r') as f:
        lines = f.readlines()
        lines[12] = '         {}   HWindSpeed     - Horizontal wind speed                           (m/s)\n'.format(WindVel)

    with open('NRELOffshrBsline5MW_InflowWind_Steady8mps'+str(c+1)+'.dat', 'w') as f:
        f.writelines(lines)

    with open('NRELOffshrBsline5MW_OC4DeepCwindSemi_HydroDyn.dat', 'r') as f:
        lines = f.readlines()
        lines[13] = '            {}   WaveHs         - Significant wave height of incident waves (meters) [used only when WaveMod=1, 2, or 3]\n'.format(Hs)
        lines[12] = '		 {}   WaveTp         - Peak-spectral period of incident waves       (sec) [used only when WaveMod=1 or 2]\n'.format(Tp)

    with open('NRELOffshrBsline5MW_OC4DeepCwindSemi_HydroDyn'+str(c+1)+'.dat', 'w') as f:
        f.writelines(lines)
    
    with open('fastsim.fst', 'r') as f:
        lines = f.readlines()
        lines[25] = '"NRELOffshrBsline5MW_InflowWind_Steady8mps{}.dat"    InflowFile      - Name of file containing inflow wind input parameters (quoted string)\n'.format(c+1)
        lines[28] = '"NRELOffshrBsline5MW_OC4DeepCwindSemi_HydroDyn{}.dat"    HydroFile       - Name of file containing hydrodynamic input parameters (quoted string)\n'.format(c+1)

    with open('fastsim'+str(c)+'.fst', 'w') as f:
        f.writelines(lines)

for co in range(int((in1-1)*tot_sims/tot_procs), int(in1*tot_sims/tot_procs)):
    ChangeParams(co, len(df_combos), WindVel=df_combos['WindVel'].iloc[co], Hs=df_combos['Hs'].iloc[co], Tp= df_combos['Tp'].iloc[co])

#print('{}, {}, {}'.format(dh['WindVel'].iloc[co], dh['Hs'].iloc[co], dh['Tp'].iloc[co]))
