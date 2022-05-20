#! /bin/bash

simdir='SimResults-2022-05-10-15.07'
folder=$1

#Initialise
co=$(python3 input_co.py $1)

#Define number of combinations
tot_co=$(python3 input_tot.py $1)

while [ $co -lt $tot_co ];
do
  # Perform simulation
  openfast $simdir/$folder/DatFiles/fastsim$co.fst #| tee $simdir/$folder/outputlog{$co}.log

  mv $simdir/$folder/DatFiles/fastsim$co.out $simdir/$folder/SimFiles/sim{$co}.out
  #mv $simdir/$folder/outputlog{$co}.log $simdir/$folder/OutputLogs/.

  # Change parameters
  co=$((co+1))
done
