class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [2, 3, 1, 5, 3]
target = 8

s = Solution()
result = s.twoSum(nums, target)

print(result)
