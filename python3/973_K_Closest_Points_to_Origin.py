class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if points is None or len(points) == 0:
            return []
        hash = {}
        
        for point in points:
            dist_sq = point[0]**2 + point[1]**2
            if dist_sq in hash:
                hash[dist_sq].append(point)
            else:
                hash[dist_sq] = [point]
        
        keys = sorted(list(hash.keys()))
        
        size = len(hash)
        if K > size:
            K = size
        
        res = []
        for key in keys[:K]:
            res += hash[key]
                
        return res
