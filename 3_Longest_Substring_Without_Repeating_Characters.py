class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        m=0
        same=set()
        for r in range (0, len(s)):
            while s[r] in same :
                same.remove(s[l])
                l+=1
                 
            m=max(m, (r-l)+1)
            same.add(s[r])
        return m