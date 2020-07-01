# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        dp = []
        def digui(x):
            if x:
                digui(x.left)
                dp.append(x.val)
                digui(x.right)
        digui(root.left)
        dp.append(root.val)
        digui(root.right)
        return dp
