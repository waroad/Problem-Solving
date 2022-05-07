from collections import deque


class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.par_right=None
        self.par_left=None


def print_level(tree):
    deq=deque()
    deq.append(tree)
    deq2=[]
    while len(deq):
        tmp=deq.popleft()
        if not tmp:
            deq2.append('Null')
            continue
        if deq2:
            print(*deq2,end=' ')
        deq2=[]
        print(tmp.value, end=' ')
        deq.append(tmp.left)
        deq.append(tmp.right)
    print("")


def build_binary_tree(items):
    if not items:
        return None

    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            node.left.par_left=node
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            node.right.par_right=node
            q.append(node.right)
    return root


def deletion(tree, key):
    node = build_binary_tree(tree)
    tree=node
    while key!=node.value:
        if key<node.value:
            node=node.left
        else:
            node=node.right
    if not node.left and not node.right:
        if node.par_left:
            node.par_left.left=None
        elif node.par_right:
            node.par_right.right=None
    elif node.left and not node.right:
        if node.par_left:
            node.par_left.left=node.left
            node.left.par_left=node.par_left
        elif node.par_right:
            node.par_right.right=node.left
            node.left.par_right=node.par_right
    elif not node.left and node.right:
        if node.par_left:
            node.par_left.left = node.right
            node.right.par_left = node.par_left
        elif node.par_right:
            node.par_right.right = node.right
            node.right.par_right = node.par_right
    else:
        tmp_node=node.right
        while tmp_node.left:
            tmp_node=tmp_node.left
        node.value = tmp_node.value
        if tmp_node.par_left:
            tmp_node.par_left.left=tmp_node.right
            if tmp_node.right:
                tmp_node.right.par_left=tmp_node.par_left
        else:
            node.right=node.right.right
            if node.right:
                node.right.par_right=node
    print_level(tree)


deletion([5,3,6,2,4,None,7], 3)
deletion([5,3,6,2,4,None,7], 5)
deletion([5, 2, 6, 1, 4, None, 7, None, None, 3], 7)
deletion([5, 2, 6, 1, 4, None, 7, None, None, 3], 2)
deletion([15, 10, 18, 8, None, 17, 20, 7, 9, None, None, None, 21], 9)