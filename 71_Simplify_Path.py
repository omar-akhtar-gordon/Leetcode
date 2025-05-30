class Solution(object):
    def simplifyPath(self, path):
        parts=path.split("/")
        
        stack=[]
        for x in parts:
            if x=="." or x=="":
                continue
            elif x=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        
        return "/" + "/".join(stack)
        