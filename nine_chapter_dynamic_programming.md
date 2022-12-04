# 九章動態規劃

* 依據題目的形式，可以分成
  * 座標型: f[i] 就是以 ai 結尾的性質，f[i][j] 就是格子 (i, j) 的性質。初始條件 f[0] 就是以 a0 結尾的性質
  * 序列型: f[i] 是前 i 個元素 a[0]...a[i-1] 的某種性質，初始條件 f[0] 就是空序列的性質
  * 劃分型
  * 區間型
  * 背包型
  * 最長序列型
  * 博弈型
  * 綜合型

* 依據題目要求的答案，可以分成
  * 計數型
    * 求有多少種方式
  * 最值型
    * 求最大值或最小值 
  * 存在型
    * 求是否存在，或是能不能幹嘛 

* DP 的組成部分
  1. 確定狀態
     - 最後一步
     - 子問題
     - 定義狀態
  2. 轉移方程
     - 根據狀態推得 
  3. 初始值與邊界條件
     - 要細心考慮周全
  4. 計算順序 

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
|位操作型, 計數型|664|[Counting Bits](https://www.lintcode.com/problem/664/)|Medium||

## Ch3

### Examples (9 題)

|Type|No|Problem|Level|Solution|
|:---|:---|:---|:---|:---|
|序列型, 最值型|516|[Paint House II](https://www.lintcode.com/problem/516/)||[http://www.jiuzhang.com/solutions/paint-house-ii/](http://www.jiuzhang.com/solutions/paint-house-ii/)|
|392|[House Robber](http://www.lintcode.com/problem/house-robber/)||[http://www.jiuzhang.com/solutions/house-robber/](http://www.jiuzhang.com/solutions/house-robber/)|
|534|[House Robber II](http://www.lintcode.com/problem/house-robber-ii/)||[http://www.jiuzhang.com/solutions/house-robber-ii/](http://www.jiuzhang.com/solutions/house-robber-ii/)|
|149|[Best Time To Buy And Sell Stock](http://www.lintcode.com/en/problem/best-time-to-buy-and-sell-stock/)||[http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock/](http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock/)|
|150|[Best Time To Buy And Sell Stock II](http://www.lintcode.com/en/problem/best-time-to-buy-and-sell-stock-ii/)||[http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-ii/](http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-ii/)|
|151|[Best Time To Buy And Sell Stock III](http://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iii/)||[http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iii/](http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iii/)|
|393|[Best Time To Buy And Sell Stock IV](http://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iv/)||[http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iv/](http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iv/)|
|76|[Longest Increasing Subsequence](http://www.lintcode.com/problem/longest-increasing-subsequence/)||[http://www.jiuzhang.com/solutions/longest-increasing-subsequence/](http://www.jiuzhang.com/solutions/longest-increasing-subsequence/)|
|602|[Russian Doll Envelopes](http://www.lintcode.com/problem/russian-doll-envelopes/)||[http://www.jiuzhang.com/solutions/russian-doll-envelopes/](http://www.jiuzhang.com/solutions/russian-doll-envelopes/)|

## Ch4

### Examples (7 題)

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
|513|[Perfect Squares](http://www.lintcode.com/problem/perfect-squares/)||[http://www.jiuzhang.com/solutions/perfect-squares/](http://www.jiuzhang.com/solutions/perfect-squares/)|
|108|[Palindrome Partitioning II](http://www.lintcode.com/problem/palindrome-partitioning-ii/)||[http://www.jiuzhang.com/solutions/palindrome-partitioning-ii/](http://www.jiuzhang.com/solutions/palindrome-partitioning-ii/)|
|437|[Copy Books](http://www.lintcode.com/problem/copy-books/)||[http://www.jiuzhang.com/solutions/copy-books/](http://www.jiuzhang.com/solutions/copy-books/)|
|394|[Coins in A Line](http://www.lintcode.com/problem/coins-in-a-line/)||[http://www.jiuzhang.com/solutions/coins-in-a-line/](http://www.jiuzhang.com/solutions/coins-in-a-line/)|
|92|[Backpack](http://www.lintcode.com/en/problem/backpack/)||[http://www.jiuzhang.com/solutions/backpack/](http://www.jiuzhang.com/solutions/backpack/)|
|563|[Backpack V](http://www.lintcode.com/problem/backpack-v/)||[http://www.jiuzhang.com/solutions/backpack-v/](http://www.jiuzhang.com/solutions/backpack-v/)|
|564|[Backpack VI](http://www.lintcode.com/problem/backpack-vi/)||[http://www.jiuzhang.com/solutions/backpack-vi/](http://www.jiuzhang.com/solutions/backpack-vi/)|

## Ch5

### Examples (6 題)

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
|125|[Backpack II](http://www.lintcode.com/problem/backpack-ii/)||[http://www.jiuzhang.com/solutions/backpack-ii/](http://www.jiuzhang.com/solutions/backpack-ii/)|
|440|[Backpack III](http://www.lintcode.com/problem/backpack-iii/)||[http://www.jiuzhang.com/solutions/backpack-iii/](http://www.jiuzhang.com/solutions/backpack-iii/)|
|667|[Longest Palindromic Subsequence](http://www.lintcode.com/en/problem/longest-palindromic-subsequence/)||[https://www.jiuzhang.com/solution/longest-palindromic-subsequence/](https://www.jiuzhang.com/solution/longest-palindromic-subsequence/)|
|396|[Coins In A Line III](http://www.lintcode.com/en/problem/coins-in-a-line-iii/)||[http://www.jiuzhang.com/solution/coins-in-a-line-iii/](http://www.jiuzhang.com/solution/coins-in-a-line-iii/)|
|430|[Scramble String](http://www.lintcode.com/problem/scramble-string/)||[http://www.jiuzhang.com/solutions/scramble-string/](http://www.jiuzhang.com/solutions/scramble-string/)|
|168|[Burst Balloons](http://www.lintcode.com/problem/burst-ballons/)||[http://www.jiuzhang.com/solutions/burst-ballons/](http://www.jiuzhang.com/solutions/burst-ballons/)|

## Ch6

### Examples (7 題)

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
|77|[Longest Common Subsequence](http://www.lintcode.com/problem/longest-common-subsequence/)||[http://www.jiuzhang.com/solutions/longest-common-subsequence/](http://www.jiuzhang.com/solutions/longest-common-subsequence/)|
|29|[Interleaving String](http://www.lintcode.com/en/problem/interleaving-string/)||[http://www.jiuzhang.com/solutions/interleaving-string/](http://www.jiuzhang.com/solutions/interleaving-string/)|
|119|[Edit Distance](http://www.lintcode.com/problem/edit-distance/)||[https://www.jiuzhang.com/solutions/edit-distance/](https://www.jiuzhang.com/solutions/edit-distance/)|
|118|[Distinct Subsequences](http://www.lintcode.com/problem/distinct-subsequences/)||[http://www.jiuzhang.com/solutions/distinct-subsequences/](http://www.jiuzhang.com/solutions/distinct-subsequences/)|
|154|[Regular Expression Matching](http://www.lintcode.com/problem/regular-expression-matching/)||[http://www.jiuzhang.com/solutions/regular-expression-matching/](http://www.jiuzhang.com/solutions/regular-expression-matching/)|
|192|[Wildcard Matching](http://www.lintcode.com/problem/wildcard-matching/)||[http://www.jiuzhang.com/solutions/wildcard-matching/](http://www.jiuzhang.com/solutions/wildcard-matching/)|
|668|[Ones and Zeroes](http://www.lintcode.com/en/problem/ones-and-zeroes/)||[http://www.jiuzhang.com/solutions/ones-and-zeroes](http://www.jiuzhang.com/solutions/ones-and-zeroes)|

## Ch7

### Examples (7 題)

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
|91|[Minimum Adjustment Cost](http://www.lintcode.com/en/problem/minimum-adjustment-cost/)||[http://www.jiuzhang.com/solutions/minimum-adjustment-cost/](http://www.jiuzhang.com/solutions/minimum-adjustment-cost/)|
|89|[K-Sum](http://www.lintcode.com/en/problem/k-sum/)||[http://www.jiuzhang.com/solutions/k-sum/](http://www.jiuzhang.com/solutions/k-sum/)|
|76|[Longest Increasing Subsequence](http://www.lintcode.com/problem/longest-increasing-subsequence/)||[http://www.jiuzhang.com/solutions/longest-increasing-subsequence/](http://www.jiuzhang.com/solutions/longest-increasing-subsequence/)|
|623|[K Edit Distance](http://www.lintcode.com/problem/k-edit-distance/)||[https://www.jiuzhang.com/solutions/k-edit-distance/](https://www.jiuzhang.com/solutions/k-edit-distance/)|
|622|[Frog Jump](http://www.lintcode.com/problem/frog-jump/)||[http://www.jiuzhang.com/solutions/frog-jump/](http://www.jiuzhang.com/solutions/frog-jump/)|
|676|[Decode Ways II](http://www.lintcode.com/en/problem/decode-ways-ii/)||[http://www.jiuzhang.com/solution/decode-ways-ii/](http://www.jiuzhang.com/solution/decode-ways-ii/)|
|436|[Maximal Square](http://www.lintcode.com/problem/maximal-square/)||[http://www.jiuzhang.com/solutions/maximal-square/](http://www.jiuzhang.com/solutions/maximal-square/)|

