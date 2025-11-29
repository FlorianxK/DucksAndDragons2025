from typing import *

def dayFourteen():
    #read
    arr = []
    with open("Day14/14_1.txt", 'r') as file:
        for line in file:
            arr.append(list(line.rstrip()))
    rounds = 10
    dir = [(1,1),(-1,-1),(1,-1),(-1,1)]
    m,n = len(arr),len(arr[0])

    def oneRound(arr):
        nextArr = [ ['0']*n for _ in range(m) ]
        active = 0

        for i in range(m):
            for j in range(n):
                activeNeigh = 0
                for dx,dy in dir:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<m and 0<=ny<n:
                        if arr[nx][ny] == '#':
                            activeNeigh += 1

                if arr[i][j] == '#':
                    if activeNeigh % 2 != 0:
                        nextArr[i][j] = '#'
                        active += 1
                    else:
                        nextArr[i][j] = '.'

                elif arr[i][j] == '.':
                    if activeNeigh % 2 == 0:
                        nextArr[i][j] = '#'
                        active += 1
                    else:
                        nextArr[i][j] = '.'
        return nextArr,active

    res = 0
    for _ in range(1,rounds+1):
        arr,active = oneRound(arr)
        res += active
    return res

def dayFourteen2():
    #read
    arr = []
    with open("Day14/14_2.txt", 'r') as file:
        for line in file:
            arr.append(list(line.rstrip()))
    rounds = 2025
    dir = [(1,1),(-1,-1),(1,-1),(-1,1)]
    m,n = len(arr),len(arr[0])

    def oneRound(arr):
        nextArr = [ ['0']*n for _ in range(m) ]
        active = 0

        for i in range(m):
            for j in range(n):
                activeNeigh = 0
                for dx,dy in dir:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<m and 0<=ny<n:
                        if arr[nx][ny] == '#':
                            activeNeigh += 1

                if arr[i][j] == '#':
                    if activeNeigh % 2 != 0:
                        nextArr[i][j] = '#'
                        active += 1
                    else:
                        nextArr[i][j] = '.'

                elif arr[i][j] == '.':
                    if activeNeigh % 2 == 0:
                        nextArr[i][j] = '#'
                        active += 1
                    else:
                        nextArr[i][j] = '.'
        return nextArr,active

    res = 0
    for _ in range(1,rounds+1):
        arr,active = oneRound(arr)
        res += active
    return res

def dayFourteen3():
    #read
    pattern = []
    with open("Day14/14.txt", 'r') as file:
        for line in file:
            pattern.append(list(line.rstrip()))

    rounds = 1000000000
    n = 34
    patternI = len(pattern)
    dir = [(1,1),(-1,-1),(1,-1),(-1,1)]

    start = [ ['.']*n for _ in range(n) ]

    def oneRound(arr):
        nextArr = [ ['0']*n for _ in range(n) ]
        active = 0
        found = True
        l = n//2-patternI//2
        r = l+patternI-1

        for i in range(n):
            for j in range(n):
                activeNeigh = 0
                for dx,dy in dir:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<n and 0<=ny<n:
                        if arr[nx][ny] == '#':
                            activeNeigh += 1

                if arr[i][j] == '#':
                    if activeNeigh % 2 != 0:
                        nextArr[i][j] = '#'
                        active += 1
                    else:
                        nextArr[i][j] = '.'

                elif arr[i][j] == '.':
                    if activeNeigh % 2 == 0:
                        nextArr[i][j] = '#'
                        active += 1
                    else:
                        nextArr[i][j] = '.'

                #pattern
                if l<=i<=r and l<=j<=r:
                    if arr[i][j] != pattern[i-l][j-l]:
                        found = False

        return nextArr,active,found

    res = 0
    for k in range(1,rounds+1):
        start,active,found = oneRound(start)
        if found:
            res += active

            print(k-1)

def main():
    print("Hallo")
    #print(dayFourteen(), "ist die Lösung von Teil 1")
    #print(dayFourteen2(), "ist die Lösung von Teil 2")
    print(dayFourteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()