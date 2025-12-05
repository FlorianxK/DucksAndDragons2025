from typing import *

def dayEighteen():
    #read
    score = {}
    thickness = {}
    node = 0
    first = True
    with open("Day18/18_1.txt", 'r') as file:
        for line in file:
            if line == '\n':
                if score[node] < thickness[node]:
                    score[node] = 0
                first = True
                continue

            if first:
                line = line[:len(line)-2]
                t = line.split(' ')
                node = int(t[1])
                ownthic = int(t[-1])
                thickness[node] = ownthic
                score[node] = 0
                first = False
            else:
                line = line.rstrip()
                t = line.split(' ')
                if t[1] == "free":
                    score[node] += 1
                else:
                    to = int(t[4])
                    thic = int(t[-1])
                    score[node] += score[to]*thic

    if score[node] < thickness[node]:
        score[node] = 0
    return score[node]
    
def dayEighteen2():
    score = {}
    thickness = {}
    res = 0
    #read
    with open("Day18/18_2.txt", 'r') as file:
        test = file.read()
        plants,cases = test.split("\n\n\n")
        rows = plants.split("\n\n")

    for case in cases.splitlines():
        arr = [int(x) for x in case.split()]
        arrIndex = 0
        for i,row in enumerate(rows):
            lines = row.splitlines()
            line = lines[0]
            line = line[:len(line)-1]
            t = line.split(' ')
            node = int(t[1])
            ownthic = int(t[-1])
            thickness[node] = ownthic
            score[node] = 0

            for line in lines[1:]:
                t = line.split(' ')
                if t[1] == "free":
                    score[node] += arr[arrIndex]
                    arrIndex += 1
                else:
                    to = int(t[4])
                    thic = int(t[-1])
                    score[node] += score[to]*thic
            if score[node] < thickness[node]:
                score[node] = 0
            if i == len(rows)-1:
                res += score[node]
    return res

def dayEighteen3():
    score = {}
    thickness = {}
    res = 0
    #read
    with open("Day18/18_3.txt", 'r') as file:
        test = file.read()
        plants,cases = test.split("\n\n\n")
        rows = plants.split("\n\n")

    free = set()
    good = set()
    bad = set()
    for i,row in enumerate(rows):
        lines = row.splitlines()
        line = lines[0]
        line = line[:len(line)-1]
        t = line.split(' ')
        node = int(t[1])
        ownthic = int(t[-1])

        for line in lines[1:]:
            t = line.split(' ')
            if t[1] == "free":
                free.add(node)
            else:
                to = int(t[4])
                thic = int(t[-1])
                if to in free:
                    if thic > 0:
                        good.add(to)
                    else:
                        bad.add(to)

    best = 0
    for i,row in enumerate(rows):
        lines = row.splitlines()
        line = lines[0]
        line = line[:len(line)-1]
        t = line.split(' ')
        node = int(t[1])
        ownthic = int(t[-1])
        thickness[node] = ownthic
        score[node] = 0

        for line in lines[1:]:
            t = line.split(' ')
            if t[1] == "free":
                if node in good:
                    score[node] = 1
                else:
                    score[node] = 0
            else:
                to = int(t[4])
                thic = int(t[-1])
                if to in free:
                    if thic > 0:
                        good.add(to)
                    else:
                        bad.add(to)

                score[node] += score[to]*thic
                
        if score[node] < thickness[node]:
            score[node] = 0
        if i == len(rows)-1:
            best = max(best,score[node])

    res = 0
    for case in cases.splitlines():
        arr = [int(x) for x in case.split()]
        arrIndex = 0
        for i,row in enumerate(rows):
            lines = row.splitlines()
            line = lines[0]
            line = line[:len(line)-1]
            t = line.split(' ')
            node = int(t[1])
            ownthic = int(t[-1])
            thickness[node] = ownthic
            score[node] = 0

            for line in lines[1:]:
                t = line.split(' ')
                if t[1] == "free":
                    score[node] += arr[arrIndex]
                    arrIndex += 1
                else:
                    to = int(t[4])
                    thic = int(t[-1])
                    score[node] += score[to]*thic
            
            if score[node] < thickness[node]:
                score[node] = 0
            if i == len(rows)-1:
                if score[node] > 0:
                    res += best-score[node]
    return res

def main():
    print("Hallo")
    print(dayEighteen(), "ist die Lösung von Teil 1")
    print(dayEighteen2(), "ist die Lösung von Teil 2")
    print(dayEighteen3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()