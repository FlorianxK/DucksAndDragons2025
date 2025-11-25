from collections import deque
from typing import *

def dayTen():
    moves = 4
    #read
    arr = []
    with open("Day10/10_1.txt", 'r') as file:
        for line in file:
            arr.append(list(line.rstrip()))

    m,n = len(arr),len(arr[0])
    eaten = 0
    dragon = (m//2,n//2)
    level = deque([dragon])
    seen = set()
    seen.add(dragon)
    while moves > 0:
        nextlevel = deque([])
        while level:
            curr = level.popleft()
            x,y = curr
            for dx,dy in [(2,-1),(2,1),(-2,-1),(-2,1),(1,2),(-1,2),(1,-2),(-1,-2)]:
                nx,ny = x+dx,y+dy

                if nx < 0 or nx >= m or ny < 0 or nx >= n or (nx,ny) in seen: continue

                seen.add((nx,ny))
                nextlevel.append((nx,ny))
                if arr[nx][ny] == 'S':
                    eaten += 1
        level = nextlevel
        moves -= 1
    return eaten

def dayTen2():
    moves = 20
    res = 0
    #read
    arr = []
    sheeps = []
    with open("Day10/10_2.txt", 'r') as file:
        i = 0
        for line in file:
            for j in range(len(line)):
                if line[j] == 'S':
                    sheeps.append( (i,j) )

            i += 1
            arr.append(list(line.rstrip()))

    m,n = len(arr),len(arr[0])
    dragon = (m//2,n//2)
    level = deque([dragon])
    eaten = 0
    seen = set()
    move = 1
    while move <= moves:

        darr = [['.']*n for _ in range(m)]
        nextlevel = deque([])
        while level:
            curr = level.popleft()
            x,y = curr
            for dx,dy in [(2,-1),(2,1),(-2,-1),(-2,1),(1,2),(-1,2),(1,-2),(-1,-2)]:
                nx,ny = x+dx,y+dy

                if nx < 0 or nx >= m or ny < 0 or nx >= n and (nx,ny) not in seen: continue

                seen.add( (nx,ny) )
                darr[nx][ny] = 'X'
                nextlevel.append((nx,ny))

        level = nextlevel

        #sheep 0
        if move == 1:
            nextSheeps = []
            for x,y in sheeps:
                if darr[x][y] == 'X':
                    eaten += 1
                else:
                    nextSheeps.append( (x,y) )
            sheeps = nextSheeps

        nextSheeps = []
        for x,y in sheeps:
            nx = x+1
            if nx >= m: continue
            
            if darr[nx][y] == 'X' and arr[nx][y] != '#':
                eaten += 1
            else:
                nextSheeps.append( (nx,y) )
        sheeps = nextSheeps

        print(eaten)
        res += eaten
        move += 1

    return res

def dayTen3():
    pass

def main():
    print("Hallo")
    #print(dayTen(), "ist die Lösung von Teil 1")
    print(dayTen2(), "ist die Lösung von Teil 2")
    #print(dayTen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()