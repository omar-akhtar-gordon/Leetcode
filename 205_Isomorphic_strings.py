class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        mhash={}

        for x in range(len(s)):
            if s[x] in mhash or t[x] in mhash.values():
                if (s[x],t[x]) not in mhash.items():
                    return False
            else:
                mhash[s[x]]=t[x]
        return True
