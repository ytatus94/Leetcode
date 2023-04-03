# 九章動態規劃

### 依據題目的形式，可以分成
  * **座標型**:
    * `f[i]` 就是以 $a_{i}$ **結尾**的性質，`f[i][j]` 就是格子 (i, j) 的性質。
    * 初始條件 `f[0]` 就是以 $a_{0}$ 結尾的性質
    * **最長序列型**和**雙序列型**其實是**座標型**
      * 都是開二維數組`f = (m + 1)*(n + 1)` 數組 (要 +1 才能包含到最後一個元素)
        * `for i 從 0 到 m`, `for j 從 0 到 n` 要包含 `m` 與 `n`
      * 雙序列型要有"對子"的觀念，兩個序列的元素組成一個對子
      * 初始條件要寫幾個例子來推斷
        * 空字串時要如何處理?
      * 最長序列型都是從**最後一個字元**開始考慮
      * 不同情形要考慮清楚，如果需要加 1 時，不要忘記 
  * **序列型**:
    * `f[i]` 是**前 i 個元素 a[0]...a[i-1]** 的某種性質
    * 初始條件 `f[0]` 就是空序列 (前 0 個元素) 的性質
    * 序列 + 狀態型 DP: 最後一步會依賴於前一步的某種狀態
  * **劃分型**:
    * 不指定段數: `f[i]` = 前 i 個元素分段後的可行性或是最值
    * 指定段數: `f[i][j]` = 前 i 個元素分成 j 段後的可行性或是最值
  * **區間型**: 對序列或字符串做操作，處理一個區間
    * `f[i][j]` 就是區間 i 到 j 
    * 可以分成: 去頭，去尾，去頭又去尾
    * 區間型的子問題，是指**長度越來越短**，要按照`長度 j-i` 從小到大的順序去計算
    * 比較適合用記憶化搜索的方式
    * 如果題目是消去型的 (例如消去中間一個剩左右兩邊)，那要從最後一步倒過來想 (就是最後一個被消去的)
  * **背包型**:
    * 背包型動態規劃，**一定要把總承重放入狀態**
      * 如果物品的順序存在，就要考慮最後一個物品會不會放進背包
      * 如果物品的順序不存在，就沒有所謂的最後一個物品，因此要考慮的是誰是最後一個物品 
      * 要注意最後一個放進背包的物品是哪一個，還有最後一個物品有沒有放進背包
      * 當物品的數目無限多的時候，就以**種類**來計算
    * 可行性: `f[i][w]` = 前 i 個物品能不能拼出 w
    * 計數型: `f[i][w]` = 前 i 個物品有多少種方式能拼出 w
  * **最長序列型**: 是一種座標型 DP
  * **博弈型**:
    * 輪到誰，誰就是先手
    * 對方必輸，就是先手必勝
  * **綜合型**

### 依據題目要求的答案，可以分成
  * **計數型**
    * 求有多少種方式
  * **最值型**
    * 求最大值或最小值 
  * **存在型 (可行性)**
    * 求是否存在，或是能不能幹嘛 

### DP 的組成部分
  1. 確定狀態
     - 最後一步
     - 子問題 (縮小規模)
     - 定義狀態
  2. 轉移方程
     - 根據狀態推得 
  3. 初始值與邊界條件
     - 要細心考慮周全
  4. 計算順序 

### DP 可以用遞推與記憶化搜索的方式
  * 遞推:
    * 由下往上: `f[0]`, `f[1]`, ..., `f[N]` 中括號是因為 `f` 是陣列
    * 可以空間優化
  * 記憶化搜索
    * 由上往下: `f(N)`, `f(N-1)`, ... 圓括號是因為 `f` 是函數
    * 比較簡單好寫
    * 無法做空間優化

## Ch1

### Examples (4 題)

