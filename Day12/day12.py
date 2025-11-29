from collections import deque
from copy import deepcopy
from typing import *

def dayTwelve():
    #read
    arr = []
    with open("Day12/12_1.txt", 'r') as file:
        for line in file:
            arr.append(list(line.rstrip()))
    m,n = len(arr),len(arr[0])
    res = 1
    seen = set()
    seen.add( (0,0) )
    q = deque([(0,0)])
    while q:
        x,y = q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx,y+dy
            #false
            if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx,ny) in seen or int(arr[nx][ny]) > int(arr[x][y]): continue

            seen.add( (nx,ny) )
            q.append( (nx,ny) )
            res += 1
    return res

def dayTwelve2():
    #read
    arr = []
    with open("Day12/12_2.txt", 'r') as file:
        for line in file:
            arr.append(list(line.rstrip()))
    m,n = len(arr),len(arr[0])
    res = 2
    seen = set()
    seen.add( (0,0) )
    seen.add( (m-1,n-1) )
    q = deque([(0,0),(m-1,n-1)])
    while True:
        nextQ = deque([])
        while q:
            x,y = q.popleft()
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny = x+dx,y+dy
                #false
                if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx,ny) in seen or int(arr[nx][ny]) > int(arr[x][y]): continue

                seen.add( (nx,ny) )
                nextQ.append( (nx,ny) )
                res += 1
        q = nextQ
        if not q:
            break
    return res

def dayTwelve3():
    #read
    arr = []
    with open("Day12/12_3.txt", 'r') as file:
        for line in file:
            line = line.rstrip()
            arr.append(list(line))
    m,n = len(arr),len(arr[0])

    def explode(i,j,seen):
        nextSeen = deepcopy(seen)
        q = deque([(i,j)])

        while q:
            x,y = q.popleft()
            if 0<=x<=m and 0<=y<=n:
                if (x,y) in nextSeen: continue
                nextSeen.add( (x,y) )
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and int(arr[nx][ny]) <= int(arr[x][y]):
                        q.append( (nx,ny) )
        return nextSeen

    seen = set()
    for t in range(3):
        best = None
        for i in range(m):
            for j in range(n):
                seen1 = explode(i,j,seen)
                if best is None or len(seen1) > len(best[0]):
                    best = (seen1,(i,j))
        seen |= best[0]
        #print(t, best[1],len(seen))
    return len(seen)

def main():
    print("Hallo")
    print(dayTwelve(), "ist die Lösung von Teil 1")
    print(dayTwelve2(), "ist die Lösung von Teil 2")
    print(dayTwelve3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()