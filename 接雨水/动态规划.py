class Solution:
    def trap(self, height: list):
        if not len(height):
            return 0
        left = [height[0],]
        right = [height[-1],]
        score = 0
        for i in range(1, len(height)):
            if height[i] > left[-1]:
                left.append(height[i])
            else:
                left.append(left[-1])
            if height[-i-1] > right[-1]:
                right.append(height[-i-1])
            else:
                right.append(right[-1])
        for i in range(len(right)):
            score += min(left[i], right[-i-1]) - height[i]
        return score

if __name__ == '__main__':
    s = Solution()
    # 1729
    area = s.trap(
        [1, 2, 3, 5, 3, 3, 2, 4, 23, 2, 4, 43, 2, 3, 45, 23, 4, 325, 234, 43, 223, 354, 345, 3, 23, 5, 54, 23, 234])
    print(area)