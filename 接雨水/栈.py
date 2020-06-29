class Solution:
    def trap(self, height: list):
        area = 0
        if len(height) <= 2:
            return 0
        FILO = []
        for i in range(len(height)):
            while len(FILO) and height[FILO[-1]] < height[i]:
                top_index = FILO.pop()
                if not len(FILO): break
                area += (min(height[i], height[FILO[-1]]) - height[top_index]) * \
                        (i - FILO[-1] - 1)
            FILO.append(i)


        return area


if __name__ == '__main__':
    s = Solution()
    area = s.trap(
        [1, 2, 3, 5, 3, 3, 2, 4, 23, 2, 4, 43, 2, 3, 45, 23, 4, 325, 234, 43, 223, 354, 345, 3, 23, 5, 54, 23, 234])
    # 1729
    print(area)
