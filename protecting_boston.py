#!/bin/python3

import os
import sys

def protectingBoston(cost, rds):
    pass

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bld_cnt = int(input())
    cost = list(map(int, input().rstrip().split()))

    rds = {}
    for bld in range(bld_cnt):
        rds[bld+1] = []

    rd_cnt = int(input())
    for i in range(rd_cnt):
        u, v = list(map(int, input().rstrip().split()))
        rds[u].append(v)

    result = protectingBoston(cost, rds)

    fptr.write(str(result) + '\n')
    fptr.close()
