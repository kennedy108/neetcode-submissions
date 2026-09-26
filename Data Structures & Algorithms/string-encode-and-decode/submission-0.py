class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            count = 0
            for char in word:
                count += 1
            amount = str(count) + "#" + word
            result += amount
        return result
    def decode(self, s: str) -> List[str]:
        answer = []
        start = 0
        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1
            amount = s[start:end]
            amount = int(amount)
            word_start = end + 1
            word_end = word_start + amount
            answer.append(s[word_start: word_end])
            start = word_end
        return answer


            
                


