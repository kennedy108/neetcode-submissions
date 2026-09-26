class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amount = []
        count = {}
        for i in nums:
            key = i
            if key in count:
                count[key] += 1
            else:
                count[key] = 1
        sort = sorted(count.items(), key = lambda item: item[1], reverse = True)

        for j in range(k):
            amount.append(sort[j][0])


        return amount;
