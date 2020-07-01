class Solution:
    '''
    又叫二叉树搜索
    '''
    def preorderTraversal(self, root):
        score = []
        while root:
            score.append(root.val)
            if root.left:
                left = root.left
                while left.right:
                    left = left.right
                left.right = root.right
                root = root.left
            else:
                root = root.right
        return score