from typing import List, Tuple
import sys, time

def in_order(g: List[Tuple[int, int, int]], v:int):
    if g[v][1] > -1:
        in_order(g, g[v][1])
    print(g[v][0], end=' ')
    if g[v][2] > -1:
        in_order(g, g[v][2])

def pre_order(g: List[Tuple[int, int, int]], v:int):
    print(g[v][0], end=' ')
    if g[v][1] > -1:
        pre_order(g, g[v][1])
    if g[v][2] > -1:
        pre_order(g, g[v][2])

def post_order(g: List[Tuple[int, int, int]], v:int):
    if g[v][1] > -1:
        post_order(g, g[v][1])
    if g[v][2] > -1:
        post_order(g, g[v][2])
    print(g[v][0], end=' ')

def task1():
    sys.setrecursionlimit(200000)
    n = int(input())
    a = [tuple(map(int, input().split())) for i in range(n)]
    in_order(a, 0)
    print()
    pre_order(a, 0)
    print()
    post_order(a, 0)
    print()


if __name__ == '__main__':
    f = open("input.txt", "r")
    f1 = open("output.txt", "w")
    sys.stdout = f1
    sys.stdin = f
    t_s = time.time_ns()
    task1()
    t_e = time.time_ns()
    print(f"total time: {(t_e - t_s) / (10 ** 9)} seconds")
