#!/bin/bash

DONE=false
N=0
read X || DONE=true
until $DONE ; do
    array[${N}]=${X}
    N=$((N + 1))
    read X || DONE=true
done
echo ${array[@]/[A-Z]/.}
