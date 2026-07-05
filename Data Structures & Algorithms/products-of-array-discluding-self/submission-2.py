class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for idx,i in enumerate(nums):
            pop_nums = nums.copy()
            # print( pop_nums, nums)
            pop_nums.pop(idx)
            # print(pop_nums)
            product = 1
            for j in pop_nums:
                product = product * j
            ans.append(product)
            
        return ans

        