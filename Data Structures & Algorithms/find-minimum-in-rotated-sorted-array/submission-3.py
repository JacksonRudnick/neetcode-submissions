class Solution:
    def findMin(self, nums: List[int]) -> int:
        idx = math.ceil(len(nums)/2)-1
        step = math.ceil(len(nums)/4)
        left = 0
        right = len(nums)-1

        while left <= right:
            if nums[idx] > nums[(idx-1)%len(nums)] and nums[idx] < nums[(idx+1)%len(nums)]:
                if abs(nums[idx]-nums[left]) > abs(nums[idx]-nums[right]):
                    right = idx
                    idx = (idx - step) % len(nums)
                else:
                    left = idx
                    idx = (idx + step) % len(nums)
                step = math.ceil(step/2)
            else:
                #found number
                if not nums[idx] < nums[(idx+1)%len(nums)]:
                    return nums[(idx+1)%len(nums)]
                return nums[idx]
