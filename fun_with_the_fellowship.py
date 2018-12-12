#!/bin/python3
import os
import sys


def dot(A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """

    M = 1000000007
    m = len(A)
    n = len(B[0])
    d = len(B)
    result = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(d):
                result[i][j] += (A[i][k] * B[k][j])
            result[i][j] %= M
    return result


def fun(a, b, c, d, n):
    """
    :type a: int
    :type b: int
    :type c: int
    :type d: int
    :type n: int
    :rtype: int
    """

    l = max(a, b, c, d)
    targets = [a, b, c, d]

    matrix = [[0 for _ in range(l)]]
    for i in range(l):
        if l - i in targets:
            matrix[0][i] = 1

    for i in range(1, l):
        row = [0] + matrix[i - 1][:-1]
        for j in range(l):
            row[j] += matrix[i - 1][-1] * matrix[0][j]
        matrix.append(row)

    ind = n % l
    result = matrix
    n //= l
    while n:
        if n % 2 == 1:
            result = dot(matrix, result)
        matrix = dot(matrix, matrix)
        n //= 2

    return result[ind][0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a, b, c, d, n = [int(i) for i in input().split()]
    result = fun(a, b, c, d, n)
    fptr.write(str(result) + '\n')
    fptr.close()
