import tracemalloc
import sys
import time

def task_18_dp():
    n = int(input())
    a = [int(input()) for i in range(n)]
    dp = [[[10 ** 9 for i in range(111)] for j in range(111)] for k in range(111)]
    p = [[[0 for i in range(111)] for j in range(111)] for k in range(111)]

    dp[0][a[0] >= 100][0] = a[0]
    for i in range(1, n):
        for j in range(n + 2):
            for k in range(n + 2):
                if k > 0 and dp[i][j][k] >= dp[i - 1][j + 1][k - 1]:
                    dp[i][j][k] = dp[i - 1][j + 1][k - 1]
                    p[i][j][k] = 0
                if dp[i][j + (a[i] >= 100)][k] >= dp[i - 1][j][k] + a[i]:
                    dp[i][j + (a[i] >= 100)][k] = dp[i - 1][j][k] + a[i]
                    p[i][j + (a[i] >= 100)][k] = 1


    mn = (10 ** 9, -1000, 1000)
    for i in range(n + 1):
        for j in range(n + 1):
            mn = min(mn, (dp[n - 1][i][j], -i, j))

    print(mn[0])
    print(-mn[1], mn[2])
    s = n - 1
    k1 = -mn[1]
    k2 = mn[2]

    ans = []

    while s > 0:

        if p[s][k1][k2] == 1:
            k2 = k2
            k1 -= (a[s] >= 100)

        else:
            k2 -= 1
            k1 += 1
            ans.append(s + 1)
        s -= 1

    for i in ans[::-1]:
        print(i)



if __name__ == '__main__':
    f = open("input.txt", "r")
    sys.stdin = f
    t_s = time.time_ns()
    task_18_dp()
    t_e = time.time_ns()
    print(f"total time: {(t_e - t_s) / (10 ** 9)} seconds")
    f.close()
