class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        for i in range(0, len(nums)):
            for j, num in enumerate(nums):
                if i != j:
                    products[i] *= num
        return products