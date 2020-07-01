class Solution:
    def preorderTraversal(self, root):
        score = []
        def digui(root):
            if root:
                score.append(root.val)
                digui(root.left)
                digui(root.right)
        if root:
            score.append(root.val)
            digui(root.left)
            digui(root.right)
        return score