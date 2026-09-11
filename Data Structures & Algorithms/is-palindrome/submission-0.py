class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left <= right:
            if not s[left].isalnum():
                print('inc left')
                left += 1
            elif not s[right].isalnum():
                print('dec right')
                right -= 1
            elif s[left].lower() != s[right].lower():
                print(s[left] + ' is not equal to ' + s[right])
                return False
            else:
                print('dec both')
                left += 1
                right -= 1

        return True
        