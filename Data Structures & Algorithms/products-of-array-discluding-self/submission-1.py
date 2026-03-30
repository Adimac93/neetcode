class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num:
                product *= num
            else:
                zero_count += 1
        if zero_count > 1: return [0] * len(nums)
        products = []
        for num in nums:
            if zero_count:
                if num:
                    products.append(0)
                else:
                    products.append(product)
            else:
                products.append(product // num)
            
        return products