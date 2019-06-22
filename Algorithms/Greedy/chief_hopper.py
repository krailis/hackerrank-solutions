#!/bin/python3

# Complete the chiefHopper function below.
def chief_hopper(arr):
    init_energy = 1
    while True:
        found_energy = True
        bot_energy = init_energy
        for height in arr:
            if height >= bot_energy:
                bot_energy -= height - bot_energy
            elif bot_energy > height:
                bot_energy += bot_energy - height
            if bot_energy < 0:
                found_energy = False
                break
        if found_energy:
            return init_energy
        else:
            init_energy += 1
        

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = chief_hopper(arr)
    print(result)

