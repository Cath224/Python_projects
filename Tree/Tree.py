class Tree:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.value = 0


def in_order(trees, i):
    if trees[i].left != -1:
        in_order(trees, trees[i].left)
    print(str(trees[i].key) + " ")
    if trees[i].right != -1:
        in_order(trees, trees[i].right)


def pre_order(trees, i):
    print(str(trees[i].key) + " ")
    if trees[i].left != -1:
        pre_order(trees, trees[i].left)

    if trees[i].right != -1:
        pre_order(trees, trees[i].right)


def post_order(trees, i):
    if trees[i].left != -1:
        post_order(trees, trees[i].left)

    if trees[i].right != -1:
        post_order(trees, trees[i].right)

    print(str(trees[i].key) + " ")


def start(trees):
    in_order(trees, 0)
    pre_order(trees, 0)
    post_order(trees, 0)


def main():
    length = int(input())
    trees = [None] * length
    for i in range(length):
        trees[i] = Tree()
        array = list(map(int, input().strip().split()))[:3]
        trees[i].key = array[0]
        trees[i].left = array[1]
        trees[i].right = array[2]

    start(trees)


main()
