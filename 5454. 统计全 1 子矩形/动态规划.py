class Solution:
    def numSubmat(self, mat):
        if not mat:
            return 0
        num = 0
        dp = [[0 for _ in mat[0]] for _ in mat]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    dp[i][j] = dp[i][j-1] + 1 if j > 0 else 1
                    min_width = len(mat[0])
                    for k in range(i, -1, -1):
                        min_width = min(dp[k][j], min_width)
                        num += min_width
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