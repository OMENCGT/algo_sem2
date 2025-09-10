from typing import List, Tuple
import sys, time

def calc(n:int, a:float, b:float) -> bool:
    bb = b
    h_nm1 = (a + b * (n - 2)) / (n - 1) - (n - 2)
    print(h_nm1, bb)
    while n > 1 and h_nm1 < bb:
        nw = 2 * h_nm1 - bb + 2
        bb = h_nm1
        h_nm1 = nw
        n -= 1
        #print(nw)

    return bb > 0



def task2():
    n, a = map(float, input().split())
    n = int(n)
    cnt = 1000
    l = 0
    r = 10 ** 10
    while cnt > 0:
        print(l, r)
        m = (l + r) / 2
        if calc(n, a, m):
            r = m
        else:
            l = m
        cnt -= 1
    print(r)


#calc(692, 532.81, 10**8)
task2()
#calc(692, 532.81,446113.34434782615)
