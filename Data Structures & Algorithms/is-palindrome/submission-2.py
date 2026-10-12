class Solution:
    def isPalindrome(self, s: str) -> bool:
        sen = "".join(s)
        lower = sen.lower()
        left = 0
        right = len(lower) - 1
        while left < right:
            while left < right and not lower[left].isalnum():
                left += 1
            while left < right and not lower[right].isalnum():
                right -= 1
            if lower[left] != lower[right]:
                return False
            left += 1
            right -= 1
        return True