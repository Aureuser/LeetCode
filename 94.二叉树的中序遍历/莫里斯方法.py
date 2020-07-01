class Solution:
    '''
    又叫二叉树搜索
    '''
    def inorderTraversal(self, root):
        score = []
        while root:
            if root.left:
                left = d = root.left
                while d.right:
                    d = d.right
                d.right = root
                root.left = None
                root = left
            else:
                score.append(root.val)
                root = root.right
        return score