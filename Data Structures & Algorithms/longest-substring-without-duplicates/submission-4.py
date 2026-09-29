class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        right = 0
        left = 0
        arr = set()
        while right < len(s):
            if s[right] not in arr:
                arr.add(s[right])
                if len(arr) > longest:
                    longest = len(arr)
                right += 1
            elif s[right] in arr:
                arr.remove(s[left])
                left += 1

        return longest
