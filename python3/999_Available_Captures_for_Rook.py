class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # 題目已知棋盤是 8x8
        # 先找城堡的座標
        Rx, Ry = 0, 0
        for row in range(8):
            for col in range(8):
                if board[row][col] == 'R':
                    Rx = row
                    Ry = col
                    break
                
        # 開始計算有幾個小兵
        count = 0
        # 往右邊走
        for x in range(Rx + 1, 8):
            if board[x][Ry] != '.':
                if board[x][Ry] == 'p':
                    count += 1
                break # 這樣不論是碰到主教還是小兵都會停下來
        # 往左邊走
        for x in range(Rx - 1, -1, -1):
            if board[x][Ry] != '.':
                if board[x][Ry] == 'p':
                    count += 1
                break
        # 往上走
        for y in range(Ry - 1, -1, -1):
            if board[Rx][y] != '.':
                if board[Rx][y] == 'p':
                    count += 1
                break
        # 往下走
        for y in range(Ry + 1, 8):
            if board[Rx][y] != '.':
                if board[Rx][y] == 'p':
                    count += 1
                break

        return count
