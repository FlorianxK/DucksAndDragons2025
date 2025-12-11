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

    top = [(-1,0),(0,-1),(0,1)]
    bot = [(1,0),(0,-1),(0,1)]

    moves12 = set()
    moves23 = set()
    moves31 = set()

    def neighbour(i,j,board):
        legal = ['T','E','S']
        res = []
        # + if True bot and - if False top
        if (i + j) & 1 == 1:
            coord = bot
        else:
            coord = top
        
        for dx,dy in coord:
            nx,ny = dx+i,dy+j
            if 0<=nx<m and 0<=ny<n:
                if board[nx][ny] in legal:
                    res.append((nx,ny))
        return res

    def verify(i,j,b1,b2,switch):
        v = 0
        if b1 == 1 and b2 == 2:
            pBoard1,pBoard2 = board1,board2
            v = 1
        if b1 == 2 and b2 == 3:
            pBoard1,pBoard2 = board2,board3
            v = 2
        if b1 == 3 and b2 == 1:
            pBoard1,pBoard2 = board3,board1
            v = 3

        if pBoard1[i][j] in legal:
            if switch == -1:
                coord = top
            else:
                coord = bot
            for dx,dy in coord:
                nx,ny = dx+i,dy+j
                if 0<=nx<m and 0<=ny<n:
                    if pBoard2[nx][ny] in legal:
                        a = (i,j)
                        b = (nx,ny)
                        t = (min(a,b),max(a,b))
                        if v == 1:
                            if t not in moves12:
                                moves12.add( t )
                        elif v == 2:
                            if t not in moves23:
                                moves23.add( t )
                        elif v == 3:
                            if t not in moves31:
                                moves31.add( t )        

    #pairs between 1 and 2, 2 and 3, 3 and 1 for every move and bfs on pairs
    legal = ['T','E','S']
    for i in range(m):
        switch = -1
        for j in range(n):
            verify(i,j,1,2,switch)
            verify(i,j,2,3,switch)
            verify(i,j,3,1,switch)
            if board1[i][j] != '.':
                switch *= -1

    path = []
    def bfs():
        seen = set()
        seen.add(start)
        q = deque([(start,0,0)])
        #currRot 0,1,2%3
        # CURR ROT IN DEQUE DURCHGEBEN WEIL JEDE MUSS SELBER GUCKEN
        while True:
            nextQ = deque([])
            while q:
                coord,v,currRot = q.popleft()
                i,j = coord
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx,ny = dx+i,dy+j
                    #legal
                    if 0<=nx<m and 0<=ny<n:
                        a = (i,j)
                        b = (nx,ny)
                        t = (min(a,b),max(a,b))
                        if currRot == 0:
                            if board2[nx][ny] == 'E' and t in moves12:
                                return v+1
                            elif board2[nx][ny] == 'T' and (nx,ny) not in seen:
                                if t in moves12:
                                    seen.add( (nx,ny) )
                                    path.append( ((nx,ny),(currRot+1)%3) )
                                    nextQ.append( (b,v+1,(currRot+1)%3) )

                        elif currRot == 1:
                            if board3[nx][ny] == 'E' and t in moves23:
                                return v+1
                            elif board3[nx][ny] == 'T' and (nx,ny) not in seen:
                                if t in moves23:
                                    seen.add( (nx,ny) )
                                    path.append( ((nx,ny),(currRot+1)%3) )
                                    nextQ.append( (b,v+1,(currRot+1)%3) )

                        if currRot == 2:
                            if board1[nx][ny] == 'E' and t in moves31:
                                return v+1
                            elif board1[nx][ny] == 'T' and (nx,ny) not in seen:
                                if t in moves31:
                                    seen.add( (nx,ny) )
                                    path.append( ((nx,ny),(currRot+1)%3) )
                                    nextQ.append( (b,v+1,(currRot+1)%3) )
            q = nextQ
            if not q:
                print(path)
                return -1

    res = bfs()
    return res

def main():
    print("Hallo")
    #print(dayTwenty(), "ist die Lösung von Teil 1")
    #print(dayTwenty2(), "ist die Lösung von Teil 2")
    print(dayTwenty3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()