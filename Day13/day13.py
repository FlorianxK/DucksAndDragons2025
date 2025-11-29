from collections import deque
from typing import *

def dayThirteen():
    #read
    arr = []
    turn = 2025
    with open("Day13/13_1.txt", 'r') as file:
        for line in file:
            arr.append(int(line.rstrip()))
    wheel = deque([1])
    right = True

    for v in arr:
        if right:
            wheel.append(v)
        else:
            wheel.appendleft(v)

        right = not right

    res = wheel[(wheel.index(1)+turn)%len(wheel)]

    return res

def dayThirteen2():
    #read
    arr = []
    turn = 20252025
    with open("Day13/13_2.txt", 'r') as file:
        for line in file:
            t = [int(x) for x in line.rstrip().split('-')]
            arr.append(t)
    wheel = [1]
    right = True
    for l,r in arr:
        nums = [i for i in range(l,r+1)]
        if right:
            wheel += nums
        else:
            wheel = nums[::-1] + wheel
        right = not right

    res = wheel[(wheel.index(1)+turn)%len(wheel)]
    return res

def dayThirteen3():
    #read
    arr = []
    turn = 202520252025
    with open("Day13/13_3.txt", 'r') as file:
        for line in file:
            t = [int(x) for x in line.rstrip().split('-')]
            arr.append(t)
    wheel = [(1,1)]
    right = True

    for l,r in arr:
        if right:
            wheel.append((l,r))
        else:
            wheel.insert(0,(r,l))
        right = not right

    iOne = wheel.index((1,1))
    wheel = wheel[iOne:] + wheel[:iOne]
    size = sum(abs(x-y)+1 for x,y in wheel)
    index = turn % size
    for x,y in wheel:
        if index > abs(x-y):
            index -= abs(x-y)+1
            continue
        if x > y:
            return x-index
        else:
            return x+index

def main():
    print("Hallo")
    print(dayThirteen(), "ist die Lösung von Teil 1")
    print(dayThirteen2(), "ist die Lösung von Teil 2")
    print(dayThirteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()