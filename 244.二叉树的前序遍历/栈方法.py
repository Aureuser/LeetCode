class Solution:
    def preorderTraversal(self, root):
        score = []
        dp = []
        while root or dp:
            if root:
                score.append(root.val)
                dp.append(root.right)
                root = root.left
            else:
                root = dp.pop()
        return score