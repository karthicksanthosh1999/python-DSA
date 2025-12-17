class BubbleSort:
    def bubble(self, nums):
        n = len(nums)
        for i in range(n):
            swapped=False
            for j in range(0,n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped=True
            if not swapped:
                break
        return nums
 
bubbleSortObj = BubbleSort()
nums = [100,40,20,2,5,8,90]
print(bubbleSortObj.bubble(nums))


