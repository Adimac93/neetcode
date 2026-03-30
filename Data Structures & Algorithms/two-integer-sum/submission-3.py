class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for i, num in enumerate(nums):
            if num in lookup:
                lookup[num].append(i)
            else:
                lookup[num] = [i]
        print(lookup)
        for i, num in enumerate(nums):
            diff = target - num
            print(f"diff {diff}")
            if diff in lookup:
                for j in lookup[diff]:
                    if j != i:
                        return [i, j]
        return []