|Type|LeetCode No|LintCode No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|:---|
|最值型|322|669|[Coin Change](https://www.lintcode.com/problem/669/)|Medium|[https://www.jiuzhang.com/solution/coin-change/](https://www.jiuzhang.com/solution/coin-change/)|
|計數型|62|114|[Unique Paths](https://www.lintcode.com/problem/114/)|Easy|[http://www.jiuzhang.com/solutions/unique-paths/](http://www.jiuzhang.com/solutions/unique-paths/)|
|存在型|55|116|[Jump Game](https://www.lintcode.com/problem/116/)|Medium|[http://www.jiuzhang.com/solutions/jump-game/](http://www.jiuzhang.com/solutions/jump-game/)|
|最值型|152|191|[Maximum Product Subarray](https://www.lintcode.com/problem/191/)|Medium|[http://www.jiuzhang.com/solutions/maximum-product-subarray/](http://www.jiuzhang.com/solutions/maximum-product-subarray/)|

#### 轉移方程
* 669 Coin Change
  * `f[X] = min{f[X-2]+1, f[X-5]+1, f[X-7]+1}`
    - `f[x]` 拼出 x 所需的最少硬幣數目
    - `f[x-2]+1` 拼出 x-2 所需的最少硬幣數目，再加上最後一枚 2 元的硬幣
    - `f[x-5]+1` 拼出 x-5 所需的最少硬幣數目，再加上最後一枚 5 元的硬幣
    - `f[x-5]+1` 拼出 x-7 所需的最少硬幣數目，再加上最後一枚 7 元的硬幣
* 114 Unique Paths
  * `f[i][j] = f[i-1][j] + f[i][j-1]`
    - `f[i][j]` 有多少種方式走到 (i, j)
    - `f[i-1][j]` 有多少種方式走到 (i-1, j)
    - `f[i][j-1]` 有多少種方式走到 (i, j-1)
    - 要注意第一 row 只能從左邊走過來，第一 column 只能從上面走過來
* 116 Jump Game
  * `f[j] = OR_{0<=i<j} (f[i] AND i + a[i] >= j)`
    - `f[j]` 能不能跳到石頭 j
    - `0<=i<j` 枚舉上一個跳到的石頭 i
    - `f[i]` 能不能跳到石頭 i
    - `i + a[i] >= j` 最後一跳的距離不能超過 a[i]
  * 這一題用 DP 會超時，要用貪心法才會不超時
    - 記錄在每個 index 上時，所能跳的最大距離，然後打擂台
* 191 Maximum Product Subarray
  * `f[j] = max{ a[j], max{ a[j]*f[j-1], a[j]*g[j-1] }| j>0 }`
    - `f[j]` 以 a[j] 結尾的連續子序列的最大乘積
    - 情況1. `a[j]` 子序列就是 a[j] 自己而已
    - 情況2. `max{ a[j]*f[j-1], a[j]*g[j-1] }| j>0` 以 a[j-1] 結尾的連續子序列最大或最小乘積，再乘上 a[j]
  * `g[j] = min{ a[j], min{ a[j]*f[j-1], a[j]*g[j-1] }| j>0 }`
    - `g[j]` 以 a[j] 結尾的連續子序列的最小乘積
    - 情況1. `a[j]` 子序列就是 a[j] 自己而已
    - 情況2. `min{ a[j]*f[j-1], a[j]*g[j-1] }| j>0` 以 a[j-1] 結尾的連續子序列最大或最小乘積，再乘上 a[j]

## Ch2

### Examples (7 題)

|Type|LeetCode No|LintCode No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|:---|
|座標型, 計數型|63|115|[Unique Paths II](https://www.lintcode.com/problem/115/)|Easy|[http://www.jiuzhang.com/solutions/unique-paths-ii/](http://www.jiuzhang.com/solutions/unique-paths-ii/)|
|序列型, 最值型|256 (鎖)|515|[Paint House](https://www.lintcode.com/problem/515/)|Medium|[https://www.jiuzhang.com/solution/paint-house/](https://www.jiuzhang.com/solution/paint-house/)|
|劃分型, 計數型|91|512|[Decode Ways](https://www.lintcode.com/problem/512/)|Medium|[http://www.jiuzhang.com/solutions/decode-ways/](http://www.jiuzhang.com/solutions/decode-ways/)|
|座標型, 計數型|674|397|[Longest Increasing Continuous Subsequence](https://www.lintcode.com/problem/397/)|Easy|[http://www.jiuzhang.com/solutions/longest-increasing-continuous-subsequence/](http://www.jiuzhang.com/solutions/longest-increasing-continuous-subsequence/)|
|座標型, 最值型|64|110|[Minimum Path Sum](https://www.lintcode.com/problem/110/)|Easy|[http://www.jiuzhang.com/solutions/minimum-path-sum/](http://www.jiuzhang.com/solutions/minimum-path-sum/)|
|座標型, 最值型|361 (鎖)|553|[Bomb Enemy](https://www.lintcode.com/problem/553/)|Medium|[http://www.jiuzhang.com/solutions/bomb-enemy/](http://www.jiuzhang.com/solutions/bomb-enemy/)|
|位操作型, 計數型|338|664 (鎖)|[Counting Bits](https://www.lintcode.com/problem/664/) (鎖住了)|Medium|[https://www.jiuzhang.com/solutions/counting-bits/](https://www.jiuzhang.com/solutions/counting-bits/)|

#### 轉移方程
* 115 Unique Paths II
  ```
            ┌ 0, 如果 (i, j) 是障礙
            ├ 1, (i, j)=(0, 0)
  f[i][j] = ├ f[i-1][j], 如果 j=1, 即 first column
            ├ f[i][j-1], 如果 i=1, 即 first row
            └ f[i-1][j] + f[i][j-1], 其他情況
  ```
    - `f[i][j]` 有多少種方式走到 (i, j)
    - `f[i-1][j]` 有多少種方式走到 (i-1, j)
    - `f[i][j-1]` 有多少種方式走到 (i, j-1) 
* 515 Paint House
  * 先看漆成紅色 `f[i][0] = min{f[i-1][1] + cost[i-1][0], f[i-1][2] + cost[i-1][0]}`
    - `f[i][0]` 油漆前 i 棟房子並且房子 i-1 是紅色的最小花費  
    - `f[i-1][1] + cost[i-1][0]` 油漆前 i-1 棟房子並且房子 i-2 是藍色的最小花費，加上油漆房子 i-1 的花費
    - `f[i-1][2] + cost[i-1][0]` 油漆前 i-1 棟房子並且房子 i-2 是綠色的最小花費，加上油漆房子 i-1 的花費
    - 房子編號從 0 開始，油漆前 i 棟房子，那最後一棟的編號是 i-1
  * 同理應用到藍色和綠色
    - `f[i][1] = min{f[i-1][0] + cost[i-1][1], f[i-1][2] + cost[i-1][1]}`
    - `f[i][2] = min{f[i-1][0] + cost[i-1][2], f[i-1][1] + cost[i-1][2]}`
* 512 Decode Ways
  * `f[i] = f[i-1]|S[i-1] 對應一個字母 + f[i-2]|S[i-2]S[i-1]對應一個字母`
    - `f[i]` 數字串 s 的前 i 個數字解密成字母串的方式數
    - 注意 s="0X" 的時候無法解密，因為 "0X" 和 "X" 不同
    - 因為是前 1 個元素 S[i-1] 或前 2 個元素 S[i-2][i-1] 分段，所以是劃分型
* 397 Longest Increasing Continuous Subsequence
  * `f[j] = max{ 1, f[j–1]+1| j>0 and a[j-1] < a[j]}`
    - `f[j]` 以 a[j] 結尾的最長連續上升子序列的長度
    - 情況1. 子序列就是 a[j] 本身
    - 情況2. 以 a[j-1] 結尾的最長連續上升子序列的長度，再加上 a[j] 一個
  * 開兩個數紀錄當前長度，和最大長度，然後打擂台。
* 110 Minimum Path Sum
  * 其實就是 Unique Path 的變形 
  * `f[i][j] = min{f[i-1][j], f[i][j-1]} + A[i][j]`
    - `f[i][j]` 從 (0, 0) 走到 (i, j) 的最小路徑數字和
* 553 Bomb Enemy
  ```
             ┌ up[i-1][j], 如果 (i, j) 是空地
  up[i][j] = ├ up[i-1][j]+1, 如果 (i, j) 是敵人
             └ 0, 如果 (i, j) 是牆
  ```
    - `up[i][j]` 表示在 (i, j) 上放炸彈，往上方可以炸死多少敵人
  * 要用同樣的方式推廣至 `down[i][j]`, `left[i][j]`, `right[i][j]`
  * 如果 (i, j) 是空地，放炸彈能炸死最多的敵人數 = up[i][j] + down[i][j] + left[i][j] + right[i][j]
    * 最後在計算炸死最多的人的時候，只要看"空地"
  * 開數組時要用 f = [[0 for col in range(cols)] for row in range(rows)] 不要用 f = [[0] * cols] * rows，因為後者的 [0] * cols 的記憶體是連再一起的
* 664 Counting Bits
  * `f[i] = f[i >> 1] + (i mod 2)`
    - `f[i]` 表示 i 的二進制中有多少個 1
    - `f[i >> 1]` 表示 i 的二進制中去掉最後一個數之後有多少個 1, i>>1 表示右移一位
    - `i mod 2` i 的二進制中的最後一位

## Ch3

### Examples (9 題)

|Type|LeetCode No|LintCode No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|:---|
|序列＋狀態型, 最值型|265 (鎖)|516|[Paint House II](https://www.lintcode.com/problem/516/)|hard|[http://www.jiuzhang.com/solutions/paint-house-ii/](http://www.jiuzhang.com/solutions/paint-house-ii/)|
|序列＋狀態型, 最值型|198|392|[House Robber](https://www.lintcode.com/problem/392/)|Medium|[http://www.jiuzhang.com/solutions/house-robber/](http://www.jiuzhang.com/solutions/house-robber/)|
|序列＋狀態型, 最值型|213|534|[House Robber II](https://www.lintcode.com/problem/534/)|Medium|[http://www.jiuzhang.com/solutions/house-robber-ii/](http://www.jiuzhang.com/solutions/house-robber-ii/)|
|序列型, 最值型|121|149|[Best Time To Buy And Sell Stock](https://www.lintcode.com/problem/149/)|Medium|[http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock/](http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock/)|
|序列型, 最值型|122|150|[Best Time To Buy And Sell Stock II](https://www.lintcode.com/problem/150/)|Medium|[http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-ii/](http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-ii/)|
|序列＋狀態型, 最值型|123|151|[Best Time To Buy And Sell Stock III](https://www.lintcode.com/problem/151/)|Medium|[http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iii/](http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iii/)|
|序列型, 最值型|188|393|[Best Time To Buy And Sell Stock IV](https://www.lintcode.com/problem/393/)|Medium|[http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iv/](http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iv/)|
|最長序列型, |300|76|[Longest Increasing Subsequence](https://www.lintcode.com/problem/76/)|Medium|[http://www.jiuzhang.com/solutions/longest-increasing-subsequence/](http://www.jiuzhang.com/solutions/longest-increasing-subsequence/)|
|最長序列型, |354|602|[Russian Doll Envelopes](https://www.lintcode.com/problem/602/)|hard|[http://www.jiuzhang.com/solutions/russian-doll-envelopes/](http://www.jiuzhang.com/solutions/russian-doll-envelopes/)|

* 602 Russian Doll Envelopes 會超時

#### 轉移方程
* 516 Paint House II
  * `f[i][j] = min_{k!=j} { f[i-1][k] } + cost[i-1][j]` 
    * `f[i][j]` 油漆前 i 棟房子，且房子 i-1 是顏色 j 的最小花費
    * `min_{k!=j} { f[i-1][k] }` 油漆前 i-1 棟房子，且房子 i-2 不是顏色 j 的最小花費
    * `cost[i-1][j]` 油漆房子 i-1 的花費
  * 要記錄最小值和次小值，不然用上面的轉移方程算會超時
    * 房子 i-2 和 i-1 的顏色不可以一樣，所以在 loop 房子 i-2 的顏色時 
      * 只要房子 i-2 的顏色和 i-1 的顏色不同，就用最小值
      * 如果房子 i-2 的顏色和 i-1 的顏色相同，這個顏色要排除，所以就用次小值 
* 392 House Robber
  * `f[i] = max{ f[i-1], f[i-2] + A[i-1] }` 
    - 情況1. 不偷房子 i-1 `f[i][0] = max{ f[i-1][0], f[i-1][1] }` 此時房子 i-2 可偷可不偷
    - 情況2. 偷房子 i-1 `f[i][1] = f[i-1][0] + A[i-1]` 此時房子 i-2 不能偷
    - 房子編號從 0 開始，偷前 i 棟房子，那最後一棟的編號是 i-1
* 534 House Robber II
  * 因為環狀，所以房子 0 和 N-1 相連，其中一個必須不偷 
  * 情況1. 沒偷房子 0 變成 1...N-1 的 House Robber
  * 情況2. 沒偷房子 N-1 變成 0...N-2 的 House Robber
* 149 Best Time To Buy And Sell Stock
  * 枚舉第 j 天賣出 $0 \le j \le N-1$，時刻保存最低價格 $P_{i}$, 最大獲利 = $P_{j} - P_{i}$
  * `f[i] = min(f[i], prices[i] - prices[j])`
    * `f[i]` = 第 i 天賣的最大獲利
    * `f[0] = 0`, `f[1] = 0` 第一天買又第一天賣，賺到 0 元
* 150 Best Time To Buy And Sell Stock II
  * 每天手上只持有一個股票，拆解成每日交易，今天買明天賣
    * (第 1 天買，第 3 天賣)，可以理解成和 (第 1 天買，第 2 天賣，第 2 天再買回來，第 3 天賣) 等價 
* 151 Best Time To Buy And Sell Stock III
  * 手中無股票 `f[i][j] = max{ f[i-1][j], f[i-1][j-1] + $P_{i-1}$ – $P_{i-2}$ }`
    - `f[i][j]` 前 i 天 (第 i-1 天) 結束後，在階段 j 的最大獲利
    - `f[i-1][j]` 昨天手上沒有股票
    - `f[i-1][j-1] + $P_{i-1}$ – $P_{i-2}$` 昨天手上有股票，今天賣出清倉
  * 手上有股票 `f[i][j] = max{ f[i-1][j] + $P_{i-1}$ – $P_{i-2}$, f[i-1][j-1] }`
    - `f[i-1][j] + $P_{i-1}$ – $P_{i-2}$` 昨天就持有股票，並且繼續持有並獲利
    - `f[i-1][j-1]` 昨天手上沒有股票，今天買入
* 393 Best Time To Buy And Sell Stock IV
  * 能買賣 k 次，所以會有 2k + 1 個狀態
    * 基本上就是 Best Time To Buy And Sell Stock III 的推廣
    * 但是照 Best Time To Buy And Sell Stock III 的方式會超時，用滾動數組才不會超時
  * 手中無股票 `f[i][j] = max{ f[i-1][j], f[i-1][j-1] + $P_{i-1}$ – $P_{i-2}$ }`
  * 手上有股票 `f[i][j] = max{ f[i-1][j] + $P_{i-1}$ – $P_{i-2}$, f[i-1][j-1] }`
* 76 Longest Increasing Subsequence
  * 簡寫為 LIS 
  * `f[j]=max{ 1, f[i]+1 | i<j and a[i]<a[j] }`
    - `f[j]` 以 a[j] 結尾的最長上升子序列的長度
    - 情況1. `1` 子序列就是 a[j] 本身
    - 情況2. `f[i]+1 | i<j and a[i]<a[j]` 以 a[i] 結尾的最長上升子序列的長度，再加上 a[j] 一個
* 602 Russian Doll Envelopes
  * 其實是 LIS 的 2 維版本，但是照 LIS 的方法會超時
  * `f[i] = max{ 1, f[j]+1 | Ej 能放在 Ei 裡面, j<i }`
    - `f[i]` 以 Ei 為最外層信封時，最多的嵌套層數
    - 情況1. `1` 只有 Ei 這個信封
    - 情況2. `f[j]+1 | Ej 能放在 Ei 裡面` 以 Ej 為次外層信封時，最多的嵌套層數，再加上 Ei

## Ch4

### Examples (7 題)

|Type|LeetCode No|LintCode No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|:---|
|劃分型, 最值型|279|513|[Perfect Squares](http://www.lintcode.com/problem/513/)|Medium|[http://www.jiuzhang.com/solutions/perfect-squares/](http://www.jiuzhang.com/solutions/perfect-squares/)|
|劃分型, 最值型|132|108|[Palindrome Partitioning II](https://www.lintcode.com/problem/108/)|Medium|[http://www.jiuzhang.com/solutions/palindrome-partitioning-ii/](http://www.jiuzhang.com/solutions/palindrome-partitioning-ii/)|
|劃分型, 最值型|not found|437|[Copy Books](https://www.lintcode.com/problem/437/)|Medium|[http://www.jiuzhang.com/solutions/copy-books/](http://www.jiuzhang.com/solutions/copy-books/)|
|博弈型, 存在型|not found|394|[Coins in A Line](https://www.lintcode.com/problem/394/)|Medium|[http://www.jiuzhang.com/solutions/coins-in-a-line/](http://www.jiuzhang.com/solutions/coins-in-a-line/)|
|背包型, 可行性|not found|92|[Backpack](https://www.lintcode.com/problem/92/)|Medium|[http://www.jiuzhang.com/solutions/backpack/](http://www.jiuzhang.com/solutions/backpack/)|
|背包型, 計數型|not found|563|[Backpack V](https://www.lintcode.com/problem/563/)|Medium|[http://www.jiuzhang.com/solutions/backpack-v/](http://www.jiuzhang.com/solutions/backpack-v/)|
|背包型, 計數型|not found|564|[Backpack VI](http://www.lintcode.com/564/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/backpack-vi/](http://www.jiuzhang.com/solutions/backpack-vi/)|

* 513 會 Memory Limit Exceeded
* 437 會超時
* 564 不知道寫得對不對

#### 轉移方程
* 513 Perfect Squares
  * `f[i] = min_{1<=j*j<=i}{f[i-j2] + 1}`
    - `f[i]` 表示 i 最少被分成幾個完全平方數之和
    - `1<=j*j<=i` 最後一個完全平方數是 $j^{2}$
* 108 Palindrome Partitioning II
  * `f[i] = min_{j=0,...,i-1}{f[j] + 1| S[j..i-1] 是回文串}`
    - `f[i]` s 的前 i 個字元 s[0...i-1] 最少可以劃分成幾個回文串
* 437 Copy Books
  * `f[k][i] = min_{j=0,...,i}{max{f[k-1][j], A[j] +... +A[i-1]}}`
    - `f[k][i]` k 個抄寫員需要多少時間抄完前 i 本書
    - `A[j] +... +A[i-1]` 第 k 個抄寫員抄完第 j 本書到第 i-1 本書所需的時間
* 394 Coins in A Line
  ```
  f[i] = ┌ True, f[i-1]=False && f[i-2]=False 先手拿一顆或兩顆都必勝
         ├ True, f[i-1]=False && f[i-2]=True, 先手拿一顆必勝
         ├ True, f[i-1]=True && f[i-2]=False, 先手拿兩顆必勝
         └ False, f[i-1]=True && f[i-2]=True, 先手必敗
  ```
  * 整理後可得 `f[i] = f[i-1] == FALSE OR f[i-2] == FALSE`
    - `f[i]` 表示剩下 i 顆石子時，先手是否必勝 
* 92 Backpack
  * `f[i][w] = f[i-1][w] OR f[i-1][w-$A_{i-1}$]`
    - `f[i][w]` 能否用前 i 個物品拼出重量 w
    - 情況1. 如果用前 n-1 個物品能拼出 w, 那用前 n 個物品也能拼出 w
    - 情況2. 如果前 n-1 個物品只能拼出 w-$A_{n-1}$，再加上最後的物品 $A_{n-1}$ 就能拼出 w
* 563 Backpack V
  * `f[i][w] = f[i-1][w] + f[i-1][w-$A_{i-1}$]`
    - `f[i][w]` 用前 i 個物品拼出重量 w 有多少種方式
* 564 Backpack VI
  * `f[i] = f[i-$A_{0}$] + f[i-$A_{1}$] +...+ f[i-$A_{N-1}$]`
    - `f[i]` 有多少種組合能拼出重量 i

## Ch5

### Examples (6 題)

|Type|LeetCode No|LintCode No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|:---|
|背包型, 最值型|not found|125|[Backpack II](https://www.lintcode.com/problem/125/)|Medium|[http://www.jiuzhang.com/solutions/backpack-ii/](http://www.jiuzhang.com/solutions/backpack-ii/)|
|背包型, 最值型|not found|440|[Backpack III](https://www.lintcode.com/problem/440/)|Medium|[http://www.jiuzhang.com/solutions/backpack-iii/](http://www.jiuzhang.com/solutions/backpack-iii/)|
|區間型|516|667|[Longest Palindromic Subsequence](https://www.lintcode.com/problem/667/)|Medium|[https://www.jiuzhang.com/solution/longest-palindromic-subsequence/](https://www.jiuzhang.com/solution/longest-palindromic-subsequence/)|
|博弈型, 存在型|396|[Coins In A Line III](https://www.lintcode.com/problem/396/) (鎖住了)|Hard|[http://www.jiuzhang.com/solution/coins-in-a-line-iii/](http://www.jiuzhang.com/solution/coins-in-a-line-iii/)|
|區間型, |87|430|[Scramble String](https://www.lintcode.com/problem/430/)|Hard|[http://www.jiuzhang.com/solutions/scramble-string/](http://www.jiuzhang.com/solutions/scramble-string/)|
|區間型, |312|168|[Burst Balloons](https://www.lintcode.com/problem/168/)|Hard|[http://www.jiuzhang.com/solutions/burst-ballons/](http://www.jiuzhang.com/solutions/burst-ballons/)|

* 667 用記憶化搜索時會超時
* 168 wrong answer

#### 轉移方程
* 125 Backpack II
  * `f[i][w] = max{f[i-1][w], f[i-1][w-$A_{i-1}$] + Vi-1 | w>=$A_{i-1}$ 且f[i-1][w-$A_{i-1}$] !=-1}`
    - `f[i][w]` 用前 i 個物品拼出重量 w 時的最大總價值
    - 情況1. 前 n-1 個物品能拼出 w 最大總價值 v 那麼前 n 個物品也能拼出 w 且最大總價值是 v
    - 情況2. 前 n-1 個物品能拼出 w-$A_{n-1}$ 最大總價值 v ，那麼再加上最後一個物品 (重量 $A_{n-1}$ 價值 $V_{n-1}$) 就能拼出 w 且最大總價值是 $V + V_{n-1}$
* 449 Backpack III
  * `f[i][w] = max_{k>=0}{f[i-1][w-k*$A_{i-1}$] + k*$V_{i-1}$}`
    - `f[i][w]` 用前 i **種**物品拼出重量 w 時的最大總價值
    - `f[i-1][w-k*$A_{i-1}$] + k*$V_{i-1}$` 用前 i-1 **種**物品拼出重量 w-$A_{i-1}$ 時的最大總價值，再加上 k 個第 i **種**物品的總價值
  * 把上式展開後歸納可以得到 `f[i][w] = max{f[i-1][w], f[i][w-$A_{i-1}$] + $V_{i-1}$}`
    - `f[i-1][w]` 用前 i-1 **種**物品拼出重量 w 時的最大總價值
    - `f[i][w-$A_{i-1}$] + $V_{i-1}` 用前 i **種**物品拼出重量 w-$A_{i-1}$ 時的最大總價值，加上第 i 種物品的價值
* 667 Longest Palindromic Subsequence
  * `f[i][j] = max{f[i+1][j], f[i][j-1], f[i+1][j-1] + 2|S[i]=S[j]}`
    - `f[i][j]` 是 s[i...j] 的最長回文子字串的長度
    - 假設最長回文子字串是 T 長度是 M
      - 情況1. 如果長度 M=1 就是一個字母
      - 情況2. 如果長度 M>1 則必定 T[0] = T[M-1]，如果 T[0]=S[i], T[M-1]=S[j] 那剩下的部分 T[1...M-2] 也是回文串，而且是 S[i+1...j-1] 的最長回文子字串
    - 要按照長度 M=j-i 從小到大去計算 
* 396 Coins In A Line III
  * `f[i][j] = max{a[i] - f[i+1][j], a[j] - f[i][j-1]}`
    - `f[i][j]` 當剩下的數是 a[i...j] 的時候，取 a[i] 或 a[j] 時能得到的最大數字差
    - 情況1. `a[i] - f[i+1][j]` 取 a[i] 而對手採取最優策略 `f[i+1][j]` 時，先手所能得到的最大數字差
    - 情況2. `a[j] - f[i][j-1]` 取 a[j] 而對手採取最優策略 `f[i][j-1]` 時，先手所能得到的最大數字差
  * 面對當前的數組，先手的數字和是 A 對手的數字和是 B
    * 先手看到的數字差 $S_{A} = A - B$
    * 對手看到的數字差 $S_{B} = B - A = -S_{A}$  
* 430 Scramble String
  ```
  f[i][j][k] = OR_{1<=w<=k-1} {f[i][j][w] AND f[i+w][j+w][k-w]}
  or
  f[i][j][k] = OR_{1<=w<=k-1} {f[i][j+k-w][w] AND f[i+w][j][k-w]}
  ```
    - `f[i][j][k]` 表示字串 S1[i...i+k-1] 能否通過變換變成 T1[j...j+k-1]
    - S 能拆解成 S1 和 S2 兩部分，T 能拆解成 T1 和 T2 兩部分
      - 情況1. T1 是 S1 變來的，T2 是 S2 變來的
      - 情況2. T1 是 S2 變來的，T2 是 S1 變來的
      - S1 從 i 開始長度為 k
      - T1 從 j 開始長度為 k
* 168 Burst Balloons
  * `f[i][j] = max_{i<k<j} {f[i][k] + f[k][j] + a[i] * a[k] * a[j]}`
    - `f[i][j]` 是扎破氣球 i+1...j-1 獲得的最大金幣數
    - 要倒著想，最後一顆札破的氣球左右兩邊是彼此獨立的

## Ch6

### Examples (7 題)

|Type|LeetCode No|LintCode No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|:---|
|雙序列型, 最值型|1143|77|[Longest Common Subsequence](https://www.lintcode.com/problem/77/)|Medium|[http://www.jiuzhang.com/solutions/longest-common-subsequence/](http://www.jiuzhang.com/solutions/longest-common-subsequence/)|
|雙序列型, 存在型|97|29|[Interleaving String](https://www.lintcode.com/problem/29/)|Hard|[http://www.jiuzhang.com/solutions/interleaving-string/](http://www.jiuzhang.com/solutions/interleaving-string/)|
|雙序列型, 最值型|72|119|[Edit Distance](https://www.lintcode.com/problem/119/)|Medium|[https://www.jiuzhang.com/solutions/edit-distance/](https://www.jiuzhang.com/solutions/edit-distance/)|
|雙序列型, 計數型|115|118|[Distinct Subsequences](https://www.lintcode.com/problem/118/)|Medium|[http://www.jiuzhang.com/solutions/distinct-subsequences/](http://www.jiuzhang.com/solutions/distinct-subsequences/)|
|雙序列型, 存在型|10|154|[Regular Expression Matching](https://www.lintcode.com/problem/154/)|Hard|[http://www.jiuzhang.com/solutions/regular-expression-matching/](http://www.jiuzhang.com/solutions/regular-expression-matching/)|
|雙序列型, 存在型|44|192|[Wildcard Matching](http://www.lintcode.com/problem/192/)|Hard|[http://www.jiuzhang.com/solutions/wildcard-matching/](http://www.jiuzhang.com/solutions/wildcard-matching/)|
|雙序列型, 最值型|474|668|[Ones and Zeroes](https://www.lintcode.com/problem/668/)|Medium|[http://www.jiuzhang.com/solutions/ones-and-zeroes](http://www.jiuzhang.com/solutions/ones-and-zeroes)|

* 154 wrong answer
* 668 wrong answer

#### 轉移方程
* 77 Longest Common Subsequence
  * `f[i][j] = max{ f[i-1][j], f[i][j-1], f[i-1][j-1]+1|A[i-1]=B[j-1] }`
    - `f[i][j]` 是 A 的前 i 個字元 A[0...i-1] 和 B 的前 j 個字元 B[0...j-1] 的最長 LCS 的長度
    - 情況 1. `f[i-1][j]` A[0...i-2] 和 B[0...j-1] 的最長 LCS
    - 情況 2. `f[i][j-1]` A[0...i-1] 和 B[0...j-2] 的最長 LCS
    - 情況 3. `f[i-1][j-1]+1|A[i-1]=B[j-1]` A[0...i-2] 和 B[0...j-2] 的最長 LCS + A[i-1] 一個字元
* 29 Interleaving String
  * `f[i][j] = (f[i-1][j] AND X[i+j-1]==A[i-1]) OR (f[i][j-1] AND X[i+j-1]==B[j-1])`
    - `f[i][j]` X 的前 i+j 個字元是否由 A 的前 i 個字元 A[0...i-1] 和 B 的前 j 個字元 B[0...j-1] 交錯組成
    - 情況 1. `f[i-1][j] AND X[i+j-1]==A[i-1]` X 的前 i+j-1 個字元是否由 A 的前 i-1 個字元 A[0...i-2] 和 B 的前 j 個字元 B[0...j-1] 交錯組成，且 X 的第 i+j 個字元 X[i+j-1] 等於 A 的第 i 個字元 A[i-1]
    - 情況 2. `f[i][j-1] AND X[i+j-1]==B[j-1]` X 的前 i+j-1 個字元是否由 A 的前 i 個字元 A[0...i-1] 和 B 的前 j-1 個字元 B[0...j-2] 交錯組成，且 X 的第 i+j 個字元 X[i+j-1] 等於 B 的第 j 個字元 B[j-1]
* 119 Edit Distance
  * `f[i][j] = min{ f[i][j-1]+1, f[i-1][j-1]+1, f[i-1][j]+1, f[i-1][j-1]|A[i-1]=B[j-1] }`
    - `f[i][j]` 是 A 的前 i 個個字元 A[0...i-1] 和 B 的前 j 個字元 B[0...j-1] 的最小編輯距離
    - 情況 1. `f[i][j-1]+1` 在 A 最後面插入 B[j-1]
    - 情況 2. `f[i-1][j-1]+1` A 的最後一個字元替換成 B[j-1]
    - 情況 3. `f[i-1][j]+1` A 刪掉最後一個字元
    - 情況 4. `f[i-1][j-1]|A[i-1]=B[j-1]` A 和 B 的最後一個字元相等
* 118 Distinct Subsequences
  * `f[i][j] = f[i-1][j-1]|A[i-1]=B[j-1] + f[i-1][j]`
    - 情況 1. A[i-1]=B[j-1] 結成對子
    - 情況 2. A[i-1]!=B[j-1] 不結成對子
* 154 Regular Expression Matching
  ```
            ┌ f[i-1][j-1]，如果 B[j-1]='.' 或者 A[i-1]=B[j-1]
  f[i][j] = |
            └ f[i][j-2] OR (f[i-1][j] AND (B[j-2]='.' OR B[j-2]=A[i-1]))，如果B [j-1]='*'
  ```
* 192 Wildcard Matching
  ```
            ┌ f[i-1][j-1]，如果 B[j-1]='?' 或者A[i-1]=B[j-1]
  f[i][j] = |
            └ f[i-1][j] OR f[i][j-1]，如果B [j-1]='*'
  ```
* 668 Ones and Zeroes
  * `f[i][j][k] = max{ f[i-1][j][k], f[i-1][j-$a_{i-1}$][k-$b_{i-1}$] + 1| j>=$a_{i-1}$ AND k>=$b_{i-1}$ }`
    - `f[i][j][k]` 前 i 個 01 串最多能有多少個被 j 個 0 和 k 個 1 組成
    - 情況 1. 最後一個不進 `f[i-1][j][k]` 前 i-1 個 01 串最多能有多少個被 j 個 0 和 k 個 1 組成
    - 情況 2. 最後一個進 `f[i-1][j-$a_{i-1}$][k-$b_{i-1}$] + 1| j>=$a_{i-1}$ AND k>=$b_{i-1}$` 前 i-1 個 01 串最多能有多少個被 j- $a_{i-1}$ 個 0 和 k- $b_{i-1}$ 個 1 組成，再加上最後一個 $S_{i-1}$


## Ch7

### Examples (7 題)

|Type|LeetCode No|LintCode No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|:---|
|序列+狀態, 最值型|not found|91|[Minimum Adjustment Cost](https://www.lintcode.com/problem/91/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/minimum-adjustment-cost/](http://www.jiuzhang.com/solutions/minimum-adjustment-cost/)|
|背包+狀態型, 計數型|not found|89|[K-Sum](https://www.lintcode.com/problem/89/)|Hard|[http://www.jiuzhang.com/solutions/k-sum/](http://www.jiuzhang.com/solutions/k-sum/)|
|最長序列型,|300|76|[Longest Increasing Subsequence](https://www.lintcode.com/problem/76/)|Medium|[http://www.jiuzhang.com/solutions/longest-increasing-subsequence/](http://www.jiuzhang.com/solutions/longest-increasing-subsequence/)|
||not found|623|[K Edit Distance](https://www.lintcode.com/problem/623/) (鎖住了)|Hard|[https://www.jiuzhang.com/solutions/k-edit-distance/](https://www.jiuzhang.com/solutions/k-edit-distance/)|
|座標+狀態型, 可行性|403|622|[Frog Jump](https://www.lintcode.com/problem/622/)|Hard|[http://www.jiuzhang.com/solutions/frog-jump/](http://www.jiuzhang.com/solutions/frog-jump/)|
||639|676|[Decode Ways II](https://www.lintcode.com/problem/676/) (鎖住了)|Hard|[http://www.jiuzhang.com/solution/decode-ways-ii/](http://www.jiuzhang.com/solution/decode-ways-ii/)|
||221|436|[Maximal Square](https://www.lintcode.com/problem/436/)|Medium|[http://www.jiuzhang.com/solutions/maximal-square/](http://www.jiuzhang.com/solutions/maximal-square/)|

#### 轉移方程
* 91 Minimum Adjustment Cost
  * `f[i][j] = min_{j-Target<=k<=j+Target, 1<=k<=100}{ f[i-1][k] + |j-A[i-1]| }`
    - `f[i][j]` A 的前 i 個元素改成 B 的最小代價，而且改成 B 之後相鄰的兩個元素的差，不能超過 target，並且 A[i-1]=j
    - `f[i-1][k]` A 的前 i-1 個元素改成 B 的最小代價，並且 A[i-2]=k 
    - `|j-A[i-1]|` A[i-1] 改成 j 的代價
* 89 K-Sum
  * 其實就是背包問題，A 的元素就是物品重量，Target 就是背包最大承重
  * `f[i][k][s] = f[i-1][k][s] + f[i-1][k-1][s-A[i-1]]|s>=A[i-1]`
    - `f[i][k][s]` 有多少種方式可以在前 i 個數中選出 k 個，使得和是 s
    - 情況1. A[n-1] 不進背包 `f[i-1][k][s]` 在前 i-1 個數中選出 k 個，使得和是 s 的方法數
    - 情況2. A[n-1] 進背包 `f[i-1][k-1][s-A[i-1]]` 在前 i-1 個數中選出 k-1 個，使得和是 s-A[i-1] 的方法數
* 76 Longest Increasing Subsequence
  * 用二分法來把 TC 從 O(N^2) 變成 O(N logN) 
* 623 K Edit Distance
* 622 Frog Jump
  * `f[i][j] = f[k][j-1] OR f[k][j] OR f[k][j+1] | a_{k} = a_{i} - j`
    - `f[i][j]` 能否在最後一跳的長度 j 跳到石頭 $a_{i}$
    - 石頭 $a_{i}$ 是從石頭 $a_{k}$ 以長度為 j 跳過來的: $a_{k} = a_{i} - j$
    - 要跳到石頭 $a_{k}$，可以是從上一塊石頭以 j-1, j, j+1 其中一個長度跳過來
    - `f[k][j-1]` 最後一跳 j-1 跳到石頭 $a_{k}$
    - `f[k][j]` 最後一跳 j 跳到石頭 $a_{k}$
    - `f[k][j+1]` 最後一跳 j+1 跳到石頭 $a_{k}$
  * 假設 `f[k][j] = True` 了，表示從上一顆石頭跳了 j 到石頭 k。
    - 那從 k 可以跳到 $a_{k}+(j-1)$, $a_{k}+j$, $a_{k}+(j+1)$ 的距離
    - 看這三個距離上有沒有石頭，有就紀錄到 Si 集合中
    - Si 集合內存的是所有能跳到石頭 i 的距離 L，所以從石頭 i 能跳的距離就是 L-1, L, L+1，這個距離內有石頭 j 就把結果紀錄到 Sj = {距離}
* 676 Decode Ways II
* 436 Maximal Square
