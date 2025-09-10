import sys, time

class Node:
    __slots__ = ('key', 'left', 'right')

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


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


def task3():
    data = sys.stdin.read().splitlines()
    bst = BST()
    for line in data:
        parts = line.split()
        op = parts[0]
        num = int(parts[1])
        if op == '+':
            bst.insert(num)
        elif op == '>' :
            res = bst.find_min_greater(num)
            print(str(res))


if __name__ == '__main__':
    f = open("input.txt", "r")
    sys.stdin = f
    t_s = time.time_ns()
    task3()
    t_e = time.time_ns()
    print(f"total time: {(t_e - t_s) / (10 ** 9)} seconds")
    f.close()
