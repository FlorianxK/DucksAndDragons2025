from collections import deque
from typing import *

def dayFifteen():
    #read
    arr = []
    with open("Day15/15_1.txt", 'r') as file:
        for line in file:
            arr = line.rstrip().split(',')
    
    coord = { 0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1) }

    #find width and height
    minI,maxI = 0,0
    minJ,maxJ = 0,0
    posI,posJ = 0,0
    dir = 0
    for a in arr:
        nextDir,v = a[0],int(a[1:])
        if nextDir == 'R':
            dir = (dir+1)%4
        else:
            dir = (dir-1)%4

        nx,ny = coord[dir]
        posI += nx*v
        posJ += ny*v

        minI = min(minI,posI)
        maxI = max(maxI,posI)
        minJ = min(minJ,posJ)
        maxJ = max(maxJ,posJ)

    maxW,maxH = abs(minJ)+maxJ+1,abs(minI)+maxI+1
    sx,sy = abs(minI),abs(minJ)
    grid = [ [' ']*(maxW) for _ in range(maxH) ]

    #create grid
    grid[sx][sy] = 'S'
    currI,currJ = sx,sy
    dir = 0
    for a in arr:
        nextDir,v = a[0],int(a[1])
        if nextDir == 'R':
            dir = (dir+1)%4
        else:
            dir = (dir-1)%4

        nx,ny = coord[dir]
        while v > 0:
            currI += nx
            currJ += ny
            grid[currI][currJ] = '#'
            v -= 1

    grid[currI][currJ] = 'E'

    #bfs to find goal
    def bfs(start):
        seen = set()
        q = deque([ (0,start) ])
        seen.add( start )
        while q:
            v,coord = q.popleft()
            x,y = coord
            #check goal
            if grid[x][y] == 'E':
                return v

            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny = x+dx,y+dy
                if 0<=nx<maxH and 0<=ny<maxW and grid[nx][ny] != '#' and (nx,ny) not in seen:
                    seen.add( (nx,ny) )
                    q.append( (v+1,(nx,ny)) )

    res = bfs((sx,sy))
    return res

def dayFifteen2():
    #read
    arr = []
    with open("Day15/15_2.txt", 'r') as file:
        for line in file:
            arr = line.rstrip().split(',')
    
    coord = { 0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1) }

    #find width and height
    minI,maxI = 0,0
    minJ,maxJ = 0,0
    posI,posJ = 0,0
    dir = 0
    for a in arr:
        nextDir,v = a[0],int(a[1:])
        if nextDir == 'R':
            dir = (dir+1)%4
        else:
            dir = (dir-1)%4

        nx,ny = coord[dir]
        posI += nx*v
        posJ += ny*v

        minI = min(minI,posI)
        maxI = max(maxI,posI)
        minJ = min(minJ,posJ)
        maxJ = max(maxJ,posJ)

    maxW,maxH = abs(minJ)+maxJ+1,abs(minI)+maxI+1
    sx,sy = abs(minI),abs(minJ)
    grid = [ [' ']*(maxW) for _ in range(maxH) ]

    #create grid
    grid[sx][sy] = 'S'
    currI,currJ = sx,sy
    dir = 0
    for a in arr:
        nextDir,v = a[0],int(a[1])
        if nextDir == 'R':
            dir = (dir+1)%4
        else:
            dir = (dir-1)%4

        nx,ny = coord[dir]
        while v > 0:
            currI += nx
            currI += ny
            grid[currI][currJ] = '#'
            v -= 1

    grid[currI][currJ] = 'E'

    #bfs to find goal
    def bfs(start):
        seen = set()
        q = deque([ (0,start) ])
        seen.add( start )
        while q:
            v,coord = q.popleft()
            x,y = coord
            #check goal
            if grid[x][y] == 'E':
                return v

            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny = x+dx,y+dy
                if 0<=nx<maxH and 0<=ny<maxW and grid[nx][ny] != '#' and (nx,ny) not in seen:
                    seen.add( (nx,ny) )
                    q.append( (v+1,(nx,ny)) )
    
    res = bfs((sx,sy))
    return res

def dayFifteen3():
    pass

def main():
    print("Hallo")
    #print(dayFifteen(), "ist die Lösung von Teil 1")
    print(dayFifteen2(), "ist die Lösung von Teil 2")
    #print(dayFifteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()