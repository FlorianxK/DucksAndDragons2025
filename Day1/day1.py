from typing import *

def dayOne():
    names = []
    rules = []
    #read
    first = True
    with open("Day1/1_2.txt", 'r') as file:
        for line in file:
            if line == '\n':
                first = False
                continue
            line = line.rstrip()
            if first:
                names = line.split(',')
            else:
                rules = line.split(',')
      
    i = 0
    n = len(names)
    for r in rules:
        v = int(r[1:])
        if r[0] == 'L':
            v *= -1
        i += v
        if i < 0:
            i = 0
        elif i >= n:
            i = n-1

    return names[i]

def dayOne2():
    names = []
    rules = []
    #read
    first = True
    with open("Day1/1_3.txt", 'r') as file:
        for line in file:
            if line == '\n':
                first = False
                continue
            line = line.rstrip()
            if first:
                names = line.split(',')
            else:
                rules = line.split(',')
      
    i = 0
    n = len(names)
    for r in rules:
        v = int(r[1:])
        if r[0] == 'L':
            v *= -1
        i = (i+v)%n
    return names[i]

def dayOne3():
    names = []
    rules = []
    #read
    first = True
    with open("Day1/1_4.txt", 'r') as file:
        for line in file:
            if line == '\n':
                first = False
                continue
            line = line.rstrip()
            if first:
                names = line.split(',')
            else:
                rules = line.split(',')

    n = len(names)
    for r in rules:
        v = int(r[1:])
        if r[0] == 'L':
            i = n-v
        else:
            i = v
        names[0],names[i%n] = names[i%n],names[0]
    return names[0]

def main():
    print("Hallo")
    print(dayOne(), "ist die Lösung von Teil 1")
    print(dayOne2(), "ist die Lösung von Teil 2")
    print(dayOne3(), "ist die Lösung von Teil 3")

if __name__=="__main__":
    main()