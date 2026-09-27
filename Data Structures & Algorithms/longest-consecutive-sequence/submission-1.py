class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        beginning = 0
        longest = 1
        for smallest in numSet:
            if smallest - 1 not in numSet:
                counter = 1
                beginning = smallest
                while beginning + 1 in numSet:
                    counter += 1
                    beginning += 1
                if counter > longest:
                    longest = counter
        return longest