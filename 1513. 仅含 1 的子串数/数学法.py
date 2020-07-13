class Solution:
    def numSub(self, s):
        num = 0
        count = 0
        for i in s:
            if i == '1':
                count += 1
                num += count
            else:
                count = 0
        return int(num % (1e9 + 7))

if __name__ == '__main__':
    s = Solution()
    # 117
    print(s.numSub('11110000000111111111110000000111111110101010101'))