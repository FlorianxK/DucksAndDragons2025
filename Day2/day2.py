import itertools
from typing import *

def dayTwo():
    a = [0,0]
    #read
    with open("Day2/2_1.txt", 'r') as file:
        for line in file:
            x,y = line.rstrip()[3:len(line)-1].split(',')
            a = [int(x),int(y)]

    def add(c1,c2):
        x = c1[0]+c2[0]
        y = c1[1]+c2[1]
        return [x,y]

    def mult(c1,c2):
        x = c1[0]*c2[0]-c1[1]*c2[1]
        y = c1[0]*c2[1]+c1[1]*c2[0]
        return [x,y]
    
    def div(c1,c2):
        return [c1//c2 if c1>=0 else -((-c1)//c2) for c1,c2 in zip(c1,c2)]

    def cycle(R,A):
        R = mult(R,R)
        R = div(R,[10,10])
        R = add(R,A)
        return R

    res = [0,0]
    #cycle
    for _ in range(3):
        res = cycle(res,a)
    
    return res

def dayTwo2():
    a = [0,0]
    #read
    with open("Day2/2_2.txt", 'r') as file:
        for line in file:
            x,y = line.rstrip()[3:len(line)-1].split(',')
            a = [int(x),int(y)]

    b = [a[0]+1000,a[1]+1000]

    def add(c1,c2):
        x = c1[0]+c2[0]
        y = c1[1]+c2[1]
        return [x,y]

    def mult(c1,c2):
        x = c1[0]*c2[0]-c1[1]*c2[1]
        y = c1[0]*c2[1]+c1[1]*c2[0]
        return [x,y]
    
    def div(c1,c2):
        return [c1//c2 if c1>=0 else -((-c1)//c2) for c1,c2 in zip(c1,c2)]

    def cycle(R,A):
        R = mult(R,R)
        R = div(R,[100000,100000])
        R = add(R,A)
        return R

    points = 0
    while a[0] <= b[0] and a[1] <= b[1]:
        res = [0,0]
    #cycle
        correct = True
        for _ in range(100):
            res = cycle(res,a)
            x,y = res
            if x < -1000000 or x > 1000000 or y < -1000000 or y > 1000000:
                correct = False
                break

        if correct:
            points += 1
        a[0] += 10
        if a[0] > b[0]:
            a[0] -= 1010
            a[1] += 10
    return points

def dayTwo3():
    a = [0,0]
    #read
    with open("Day2/2_3.txt", 'r') as file:
        for line in file:
            x,y = line.rstrip()[3:len(line)-1].split(',')
            a = [int(x),int(y)]

    def add(c1,c2):
        x = c1[0]+c2[0]
        y = c1[1]+c2[1]
        return [x,y]

    def mult(c1,c2):
        x = c1[0]*c2[0]-c1[1]*c2[1]
        y = c1[0]*c2[1]+c1[1]*c2[0]
        return [x,y]
    
    def div(c1,c2):
        return [c1//c2 if c1>=0 else -((-c1)//c2) for c1,c2 in zip(c1,c2)]

    def cycle(R,A):
        R = mult(R,R)
        R = div(R,[100000,100000])
        R = add(R,A)
        return R

    count = 0
    for xd,yd in itertools.product(range(1001),range(1001)):
        P = [a[0]+xd,a[1]+yd]
        result = [0,0]
        correct = True
        for _ in range(100):
            result = cycle(result,P)
            if any(abs(num)>1000000 for num in result):
                correct = False
                break
        if correct:
            count += 1
    return count

def main():
    print("Hallo")
    print(str(dayTwo()).replace(" ", ""), "ist die Lösung von Teil 1")
    print(dayTwo2(), "ist die Lösung von Teil 2")
    print(dayTwo3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()