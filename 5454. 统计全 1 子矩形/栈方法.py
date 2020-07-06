class Solution:
    '''
    本方法借用85.最大矩阵的栈方法
    但还是有些许不同，在85中,出栈时计算出栈元素左右两端的下标差再乘以自身高度，因为栈内递增，比该元素大的元素已经提前出栈了
    而左边的第一个是除该元素之外该元素左边第一大的数（也可能与该元素登高），同理如果该元素右边存在比该元素小的数，那么该元素已经出栈，
    所以它右边是第一个比它小的数，所以该元素的最大宽度是右元素下标与左元素下标之间的宽度。
    5454中，出栈的目的是求元素左边能组成的最大矩阵，所以不再是右元素下标-做元素下标，而是我也说不清楚
    '''
    def numSubmat(self, mat):
        num = 0
        if not mat:
            return 0
        height = [0 for _ in mat[0]]
        for i in range(len(mat)):
            widths = list()
            sum = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1: height[j] +=  1
                else: height[j] = 0
                while widths and height[widths[-1]] >= height[j]:
                    idx = widths.pop()
                    width = idx - (widths[-1] if widths else -1)
                    sum -= width * (height[idx] - height[j])
                widths.append(j)
                sum += height[j]
                num += sum
        return num

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