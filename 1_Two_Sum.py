class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        thash={}


        for i,x in enumerate(nums):
            diff=target-x
            if diff in thash:
                return [i,thash[diff]]
            else: 
                thash[x]=i
        return


        