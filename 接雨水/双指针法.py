# -*- coding: utf-8 -*- 
# @Time : 2020/6/29 14:29 
# @Author : lxd 
# @File : 双指针法.py

class Solution:
    def trap(self, height: list):
        if len(height) < 3:
            return 0
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        area = 0
        while left != right:
            if height[left] > height[right]:
                if height[right] <= right_max:
                    area += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
            else:
                if height[left] <= left_max:
                    area += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
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
