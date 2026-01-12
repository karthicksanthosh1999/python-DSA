class Solution:
    def native(self, nums):
        n = len(nums)
        result = []

        for i  in range(n):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    break
            else:
                result.append(nums[i])
        return result


result = Solution()
nums =  [16, 17, 4, 3, 5, 2]
print(result.native(nums))