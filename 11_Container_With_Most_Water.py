class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        m=0

        while l<r:
            m=max(min(height[r],height[l])*(r-l),m)

            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        
        return m