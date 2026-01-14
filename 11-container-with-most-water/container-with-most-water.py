class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea=0
        l,r=0,len(height)-1

        while l<r:
            h=min(height[l],height[r])
            w=r-l
            area=h*w
            maxarea=max(maxarea,area)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return maxarea
            
        