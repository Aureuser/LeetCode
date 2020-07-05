class Solution:
    '''
    本方法借用85.最大矩阵的栈方法
    但还是有些许不同，在85中栈内是递增的，但是允许包含相同的高度，比如[1,2,3,4,4,5]
    但是在笨方法中，栈内是严格递增的，即不允许包含相同高度，比如[1,2,3,4,5,6]
    目前本方法还存在缺陷。
    '''
    def numSubmat(self, mat):
        num = 0
        if not mat:
            return 0
        height = [0 for _ in mat[0]]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1: height[j] +=  1
                else: height[j] = 0
            num += self.largestRectangleArea(height)
        return num

    def largestRectangleArea(self, heights):
        height_list = list()
        num = 0
        for i in range(len(heights)):
            while height_list and heights[i] <= heights[height_list[-1]]:
                top = height_list.pop()
                if height_list:
                    num += self.get_sun(heights[top], (i - height_list[-1] - 1))
                else:
                    num += self.get_sun(heights[top], i)
            height_list.append(i)
        while height_list:
            top = height_list.pop()
            if height_list:
                num += self.get_sun(heights[top], (len(heights) - height_list[-1] - 1))
            else:
                num += self.get_sun(heights[top], len(heights))
        # print(num)
        return num

    def get_sun(self, width, height):
        '''
        计算一个大矩阵包含多少个小矩阵(包括自身)
        :param width: 矩阵宽度
        :param height: 矩阵高度
        :return: 子矩阵个数
        '''
        return sum([i * j for i in range(1, width + 1) for j in range(1, height + 1)])

if __name__ == '__main__':
    s = Solution()
    area = s.numSubmat([[1,0,1],[1,1,0],[1,1,0]])
    # 13
    print(area)
    area = s.numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]])
    # 24
    print(area)
    area = s.numSubmat([[1,1,1,1,1,1]])
    # 21
    print(area)
    area = s.numSubmat([[1,0,1],[0,1,0],[1,0,1]])
    # 5
    print(area)
    area = s.numSubmat([[0,1,1,1],[1,1,0,1],[1,1,0,0],[1,1,1,1],[0,1,0,0]])
    # 41
    print(area)
    area = s.numSubmat([[1,1,1,1,0,1,0],[1,1,1,0,0,0,1],[0,1,1,1,1,0,0],[1,1,0,1,1,0,1],
                        [1,0,0,0,0,0,1],[1,1,0,1,1,1,1],[1,1,0,0,1,1,1]])
    # 96
    print(area)