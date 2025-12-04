from typing import *

def daySixteen():
    #read
    arr = []
    with open("Day16/16_1.txt", 'r') as file:
        for line in file:
            arr = [int(x) for x in line.rstrip().split(',')]

    columns = 90
    res = 0
    for v in arr:
        res += columns//v
    return res

def daySixteen2():
    #read
    arr = []
    with open("Day16/16_2.txt", 'r') as file:
        for line in file:
            arr = [int(x) for x in line.rstrip().split(',')]

    prod = 1
    size = sum(arr)
    while size > 0:
        index = [v > 0 for v in arr].index(True)
        prod *= index + 1
        for i in range(index, len(arr), index+1):
            arr[i] -= 1
            size -= 1
    return prod

def daySixteen3():
    #read
    arr = []
    with open("Day16/16_3.txt", 'r') as file:
        for line in file:
            arr = [int(x) for x in line.rstrip().split(',')]

    spell = []
    size = sum(arr)
    while size > 0:
        index = [v > 0 for v in arr].index(True)
        spell.append(index + 1)
        for i in range(index, len(arr), index+1):
            arr[i] -= 1
            size -= 1

    blocks = 202520252025000
    l,r = 0,blocks
    while l < r:
        mid = (l+r)//2
        res = 0
        for v in spell:
            res += mid//v

        if res == blocks or mid == l:
            break
        elif res < blocks:
            l = mid
        else:
            r = mid
    return mid

def main():
    print("Hallo")
    print(daySixteen(), "ist die Lösung von Teil 1")
    print(daySixteen2(), "ist die Lösung von Teil 2")
    print(daySixteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()