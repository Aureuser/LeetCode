# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        if root:
            left = self.inorderTraversal(root.left)
            right = self.inorderTraversal(root.right)
            return [*left ,root.val, *right]
        else:
            return []