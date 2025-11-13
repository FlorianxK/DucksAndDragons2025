from typing import *

def dayFive():
    #read
    id = 0
    arr = []

    with open("Day5/5_1.txt", 'r') as file:
        for line in file:
            l,r = line.rstrip().split(':')
            id = int(l)
            arr = [int(x) for x in r.split(',')]

    fish = []
    res = ""
    for v in arr:
        for segment in fish:
            if v < segment[1] and segment [0] is None:
                segment[0] = v
                break
            if v > segment[1] and segment [2] is None:
                segment[2] = v
                break
        else:
            res += str(v)
            fish.append([None,v,None])
    return res

def dayFive2():
    #read
    id = 0
    arr = []
    swords = {}

    with open("Day5/5_2.txt", 'r') as file:
        for line in file:
            l,r = line.rstrip().split(':')
            id = int(l)
            arr = [int(x) for x in r.split(',')]
            swords[id] = arr

    def makeFish(arr:List[int]) -> str:
        fish = []
        res = ""
        for v in arr:
            for segment in fish:
                if v < segment[1] and segment [0] is None:
                    segment[0] = v
                    break
                if v > segment[1] and segment [2] is None:
                    segment[2] = v
                    break
            else:
                res += str(v)
                fish.append([None,v,None])
        return res

    weakest = float('inf')
    strongest = float('-inf')
    for v in swords.values():
        rating = int(makeFish(v))
        weakest = min(weakest,rating)
        strongest = max(strongest,rating)

    return strongest-weakest

def dayFive3():
    #read
    id = 0
    arr = []
    swords = {}

    with open("Day5/5_3.txt", 'r') as file:
        for line in file:
            l,r = line.rstrip().split(':')
            id = int(l)
            arr = [int(x) for x in r.split(',')]
            swords[id] = arr

    def makeFish(arr:List[int]) -> str:
        fish = []
        res = ""
        for v in arr:
            for segment in fish:
                if v < segment[1] and segment [0] is None:
                    segment[0] = v
                    break
                if v > segment[1] and segment [2] is None:
                    segment[2] = v
                    break
            else:
                res += str(v)
                fish.append([None,v,None])
        return int(res),fish

    fullCon = []
    for k,v in swords.items():
        rating,temp = makeFish(v)
        levels = []
        for t in temp:
            s = ""
            for v in t:
                if v is not None:
                    s += str(v)
            levels.append(int(s))

        fullCon.append([rating,levels,k])

    fullCon.sort(reverse=True)
     
    res = 0
    index = 1
    for r,l,k in fullCon:
        res += index*k
        index += 1
    return res

def main():
    print("Hallo")
    print(dayFive(), "ist die Lösung von Teil 1")
    print(dayFive2(), "ist die Lösung von Teil 2")
    print(dayFive3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()