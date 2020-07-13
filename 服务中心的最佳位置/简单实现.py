import math
class Solution:
    '''

    '''
    def getMinDistSum(self, positions):
        x_, y_, count = 0, 0, 0
        for i, j in positions:
            x_ += i
            y_ += j
            count += 1
        x_ /= count
        y_ /= count
        d = 0
        for i, j in positions:
            d += math.sqrt(pow(x_ - i, 2)+pow(y_ - j, 2))
        return d

if __name__ == '__main__':
    s = Solution()
    print(s.getMinDistSum([[0,1],[1,0],[1,2],[2,1]]))