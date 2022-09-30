class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = list(zip(names, heights))
        sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
        # 用這個比較慢
        # names_descending = [n for n, h in l]
        # return names_descending
        
        # 用這個快一點
        names_descending = list(zip(*sorted_data))
        return names_descending[0]
