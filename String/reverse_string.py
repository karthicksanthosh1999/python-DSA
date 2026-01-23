class Solution:
    def reverse_string(self, nums):
        n = len(nums)
        result = []
        for i in range(n-1, -1,-1):
            result.append(nums[i])
        return result

result = Solution()
nums = ["h","e","l","l","0"]
print(result.reverse_string(nums))