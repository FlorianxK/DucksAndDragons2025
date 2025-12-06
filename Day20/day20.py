from collections import deque
from typing import *

def dayTwenty():
    #read
    arr = []
    with open("Day20/20_1.txt", 'r') as file:
        for line in file:
            arr.append(line.rstrip())

    m,n = len(arr),len(arr[0])

    top = [(-1,0),(0,-1),(0,1)]
    bot = [(1,0),(0,-1),(0,1)]
    pair = set()

    for i in range(m):
        switch = -1
        for j in range(n):
            if arr[i][j] == 'T':
                if switch == -1:
                    coord = top
                else:
                    coord = bot
                for dx,dy in coord:
                    nx,ny = dx+i,dy+j
                    if 0<=nx<m and 0<=ny<n:
                        if arr[nx][ny] == 'T':
                            a = (i,j)
                            b = (nx,ny)
                            t = (min(a,b),max(a,b))
                            if t not in pair:
                                pair.add( t )

            if arr[i][j] != '.':
                switch *= -1

    return len(pair)

def dayTwenty2():
    #read
    arr = []
    start = ()
    i = 0
    with open("Day20/20_2.txt", 'r') as file:
        for line in file:
            arr.append(line.rstrip())
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
            i += 1

    m,n = len(arr),len(arr[0])

    top = [(-1,0),(0,-1),(0,1)]
    bot = [(1,0),(0,-1),(0,1)]
    pair = set()

    legal = ['T','E','S']
    for i in range(m):
        switch = -1
        for j in range(n):
            if arr[i][j] in legal:
                if switch == -1:
                    coord = top
                else:
                    coord = bot
                for dx,dy in coord:
                    nx,ny = dx+i,dy+j
                    if 0<=nx<m and 0<=ny<n:
                        if arr[nx][ny] in legal:
                            a = (i,j)
                            b = (nx,ny)
                            t = (min(a,b),max(a,b))
                            if t not in pair:
                                pair.add( t )

            if arr[i][j] != '.':
                switch *= -1

    def bfs():
        seen = set()
        seen.add(start)
        q = deque([(start,0)])
        while True:
            nextQ = deque([])
            while q:
                coord,v = q.popleft()
                i,j = coord
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx,ny = dx+i,dy+j
                    #legal
                    if 0<=nx<m and 0<=ny<n:
                        a = (i,j)
                        b = (nx,ny)
                        t = (min(a,b),max(a,b))
                        if arr[nx][ny] == 'E' and t in pair:
                            return v+1
                        
                        elif arr[nx][ny] == 'T' and (nx,ny) not in seen:
                            #does pair exist
                            if t in pair:
                                seen.add( (nx,ny) )
                                nextQ.append( (b,v+1) )
            q = nextQ
            if not q:
                return -1
            
    res = bfs()
    return res

def dayTwenty3():
    #read
    board1 = []
    start = ()
    i = 0
    with open("Day20/20.txt", 'r') as file:
        for line in file:
            board1.append(line.rstrip().strip('.'))
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
            i += 1

    m,n = len(board1),len(board1[0])

    # von unten links bis oben rechts wird im neuen board oben links bis unten rechts

    board2 = []
    board3 = []

    top = [(-1,0),(0,-1),(0,1)]
    bot = [(1,0),(0,-1),(0,1)]
    pair = set()

    for a in board1:
        print(a)
    return

    #pairs between 1 and 2, 2 and 3, 3 and 1 for every move and bfs on pairs
    legal = ['T','E','S']
    for i in range(m):
        switch = -1
        for j in range(n):
            if board1[i][j] in legal:
                if switch == -1:
                    coord = top
                else:
                    coord = bot
                for dx,dy in coord:
                    nx,ny = dx+i,dy+j
                    if 0<=nx<m and 0<=ny<n:
                        if board1[nx][ny] in legal:
                            a = (i,j)
                            b = (nx,ny)
                            t = (min(a,b),max(a,b))
                            if t not in pair:
                                pair.add( t )

            if board1[i][j] != '.':
                switch *= -1

    def bfs():
        seen = set()
        seen.add(start)
        q = deque([(start,0)])
        while True:
            nextQ = deque([])
            while q:
                coord,v = q.popleft()
                i,j = coord
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx,ny = dx+i,dy+j
                    #legal
                    if 0<=nx<m and 0<=ny<n:
                        a = (i,j)
                        b = (nx,ny)
                        t = (min(a,b),max(a,b))
                        if board1[nx][ny] == 'E' and t in pair:
                            return v+1
                        
                        elif board1[nx][ny] == 'T' and (nx,ny) not in seen:
                            #does pair exist
                            if t in pair:
                                seen.add( (nx,ny) )
                                nextQ.append( (b,v+1) )
            q = nextQ
            if not q:
                return -1
            
    res = bfs()
    return res

def main():
    print("Hallo")
    print(dayTwenty(), "ist die Lösung von Teil 1")
    print(dayTwenty2(), "ist die Lösung von Teil 2")
    #print(dayTwenty3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()