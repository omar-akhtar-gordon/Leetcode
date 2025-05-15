class Solution(object):
    def insert(self, intervals, newInterval):
        res=[]

        if not intervals:
            return [newInterval]

        for x in range(len(intervals)):
            if  newInterval[1]< intervals[x][0]:
                res.append(newInterval)
                return res + intervals[x:]
            elif newInterval[0]> intervals[x][1]:
                res.append(intervals[x])
            else:
                newInterval[0]=min(newInterval[0],intervals[x][0])
                newInterval[1]=max(newInterval[1],intervals[x][1])

        res.append(newInterval)



        return res
            

    