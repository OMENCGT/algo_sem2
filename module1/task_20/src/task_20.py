import tracemalloc
import time
import sys

def task_20_dp():
    n, k = map(int, input().split())
    a = input()
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i - j >= 0 and i + j < n:
                cnt += a[i - j] != a[i + j]
                if cnt > k:
                    break
                else:
                    ans += 1
            else:
                break

    for i in range(n):
        cnt = 0
        for j in range(n):
            if i - j >= 0 and i + j + 1 < n:
                cnt += a[i - j] != a[i + j + 1]
                if cnt > k:
                    break
                else:
                    ans += 1
            else:
                break

    print(ans)

if __name__ == '__main__':
    f = open("input.txt", "r")
    sys.stdin = f
    t_s = time.time_ns()
    task_20_dp()
    t_e = time.time_ns()
    print(f"total time: {(t_e - t_s) / (10 ** 9)} seconds")
    f.close()
