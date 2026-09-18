class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 100
        best = 0

        for i in prices:
            if i < low:
                low = i
            elif i - low > best:
                best = i - low

        return best