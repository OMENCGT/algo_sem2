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

def task_6():
    print(*(calc(input())[1:]))

if __name__ == '__main__':
    f = open("input.txt", "r")
    f1 = open("output.txt", "w")
    sys.stdin = f
    sys.stdout = f1
    t_s = time.time_ns()
    task_6()
    t_e = time.time_ns()
    print(f"total time: {(t_e - t_s) / (10 ** 9)} seconds")
    f.close()
