class InsertionSort:
    def insertion(self, nums):
        n=len(nums)
        for i in range(n):
            minIndex = i
            for j in range(i+1, n):
                if nums[j] < nums[minIndex]:
                    minIndex=j
                nums[i], nums[minIndex] = nums[minIndex], nums[i]
        return nums
insertionObj = InsertionSort()
nums = [3,2,10,1,5,2,1]
print(insertionObj.insertion(nums))

            
            