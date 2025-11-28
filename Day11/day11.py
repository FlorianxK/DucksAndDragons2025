from typing import *

def dayEleven():
    rounds = 10
    #read
    arr = []
    with open("Day11/11.txt", 'r') as file:
        for line in file:
            arr.append(int(line.rstrip()))
    n = len(arr)

    def firstPhase(arr):
        moved = True
        round = 0
        while moved:
            moved = False
            for i in range(n-1):
                if arr[i] > arr[i+1]:
                    arr[i] -= 1
                    arr[i+1] += 1
                    moved = True
            round += 1
        return round-1

    def secondPhase(arr,left):
        for _ in range(left):
            for i in range(n-1):
                if arr[i] < arr[i+1]:
                    arr[i+1] -= 1
                    arr[i] += 1

    used = firstPhase(arr)
    secondPhase(arr,rounds-used)
    res = 0
    for i in range(1,n+1):
        res += i*arr[i-1]
    return res

def dayEleven2():
    #read
    arr = []
    with open("Day11/11_2.txt", 'r') as file:
        for line in file:
            arr.append(int(line.rstrip()))
    n = len(arr)

    def firstPhase(arr):
        moved = True
        round = 0
        while moved:
            moved = False
            for i in range(n-1):
                if arr[i] > arr[i+1]:
                    arr[i] -= 1
                    arr[i+1] += 1
                    moved = True
            round += 1
        return round-1

    def secondPhase(arr,used):
        change = True
        counter = 0
        while change:
            change = False
            for i in range(n-1):
                if arr[i] < arr[i+1]:
                    arr[i+1] -= 1
                    arr[i] += 1
                    change = True
            counter += 1
        return counter+used-1

    used = firstPhase(arr)
    res = secondPhase(arr,used)

    return res

def dayEleven3():
    #read
    arr = []
    with open("Day11/11_3.txt", 'r') as file:
        for line in file:
            arr.append(int(line.rstrip()))

    average = sum(arr) // len(arr)
    balance = [average-v for v in arr if v < average]
    return sum(balance)

def main():
    print("Hallo")
    print(dayEleven(), "ist die Lösung von Teil 1")
    print(dayEleven2(), "ist die Lösung von Teil 2")
    print(dayEleven3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()