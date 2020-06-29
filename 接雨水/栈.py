class Solution:
    def trap(self, height: list):
        area = 0
        if len(height) < 2:
            return 0
        lists = [0, 1]
        for i in range(2, len(height)):
            print(lists)
            if len(lists) and height[i] > height[lists[-1]]:
                top = lists.pop()
                while len(lists) and height[lists[-1]] <= height[i]:
                    area += (height[lists[-1]] - top) * (i - lists[-1] - 1)
                    top = lists.pop()
                lists.append(top)
            lists.append(i)

        return area


if __name__ == '__main__':
    s = Solution()
    area = s.trap(
        [1, 2, 3, 5, 3, 3, 2, 4, 23, 2, 4, 43, 2, 3, 45, 23, 4, 325, 234, 43, 223, 354, 345, 3, 23, 5, 54, 23, 234])
    # 1729
    print(area)
