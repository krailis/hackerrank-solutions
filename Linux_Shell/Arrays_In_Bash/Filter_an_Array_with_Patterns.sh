#!/bin/bash

DONE=false
N=0
until $DONE ; do
    read X || DONE=true
    array[${N}]=${X}
    N=$((N + 1))
done
removed_a=( ${array[@]/*a*/} )
removed_A=( ${removed_a[@]/*A*/} )
echo ${removed_A[@]}
