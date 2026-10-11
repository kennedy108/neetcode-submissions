class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t) or len(s) < len(t):
            return False
        apl = [0] * 26
        for i in s:
            apl[ord(i) - ord('a')] = apl[ord(i) - ord('a')] + 1
        for j in t:
            apl[ord(j) - ord('a')] = apl[ord(j) - ord('a')] - 1

        if apl == [0] * 26:
            return True

        return False