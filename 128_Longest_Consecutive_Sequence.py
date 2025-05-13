class Solution(object):
    def longestConsecutive(self, nums):

        arrset=set(nums)
        maxi=0

        for x in arrset:
            if x-1 not in arrset:
                length=0
                while (x+length) in arrset:
                    length+=1
                    maxi=max(length,maxi)
        
        return maxi



        """
        :type nums: List[int]
        :rtype: int
        """
        