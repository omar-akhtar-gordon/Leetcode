class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        phash={}
        splitup=s.split(' ')

        if len(pattern)!=len(splitup):
            return False
        
        if len(set(pattern))!=len(set(splitup)):
            return False

        for x in range(len(pattern)):
            if pattern[x] in phash or splitup[x] in phash.values():
                if (pattern[x],splitup[x]) not in phash.items():
                    return False
            else:
                phash[pattern[x]]=splitup[x]
        return True

