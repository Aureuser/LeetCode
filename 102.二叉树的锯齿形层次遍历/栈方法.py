# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        dp1 = [root,]
        dp2 = []
        score = []
        while dp1 or dp2:
            line = []
            while dp1:
                root = dp1.pop()
                if root:
                    line.append(root.val)
                    dp2.append(root.left)
                    dp2.append(root.right)
            if line:
                score.append(line)
            line = []
            while dp2:
                root = dp2.pop()
                if root:
                    line.append(root.val)
                    dp1.append(root.right)
                    dp1.append(root.left)
            if line:
                score.append(line)
        return score