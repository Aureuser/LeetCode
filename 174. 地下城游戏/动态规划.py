class Solution:
    def calculateMinimumHP(self, dungeon):
        if not dungeon:
            return 0
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[10e9 for _ in range(m+1)] for _ in range(n+1)]
        dp[n][m-1] = dp[n-1][m] = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        return dp[0][0]

if __name__ == '__main__':
    s = Solution()
    # 6
    print(s.calculateMinimumHP([[-2,-3,3, 9],[-5,-10,1,-2],[10,30,-5,-9]]))