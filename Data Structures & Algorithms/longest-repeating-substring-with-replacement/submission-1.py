class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        count = 0
        arr = [0] * 26
        for right in range(len(s)):
            arr[ord(s[right]) - ord("A")] += 1
            count = right - left + 1
            most = max(arr)
            while count - most > k:
                arr[ord(s[left]) - ord("A")] -= 1
                left += 1
                count = right - left + 1
                most = max(arr)
            if count > longest:
                longest = count
        return longest

