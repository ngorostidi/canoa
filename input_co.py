import sys

in1 = int(sys.argv[1])

tot_procs = 8
tot_sims = 6*6*6
co = int((in1-1)*tot_sims/tot_procs)

print(co)
