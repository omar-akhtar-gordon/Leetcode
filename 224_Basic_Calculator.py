class Solution(object):
    def calculate(self, s):
        cur=0
        res=0
        sign=1  
        stack=[]

        for x in s:
            if x.isdigit():
                cur=cur*10+int(x)
            elif x in ["+","-"]:
                res+= sign*cur
                if x=="+":
                    sign=1
                else:
                    sign=-1
                cur=0
            elif x=="(":
                stack.append(res)
                stack.append(sign)
                sign=1
                res=0
            elif x==")":
                res+=sign*cur
                res*= stack.pop()
                res+=stack.pop()
                cur=0
        
        return res+sign*cur