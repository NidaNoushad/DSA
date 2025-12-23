class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax,currmin=1,1
        res=nums[0]
        for n in nums:
            temp=currmax*n
            currmax=max(temp,currmin*n,n)
            currmin=min(temp,currmin*n,n)
            res=max(res,currmax)
        return res