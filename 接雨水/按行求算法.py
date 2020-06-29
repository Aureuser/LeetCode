# -*- coding: utf-8 -*- 
# @Time : 2020/6/29 16:25 
# @Author : lxd 
# @File : 按行求算法.py

class Solution:
    def trap(self, height: list):
        '''此方法适用于高度不是很高的场景'''
        if len(height) < 3:
            return 0
        area = 0
        height_max = max(height)
        for i in range(height_max):
            left, right, count = 0, 0, 0
            for j in range(len(height)):
                if height[j] > i:
                    count += 1
                    left = left if height[left] > i else j
                    right = j
            area += right - left - count + 1

        return area


if __name__ == '__main__':
    s = Solution()
    area = s.trap([2,0,2])
    # 2
    print(area)
    area = s.trap(
        [1, 2, 3, 5, 3, 3, 2, 4, 23, 2, 4, 43, 2, 3, 45, 23, 4, 325, 234, 43, 223, 354, 345, 3, 23, 5, 54, 23, 234])
    # 1729
    print(area)
    area = s.trap([])
    # 0
    print(area)