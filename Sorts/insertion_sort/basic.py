class Solution:
    def insertionSort(self, nums):
        n=len(nums)
        for i in range(1,n):
            insert_value=i
            current_value=nums[i]
            for j in range(i-1,-1,-1):
                if nums[j] > current_value:
                    nums[j+1] = nums[j]
                    insert_value=j
                else:
                    break
            nums[insert_value] = current_value

insertionObj = Solution()
nums = [3,2,10,1,5,2,1]
print(insertionObj.insertionSort(nums))