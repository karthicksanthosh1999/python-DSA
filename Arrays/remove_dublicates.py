class Solution:
    def expect(self, nums):
        n = len(nums)
        idx = 1
        result = []
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                result.append(nums[idx])
                print(idx)
                idx +=1
        return idx, result

result = Solution()
nums = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(result.expect(nums))