class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff=[]
        total=0
        for x in range(len(gas)):
            diff.append(gas[x]-cost[x])
            total+=diff[x]
        
        if total<0:
            return -1
    
    
        move=diff[0]
        pos=0

        for d in range(1,len(diff)):
            if move<0:
                move=diff[d]
                pos=d
            else:
                move+=diff[d]
        return pos


             

        

        
        

        