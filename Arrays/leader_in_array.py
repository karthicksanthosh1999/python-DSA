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

    def expect(self, nums):
        n = len(nums)
        maxEle = nums[-1]
        result = []
        result.append(maxEle)
        for i in range(n-2, -1, -1):
            if nums[i] >= maxEle:
                maxEle = nums[i]
                result.append(nums[i])
        result.reverse()
        return result


result = Solution()
nums =  [16, 17, 4, 3, 5, 2]
print(result.expect(nums))