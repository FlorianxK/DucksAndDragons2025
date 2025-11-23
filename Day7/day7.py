from collections import defaultdict
from typing import *

def daySeven():
    #read
    arr = []
    d = defaultdict(list[str])
    first = True
    with open("Day7/7_1.txt", 'r') as file:
        for line in file:
            if line == '\n':
                first = False
                continue
            line = line.rstrip()
            if first:
                arr = line.split(',')
            else:
                l,r = line.split(" > ")
                d[l] = r.split(',')

    for name in arr:
        i = 0
        while i != len(name)-1:
            if name[i+1] in d[name[i]]:
                i += 1
            else:
                break
        if i == len(name)-1:
            return name

def daySeven2():
    #read
    arr = []
    d = defaultdict(list[str])
    first = True
    with open("Day7/7_2.txt", 'r') as file:
        for line in file:
            if line == '\n':
                first = False
                continue
            line = line.rstrip()
            if first:
                arr = line.split(',')
            else:
                l,r = line.split(" > ")
                d[l] = r.split(',')

    index = 1
    res = 0
    for name in arr:
        i = 0
        while i != len(name)-1:
            if name[i+1] in d[name[i]]:
                i += 1
            else:
                break
        if i == len(name)-1:
            res += index

        index += 1
    return res

def daySeven3():
    #read
    temp = []
    d = defaultdict(list[str])
    first = True
    with open("Day7/7_3.txt", 'r') as file:
        for line in file:
            if line == '\n':
                first = False
                continue
            line = line.rstrip()
            if first:
                temp = line.split(',')
            else:
                l,r = line.split(" > ")
                d[l] = r.split(',')

    names = []
    #sort out wrong names
    for name in temp:
        correct = True
        for i in range(len(name)-1):
            if name[i+1] not in d[name[i]]:
                correct = False
                break
        if correct:
            names.append(name)

    def add_letters(name: str) -> set[str]:
        names = set()
        if 7 <= len(name) <= 11:
            names.add(name)
        if len(name) == 11:
            return names

        for letter in d.get(name[-1], []):
            names |= add_letters(name + letter)

        return names

    total_names = set()
    for prefix in names:
        total_names |= add_letters(prefix)

    return len(total_names)

def main():
    print("Hallo")
    print(daySeven(), "ist die Lösung von Teil 1")
    print(daySeven2(), "ist die Lösung von Teil 2")
    print(daySeven3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()