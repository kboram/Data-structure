from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_complete_binary_tree(root):
    if not root:
        return True

    queue = deque([root])
    while queue:
        current = queue.popleft()

        if current:
            queue.append(current.left)
            queue.append(current.right)
        else:
            for node in queue:
                if node:
                    return False

    return True

# 주어진 이진 트리 생성
a = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')

a.left = b
a.right = e
b.left = c
b.right = d
e.right = f

# 완전 이진 트리 여부 검사
result = is_complete_binary_tree(a)
print("Is Complete Binary Tree:", result)