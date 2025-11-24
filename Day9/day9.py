from collections import defaultdict
from itertools import combinations
from typing import *

def dayNine():
    #read
    dna = []
    with open("Day9/9_1.txt", 'r') as file:
        for line in file:
            l,r = line.rstrip().split(':')
            dna.append(r)
    n,m = len(dna[0]),len(dna)

    def findChild(dna):
        child = [1]*m
        for i in range(n):
            if dna[1][i] == dna[2][i] and dna[0][i] != dna[1][i]:
                child[0] = 0
            elif dna[0][i] == dna[2][i] and dna[1][i] != dna[0][i]:
                child[1] = 0
            elif dna[0][i] == dna[1][i] and dna[0][i] != dna[2][i]:
                child[2] = 0
        
        for i in range(m):
            if child[i] == 1:
                return i

    def compareChild(dna,childIndex):
        same = [0]*m
        for i in range(n):
            for j in range(m):
                if j == childIndex: continue
                if dna[childIndex][i] == dna[j][i]:
                    same[j] += 1
        res = 1
        for v in same:
            if v == 0: continue
            res *= v
        return res

    childI = findChild(dna)
    res = compareChild(dna,childI)
    return res

def dayNine2():
    #read
    dna = []
    with open("Day9/9_2.txt", 'r') as file:
        for line in file:
            l,r = line.rstrip().split(':')
            dna.append(r)
    n,m = len(dna[0]),len(dna)
    
    h = {}
    def findMatch(child,parent1,parent2):
        for i in range(n):
            if dna[child][i] != dna[parent1][i] and dna[child][i] != dna[parent2][i]:
                return False
        return True

    for child in range(m):
        for parent1 in range(m):
            for parent2 in range(m):
                if child == parent1 or child == parent2 or parent1 == parent2 or child in h: continue
                
                if findMatch(child,parent1,parent2):
                    h[child] = (parent1,parent2)

    def compare(child,parent1,parent2):
        p1,p2 = 0,0
        for i in range(n):
            if dna[child][i] == dna[parent1][i]:
                p1 += 1
            if dna[child][i] == dna[parent2][i]:
                p2 += 1
        return p1*p2

    res = 0
    for k,v in h.items():
        p1,p2 = v
        res += compare(k,p1,p2)
    return res

def dayNine3():
    #read

    dnas = {}
    with open("Day9/9.txt", 'r') as file:
        for line in file:
            l,r = line.rstrip().split(':')
            dnas[int(l)] = r

    def findMatch(child,parent1,parent2):
        for i in range(len(dnas[child])):
            if dnas[child][i] != dnas[parent1][i] and dnas[child][i] != dnas[parent2][i]:
                return False
        return True

    parent = {num: num for num in dnas}
    size = {num: 1 for num in dnas}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX, rootY = find(x), find(y)
        if rootX == rootY:
            return
        if size[rootX] < size[rootY]:
            rootX, rootY = rootY, rootX
        parent[rootY] = rootX
        size[rootX] += size[rootY]

    for num1, num2, num3 in combinations(dnas, 3):
        if findMatch(num1, num2, num3) or findMatch(num2, num1, num3) or findMatch(num3, num1, num2):
            union(num1, num2)
            union(num1, num3)

    groups = defaultdict(list)
    for num in dnas:
        groups[find(num)].append(num)

    return sum(max(groups.values(), key=len))

def main():
    print("Hallo")
    print(dayNine(), "ist die Lösung von Teil 1")
    print(dayNine2(), "ist die Lösung von Teil 2")
    print(dayNine3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()