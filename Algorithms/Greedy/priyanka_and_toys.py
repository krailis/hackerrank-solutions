#!/bin/python3

def toys(w):
    w.sort()
    containers = 0
    while (w != []):
        lighter, i = w[0], 0
        while (i < len(w)):
            if w[i] > lighter + 4:
                break
            i += 1    
        w = w[i:]
        containers += 1
    return containers

if __name__ == '__main__':
    n = int(input())
    w = list(map(int, input().rstrip().split()))
    result = toys(w)
    print(result)

