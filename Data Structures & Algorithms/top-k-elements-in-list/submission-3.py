class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        return list(entry[0] for entry in sorted(counter.items(), key=lambda entry: entry[1], reverse=True))[0:k]
