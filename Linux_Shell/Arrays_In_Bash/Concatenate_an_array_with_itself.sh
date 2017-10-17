#!/bin/bash

DONE=false
N=0
until $DONE ; do
    read X || DONE=true
    array[${N}]=${X}
    N=$((N + 1))
done
concatenated=("${array[@]}" "${array[@]}" "${array[@]}")
echo ${concatenated[@]}
