import typing
from typing import Tuple, List, Dict
import sys, time


def dfs(target:int, v: int,used: List[bool], g: List[List[int]]) -> bool:
    if v == target:
        return True
    used[v] = True
    for i in g[v]:
        if not used[i]:
            if dfs(target, i, used, g):
                return True
    return False

def dist(p1:Tuple[int, int], p2:Tuple[int, int]) -> int:
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def mst(n:int, e: List[Tuple[int,int]], coords:Dict[int,Tuple[int, int]]) -> float:
    ans = 0
    e = sorted(e, key=lambda item: dist(coords[item[0]], coords[item[1]]))
    g = [[] for i in range (n)]
    for i in e:
        if not dfs(i[1], i[0], [False for i in range(n)],g):
            ans += dist(coords[i[1]], coords[i[0]]) ** 0.5
            g[i[0]].append(i[1])
            g[i[1]].append(i[0])

    return ans

def task18():
    n = int(input())
    coords = dict()
    e = []
    for i in range(n):
        x, y = map(int, input().split())
        coords[i] = (x, y)

    for i in range(n):
        for j in range(n):
            if i >= j:
                continue
            e.append((i, j))

    print(mst(n,e,coords))

if __name__ == '__main__':
    f = open("input.txt", "r")
    sys.stdin = f
    t_s = time.time_ns()
    task18()
    t_e = time.time_ns()
    print(f"total time: {(t_e - t_s) / (10 ** 9)} seconds")

