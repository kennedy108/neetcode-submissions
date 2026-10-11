class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            alp = [0]*26
            for j in i:
                alp[ord(j) - ord('a')] = alp[ord(j) - ord('a')] + 1
            result[tuple(alp)].append(i)
        return list(result.values())