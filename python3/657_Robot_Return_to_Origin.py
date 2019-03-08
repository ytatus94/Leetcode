class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # 建立字典，保存每個方向移動了幾次
        move_counts = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
        for i in moves:
            move_counts[i] += 1
        
        # 如果會回到原點，那要滿足
        # 1. 往上和往下移動的次數要一樣
        # 2. 往左和往右移動的次數要一樣
        if move_counts['U'] != move_counts['D']:
            return False
        if move_counts['L'] != move_counts['R']:
            return False
        
        return True
