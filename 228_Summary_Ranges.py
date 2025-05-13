class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res=[]

        if not nums:
            return []
        
        s=nums[0]
        e=nums[0]

        for x in nums[1:]:
            if x==e+1:
                e=x
            else:
                if s==e:
                    res.append(str(e))
                else:
                    res.append(str(s) + "->" + str(e))
                
                s=x
                e=x
        if s==e:
            res.append(str(e))
        else:
            res.append(str(s) + "->" + str(e))
        
        return res



        