from typing import *

def dayEight():
    #read
    order = []
    nails = 32
    with open("Day8/8_1.txt", 'r') as file:
        for line in file:
            order = [int(x) for x in line.rstrip().split(',')]

    middle = 0
    half = nails//2
    for i in range(1,len(order)):
        if abs(order[i-1]-order[i]) == half:
            middle += 1
    return middle
        
def dayEight2():
    #read
    order = []
    with open("Day8/8_2.txt", 'r') as file:
        for line in file:
            order = [int(x) for x in line.rstrip().split(',')]

    points = []
    knots = 0
    for i in range(1,len(order)):
        x = min(order[i-1],order[i])
        y = max(order[i-1],order[i])
        for a,b in points:
            if x == a or x == b or y == a or y == b: continue
            if (a < x < b) != (a < y < b):
                knots += 1
        points.append([x,y])
    return knots

def dayEight3():
    #read
    order = []
    nails = 256
    with open("Day8/8_3.txt", 'r') as file:
        for line in file:
            order = [int(x) for x in line.rstrip().split(',')]
    d = {}
    for i in range(1, nails+1):
        for j in range(i+1,nails+1):
            d[ (i,j) ] = 0

    for i in range(1,len(order)):
        x = min(order[i-1],order[i])
        y = max(order[i-1],order[i])
        for k in d.keys():
            a,b = k
            if (x < a and x < b and y > a and y < b) or (x > a and x < b and y > a and y > b) or (x == a and y == b):
                d[k] += 1

    return max(d.values())

def main():
    print("Hallo")
    print(dayEight(), "ist die Lösung von Teil 1")
    print(dayEight2(), "ist die Lösung von Teil 2")
    print(dayEight3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()