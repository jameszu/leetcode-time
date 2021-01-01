class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        lenz = len(points)
        if lenz == 0:
            return 0
        
        points.sort(key=lambda key : key[1])
        starting = points[0][1]
        count = 1
        i = 0
        while i < lenz:
            

            if starting >= points[i][0]:
                i += 1
                continue
            count += 1
            starting = points[i][1]
            i += 1
        return count
            