class Solution:
    def binarySearch(self,nums,target):
        n=len(nums)
        left=0
        right=n-1
        while left < right:
            middle = (right+left) //2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle+1
            else:
                right = middle-1
        return None


nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
targetValue = 5

obj = Solution()
print(obj.binarySearch(nums,targetValue))