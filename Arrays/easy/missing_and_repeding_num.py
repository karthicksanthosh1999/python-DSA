class Solution:
    def missing(self, nums):
        n=len(nums)
        missing = -1
        repeat = -1
        freq = [0] * (n+1)
        for i in nums:
            freq[i] += 1
        for j in range(1,n+1):
            if freq[j] == 0:
                missing = j
            elif freq[j] == 2:
                repeat = i
        return [repeat, missing]

result = Solution()
print(result.missing([6, 5, 8, 7, 1, 4, 1, 3, 2])) 
