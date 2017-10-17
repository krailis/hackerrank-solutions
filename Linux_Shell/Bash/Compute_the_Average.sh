#!/bin/bash

read N
SUM=0
for I in `seq 1 ${N}`
do
    read X
    SUM=$((${SUM}+${X}))
done
printf "%.3f\n" "$(bc -l <<< "$SUM"/"$N")"

