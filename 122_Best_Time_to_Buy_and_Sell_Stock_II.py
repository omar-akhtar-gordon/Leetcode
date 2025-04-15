class Solution(object):
    def maxProfit(self, prices):
        profits=0
        buy=prices[0]
        for x in range(1,len(prices)):
            if buy<prices[x]:
                profits=profits+(prices[x]-buy)
            buy=prices[x]
        return profits