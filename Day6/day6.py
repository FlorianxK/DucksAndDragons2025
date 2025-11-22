from typing import *

def daySix():
    #read
    input = []
    with open("Day6/6_1.txt", 'r') as file:
        for line in file:
            input = list(line.rstrip())

    res = 0
    knightA = 0
    for c in input:
        if c == 'A':
            knightA += 1
        elif c == 'a':
            res += knightA
    return res

def daySix2():
    #read
    input = []
    with open("Day6/6_2.txt", 'r') as file:
        for line in file:
            input = list(line.rstrip())

    res = 0
    knights = {}

    for c in input:
        if c.isupper():
            if c in knights:
                knights[c] += 1
            else:
                knights[c] = 1
        else:
            big = c.upper()
            if big in knights:
                res += knights[big]
    return res

def daySix3():
    #read
    input = []
    with open("Day6/6_3.txt", 'r') as file:
        for line in file:
            input = list(line.rstrip())
    
    n = len(input)
    input_repeated = input*3

    first_count = [0 for _ in range(n)]
    mid_count = [0 for _ in range(n)]
    last_count = [0 for _ in range(n)]

    for i,char in enumerate(input):
        if char == char.lower():
            mid_count[i] = input_repeated[n+i-1000:n+i+1001].count(char.upper())
            first_count[i] = input_repeated[max(n+i-1000,n):n+i+1001].count(char.upper())
            last_count[i] = input_repeated[n+i-1000:min(n+i+1001,2*n)].count(char.upper())

    res = sum(first_count)+998*sum(mid_count)+sum(last_count)
    return res

def main():
    print("Hallo")
    print(daySix(), "ist die Lösung von Teil 1")
    print(daySix2(), "ist die Lösung von Teil 2")
    print(daySix3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()