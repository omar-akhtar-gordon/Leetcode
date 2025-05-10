class Solution:
    def isHappy(self, n: int) -> bool:

        def getsum(num):
            return sum(int(x)**2 for x in str(num))

        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            n=getsum(n)
        return n==1
