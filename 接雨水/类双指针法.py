# -*- coding: utf-8 -*- 
# @Time : 2020/6/29 15:11 
# @Author : lxd 
# @File : 类双指针法.py

class Solution:
    def trap(self, height: list):
        '''
        本方法类似双指针法
        :param height:
        :return:
        '''
        if len(height) < 3:
            return 0
        max_indx = height.index(max(height))
        left_max, right_max = 0, 0
        area = 0
        for i in height[: max_indx]:
            if left_max > i:
                area += left_max - i
            else:
                left_max = i
        for i in height[:max_indx:-1]:
            if right_max > i:
                area += right_max - i
            else:
                right_max = i

        return area


if __name__ == '__main__':
    s = Solution()
    area = s.trap(
        [1, 2, 3, 5, 3, 3, 2, 4, 23, 2, 4, 43, 2, 3, 45, 23, 4, 325, 234, 43, 223, 354, 345, 3, 23, 5, 54, 23, 234])
    # 1729
    print(area)
    area = s.trap([])
    # 0
    print(area)
