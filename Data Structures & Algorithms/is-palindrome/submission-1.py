class Solution:
    def isPalindrome(self, s: str) -> bool:
        sen = "".join(s)
        lowerCase = sen.lower()
        right = len(lowerCase) - 1
        left = 0
        while left < right:
            while left < right and not lowerCase[left].isalnum():
                left += 1
            while left < right and not lowerCase[right].isalnum():
                right -= 1
            if lowerCase[left] != lowerCase[right]:
                return False
            left += 1
            right -= 1
        return True
                
            