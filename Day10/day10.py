from collections import deque
from functools import cache
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
    res = []
    #read
    arr = []
    sheep = set()
    with open("Day10/10_2.txt", 'r') as file:
        i = 0
        for line in file:
            for j in range(len(line)):
                if line[j] == 'S':
                    sheep.add( (i,j) )
            i += 1
            arr.append(list(line.rstrip()))

    m,n = len(arr),len(arr[0])
    dragon = (m//2,n//2)
    level = set([dragon])
    move = 1
    while move <= moves:
        eaten = 0
        nextLevel = set()
        while level:
            x,y = level.pop()
            for dx,dy in [(2,-1),(2,1),(-2,-1),(-2,1),(1,2),(-1,2),(1,-2),(-1,-2)]:
                nx,ny = x+dx,y+dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                nextLevel.add( (nx,ny) )
                if (nx,ny) in sheep and arr[nx][ny] != '#':
                    eaten += 1
                    sheep.remove( (nx,ny) )
        
        #move sheep
        nextSheep = set()
        for x,y in sheep:
            nx = x+1
            if nx >= m: continue
            if (nx,y) in nextLevel and arr[nx][y] != '#':
                eaten += 1
            else:
                nextSheep.add( (nx,y) )

        sheep = nextSheep
        level = nextLevel
        res.append(eaten)
        move += 1

    return sum(res)

def dayTen3():
    #read
    arr = []
    sheep = []
    dragon = (0,0)
    with open("Day10/10_3.txt", 'r') as file:
        i = 0
        for line in file:
            for j in range(len(line)):
                if line[j] == 'S':
                    sheep.append( (i,j) )
                elif line[j] == 'D':
                    dragon = (i,j)
            i += 1
            arr.append(list(line.rstrip()))

    m,n = len(arr),len(arr[0])
    sheep = tuple(sheep)

    @cache
    def count(sheep,dragon,turn="sheep"):
        if turn == "sheep":
            if len(sheep):
                total = 0
                moved = 0
                for i, (x,y) in enumerate(sheep):
                    #escape
                    if x == m-1:
                        moved += 1
                    elif arr[x+1][y] == '#' or dragon != (x+1,y):
                        moved += 1
                        nextSheep = (*sheep[:i],(x+1,y),*sheep[i+1:])
                        total += count( nextSheep,dragon,turn="dragon" )
                if moved == 0: return count(sheep,dragon,turn="dragon")
                return total
            else:
                return 1
        if turn == "dragon":
            total = 0
            for dx,dy in [(2,-1),(2,1),(-2,-1),(-2,1),(1,2),(-1,2),(1,-2),(-1,-2)]:
                x,y = dragon
                nx,ny = x+dx,y+dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
                nextSheep = tuple( (sx,sy) for sx,sy in sheep if arr[sx][sy] == '#' or (sx,sy) != (nx,ny) )
                total += count( nextSheep , (nx,ny) , turn="sheep" )
            return total

    return count(sheep,dragon)
    
def main():
    print("Hallo")
    print(dayTen(), "ist die Lösung von Teil 1")
    print(dayTen2(), "ist die Lösung von Teil 2")
    print(dayTen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()