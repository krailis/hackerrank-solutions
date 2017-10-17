#!/bin/bash

read -e X
read -e Y
SUM=$((X + Y))
DIF=$((X - Y))
PRO=$((X * Y))
QUO=$((X / Y))
echo ${SUM}
echo ${DIF}
echo ${PRO}
echo ${QUO}
