class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        total = 1

        for i in range(1, len(nums)):
            total *= nums[i-1]
            prefix.append(total)

        total = 1

        for i in range(len(nums)-2, -1, -1):
            total *= nums[i+1]
            suffix.append(total)

        res = []

        for i in range(len(prefix)):
            res.append(prefix[i] * suffix[len(suffix)-i-1])

        return res

            
