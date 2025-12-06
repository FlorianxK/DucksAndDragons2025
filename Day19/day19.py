from collections import defaultdict
from functools import cache
import math
from typing import *

def dayNineteen():
    #read
    arr = []
    with open("Day19/19_1.txt", 'r') as file:
        for line in file:
            arr.append( [int(x) for x in line.rstrip().split(',')] )
    n = len(arr)
    flaps = 0
    pos = 0
    height = 0

    for i in range(n):
        minh = 0
        nextPos = arr[i][0]
        for x,h,_ in arr[i:]:
            minh = max( minh, h-(x-nextPos) )
        
        neededH = int( math.ceil((minh-height + nextPos-pos)/2) )
        sprint = max(0,neededH)
        flaps += sprint
        height += sprint - (nextPos-pos-sprint)
        pos = nextPos

    return flaps

def dayNineteen2():
    walls = defaultdict(list)

    with open("Day19/19_2.txt", 'r') as file:
        for line in file:
            x,h,opening = [int(x) for x in line.rstrip().split(',')]
            walls[x].append((h,opening))

    @cache
    def dfs(currPos,currHeight):
        futurePos = sorted(pos for pos in walls if pos > currPos)
        if len(futurePos) == 0: return 0
        nextPos = futurePos[0]
        futurePos = futurePos[1:]

        best = float("inf")
        for height,opening in walls[nextPos]:
            minh = height
            maxh = height+opening-1
            for pos in futurePos:
                lh,_ = min(walls[pos])
                hh,ho = max(walls[pos])
                minh = max(minh, lh-(pos-nextPos) )
                maxh = min(maxh, hh+ho-1+(pos-nextPos) )
            neededminH = int( math.ceil((minh-currHeight + nextPos-currPos)/2) )
            minsprint = max(0,neededminH)
            neededmaxH = (maxh-currHeight + nextPos-currPos)//2
            maxsprint = max(0,neededmaxH)
            for sprint in range(minsprint,maxsprint+1):
                newHeight = currHeight + sprint - (nextPos-currPos-sprint)
                best = min( best, sprint+dfs(nextPos,newHeight) )

        return best

    return dfs(0,0)
    
def dayNineteen3():
    walls = defaultdict(list)

    with open("Day19/19_3.txt", 'r') as file:
        for line in file:
            x,h,opening = [int(x) for x in line.rstrip().split(',')]
            walls[x].append((h,opening))

    @cache
    def dfs(currPos,currHeight):
        futurePos = sorted(pos for pos in walls if pos > currPos)
        if len(futurePos) == 0: return 0
        nextPos = futurePos[0]
        futurePos = futurePos[1:]

        best = float("inf")

        global_minh = 0
        global_maxh = float("inf")

        for pos in futurePos:
            lh,_ = min(walls[pos])
            hh,ho = max(walls[pos])
            global_minh = max(global_minh, lh-(pos-nextPos) )
            global_maxh = min(global_maxh, hh+ho-1+(pos-nextPos) )

        for height,opening in walls[nextPos]:
            minh = max(global_minh,height)
            maxh = min(global_maxh,height+opening-1)

            neededminH = int( math.ceil((minh-currHeight + nextPos-currPos)/2) )
            minsprint = max(0,neededminH)
            neededmaxH = (maxh-currHeight + nextPos-currPos)//2
            maxsprint = max(0,neededmaxH)

            for sprint in range(minsprint,maxsprint+1):
                newHeight = currHeight + sprint - (nextPos-currPos-sprint)
                best = min( best, sprint+dfs(nextPos,newHeight) )

        return best

    return dfs(0,0)

def main():
    print("Hallo")
    print(dayNineteen(), "ist die Lösung von Teil 1")
    print(dayNineteen2(), "ist die Lösung von Teil 2")
    print(dayNineteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()