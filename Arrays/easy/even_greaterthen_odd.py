class Solution:
    def odd_even(self, nums):
        n = len(nums)
        for i in range(n):
            if (i+1) % 2 == 0:
                if nums[i] < nums[i -1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
            else:
                if nums[i] > nums[i-1]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums
    
result = Solution()
print(result.odd_even([1,2,3,4,5]))