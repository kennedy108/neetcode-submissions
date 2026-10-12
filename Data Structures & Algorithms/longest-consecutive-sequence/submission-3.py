class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numset = set(nums)
        start = 0
        longest = 1
        for i in numset:
            if i - 1 not in numset:
                count = 1
                start = i
                while start + 1 in numset:
                    count += 1
                    start += 1
                if count > longest:
                    longest = count
        return longest