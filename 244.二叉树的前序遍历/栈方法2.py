class Solution:
    def preorderTraversal(self, root):
        score = []
        dp = []
        while root or dp:
            while root:
                score.append(root.val)
                dp.append(root.right)
                root = root.left
            if dp:
                root = dp.pop()
        return score