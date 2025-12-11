from collections import defaultdict, deque
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
    with open("Day20/20_3.txt", 'r') as file:
        for line in file:
            board1.append(list(line.rstrip()))
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
            i += 1
    m,n = len(board1),len(board1[0])

    def board120(board):
        newBoard = [['.']*n for _ in range(m)]
        t = []
        c = 0
        ni,nj = 0,0
        s1,s2 = start
        while s1 >= 0:
            line = []
            i,j = s1,s2
            # one line
            while i >= 0:
                line.append(board[i][j])
                i-=1
                j+=1

            # change start point
            if c % 2 == 0:
                s1 -= 1
            else:
                s2 -= 1
            c += 1

            t.append(line)
            # line on new board
            i,j = ni,nj
            for v in line:
                newBoard[i][j] = v
                i+=1
                j+=1
            nj+=1
        return newBoard

    board2 = board120(board1)
    board3 = board120(board2)
    grids = [board1,board2,board3]

    top = [(-1,0),(0,-1),(0,1)]
    bot = [(1,0),(0,-1),(0,1)]

    def neighbour(i,j):
        # + if True bot and - if False top
        if (i + j) & 1 == 1:
            coord = bot
        else:
            coord = top

        res = []
        for dx,dy in coord:
            nx,ny = i+dx,j+dy
            if 0 <= nx < m and nx <= ny <= n-1-nx:
                res.append((nx, ny))
        return res

    def neighbours3(i, j, s):
        return [(nx, dy, (s+1)%3) for nx, dy in ([(i, j)] + neighbour(i, j))]

    def bfs(start):
        dist = defaultdict(lambda: float("inf"), {start: 0})
        todo = [start]
        for i, j, s in todo:
            if grids[s][i][j] == "E":
                return dist[i, j, s]
            for rn, cn, sn in neighbours3(i, j, s):
                if grids[sn][rn][cn] in "TSE" and dist[rn, cn, sn] == float("inf"):
                    dist[rn, cn, sn] = dist[i, j, s] + 1
                    todo.append((rn, cn, sn))
        return float("inf")

    res = bfs( (*start,0) )
    return res

def main():
    print("Hallo")
    print(dayTwenty(), "ist die Lösung von Teil 1")
    print(dayTwenty2(), "ist die Lösung von Teil 2")
    print(dayTwenty3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()