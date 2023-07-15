class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = suffix = 1
        maxProd = float("-inf")

        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1

            if suffix == 0:
                suffix = 1

            prefix *= nums[i]
            suffix *= nums[len(nums) - 1 - i]

            maxProd = max(maxProd, max(prefix, suffix))

        return maxProd
