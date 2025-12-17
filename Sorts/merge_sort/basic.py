class Solution:
    def merge(self,left, right):
        result=[]
        i=j=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result = result.extend(left[i:])
        result = result.extend(right[j:]) 
        return result
        
    def mergeSort(self,nums):
        n=len(nums)
        if n <= 1:
            return nums
        middle = n//2
        left=nums[:middle]
        right=nums[middle:]

        sortedLeft = self.mergeSort(left)
        sortedRight = self.mergeSort(right)

        return self.merge(sortedLeft, sortedRight)
    


obj = Solution()
nums = [3,2,10,1,5,2,1]
print(obj.mergeSort(nums))