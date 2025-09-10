import sys, time

def calc(a:str):
    n = len(a)
    p = [0 for i in range(n)]
    for i in range(1, n):
        cur = p[i - 1]

        while a[i] != a[cur] and cur > 0:
            cur = p[cur - 1]

        if a[i] == a[cur]:
            p[i] = cur + 1

    return p

def task_5():
    a = input()
    print(*calc(a))
    
if __name__ == '__main__':
    f = open("input.txt", "r")
    sys.stdin = f
    t_s = time.time_ns()
    task_5()
    t_e = time.time_ns()
    print(f"total time: {(t_e - t_s) / (10 ** 9)} seconds")
    f.close()
