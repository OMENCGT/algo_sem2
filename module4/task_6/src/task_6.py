import sys, time

def calc(a:str):
    n = len(a)
    l, r = 0, 0
    z = [0 for i in range(n)]

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < n and a[z[i]] == a[i + z[i]]:
            z[i] += 1

        if i + z[i] - 1 > r:
            r = i + z[i] - 1
            l = i

    return z

if __name__ == '__main__':
