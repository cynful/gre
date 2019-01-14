#!/usr/bin/env python

import sys

def getinfo(filename):
    infolist = list()
    line = filename.readline()
    while line.strip() != '\n':
        infolist.append(line.strip())
        line = filename.readline()
    print(infolist)

def readinquiz(filename):
    f = open(filename)
    for line in f:
        l = line.strip()
        if l == "Q." or l == "A." or l == "S.":
            infolist = list()
            while line != '\n':
                infolist.append(line.strip())
                line = f.readline()
            print(infolist)
    f.close()
    return

def main():    
    arg = sys.argv[1]
    readinquiz(arg)

if __name__ == '__main__':
    main()