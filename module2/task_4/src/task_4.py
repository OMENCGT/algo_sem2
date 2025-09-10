import sys, time

class Node:
    __slots__ = ('key', 'left', 'right', 'cnt')

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.cnt = 1


class BST:
    __slots__ = ('root',)

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root
        while current:

            if key < current.key:
                current.cnt += 1
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right
            else:
                return

    def exist(self, key) -> bool:
        if self.root is None:
            return False

        current = self.root
        while current:
            if key < current.key:
                if current.left is None:
                    return False
                current = current.left
            elif key > current.key:
                if current.right is None:
                    return False
                current = current.right
            else:
                return True
        return False

    def find_min_greater(self, x):
        candidate = 0
        current = self.root
        while current is not None:
            if current.key > x:
                candidate = current.key
                current = current.left
            else:
                current = current.right
        return candidate

    def find_kth(self, k:int):
        current = self.root
        while k > 0:
            if k == current.cnt:
                return current.key
            elif k > current.cnt:
                k -= current.cnt
                current = current.right
            else:
                current = current.left
        return None




def task4():
    data = sys.stdin.read().splitlines()
    bst = BST()
    for line in data:
        parts = line.split()
        op = parts[0]
        num = int(parts[1])
        if op == '+':
            if not bst.exist(num):
                bst.insert(num)
        elif op == '?' :
            res = bst.find_kth(num)
            print(str(res))


if __name__ == '__main__':
    f = open("input.txt", "r")
    sys.stdin = f
    t_s = time.time_ns()
    task4()
    t_e = time.time_ns()
    print(f"total time: {(t_e - t_s) / (10 ** 9)} seconds")
    f.close()
