class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo = 0
        hi = len(heights)-1
        prev_cap = -1

        while lo < hi:
            cap = (hi-lo) * min(heights[lo], heights[hi])

            if cap > prev_cap:
                prev_cap = cap

            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1

        return prev_cap
