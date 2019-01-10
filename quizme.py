#!/usr/bin/env python

import sys

def whichquiz(filename):
    print(filename)

def main():    
    arg = sys.argv[1]
    whichquiz(arg)    

if __name__ == '__main__':
    main()