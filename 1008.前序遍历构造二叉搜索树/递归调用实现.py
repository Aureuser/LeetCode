# coding:utf-8
# @Time : 2021/6/8 21:40 
# @Author : lxd
# @File : 递归调用实现.py
# @Software: PyCharm
# @E-mail: 1355087842@qq.com

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstFromPreorder(preorder):
    if len(preorder) == 0: return None
    node = TreeNode(preorder[0])
    node.left, node.right = bstFromPreorder([i for i in preorder[1:] if i < preorder[0]]), bstFromPreorder([i for i in preorder[1:] if i > preorder[0]])
    return node

def bfs(node):
    if node:
        print(node.val, end=' ')
        bfs(node.left)
        bfs(node.right)



if __name__ == '__main__':
    node = bstFromPreorder([8, 5, 1, 7, 10, 12])
    bfs(node)