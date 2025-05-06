class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ahash=defaultdict(int)

        if len(s)!=len(t):
            return False

        for x in s:
            ahash[x]+=1
        
        for x in t:
            if x not in ahash:
                return False
            elif ahash[x]<1:
                return False
            else:
                ahash[x]-=1
        return True






        