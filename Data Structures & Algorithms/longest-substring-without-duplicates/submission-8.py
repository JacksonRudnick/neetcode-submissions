class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        best = 0
        length = 0

        for i in range(len(s)):
            if s[i] in chars and chars[s[i]] >= i - length:
                length = i - chars[s[i]]
            else:
                length += 1
            if length > best:
                best = length
            chars[s[i]] = i

        return best
