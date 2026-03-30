class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        nums.sort()
        print(nums)
        longest = 0
        sequence = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] - 1:
                sequence += 1
                print(nums[i], nums[i + 1], sequence)
            elif nums[i] == nums[i + 1]:
                continue
            else:
                longest = max(longest, sequence)
                sequence = 1
        longest = max(longest, sequence)
        return longest