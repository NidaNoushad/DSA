class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p,min_p=nums[0],nums[0]
        res=nums[0]
        for n in nums[1:]:
            max_temp=max(n,n*max_p,n*min_p)
            min_p=min(n,n*max_p,n*min_p)
            max_p=max_temp
            res=max(res,max_p)
        return res