class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res=[]

        if not intervals:
            return res

        intervals.sort()
        s=intervals[0][0]
        e=intervals[0][1]

        for x in intervals[1:]:
            if e>=x[0]:
                e=max(e,x[1])
                s=min(s,x[0])
            else:
                res.append([s,e])
                s=x[0]
                e=x[1]
        res.append([s,e])
        return res




        


        