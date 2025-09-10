import sys, time


def num(a:str):
    return ord(a) - ord('a')


def count():
    a = sys.stdin.readline()
    a = "".join(a.split())
    cnt_l = [0 for i in range(26)]
    cnt_r = [0 for i in range(26)]
    ans = 0
    ans_at_point = 0
    prev_ans_ap = 0
    prev_ans_ap_lett = [0 for i in range(26)]
    for i in a:
        cnt_r[num(i)] += 1
    cnt_r[num(a[0])] -= 1
    for i in range(1, len(a)):
        cnt_r[num(a[i])] -= 1
        cnt_l[num(a[i - 1])] += 1
        ans_at_point = prev_ans_ap - prev_ans_ap_lett[num(a[i - 1])] + cnt_l[num(a[i - 1])] * cnt_r[num(a[i - 1])]
        ans_at_point += -prev_ans_ap_lett[num(a[i])] + cnt_l[num(a[i])] * cnt_r[num(a[i])]
        ans += ans_at_point
        prev_ans_ap = ans_at_point
        prev_ans_ap_lett[num(a[i - 1])] = cnt_l[num(a[i - 1])] * cnt_r[num(a[i - 1])]
        prev_ans_ap_lett[num(a[i])] = cnt_l[num(a[i])] * cnt_r[num(a[i])]

    print(ans)

if __name__ == '__main__':
    f = open("input.txt", "r")
    sys.stdin = f
    t_s = time.time_ns()
    count()
    t_e = time.time_ns()
    print(f"total time: {(t_e - t_s) / (10 ** 9)} seconds")
    f.close()
