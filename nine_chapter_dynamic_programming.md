# 九章動態規劃

### 依據題目的形式，可以分成
  * **座標型**:
    * `f[i]` 就是以 ai 結尾的性質，`f[i][j]` 就是格子 (i, j) 的性質。
    * 初始條件 `f[0]` 就是以 a0 結尾的性質
    * 最長序列型和雙序列型其實是座標型，都是開二維數組
  * **序列型**:
    * `f[i]` 是前 i 個元素 a[0]...a[i-1] 的某種性質
    * 初始條件 `f[0]` 就是空序列 (前 0 個元素) 的性質
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
      * 當物品的數目無限多的時候，就以種類來計算
    * 可行性: `f[i][w]` = 前 i 個物品能不能拼出 w
    * 計數型: `f[i][w]` = 前 i 個物品有多少種方式能拼出 w
  * **最長序列型**: 是一種座標型 DP
  * **博弈型**:
    * 輪到誰，誰就是先手 
  * **綜合型**

### 依據題目要求的答案，可以分成
  * 計數型
    * 求有多少種方式
  * 最值型
    * 求最大值或最小值 
  * 存在型 (可行性)
    * 求是否存在，或是能不能幹嘛 

### DP 的組成部分
  1. 確定狀態
     - 最後一步
     - 子問題
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
    * 比較簡單

## Ch1

### Examples (4 題)

|Type|No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|
|最值型|669|[Coin Change](https://www.lintcode.com/problem/669/)|Medium|[https://www.jiuzhang.com/solution/coin-change/](https://www.jiuzhang.com/solution/coin-change/)|
|計數型|114|[Unique Paths](https://www.lintcode.com/problem/114/)|Easy|[http://www.jiuzhang.com/solutions/unique-paths/](http://www.jiuzhang.com/solutions/unique-paths/)|
|存在型|116|[Jump Game](https://www.lintcode.com/problem/116/)|Medium|[http://www.jiuzhang.com/solutions/jump-game/](http://www.jiuzhang.com/solutions/jump-game/)|
|最值型|191|[Maximum Product Subarray](https://www.lintcode.com/problem/191/)|Medium|[http://www.jiuzhang.com/solutions/maximum-product-subarray/](http://www.jiuzhang.com/solutions/maximum-product-subarray/)|

## Ch2

### Examples (7 題)

|Type|No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|
|座標型, 計數型|115|[Unique Paths II](https://www.lintcode.com/problem/115/)|Easy|[http://www.jiuzhang.com/solutions/unique-paths-ii/](http://www.jiuzhang.com/solutions/unique-paths-ii/)|
|序列型, 最值型|515|[Paint House](https://www.lintcode.com/problem/515/)|Medium|[https://www.jiuzhang.com/solution/paint-house/](https://www.jiuzhang.com/solution/paint-house/)|
|劃分型, 計數型|512|[Decode Ways](https://www.lintcode.com/problem/512/)|Medium|[http://www.jiuzhang.com/solutions/decode-ways/](http://www.jiuzhang.com/solutions/decode-ways/)|
|座標型, 計數型|397|[Longest Increasing Continuous Subsequence](https://www.lintcode.com/problem/397/)|Easy|[http://www.jiuzhang.com/solutions/longest-increasing-continuous-subsequence/](http://www.jiuzhang.com/solutions/longest-increasing-continuous-subsequence/)|
|座標型, 最值型|110|[Minimum Path Sum](https://www.lintcode.com/problem/110/)|Easy|[http://www.jiuzhang.com/solutions/minimum-path-sum/](http://www.jiuzhang.com/solutions/minimum-path-sum/)|
|座標型, 最值型|553|[Bomb Enemy](https://www.lintcode.com/problem/553/)|Medium|[http://www.jiuzhang.com/solutions/bomb-enemy/](http://www.jiuzhang.com/solutions/bomb-enemy/)|
|位操作型, 計數型|664|[Counting Bits](https://www.lintcode.com/problem/664/) (鎖住了)|Medium|[https://www.jiuzhang.com/solutions/counting-bits/](https://www.jiuzhang.com/solutions/counting-bits/)|

## Ch3

### Examples (9 題)

|Type|No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|
|序列＋狀態型, 最值型|516|[Paint House II](https://www.lintcode.com/problem/516/)|hard|[http://www.jiuzhang.com/solutions/paint-house-ii/](http://www.jiuzhang.com/solutions/paint-house-ii/)|
|序列＋狀態型, 最值型|392|[House Robber](https://www.lintcode.com/problem/392/)|Medium|[http://www.jiuzhang.com/solutions/house-robber/](http://www.jiuzhang.com/solutions/house-robber/)|
|序列＋狀態型, 最值型|534|[House Robber II](https://www.lintcode.com/problem/534/)|Medium|[http://www.jiuzhang.com/solutions/house-robber-ii/](http://www.jiuzhang.com/solutions/house-robber-ii/)|
|序列型, 最值型|149|[Best Time To Buy And Sell Stock](https://www.lintcode.com/problem/149/)|Medium|[http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock/](http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock/)|
|序列型, 最值型|150|[Best Time To Buy And Sell Stock II](https://www.lintcode.com/problem/150/)|Medium|[http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-ii/](http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-ii/)|
|序列＋狀態型, 最值型|151|[Best Time To Buy And Sell Stock III](https://www.lintcode.com/problem/151/)|Medium|[http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iii/](http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iii/)|
|序列型, 最值型|393|[Best Time To Buy And Sell Stock IV](https://www.lintcode.com/problem/393/)|Medium|[http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iv/](http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iv/)|
|最長序列型, |76|[Longest Increasing Subsequence](https://www.lintcode.com/problem/76/)|Medium|[http://www.jiuzhang.com/solutions/longest-increasing-subsequence/](http://www.jiuzhang.com/solutions/longest-increasing-subsequence/)|
|最長序列型, |602|[Russian Doll Envelopes](https://www.lintcode.com/problem/602/)||[http://www.jiuzhang.com/solutions/russian-doll-envelopes/](http://www.jiuzhang.com/solutions/russian-doll-envelopes/)|

## Ch4

### Examples (7 題)

|Type|No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|
|劃分型, 最值型|513|[Perfect Squares](http://www.lintcode.com/problem/513/)|Medium|[http://www.jiuzhang.com/solutions/perfect-squares/](http://www.jiuzhang.com/solutions/perfect-squares/)|
|劃分型, 最值型|108|[Palindrome Partitioning II](https://www.lintcode.com/problem/108/)|Medium|[http://www.jiuzhang.com/solutions/palindrome-partitioning-ii/](http://www.jiuzhang.com/solutions/palindrome-partitioning-ii/)|
|劃分型, 最值型|437|[Copy Books](https://www.lintcode.com/problem/437/)|Medium|[http://www.jiuzhang.com/solutions/copy-books/](http://www.jiuzhang.com/solutions/copy-books/)|
|博弈型, 存在型|394|[Coins in A Line](https://www.lintcode.com/problem/394/)|Medium|[http://www.jiuzhang.com/solutions/coins-in-a-line/](http://www.jiuzhang.com/solutions/coins-in-a-line/)|
|背包型, 可行性|92|[Backpack](https://www.lintcode.com/problem/92/)|Medium|[http://www.jiuzhang.com/solutions/backpack/](http://www.jiuzhang.com/solutions/backpack/)|
|背包型, 計數型|563|[Backpack V](https://www.lintcode.com/problem/563/)|Medium|[http://www.jiuzhang.com/solutions/backpack-v/](http://www.jiuzhang.com/solutions/backpack-v/)|
|背包型, 計數型|564|[Backpack VI](http://www.lintcode.com/564/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/backpack-vi/](http://www.jiuzhang.com/solutions/backpack-vi/)|

## Ch5

### Examples (6 題)

|Type|No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|
|背包型, 最值型|125|[Backpack II](https://www.lintcode.com/problem/125/)|Medium|[http://www.jiuzhang.com/solutions/backpack-ii/](http://www.jiuzhang.com/solutions/backpack-ii/)|
|背包型, 最值型|440|[Backpack III](https://www.lintcode.com/problem/440/)|Medium|[http://www.jiuzhang.com/solutions/backpack-iii/](http://www.jiuzhang.com/solutions/backpack-iii/)|
|區間型|667|[Longest Palindromic Subsequence](https://www.lintcode.com/problem/667/)|Medium|[https://www.jiuzhang.com/solution/longest-palindromic-subsequence/](https://www.jiuzhang.com/solution/longest-palindromic-subsequence/)|
|博弈型, 存在型|396|[Coins In A Line III](https://www.lintcode.com/problem/396/) (鎖住了)|Hard|[http://www.jiuzhang.com/solution/coins-in-a-line-iii/](http://www.jiuzhang.com/solution/coins-in-a-line-iii/)|
|區間型, |430|[Scramble String](https://www.lintcode.com/problem/430/)|Hard|[http://www.jiuzhang.com/solutions/scramble-string/](http://www.jiuzhang.com/solutions/scramble-string/)|
|區間型, |168|[Burst Balloons](https://www.lintcode.com/problem/168/)|Hard|[http://www.jiuzhang.com/solutions/burst-ballons/](http://www.jiuzhang.com/solutions/burst-ballons/)|

## Ch6

### Examples (7 題)

|Type|No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|
|雙序列型, 最值型|77|[Longest Common Subsequence](https://www.lintcode.com/problem/77/))|Medium|[http://www.jiuzhang.com/solutions/longest-common-subsequence/](http://www.jiuzhang.com/solutions/longest-common-subsequence/)|
|雙序列型, 存在型|29|[Interleaving String](https://www.lintcode.com/problem/29/)|Hard|[http://www.jiuzhang.com/solutions/interleaving-string/](http://www.jiuzhang.com/solutions/interleaving-string/)|
|雙序列型, 最值型|119|[Edit Distance](https://www.lintcode.com/problem/119/)|Medium|[https://www.jiuzhang.com/solutions/edit-distance/](https://www.jiuzhang.com/solutions/edit-distance/)|
|雙序列型, 計數型|118|[Distinct Subsequences](https://www.lintcode.com/problem/118/)|Medium|[http://www.jiuzhang.com/solutions/distinct-subsequences/](http://www.jiuzhang.com/solutions/distinct-subsequences/)|
|雙序列型, 存在型|154|[Regular Expression Matching](https://www.lintcode.com/problem/154/)|Hard|[http://www.jiuzhang.com/solutions/regular-expression-matching/](http://www.jiuzhang.com/solutions/regular-expression-matching/)|
||192|[Wildcard Matching](http://www.lintcode.com/problem/192/)|Hard|[http://www.jiuzhang.com/solutions/wildcard-matching/](http://www.jiuzhang.com/solutions/wildcard-matching/)|
||668|[Ones and Zeroes](https://www.lintcode.com/problem/668/)|Medium|[http://www.jiuzhang.com/solutions/ones-and-zeroes](http://www.jiuzhang.com/solutions/ones-and-zeroes)|

## Ch7

### Examples (7 題)

|Type|No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|
||91|[Minimum Adjustment Cost](https://www.lintcode.com/problem/91/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/minimum-adjustment-cost/](http://www.jiuzhang.com/solutions/minimum-adjustment-cost/)|
||89|[K-Sum](https://www.lintcode.com/problem/89/)|Hard|[http://www.jiuzhang.com/solutions/k-sum/](http://www.jiuzhang.com/solutions/k-sum/)|
||76|[Longest Increasing Subsequence](https://www.lintcode.com/problem/76/)|Medium|[http://www.jiuzhang.com/solutions/longest-increasing-subsequence/](http://www.jiuzhang.com/solutions/longest-increasing-subsequence/)|
||623|[K Edit Distance](https://www.lintcode.com/problem/623/) (鎖住了)|Hard|[https://www.jiuzhang.com/solutions/k-edit-distance/](https://www.jiuzhang.com/solutions/k-edit-distance/)|
||622|[Frog Jump](https://www.lintcode.com/problem/622/)|Hard|[http://www.jiuzhang.com/solutions/frog-jump/](http://www.jiuzhang.com/solutions/frog-jump/)|
||676|[Decode Ways II](https://www.lintcode.com/problem/676/) (鎖住了)|Hard|[http://www.jiuzhang.com/solution/decode-ways-ii/](http://www.jiuzhang.com/solution/decode-ways-ii/)|
||436|[Maximal Square](https://www.lintcode.com/problem/436/)|Medium|[http://www.jiuzhang.com/solutions/maximal-square/](http://www.jiuzhang.com/solutions/maximal-square/)|

