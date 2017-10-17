#!/bin/bash

read X
read Y
read Z

if (("$X" == "$Y" && "$Y" == "$Z")); then
    echo "EQUILATERAL"
elif (("$X" == "$Y" && "$Y" != "$Z")); then
    echo "ISOSCELES"
elif (("$X" == "$Z" && "$Y" != "$Z")); then
    echo "ISOSCELES"
elif (("$Y" == "$Z" && "$Y" != "$X")); then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi

