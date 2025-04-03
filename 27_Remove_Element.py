class Solution(object):
    def removeElement(self, nums, val):
        p=0
        
        for x in nums:
            if x!=val:
                
                nums[p]=x
                p+=1
            
        return p