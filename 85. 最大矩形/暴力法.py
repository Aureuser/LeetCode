# -*- coding: utf-8 -*- 
# @Time : 2020/6/30 11:28 
# @Author : lxd 
# @File : 暴力法.py

class Solution:
    def maximalRectangle(self, matrix):
        area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    for i_ in range(i, len(matrix)):
                        for j_ in range(j, len(matrix[0])):
                            if matrix[i_][j_] == '1':
                                flag = True
                                count = 0
                                for ii in range(i, i_+1):
                                    for jj in range(j, j_+1):
                                        count += 1
                                        if matrix[ii][jj] == '0':
                                            flag = False
                                if flag:
                                    area = max(area, count)
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