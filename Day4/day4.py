from collections import deque
import math
from typing import *

def dayFour():
    #read
    arr = []
    with open("Day4/4_1.txt", 'r') as file:
        for line in file:
            arr.append(int(line.rstrip()))
    res = 1
    for i in range(1,len(arr)):
        res *= arr[i-1]/arr[i]
    return int(res*2025)

def dayFour2():
    #read
    arr = []
    with open("Day4/4_2.txt", 'r') as file:
        for line in file:
            arr.append(int(line.rstrip()))
    perc = [1.0]
    for i in range(1,len(arr)):
        perc.append((arr[i-1]/arr[i])*perc[-1])

    res = 10000000000000/perc[-1]
    return math.ceil(res)

def dayFour3():
    #read
    arr = []
    skip = deque([])
    index = 0
    with open("Day4/4_3.txt", 'r') as file:
        for line in file:
            line = line.strip()
            if '|' in line:
                a,b = line.split('|')
                arr.extend([int(a),int(b)])
                skip.append(index)
                index += 1
            else:
                arr.append(int(line))
            index += 1

    res = 1
    for i in range(1,len(arr)):
        if skip and i-1 == skip[0]:
            skip.popleft()
        else:
            v = arr[i-1]/arr[i]
            res *= v

    return int(res*100)

def main():
    print("Hallo")
    print(dayFour(), "ist die Lösung von Teil 1")
    print(dayFour2(), "ist die Lösung von Teil 2")
    print(dayFour3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()