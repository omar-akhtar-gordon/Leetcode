class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for x in tokens:
            if x=="+":
                stack.append(stack.pop()+stack.pop())
            elif x=="-":
                second,first=stack.pop(),stack.pop() 
                stack.append(first-second)
            elif x=="/":
                second,first=stack.pop(),stack.pop() 
                stack.append(int(first/second))
            elif x=="*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(x))
        return stack[0]
