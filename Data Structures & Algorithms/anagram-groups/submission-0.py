class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amount = {}
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord("a")] = count[ord(j) - ord("a")] + 1
            key = tuple(count)
            if key in amount:
                amount[key].append(i)
            else:
                amount[key] =[i]
        return list(amount.values())


