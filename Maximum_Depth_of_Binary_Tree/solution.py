class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        left_depth = 1
        right_depth = 1
        if root.left:
            left_depth += self.maxDepth(root.left)
        if root.right:
            right_depth += self.maxDepth(root.right)
        return max(left_depth,right_depth)
