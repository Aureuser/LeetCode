# -*- coding: utf-8 -*- 
# @Time : 2020/6/30 17:14 
# @Author : lxd 
# @File : 动态规划.py


class Solution:
    def maximalRectangle(self, matrix):
        area = 0
        max_left_width_list = list()
        for row in matrix:
            max_left_width = []
            for i in row:
                max_left_width.append(max_left_width[-1] + 1) if i == '1' and max_left_width \
                    else max_left_width.append(0)
            max_left_width_list.append(max_left_width)
        for i in range(len(matrix[0])):
            width = 0
            height = 0
            for j in range(len(matrix)):
                height += 1
                if width < max_left_width_list[j][i]:
                    height = 1
                width = max_left_width_list[j][i]
                area = max(area, width * height)

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