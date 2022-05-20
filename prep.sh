#! /bin/bash

# 1. Create directories (SEQUENTIAL)

simdir='SimResults-2022-05-10-15.07'
mkdir $simdir

filecounter=1
while [ $filecounter -le $1 ]
do
  folder=$(python foldgen.py $filecounter)
  mkdir $simdir/$folder
  mkdir $simdir/$folder/DatFiles
  mkdir $simdir/$folder/SimFiles
  mkdir $simdir/$folder/OutputLogs

  # 2. Move .fst and .dat files to directories (SEQUENTIAL)
  cp fastsim.fst $simdir/$folder/.
  cp combos.json $simdir/$folder/.
  cp combocount.py $simdir/$folder/.
  cp NRELOffshr* $simdir/$folder/.
  
  #Initialise
  co=$(python3 input_co.py $filecounter)
  cp combogen.py $simdir/$folder/.
  #printf '%s\n' "$co"

  #Define number of combinations
  tot_co=$(python3 input_tot.py $filecounter)

  cd $simdir/$folder/
  python3 combogen.py $filecounter

  #cp fastsim.fst tempfst.fst
  mv fastsim* DatFiles/.
  chmod +x DatFiles/fastsim*
  #rm fastsim*
  #mv NRELOffshrBsline5MW_InflowWind_Steady8mps.dat tempinflow.fst
  mv NREL* DatFiles/.
  #rm NRELOffshrBsline5MW_InflowWind_Steady8mps*
  #mv NRELOffshrBsline5MW_OC4DeepCwindSemi_HydroDyn.dat temphydro.dat
  #rm NRELOffshrBsline5MW_OC4DeepCwindSemi_HydroDyn*

  #mv tempfst.fst fastsim.fst
  #mv tempinflow NRELOffshrBsline5MW_InflowWind_Steady8mps.dat
  #mv fastsim.fst tempfst.fst
  #mv temphydro.dat NRELOffshrBsline5MW_OC4DeepCwindSemi_HydroDyn.dat
  cd ../../
  filecounter=$((filecounter+1))
done
