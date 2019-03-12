class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        tot = len(candies) # 有幾顆糖果，妹妹會拿到 tot // 2 顆糖果
        kinds = set(candies) # 有幾種糖果
        
        # 糖果種類數目比妹妹拿到的糖果個數多時，妹妹可以每個糖果都拿不同種類的
        if len(kinds) > tot // 2:
            return tot // 2
        return len(kinds)
