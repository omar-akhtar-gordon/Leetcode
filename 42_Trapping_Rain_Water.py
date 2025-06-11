class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left=[0]*n
        right=[0]*n
        water=0
        left[0]=height[0]

        for x in range(1,n):
            left[x]=max(left[x-1],height[x])

        right[n-1]=height[n-1]
        for y in range(n-2,-1,-1):
            right[y]= max(right[y+1],height[y]) 

        for z in range(n):
            water+= min(left[z],right[z])-height[z]
        return water 