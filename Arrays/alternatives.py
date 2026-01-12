class Solution: 
    def alternatives(self, nuns):
        n = len(nuns)
        for i in range(0, n, 2):
            if i % 2 == 0:
                print(nums[i])

result = Solution()
nums = [-5, 1, 4, 2, 12]
result.alternatives(nums)