class Solution(object):
    def threeSum(self, nums):

        result=[]

        nums.sort()

        
        for x in range(len(nums)):
            if x>0 and nums[x]==nums[x-1]:
                continue
            
            y=x+1
            z=len(nums)-1

            while y<z:
                total=nums[x]+nums[y]+nums[z]

                if total>0:
                    z-=1
                elif total<0:
                    y+=1
                else:
                    result.append([nums[x],nums[y],nums[z]])
                    y+=1

                    while nums[y]==nums[y-1] and y<z:
                        y+=1
            

        return result



        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """