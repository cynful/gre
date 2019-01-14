#!/usr/bin/env python

import sys

def readinquiz(filename):
    with open(filename) as f:
        for line in f:
            l = line.strip()
            if l == "Q." or l == "A." or l == "S.":
                infolist = list()
                while line != '\n':
                    infolist.append(line.strip())
                    line = f.readline()
                print(infolist)

def main():    
    arg = sys.argv[1]
    readinquiz(arg)

if __name__ == '__main__':
    main()