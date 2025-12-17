class Solution:
    def linearSearch(self,nums:list,target:int):
        n=len(nums)
        for i in range(0,n):
            if nums[i] == target:
                return i
        return None
            

myList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
targetValue = 5
obj = Solution()
print(obj.linearSearch(myList,targetValue))
