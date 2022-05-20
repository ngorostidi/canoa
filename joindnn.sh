#! /bin/bash

nprocs=8
i=1
folder='SimResults-2022-05-10-15.07'

while [ $i -le $nprocs ]
do
  cp "$folder/$i/DNNLibrary.csv" "DNNLibrary$i.csv"
  i=$((i+1))
done

python joining.py
rm DNN*
mv Library.csv DNN.csv
