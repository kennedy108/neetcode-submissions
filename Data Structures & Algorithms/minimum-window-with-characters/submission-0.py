class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for char in t:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        left = 0
        right = 0
        window = {}
        required = len(count)
        formed = 0
        min_length = float('inf')
        start = 0
        while (right < len(s)):
            if s[right] not in window:
                window[s[right]] = 1
            else:
                window[s[right]] += 1
            if s[right] in count:
                if window[s[right]] == count[s[right]]:
                    formed += 1
            right += 1
            while (required == formed):
                length = right - left
                if length < min_length:
                    min_length = length
                    start = left
                window[s[left]] -= 1
                if s[left] in count and window[s[left]] < count[s[left]]:
                    formed -= 1
                left += 1
        if min_length == float("inf"):
            return ""
        end = start + min_length
        return s[start:end]
            
