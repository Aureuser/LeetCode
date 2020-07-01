# -*- coding: utf-8 -*- 
# @Time : 2020/6/30 10:58 
# @Author : lxd 
# @File : 栈方法.py

class Solution:
    '''
    该栈方法是基于84.柱状图中最大的矩阵的站方法实现的
    之前我们用过动态规划算法求出每一列元素的最大宽，通过列方向宽度矩阵类似于柱状图
    柱状图的高度就是矩阵中宽度数值，
    '''
    def largestRectangleArea(self, heights):
        height_list = list()
        area = 0
        for i in range(len(heights)):
            while height_list and heights[i] < heights[height_list[-1]]:
                top = height_list.pop()
                if height_list:
                    area = max(area, heights[top] * (i - height_list[-1] - 1))
                else:
                    area = max(area, heights[top] * i)
            height_list.append(i)
        while height_list:
            top = height_list.pop()
            if height_list:
                area = max(area, heights[top] * (len(heights) - height_list[-1] - 1))
            else:
                area = max(area, heights[top] * len(heights))
        return area


    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        area = 0
        widths = [0 for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                widths[j] = widths[j] + 1 if matrix[i][j] == '1' else  0
            area = max(self.largestRectangleArea(widths), area)
        return area

if __name__ == '__main__':
    s = Solution()
    area = s.maximalRectangle([
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]])
    # 6
    print(area)
    area = s.maximalRectangle([
        ["0","0","1","0"],
        ["0","1","1","1"],
        ["0","1","1","0"],
        ["1","0","1","0"]])
    # 4
    print(area)