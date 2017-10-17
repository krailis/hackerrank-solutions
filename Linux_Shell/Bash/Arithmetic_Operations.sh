#!/bin/bash

read X
#Y=$(echo "scale=3;$X" | bc)
#echo "$Y"
#echo $(printf %.$3f $(echo "scale=3;$X" | bc))
printf "%.3f\n" "$(bc -l <<< "$X")"
