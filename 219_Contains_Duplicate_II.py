class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seenhash={}

        for i,x in enumerate(nums):
            if x not in seenhash:
                seenhash[x]=i
            else:
                if abs(seenhash[x]-i)<=k:
                    return True
                else:
                    seenhash[x]=i
            
        return False
        