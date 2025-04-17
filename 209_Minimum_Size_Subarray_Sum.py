class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        m=float('inf')
        sum=0

        for r in range (0, len(nums)):
            sum=sum+nums[r]
            while sum>=target: 
                m=min(m,(r-l+1))
                sum=sum-nums[l]
                l+=1
        
        if m==float('inf'):
            return 0
        else:
            return m
        

