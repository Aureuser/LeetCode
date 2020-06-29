# -*- coding: utf-8 -*- 
# @Time : 2020/6/29 14:48 
# @Author : lxd 
# @File : 数学解法.py
class Solution:
    def trap(self, height: list):
        if len(height) < 3:
            return 0
        max_height, S1, S2 = 0, 0, 0
        juzhen_area = max(height) * len(height)
        zhuzi_area = sum(height)
        for i in height:
            if i > max_height:
                max_height = i
            S1+=max_height
        max_height = 0
        height.reverse()
        for i in height:
            if i > max_height:
                max_height = i
            S2+=max_height

        return S1 + S2 - juzhen_area - zhuzi_area


if __name__ == '__main__':
    s = Solution()
    area = s.trap(
        [1, 2, 3, 5, 3, 3, 2, 4, 23, 2, 4, 43, 2, 3, 45, 23, 4, 325, 234, 43, 223, 354, 345, 3, 23, 5, 54, 23, 234])
    # 1729
    print(area)
    area = s.trap([])
    # 0
    print(area)
