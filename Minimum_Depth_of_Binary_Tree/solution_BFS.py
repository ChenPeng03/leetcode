class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            res += 1
            for i in range(len(queue)):
                if not queue[0].right and not queue[0].left:
                    return res
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.pop(0)
        return res
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        queue = [root]
        root.val = 1
        while queue:
            node = queue.pop(0)
            if not node.left and not node.right:
                return node.val
            if node.left:
                queue.append(node.left)
                node.left.val = node.val + 1
            if node.right:
                queue.append(node.right)
                node.right.val = node.val + 1

