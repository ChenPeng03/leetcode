class Points(object):
    def __init__(self,a = 0,b = 0):
        self.x = a
        self.y = b
class Solution(object):
    def maxPoints(self, points):
        if not points:
            return 0
        max_points = 0
        for i in range(len(points)):
            same = 1
            slopes = collections.defaultdict(int)
            start = points[i]
            for j in range(i + 1, len(points)):

                end = points[j]
                slope = float('inf')
                if start.x = end.x and start.y = end.y:
                    same += 1
                elif start.x = end.x:
                    slopes[slope] += 1
                else:
                    slope = (start.y - end.y) * 1.0 / (start.x - end.x)
                    slopes[slope] += 1
            if slope:
                max_points = max(max_points, max(a.values()) + same)
            else:
                max_points = max(max_points, same)
        return max_points
