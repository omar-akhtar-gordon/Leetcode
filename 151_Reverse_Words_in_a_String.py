class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s=s.strip()
        words= s.split()
        reverse=words[::-1]
        
        return " ".join(reverse)