class Solution(object):
    def findMinArrowShots(self, points):
        
        arrows=1
        points.sort(key=lambda x: x[1])
        last=points[0][1]

        for s,e in points:
            if s>last:
                arrows+=1
                last=e
        return arrows

                        



      

        