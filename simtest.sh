#! /bin/bash

#Create folder
#simdir=$(python3 dirgen.py)
folder=$(python3 foldgen.py $1)
simdir='SimResults-2022-05-10-15.07'

mkdir $simdir
mkdir $simdir/$folder
cp fastsim.fst $simdir/$folder/.
cp combos.json $simdir/$folder/.
cp combocount.py $simdir/$folder/.

#Initialise
co=$(python3 input_co.py $1)
cp combogen.py $simdir/$folder/.
#printf '%s\n' "$co"

#Define number of combinations
tot_co=$(python3 input_tot.py $1)

#Define number of combinations
#tot_co=$(python3 combocount.py)

#Define combination of parameters
while [ $co -lt $tot_co ];
do
    t1=$(date +%s)
    
    cp NRELOffshrBsline* $simdir/$folder/.
    #python3 $simdir/$folder/CParams{$co}.py $co
    python3 $simdir/$folder/combogen.py $1 $co
    #vars=$(python3 $simdir/$folder/CParams.py $co)     
    #printf '%s\n' "$vars"
    
    # Perform simulation
    openfast $simdir/$folder/fastsim.fst | tee $simdir/$folder/outputlog{$co}.log

    # Move Output
    #mv 5MW_OC4Semi_WSt_WavesWN.out "sim{$co}.out"
    
    mv $simdir/$folder/fastsim.out $simdir/$folder/sim{$co}.out
    #mv "sim{$co}.out" $folder/.
    #mv outputlog{$co}.log $(python3 foldgen.py $1)/.

    # Change parameters
    co=$((co+1))
    echo "iteration $co"
    # Echo iteration time
    t2=$(date +%s)
done

#Print Program End
echo "All Done"
