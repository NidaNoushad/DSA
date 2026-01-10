class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target == nums[mid]:
                return mid
            if nums[mid]>=nums[l]:
                #left
                if target<nums[l] or target>nums[mid]:
                    #go to right
                    l=mid+1
                else:
                    # stay in left
                    r=mid-1
            else:
                #right
                if target>nums[r] or target<nums[mid]:
                    #go to left
                    r=mid-1
                else:
                    # stay in right
                    l=mid+1
        return -1


       




            
        