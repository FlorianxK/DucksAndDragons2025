import heapq
from typing import *

def daySeventeen():
    #read
    arr = []
    with open("Day17/17_1.txt", 'r') as file:
        for line in file:
            arr.append(list(line.rstrip()))

    m,n = len(arr),len(arr[0])
    radius = 10
    vr,vc = m//2,n//2
    res = 0
    for i in range(m):
        for j in range(n):
            if (i,j) != (vr,vc):
                if (vr - i) * (vr - i) + (vc - j) * (vc - j) <= radius**2:
                    res += int(arr[i][j])
    return res

def daySeventeen2():
    #read
    arr = []
    full = 0
    with open("Day17/17_2.txt", 'r') as file:
        for line in file:
            for v in line:
                if v.isnumeric():
                    full += int(v)
            arr.append(list(line.rstrip()))

    m,n = len(arr),len(arr[0])
    vr,vc = m//2,n//2
    destruct = []
    level = 1
    while full > 0:
        curr = 0
        for i in range(m):
            for j in range(n):
                if (i,j) != (vr,vc):
                    if (vr - i) * (vr - i) + (vc - j) * (vc - j) <= level**2:
                        if arr[i][j].isnumeric():
                            curr += int(arr[i][j])
                            arr[i][j] = '.'
        destruct.append( (curr,level) )
        full -= curr
        level += 1
    pair = max(destruct)
    return pair[0]*pair[1]

def daySeventeen3():
    #read
    arr = []
    i = 0
    start = ()
    volcano = ()
    full = 0
    with open("Day17/17_3.txt", 'r') as file:
        for line in file:
            line = line.rstrip()
            for j in range(len(line)):
                if line[j] == 'S':
                    start = (i,j)
                elif line[j] == '@':
                    volcano = (i,j)
                elif line[j].isnumeric():
                    full += int(line[j])
            i += 1
            arr.append(list(line))
    m,n = len(arr),len(arr[0])
    vr,vc = volcano

    def solve_dijkstra(min_radius):
        pq = [(0, start[0], start[1], 0)]
        min_costs = {} 
        min_costs[(start[0], start[1], 0)] = 0
        
        limit_sq = min_radius * min_radius
        cost_limit = 30 * (min_radius + 1)

        while pq:
            cost, r, c, phase = heapq.heappop(pq)

            if cost > cost_limit:
                return float('inf')
            if (r, c, phase) == (start[0], start[1], 1):
                return cost
            if cost > min_costs.get((r, c, phase), float('inf')):
                continue

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < m):
                    continue
                n_phase = phase
                if nc < vc:
                    if r < vr <= nr:
                        n_phase = 1
                    elif nr < vr <= r:
                        n_phase = 0
                if (nr - vr)**2 + (nc - vc)**2 <= limit_sq:
                    continue

                if arr[nr][nc].isnumeric():
                    val = int(arr[nr][nc])
                else:
                    val = 0
                new_cost = cost + val
                state = (nr, nc, n_phase)
                if new_cost < min_costs.get(state, float('inf')):
                    min_costs[state] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc, n_phase))

        return float('inf')

    level = 1
    while full > 0:
        curr = 0
        for i in range(m):
            for j in range(n):
                if (i,j) != (vr,vc):
                    if (vr - i) * (vr - i) + (vc - j) * (vc - j) <= level**2:
                        if arr[i][j].isnumeric():
                            curr += int(arr[i][j])
                            arr[i][j] = '.'
        full -= curr

        #look for possible loop
        res = solve_dijkstra(level)
        if res != float('inf'):
            return res*level

        #next level
        level += 1

def main():
    print("Hallo")
    print(daySeventeen(), "ist die Lösung von Teil 1")
    print(daySeventeen2(), "ist die Lösung von Teil 2")
    print(daySeventeen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()