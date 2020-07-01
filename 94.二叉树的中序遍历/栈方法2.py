# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        score = []
        dp = []
        while root or dp:
            while root:
                dp.append(root)
                root = root.left
            if dp:
                root = dp.pop()
                score.append(root.val)
                root = root.right
        return score