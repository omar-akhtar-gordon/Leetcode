class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]   
        profit=0
        for x in range(1,len(prices)):
            if buy>prices[x]:
                buy=prices[x]
            elif prices[x]-buy>profit:
                profit=prices[x]-buy
        return profit