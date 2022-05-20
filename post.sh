#!/bin/bash

python OUTRead.py $1
simdir='SimResults-2022-05-10-15.07'

cp $simdir/$1/DNNLibrary.csv DNN.csv
