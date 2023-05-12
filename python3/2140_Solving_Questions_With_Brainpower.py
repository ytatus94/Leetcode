class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # dp[i] = 解第 i 題以及後面所有問題，所能得到的最高分
        dp = [0] * len(questions)
        # 初始條件:
        # dp[-1] = questions[-1][0] 只解最後一題能得到的分數
        dp[-1] = questions[-1][0]

        # 注意要從倒數第二題開始往回看
        for i in range(len(questions) - 2, -1, -1):
            # 如果從第 i 題開始解 (之前的題目都不解)，那至少會得到 questions[i][0] 的分數
            # 如果要比這分數高，就是後面的題目，能解的都要解
            dp[i] = questions[i][0] # 這也是初始條件

            # 如果跳過 questions[i][1] 題後，依然在範圍內
            if i + questions[i][1] + 1 < len(questions):
                dp[i] += dp[i + questions[i][1] + 1]

            # 要解當前問題，總分 = 解之後題目的總分 + 解這題的分數
            # 不解當前的問題，總分 = 解之後題目的總分
            dp[i] = max(dp[i], dp[i + 1])

        return dp[0]
