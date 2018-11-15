#!/bin/python3

import os
import sys
import resource
from collections import defaultdict
sys.setrecursionlimit(100000)
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

def protectingBoston(n, cost, rds):
    """
    :type n: int
    :type cost: List[int]
    :type rds: Dict[List[int]]
    :rtype: int
    """


    def dfs(u, adj, stack):
        """
        :type u: int
        :type adj: Dict[List[int]]
        :type stack: List[int]
        :rtype: void
        """

        for v in adj[u]:
            if not visited[v-1]:
                visited[v-1] = True
                dfs(v, adj, stack)
        stack.append(u)


    def reverse(adj):
        """
        :type adj: Dict[List[int]]
        :rtype: Dict[List[int]]
        """

        adj_rev = defaultdict(list)
        for u in adj:
            for v in adj[u]:
                adj_rev[v].append(u)

        return adj_rev


    visited = [False] * n
    f_stack = []
    for u in range(1, n+1):
        if visited[u-1]:
            continue
        visited[u-1] = True
        dfs(u, rds, f_stack)

    rds_rev = reverse(rds)
    visited = [False] * n
    result = 0
    for i in range(-1, -n-1, -1):
        v = f_stack[i]
        if visited[v-1]:
            continue
        scc = []
        visited[v-1] = True
        dfs(v, rds_rev, scc)

        cur_min = cost[scc[0]-1]
        for i in scc[1:]:
            cur_min = min(cur_min, cost[i-1])
        result += cur_min

    return result



if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bld_cnt = int(input())
    cost = list(map(int, input().rstrip().split()))
    rd_cnt = int(input())
    rds = defaultdict(list)
    for i in range(rd_cnt):
        u, v = list(map(int, input().rstrip().split()))
        rds[u].append(v)

    result = protectingBoston(bld_cnt, cost, rds)

    fptr.write(str(result) + '\n')
    fptr.close()
