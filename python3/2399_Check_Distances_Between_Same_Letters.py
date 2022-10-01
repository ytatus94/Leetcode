class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        hash_map = {}
        diff = {}
        for i, v in enumerate(s):
            if v in hash_map:
                diff[v] = i - hash_map[v] - 1
            else:
                hash_map[v] = i
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for k, v in diff.items():
            if diff[k] != distance[alphabet.find(k)]:
                return False
        
        return True
