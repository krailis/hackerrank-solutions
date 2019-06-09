#!/bin/python3

import sys

grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
max_p = 1
for i in range(20):
    for j in range(17):
        p = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
        if max_p < p:
            max_p = p
for j in range(20):
    for i in range(17):
        p = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
        if max_p < p:
            max_p = p
for i in range(17):
    for j in range(17):
        p = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
        if max_p < p:
            max_p = p
for i in range(17):
    for j in range(19, 2, -1):
        p = grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
        if max_p < p:
            max_p = p        
print(max_p)
