#!/bin/bash

# Read Array
read N
read -a array
# Sort Array
IFS=$'\n' sorted=($(sort <<<"${array[*]}"))
unset IFS
# Create counter array
count=($(echo "${sorted[@]}"|tr ' ' '\n'|uniq -c|xargs -L1|tr '\n' ' '))
N=${#count[@]}
N=$(( N-1 ))
for i in `seq 0 2 $N`
do
    temp=${count[`echo ${i}`]}
    if ((temp % 2 != 0)); then
        echo ${count[$((i+1))]}
        break
    fi
done
