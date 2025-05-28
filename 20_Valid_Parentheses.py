class Solution(object):
    def isValid(self, s):
        mapping={"}":"{",")":"(","]":"["}
        stack=[]

        for x in s:
            if x in mapping.values():
                stack.append(x)
            elif x in mapping.keys():
                if not stack or mapping[x]!=stack.pop():
                    return False   

        return not stack