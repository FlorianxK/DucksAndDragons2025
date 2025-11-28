from collections import deque
import heapq
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
    h = []
    i = 0
    with open("Day12/12.txt", 'r') as file:
        for line in file:
            line = line.rstrip()
            arr.append(list(line))
            for j in range(len(line)):
                v = int(line[j])
                heapq.heappush(h, (-v,(i,j)) )
            i += 1
    m,n = len(arr),len(arr[0])
    seen = set()

    def explode(i,j):
        res = 1
        seen.add( (i,j) )
        q = deque([(i,j)])
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

    full = 0

    for _ in range(3):
        temp = h.copy()
        maxRes = 0
        el = None
        while True:
            v,cord = heapq.heappop(temp)
            res = explode(*cord)
            if res < maxRes:
                break
            else:
                maxRes = res
                el = (v,cord)
        h.remove(el)
        full += maxRes
    return full

def main():
    print("Hallo")
    #print(dayTwelve(), "ist die Lösung von Teil 1")
    #print(dayTwelve2(), "ist die Lösung von Teil 2")
    print(dayTwelve3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()