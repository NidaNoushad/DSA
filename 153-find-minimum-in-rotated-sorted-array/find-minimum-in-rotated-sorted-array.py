class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]


        # res=nums[0]
        # l=0
        # r=len(nums)-1
     
        # while l<=r:
        #     if nums[l]<nums[r]:
        #         res=min(res,nums[l])
        #         break

        #     m=(l+r)//2
        #     res=min(res,nums[m])
        #     if nums[l]<=nums[m]:
        #         #go to right as left is sorted ,go to unsorted part
        #         l=m+1
        #     else:
        #         #go to left aa right is sorted,go to unsorted part ,in that part min is present
        #         r=m-1
        # return res

        