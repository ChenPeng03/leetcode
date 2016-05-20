class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    def minDepth(self, root):
        if not root:
            return 0
        if root.left = None or root.right = None:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
