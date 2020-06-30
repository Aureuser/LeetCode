# -*- coding: utf-8 -*-
# @Time : 2020/6/30 23:25
# @Author : lxd
# @File : 动态规划优化.py


class Solution:
    '''
    优化后的动态规划算法时间复杂度不变，空间复杂度也没变
    只是代码看起来短了很多
    '''
    def maximalRectangle(self, matrix):
        area = 0
        max_left_width_list = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0': continue
                width = max_left_width_list[i][j] = max_left_width_list[i][j-1] + 1 if j else 1
                for k in range(i, -1, -1):
                    width = min(width, max_left_width_list[k][j])
                    area = max(width * (i - k + 1), area)
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