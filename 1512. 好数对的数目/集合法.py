class Solution:
    def numIdenticalPairs(self, nums):
        num = 0
        char = set()
        for i in nums:
            if i not in char:
                char.add(i)
                num += sum(range(nums.count(i)))
        return num

if __name__ == '__main__':
    s = Solution()
    # 4
    print(s.numIdenticalPairs([1,2,3,1,1,3]))