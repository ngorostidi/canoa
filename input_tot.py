import sys

in1 = int(sys.argv[1])

tot_procs = 8 
tot_sims = 6*6*6

if in1 < tot_procs:
    tot_co = int(in1*tot_sims/tot_procs)
else:
    tot_co = tot_sims

print(tot_co)
