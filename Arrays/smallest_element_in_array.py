class Solution:
    def smallElement(self,nums):
        smallEle = nums[0]
        for i in range(len(nums)):
            if nums[i] < smallEle:
                smallEle = nums[i]
        return smallEle
result = Solution()
nums = [2,3,4,6,1]
print(result.smallElement(nums))