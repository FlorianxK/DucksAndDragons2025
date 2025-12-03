from collections import deque
import heapq
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
    
    grid = { 0:"S" }
    d = 1j
    p = 0

    for a in arr:
        turn = a[0]
        size = int(a[1:])
        if turn == "R":
            d *= -1j
        else:
            d *= 1j

        for _ in range(size):
            p += d
            grid[p] = "#"
    grid[p] = "E"

    north = max(x.imag for x in grid)+1
    south = min(x.imag for x in grid)-1
    west = min(x.real for x in grid)-1
    east = max(x.real for x in grid)+1

    seen = {0}
    q = deque([(0,0)])
    while q:
        dist,curr = q.popleft()
        for n in [curr-1,curr+1,curr-1j,curr+1j]:
            if south <= n.imag <= north and west <= n.real <= east and n not in seen and grid.get(n) != '#':
                if grid.get(n) == "E":
                    return dist+1
                seen.add(n)
                q.append( (dist+1,n) )

def dayFifteen3():

    class Wall:
        def __init__(self,horizontal,start,end):
            self.horizontal = horizontal
            self.start = start
            self.end = end

    #read
    arr = []
    with open("Day15/15_3.txt", 'r') as file:
        for line in file:
            arr = line.rstrip().split(',')

    walls = []
    d = 1j
    p = 0
    poi_reals = set()
    poi_imags = set()

    for index,a in enumerate(arr):
        turn = a[0]
        size = int(a[1:])
        if turn == "R":
            d *= -1j
        else:
            d *= 1j

        end = p + d*size
        if index == len(arr)-1:
            end -= d

        walls.append( Wall(d in [-1,1], p+d, end) )
        p += d*size

        if d in [-1,1]:
            poi_imags |= {p.imag-1,p.imag,p.imag+1}
        else: 
            poi_reals |= {p.real-1,p.real,p.real+1}

    end = p

    poi_reals.add(end.real)
    poi_imags.add(end.imag)

    seen = set()
    h = [(0,0,0)]
    inc = 0
    while h:
        dist,_,curr = heapq.heappop(h)
        
        if curr == end:
            return int(dist)

        if curr in seen: continue
        seen.add(curr)

        for d in [1, -1, 1j, -1j]:
            horizontal = d in [1,-1]
            farthest = float("inf")
            wall: Wall
            for wall in walls:
                if horizontal:
                    if curr.imag < min(wall.start.imag, wall.end.imag): continue
                    if curr.imag > max(wall.start.imag, wall.end.imag): continue

                    if d == 1:
                        pt = min(wall.start.real,wall.end.real)
                        if pt > curr.real:
                            farthest = min( farthest, pt - curr.real - 1 )
                    else:
                        pt = max(wall.start.real,wall.end.real)
                        if pt < curr.real:
                            farthest = min( farthest, curr.real - pt - 1)

                else:
                    if curr.real < min(wall.start.real, wall.end.real): continue
                    if curr.real > max(wall.start.real, wall.end.real): continue

                    if d == 1j:
                        pt = min(wall.start.imag,wall.end.imag)
                        if pt > curr.imag:
                            farthest = min( farthest, pt - curr.imag - 1 )
                    else:
                        pt = max(wall.start.imag,wall.end.imag)
                        if pt < curr.imag:
                            farthest = min( farthest, curr.imag - pt - 1)

            if horizontal:
                for poi in poi_reals:
                    if d == 1 and poi <= curr.real or d == -1 and poi >= curr.real: continue
                    step = abs(poi-curr.real)
                    if step > farthest: continue
                    n = poi + curr.imag * 1j
                    if n in seen: continue
                    heapq.heappush(h, (dist+step,inc := inc+1,n) )
            else:
                for poi in poi_imags:
                    if d == 1j and poi <= curr.imag or d == -1j and poi >= curr.imag: continue
                    step = abs(poi-curr.imag)
                    if step > farthest: continue
                    n = curr.real + poi * 1j
                    if n in seen: continue
                    heapq.heappush(h, (dist+step,inc := inc+1,n) )

def main():
    print("Hallo")
    print(dayFifteen(), "ist die Lösung von Teil 1")
    print(dayFifteen2(), "ist die Lösung von Teil 2")
    print(dayFifteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()