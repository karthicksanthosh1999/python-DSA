class Solution:
    def duplicate(self, nums, k):
        n = len(nums)
        for i in range(n):
            for j in range(1, k+1):
                c = i + j
                if c < n and nums[i] == nums[j]:
                    return True 
        return False

result = Solution()
nums = [1, 2, 3, 4, 1, 2, 3, 4]
print("Yes" if  result.duplicate(nums,3) else "No")

