class Solution:
    def pivot_value(self,nums, low, high):
        pivot = nums[high]
        i = low -1
        for j in range(low, high):
            print(low, high, i)
            if nums[j] <= pivot:
                i+=1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[high] = nums[high], nums[i+1]
        print(nums)
        return i+1

obj = Solution()
nums = [11,9,12,7,3]
low=0
high=4
print(obj.pivot_value(nums, low, high))