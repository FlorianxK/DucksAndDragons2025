from typing import *

def dayThree():
    #read
    arr = []
    with open("Day3/3_1.txt", 'r') as file:
        for line in file:
            temp = line.rstrip().split(',')
            arr = [int(x) for x in temp]
    arr.sort(reverse=True)
    prev = arr[0]
    res = arr[0]
    for i in range(1,len(arr)):
        if arr[i] != prev:
            prev = arr[i]
            res += arr[i]
    return res

def dayThree2():
    #read
    arr = []
    with open("Day3/3_2.txt", 'r') as file:
        for line in file:
            temp = line.rstrip().split(',')
            arr = [int(x) for x in temp]
    arr.sort()
    prev = arr[0]
    res = arr[0]
    amount = 1
    for i in range(1,len(arr)):
        if arr[i] != prev:
            prev = arr[i]
            res += arr[i]
            amount += 1
        
        if amount == 20:
            break
    return res

def dayThree3():
    #read
    arr = []
    with open("Day3/3_3.txt", 'r') as file:
        for line in file:
            temp = line.rstrip().split(',')
            arr = [int(x) for x in temp]
    arr.sort(reverse=True)

    sets = 0
    while arr:
        prev = arr[0]
        rest = []
        for i in range(1,len(arr)):
            if arr[i] != prev:
                prev = arr[i]
            else:
                rest.append(arr[i])
        arr = rest[:]
        sets += 1
    return sets

def main():
    print("Hallo")
    print(dayThree(), "ist die Lösung von Teil 1")
    print(dayThree2(), "ist die Lösung von Teil 2")
    print(dayThree3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()