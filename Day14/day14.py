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
    with open("Day14/14_3.txt", 'r') as file:
        for line in file:
            pattern.append(list(line.rstrip()))

    rounds = 1000000000
    n = 34
    patternI = len(pattern)
    start = (n-patternI)//2
    targeton = {(i,j) for i,line in enumerate(pattern,start) for j,char in enumerate(line,start) if char=='#'}
    targetoff = {(i,j) for i,line in enumerate(pattern,start) for j,char in enumerate(line,start) if char=='.'}

    grid = set()

    def neighbours(coord):
        x,y = coord
        return {(x-1,y-1),(x-1,y+1),(x,y),(x+1,y-1),(x+1,y+1)}

    def oneRound(grid):
        output = set()
        for i in range(n):
            for j in range(n):
                if len(set.intersection(neighbours((i,j)),grid))%2==0:
                    output.add((i,j))
        return output

    grids = []
    while True:
        grids.append(grid)
        grid = oneRound(grid)
        if grid in grids:
            cyclestart = grids.index(grid)
            cycleend = len(grids)
            cyclelength = cycleend-cyclestart
            break

    counts = []
    for i,grid in enumerate(grids):
        if set.intersection(grid,targeton) == targeton and not set.intersection(grid,targetoff):
            counts.append([i,len(grid)])

    res = 0
    for i,count in counts:
        res += ((rounds-i)//cyclelength+1)*count

    return res

def main():
    print("Hallo")
    print(dayFourteen(), "ist die Lösung von Teil 1")
    print(dayFourteen2(), "ist die Lösung von Teil 2")
    print(dayFourteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()