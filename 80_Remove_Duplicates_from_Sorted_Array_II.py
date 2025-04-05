class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        y=0
        counter=0
        for x in range(1,len(nums)):
            if nums[y]!=nums[x]:
                nums[y+1]=nums[x]
                y+=1
                counter=0            
            elif counter!=1:
                counter+=1
                nums[y+1]=nums[x]
                y+=1 
        return y+1
                