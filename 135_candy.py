class Solution(object):
    def candy(self, ratings):
        
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        candies=[1]*(n)

        for x in range(1,n):
            if ratings[x]>ratings[x-1]: 
                candies[x]=candies[x-1]+1
        

        for y in range(n-2,-1,-1):
            if ratings[y]>ratings[y+1]:
                candies[y]=max(candies[y],candies[y+1]+1)
        
        return sum(candies)

       
        
        
        