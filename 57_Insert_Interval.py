class Solution(object):
    def insert(self, intervals, newInterval):
        res=[]

        if not intervals:
            return [newInterval]

        snew=newInterval[0]
        enew=newInterval[1]
        s=intervals[0][0]
        e=intervals[0][1]
        found=0
        length=len(intervals)

        if intervals[length-1][1]<snew or intervals[0][0]>enew:
            intervals.append([snew,enew])          
            intervals.sort()
            return intervals

        for x in intervals[1:]:
            if found==0:
                if snew<=e:
                    snew=min(snew,s)
                    if enew<=e:
                        enew=e
                        res.append([snew,enew])
                        found+=1
                    elif enew<x[0]:
                        res.append([snew,enew])
                        found+=1
                elif snew<x[0] and enew<x[0]:
                    res.append([s,e])
                    res.append([snew,enew])
                    found+=1

                else:
                    res.append([s,e])
            else:
                res.append([s,e])
            s=x[0]
            e=x[1]

        if found:
            res.append([s,e])
        else:
            res.append([min(snew,s),max(e,enew)])

        return res
            

    