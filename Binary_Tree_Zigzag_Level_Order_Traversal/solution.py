class Solution(object):
    def zigzagLevelOrder(self, root):
        goRight = 1
        ans = []
        queue = [root]
        while queue:
            next_queue = []
            ans.append([node.val for node in queue[::goRight]])
            for i in queue:
                if i.left:
                    next_queue.append(i)
                if i.right:
                    next_queue.append(i)
            queue = next_queue
            goRight *= -1
        return ans
