class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 先找出每個 R 和 D 的 index
        list_R = []
        list_D = []
        for i in range(len(senate)):
            if senate[i] == 'R':
                list_R.append(i)
            else:
                list_D.append(i)

        # ban 掉後面敵方陣營的 senator 才能讓己方陣營獲勝機率增加
        # 如果後面已經沒有敵方陣營的 senator 了，那就從頭開始 ban
        
        # list_R 和 list_D 中每個元素比較，數字大的要刪除，數字小的留下來進到下一輪
        # 因為要進到下一輪，所以要重新排隊 (把 index 加上 senate 的長度再塞入 list)
        while len(list_R) > 0 and len(list_D) > 0:
            r_idx = list_R.pop(0)
            d_idx = list_D.pop(0)
            if r_idx < d_idx:
                list_R.append(r_idx + len(senate)) # 重新排隊
            else:
                list_D.append(d_idx + len(senate))

        # 離開的時候 list_R 和 list_D 一定有一個長度是 0 了
        if len(list_R) == 0:
            return 'Dire'
        elif len(list_D) == 0:
            return 'Radiant'
