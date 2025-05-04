class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        m=defaultdict(int)

        for x in magazine: 
            m[x]+=1
        
        for y in ransomNote:
            if y not in m or m[y]<=0:
                return False
            m[y]-=1
        return True