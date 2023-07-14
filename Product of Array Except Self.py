class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        zero_count = 0
        for i in nums:
            if i != 0:
                prod *= i

        answers = [0] * len(nums)

        if zero_count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    answers[i] = prod
        elif zero_count == 0:
            for i in range(len(nums)):
                answers[i] = prod // nums[i]

        return answers


nums = [1, 2, 4, 3]
s1 = Solution()
res = s1.productExceptSelf(nums)
print(res)
