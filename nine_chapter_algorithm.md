# 九章算法

# [九章算法 Github](https://github.com/ninechapter-algorithm/leetcode-linghu-templete)

## ch1

### Examples (3 題)

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
|13|[Implement strStr()](https://www.lintcode.com/problem/13/)|Naive|[https://www.jiuzhang.com/solution/implement-strstr/](https://www.jiuzhang.com/solution/implement-strstr/)|
|17|[Subsets](https://www.lintcode.com/problem/17/)|Medium|[http://www.jiuzhang.com/solutions/subsets/](http://www.jiuzhang.com/solutions/subsets/)|
|18|[Subsets II](https://www.lintcode.com/problem/18/)|Medium|[https://www.jiuzhang.com/solution/subsets-ii/](https://www.jiuzhang.com/solution/subsets-ii/)|


## ch2 Binary Search

* T(N) = T(N/2) + O(1) = O(log N)
* T(N) = T(N/2) + O(N) = O(N)
* 三步翻轉法: [4, 5, 1, 2, 3]  --> [5, 4, 1, 2, 3] --> [5, 4, 3, 2, 1] --> [1, 2, 3, 4, 5]

### Examples (17 題)

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
||Binary search||[http://www.jiuzhang.com/solutions/binary-search/](http://www.jiuzhang.com/solutions/binary-search/)|
|457|[Classical Binary Search](https://www.lintcode.com/problem/457/)|Easy|[https://www.jiuzhang.com/solution/classical-binary-search/](https://www.jiuzhang.com/solution/classical-binary-search/)|
|14|[First Position of Target](https://www.lintcode.com/problem/14/)|Easy|[http://www.lintcode.com/problem/first-position-of-target/](http://www.lintcode.com/problem/first-position-of-target/)|
|458|[Last Position of Target](https://www.lintcode.com/problem/458/) (鎖住了)|Easy|[https://www.jiuzhang.com/solution/last-position-of-target/](https://www.jiuzhang.com/solution/last-position-of-target/)|
|74|[First Bad Version](https://www.lintcode.com/problem/74/)|Medium|[http://www.jiuzhang.com/solutions/first-bad-version/](http://www.jiuzhang.com/solutions/first-bad-version/)|
|447|[Search In a Big Sorted Array](http://www.lintcode.com/problem/447) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/search-in-a-big-sorted-array/](http://www.jiuzhang.com/solutions/search-in-a-big-sorted-array/)|
|159|[Find Minimum in Rotated Sorted Array](https://www.lintcode.com/problem/159/)|Medium|[http://www.jiuzhang.com/solutions/find-minimum-in-rotated-sorted-array/](http://www.jiuzhang.com/solutions/find-minimum-in-rotated-sorted-array/)|
|600|[Smallest Rectangle Enclosing Black Pixels](https://www.lintcode.com/problem/600/)|Hard|[https://www.jiuzhang.com/solutions/smallest-rectangle-enclosing-black-pixels/](https://www.jiuzhang.com/solutions/smallest-rectangle-enclosing-black-pixels/)
|28|[Search a 2D Matrix](https://www.lintcode.com/problem/28/)|Easy|[https://www.jiuzhang.com/solutions/search-a-2d-matrix/](https://www.jiuzhang.com/solutions/search-a-2d-matrix/)|
|38|[Search a 2D Matrix II](https://www.lintcode.com/problem/38)|Medium|[https://www.jiuzhang.com/solutions/search-a-2d-matrix-ii/](https://www.jiuzhang.com/solutions/search-a-2d-matrix-ii/)|
|61|[Search for a Range](https://www.lintcode.com/problem/61/)|Medium|[https://www.jiuzhang.com/solutions/search-for-a-range/](https://www.jiuzhang.com/solutions/search-for-a-range/)|
|462|[Total Occurance of Target](https://www.lintcode.com/problem/462/) (鎖住了)|Easy|Not found|
|585|[Maximum Number in Mountain Sequence](https://www.lintcode.com/problem/585/)|Medium|[http://www.jiuzhang.com/solutions/maximum-number-in-mountain-sequence/](http://www.jiuzhang.com/solutions/maximum-number-in-mountain-sequence/)|
|75|[Find Peak Element](https://www.lintcode.com/problem/75/)|Medium|[http://www.jiuzhang.com/solutions/find-peak-element/](http://www.jiuzhang.com/solutions/find-peak-element/)|
|62|[Search in Rotated Sorted Array](https://www.lintcode.com/problem/62/)|Medium|[http://www.jiuzhang.com/solutions/search-in-rotated-sorted-array/](http://www.jiuzhang.com/solutions/search-in-rotated-sorted-array/)|
|39|[Recover Rotated Sorted Array](https://www.lintcode.com/problem/39/)|Easy|[https://www.jiuzhang.com/solutions/recover-rotated-sorted-array/](https://www.jiuzhang.com/solutions/recover-rotated-sorted-array/)|
|1790|[Rotate String II](https://www.lintcode.com/problem/1790/)|Easy|[https://www.jiuzhang.com/solutions/rotate-string-ii/](https://www.jiuzhang.com/solutions/rotate-string-ii/)|


## ch3 Binary Tree & Divide Conquer

* 遞歸三要素:
  * 定義
  * 出口
  * 拆解
* T(N) = 2 T(N/2) + O(1) = O(N)
* T(N) = 2 T(N/2) + O(N) = O(N log N)
* Preorder 根左右
* Inorder 左根右
* Postorder 左右根
* Binary Search Tree (BST):
  * 左子樹都比跟節點小
  * 右子樹都不小於跟節點
  * 中序遍歷 (inorder traversal) 是**不下降**序列 
  * O(N) 的時間查找，刪除，插入
  * [http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/BST-delete.html](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/BST-delete.html)

### Examples (25 題)

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
|66|[Binary Tree Preorder Traversal](https://www.lintcode.com/problem/66/)|Easy|[http://www.jiuzhang.com/solutions/binary-tree-preorder-traversal/](http://www.jiuzhang.com/solutions/binary-tree-preorder-traversal/)|
|67|[Binary Tree Inorder Traversal](https://www.lintcode.com/problem/67/)|Easy|[http://www.jiuzhang.com/solutions/binary-tree-inorder-traversal/](http://www.jiuzhang.com/solutions/binary-tree-inorder-traversal/)|
|68|[Binary Tree Postorder Traversal](https://www.lintcode.com/problem/68/)|Easy|[http://www.jiuzhang.com/solutions/binary-tree-postorder-traversal/](http://www.jiuzhang.com/solutions/binary-tree-postorder-traversal/)|
|97|[Maximum Depth of Binary Tree](https://www.lintcode.com/problem/97/)|Easy|[http://www.jiuzhang.com/solutions/maximum-depth-of-binary-tree/](http://www.jiuzhang.com/solutions/maximum-depth-of-binary-tree/)|
|480|[Binary Tree Paths](https://www.lintcode.com/problem/480/)|Easy|[http://www.jiuzhang.com/solutions/binary-tree-paths/](http://www.jiuzhang.com/solutions/binary-tree-paths/)|
|596|[Minimum Subtree](https://www.lintcode.com/problem/596/) (鎖住了)|Easy|[http://www.jiuzhang.com/solutions/minimum-subtree/](http://www.jiuzhang.com/solutions/minimum-subtree/)|
|93|[Balanced Binary Tree](https://www.lintcode.com/problem/93/)|Easy|[http://www.jiuzhang.com/solutions/balanced-binary-tree/](http://www.jiuzhang.com/solutions/balanced-binary-tree/)|
|597|[Subtree with Maximum Average](https://www.lintcode.com/problem/597/) (鎖住了)|Easy|[http://www.jiuzhang.com/solutions/subtree-with-maximum-average/](http://www.jiuzhang.com/solutions/subtree-with-maximum-average/)|
|453|[Flattern Binary Tree to Linked List](https://www.lintcode.com/problem/453/)|Easy|[http://www.jiuzhang.com/solutions/flatten-binary-tree-to-linked-list/](http://www.jiuzhang.com/solutions/flatten-binary-tree-to-linked-list/)|
|88|[Lowest Common Ancestor of a Binary Tree](https://www.lintcode.com/problem/88/)|Medium|[http://www.jiuzhang.com/solutions/lowest-common-ancestor/](http://www.jiuzhang.com/solutions/lowest-common-ancestor/)|
|474|[Lowest Common Ancestor II](https://www.lintcode.com/problem/474/) (鎖住了)|Easy|[https://www.jiuzhang.com/solutions/lowest-common-ancestor-ii/](https://www.jiuzhang.com/solutions/lowest-common-ancestor-ii/)|
|578|[Lowest Common Ancestor III](https://www.lintcode.com/problem/578/) (鎖住了)|Medium|[https://www.jiuzhang.com/solutions/lowest-common-ancestor-ii/](https://www.jiuzhang.com/solutions/lowest-common-ancestor-iii/)|
|595|[Binary Tree Longest Consecutive Sequence](https://www.lintcode.com/problem/595/)|Easy|[http://www.jiuzhang.com/solutions/binary-tree-longest-consecutive-sequence/](http://www.jiuzhang.com/solutions/binary-tree-longest-consecutive-sequence/)|
|614|[Binary Tree Longest Consecutive Sequence II](https://www.lintcode.com/problem/614)|Medium|[https://www.jiuzhang.com/solutions/binary-tree-longest-consecutive-sequence-ii/](https://www.jiuzhang.com/solutions/binary-tree-longest-consecutive-sequence-ii/)|
|619|[Binary Tree Longest Consecutive Sequence III](https://www.lintcode.com/problem/619) (鎖住了)|Medium|[https://www.jiuzhang.com/solutions/binary-tree-longest-consecutive-sequence-iii/](https://www.jiuzhang.com/solutions/binary-tree-longest-consecutive-sequence-iii/)|
|376|[Binary Tree Path Sum](https://www.lintcode.com/problem/376) (鎖住了)|Easy|[https://www.jiuzhang.com/solutions/binary-tree-path-sum/](https://www.jiuzhang.com/solutions/binary-tree-path-sum/)|
|246|[Binary Tree Path Sum II](https://www.lintcode.com/problem/246) (鎖住了)|Medium|[https://www.jiuzhang.com/solutions/binary-tree-path-sum-ii/](https://www.jiuzhang.com/solutions/binary-tree-path-sum-ii/)|
|472|[Binary Tree Path Sum III](https://www.lintcode.com/problem/472) (鎖住了)|Hard|[https://www.jiuzhang.com/solutions/binary-tree-path-sum-iii/](https://www.jiuzhang.com/solutions/binary-tree-path-sum-iii/)|
|95|[Validate Binary Search Tree](https://www.lintcode.com/problem/95/)|Medium|[http://www.jiuzhang.com/solutions/validate-binary-search-tree/](http://www.jiuzhang.com/solutions/validate-binary-search-tree/)|
|1534|[Convert Binary Search Tree to Sorted Doubly Linked List](https://www.lintcode.com/problem/1534/)|Medium|[http://www.jiuzhang.com/solutions/convert-binary-search-tree-to-d oubly-linked-list/](http://www.jiuzhang.com/solutions/convert-binary-search-tree-to-d oubly-linked-list/) (不見了)|
|86|[Binary Search Tree Iterator](https://www.lintcode.com/problem/86/)|Hard|[http://www.jiuzhang.com/solutions/binary-search-tree-iterator](http://www.jiuzhang.com/solutions/binary-search-tree-iterator)|
|448|[Inorder Successor in BST](https://www.lintcode.com/problem/448/)|Medium|[http://www.jiuzhang.com/solutions/inorder-successor-in-binary-search-tree/](http://www.jiuzhang.com/solutions/inorder-successor-in-binary-search-tree/)|
|11|[Search Range in Binary Search Tree](https://www.lintcode.com/problem/11/)|Medium|[https://www.jiuzhang.com/solutions/search-range-in-binary-search-tree/](https://www.jiuzhang.com/solutions/search-range-in-binary-search-tree/)|
|85|[Insert Node in a Binary Search Tree](https://www.lintcode.com/problem/85/)|Easy|[https://www.jiuzhang.com/solutions/insert-node-in-a-binary-search-tree/](https://www.jiuzhang.com/solutions/insert-node-in-a-binary-search-tree/)|
|87|[Remove Node in Binary Search Tree](https://www.lintcode.com/problem/87/)|Hard|[https://www.jiuzhang.com/solutions/remove-node-in-binary-search-tree](https://www.jiuzhang.com/solutions/remove-node-in-binary-search-tree)|


## ch4 Breadth First Search

BFS 處理:

* 圖的遍歷 Traversal in Graph
  * 層級遍歷 Level Order Traversal
  * 由點及面
  * 拓樸排序 Topological Sorting
* 簡單圖的最短路徑

### Example (19 題) 

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
|69|[Binary Tree Level Order Traversal](https://www.lintcode.com/problem/69/)|Easy|[http://www.jiuzhang.com/solutions/binary-tree-level-order-traversal/](http://www.jiuzhang.com/solutions/binary-tree-level-order-traversal/)|
||Binary Tree Serialization||[https://www.jiuzhang.com/solutions/binary-tree-serialization/](https://www.jiuzhang.com/solutions/binary-tree-serialization/)|
|70|[Binary Tree Level Order Traversal II](https://www.lintcode.com/problem/70/)|Medium|[http://www.jiuzhang.com/solutions/binary-tree-level-order-traversal-ii/](http://www.jiuzhang.com/solutions/binary-tree-level-order-traversal-ii/)|
|71|[Binary Tree Zigzag Level Order Traversal](https://www.lintcode.com/problem/71/)|Medium|[http://www.jiuzhang.com/solutions/binary-tree-zigzag-level-order-traversal/](http://www.jiuzhang.com/solutions/binary-tree-zigzag-level-order-traversal/)|
|242|[Convert Binary Tree to Linked Lists by Depth](https://www.lintcode.com/problem/242/)|Easy|[http://www.jiuzhang.com/solutions/convert-binary-tree-to-linked-lists-by-depth/](http://www.jiuzhang.com/solutions/convert-binary-tree-to-linked-lists-by-depth/)|
|178|[Graph Valid Tree](https://www.lintcode.com/problem/178/)|Medium|[http://www.jiuzhang.com/solutions/graph-valid-tree/](http://www.jiuzhang.com/solutions/graph-valid-tree/)|
|137|[Clone Graph](https://www.lintcode.com/problem/137/)|Medium|[http://www.jiuzhang.com/solutions/clone-graph/](http://www.jiuzhang.com/solutions/clone-graph/)|
|618|[Search Graph Nodes](https://www.lintcode.com/problem/618/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/search-graph-nodes/](http://www.jiuzhang.com/solutions/search-graph-nodes/)|
|127|[Topological Sorting](https://www.lintcode.com/problem/127/)|Medium|[http://www.jiuzhang.com/solutions/topological-sorting/](http://www.jiuzhang.com/solutions/topological-sorting/)|
|615|[Course Schedule](https://www.lintcode.com/problem/615/)|Medium|[https://www.jiuzhang.com/solutions/course-schedule/](https://www.jiuzhang.com/solutions/course-schedule/)|
|616|[Course Schedule II](https://www.lintcode.com/problem/616)|Medium|[https://www.jiuzhang.com/solutions/course-schedule-ii/](https://www.jiuzhang.com/solutions/course-schedule-ii/)|
|605|[Sequence Reconstruction](https://www.lintcode.com/problem/605/)|Medium|[https://www.jiuzhang.com/solutions/sequence-reconstruction/](https://www.jiuzhang.com/solutions/sequence-reconstruction/)|
|433|[Number of Islands](https://www.lintcode.com/problem/433/)|Easy|[http://www.jiuzhang.com/solutions/number-of-islands/](http://www.jiuzhang.com/solutions/number-of-islands/)|
|598|[Zombie in Matrix](https://www.lintcode.com/problem/598/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/zombie-in-matrix/](http://www.jiuzhang.com/solutions/zombie-in-matrix/)|
|611|[Knight Shortest Path](https://www.lintcode.com/problem/611/)|Medium|[http://www.jiuzhang.com/solutions/knight-shortest-path/](http://www.jiuzhang.com/solutions/knight-shortest-path/)|
|573|[Build Post Office II](https://www.lintcode.com/problem/573/) (鎖住了)|Hard|[http://www.jiuzhang.com/solutions/build-post-office-ii/](http://www.jiuzhang.com/solutions/build-post-office-ii/)|
|431|[Connected Component in Undirected Graph](https://www.lintcode.com/problem/431/) (鎖住了)|Medium|[https://www.jiuzhang.com/solutions/connected-component-in-undirected-graph/](https://www.jiuzhang.com/solutions/connected-component-in-undirected-graph/)|
|600|[Smallest Rectangle Enclosing Black Pixels](https://www.lintcode.com/problem/600/)|Hard|[https://www.jiuzhang.com/solutions/smallest-rectangle-enclosing-black-pixels/](https://www.jiuzhang.com/solutions/smallest-rectangle-enclosing-black-pixels/)|
|120|[Word Ladder](https://www.lintcode.com/problem/120/)|Hard|[https://www.jiuzhang.com/solutions/word-ladder/](https://www.jiuzhang.com/solutions/word-ladder/)|


## ch5 Depth First Search
* DFS 用 stack
  * non-recursion 都要用 stack 
* 找所有方案的題用 DFS
  * 90% DFS 的題是排列或是組合
  * DFS 可以使用 recursion 來實現
  * Permutation 搜索的時間複雜度和 O(n!) 相關
  * Combination 搜索的時間複雜度和 O(2^n) 相關
* DFS 時間複雜度計算公式 O(答案個數 x 構造每個答案的時間) 
* 遞歸三要素
  * 定義
  * 拆解
  * 出口 

### Example (13 題) 

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
|135|[Combination Sum](https://www.lintcode.com/problem/135)|Medium|[http://www.jiuzhang.com/solutions/combination-sum/](http://www.jiuzhang.com/solutions/combination-sum/)|
|153|[Combination Sum II](https://www.lintcode.com/problem/153/)|Medium|[http://www.jiuzhang.com/solutions/combination-sum-ii/](http://www.jiuzhang.com/solutions/combination-sum-ii/)|
|136|[Palindrome Partitioning](https://www.lintcode.com/problem/136/)|Medium|[http://www.jiuzhang.com/solutions/palindrome-partitioning/](http://www.jiuzhang.com/solutions/palindrome-partitioning/)|
|15|[Permutations](https://www.lintcode.com/problem/15/)|Medium|[http://www.jiuzhang.com/solutions/permutations/](http://www.jiuzhang.com/solutions/permutations/)|
|16|[Permutations II](https://www.lintcode.com/problem/16)|Medium|[http://www.jiuzhang.com/solutions/permutations-ii/](http://www.jiuzhang.com/solutions/permutations-ii/)|
|33|[N-Queens](https://www.lintcode.com/problem/33/)|Medium|[http://www.jiuzhang.com/solutions/n-queens/](http://www.jiuzhang.com/solutions/n-queens/)|
|120|[Word Ladder](https://www.lintcode.com/problem/120/)|Hard|[https://www.jiuzhang.com/solutions/word-ladder/](https://www.jiuzhang.com/solutions/word-ladder/)|
|121|[Word Ladder II](https://www.lintcode.com/problem/121/)|Hard|[http://www.jiuzhang.com/solutions/word-ladder-ii/](http://www.jiuzhang.com/solutions/word-ladder-ii/)|
|66|[Binary Tree Preorder Traversal](https://www.lintcode.com/problem/66/)|Easy|[http://www.jiuzhang.com/solutions/binary-tree-preorder-traversal/](http://www.jiuzhang.com/solutions/binary-tree-preorder-traversal/)|
|67|[Binary Tree Inorder Traversal](https://www.lintcode.com/problem/67)|Easy|[http://www.jiuzhang.com/solutions/binary-tree-inorder-traversal/](http://www.jiuzhang.com/solutions/binary-tree-inorder-traversal/)|
|68|[Binary Tree Postorder Traversal](https://www.lintcode.com/problem/68)|Easy|[http://www.jiuzhang.com/solutions/binary-tree-postorder-traversal/](http://www.jiuzhang.com/solutions/binary-tree-postorder-traversal/)|
|86|[Binary Search Tree Iterator](https://www.lintcode.com/problem/86/)|Hard|[http://www.jiuzhang.com/solutions/binary-search-tree-iterator/](http://www.jiuzhang.com/solutions/binary-search-tree-iterator/)|
|17|[Subsets](https://www.lintcode.com/problem/17/)|Medium|[http://www.jiuzhang.com/solutions/subsets/](http://www.jiuzhang.com/solutions/subsets/)|


## ch6 Linked List & Array

* 當 linked list 結構發生變化的時候，就需要 dummy node
* 子數組的 PrefixSum[i] = A[0] + A[1] + ... + A[i-1], PrefixSum[0] = 0
  * 構造 PrefixSum 要 TC=O(N) 和 SC=O(N)
  *  計算下標 i 到 j 之間所有數的和 = sum(i ~ j) = PrefixSum[j+1] - PrefixSum[i]

### Example (22 題) 

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
|450|[Reverse Nodes in k-Group](https://www.lintcode.com/problem/450/)|Hard|[http://www.jiuzhang.com/solutions/reverse-nodes-in-k-group/](http://www.jiuzhang.com/solutions/reverse-nodes-in-k-group/)|
|96|[Partition List](https://www.lintcode.com/problem/96/)|Easy|[https://www.jiuzhang.com/solutions/partition-list/](https://www.jiuzhang.com/solutions/partition-list/)|
|165|[Merge Two Sorted Lists](https://www.lintcode.com/problem/165/)|Easy|[https://www.jiuzhang.com/solutions/merge-two-sorted-lists/](https://www.jiuzhang.com/solutions/merge-two-sorted-lists/)|
|36|[Reverse Linked List II](https://www.lintcode.com/problem/36/)|Medium|[https://www.jiuzhang.com/solutions/reverse-linked-list-ii/](https://www.jiuzhang.com/solutions/reverse-linked-list-ii/)|
|511|[Swap Two Nodes in Linked List](https://www.lintcode.com/problem/511/)|Medium|[https://www.jiuzhang.com/solutions/swap-two-nodes-in-linked-list/](https://www.jiuzhang.com/solutions/swap-two-nodes-in-linked-list/)|
|99|[Reorder List](https://www.lintcode.com/problem/99/)|Medium|[https://www.jiuzhang.com/solutions/reorder-list/](https://www.jiuzhang.com/solutions/reorder-list/)|
|170|[Rotate List](https://www.lintcode.com/problem/170/)|Medium|[https://www.jiuzhang.com/solutions/rotate-list/](https://www.jiuzhang.com/solutions/rotate-list/)|
|105|[Copy List with Random Pointer](https://www.lintcode.com/problem/105/)|Medium|[http://www.jiuzhang.com/solutions/copy-list-with-random-pointer/](http://www.jiuzhang.com/solutions/copy-list-with-random-pointer/)|
|102|[Linked List Cycle](https://www.lintcode.com/problem/102/)|Medium|[http://www.jiuzhang.com/solutions/linked-list-cycle/](http://www.jiuzhang.com/solutions/linked-list-cycle/)|
|103|[Linked List Cycle II](https://www.lintcode.com/problem/103/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/linked-list-cycle/](http://www.jiuzhang.com/solutions/linked-list-cycle-ii/)|
|380|[Intersection of Two Linked Lists](https://www.lintcode.com/problem/380/)|Medium|[https://www.jiuzhang.com/solutions/intersection-of-two-linked-lists/](https://www.jiuzhang.com/solutions/intersection-of-two-linked-lists/)|
|98|[Sort List](https://www.lintcode.com/problem/98/)|Medium|[http://www.jiuzhang.com/solutions/sort-list/](http://www.jiuzhang.com/solutions/sort-list/)|
|106|[Convert Sorted List to Binary Search Tree](https://www.lintcode.com/problem/106/)|Medium|[https://www.jiuzhang.com/solutions/convert-sorted-list-to-balanced-bst/](https://www.jiuzhang.com/solutions/convert-sorted-list-to-balanced-bst/)|
||Delete Node in the Middle of Singly Linked List||[https://www.jiuzhang.com/solutions/delete-node-in-the-middle-of-singly-linked-list/](https://www.jiuzhang.com/solutions/delete-node-in-the-middle-of-singly-linked-list/)|
|1534|[Convert Binary Search Tree to Sorted Doubly Linked List](https://www.lintcode.com/problem/1534/)|Medium|[https://www.jiuzhang.com/solutions/convert-binary-search-tree-to-doubly-linked-list/](https://www.jiuzhang.com/solutions/convert-binary-search-tree-to-doubly-linked-list/)|
|6|[Merge Two Sorted Arrays](https://www.lintcode.com/problem/6/)|Easy|[http://www.jiuzhang.com/solutions/merge-two-sorted-arrays/](http://www.jiuzhang.com/solutions/merge-two-sorted-arrays/)|
|64|[Merge Sorted Array](https://www.lintcode.com/problem/64/)|Easy|[http://www.jiuzhang.com/solutions/merge-sorted-array/](http://www.jiuzhang.com/solutions/merge-sorted-array/)|
|547|[Intersection of Two Arrays](https://www.lintcode.com/problem/547/)|Easy|[https://www.jiuzhang.com/solutions/intersection-of-two-arrays/](https://www.jiuzhang.com/solutions/intersection-of-two-arrays/)|
|65|[Median of two Sorted Arrays](https://www.lintcode.com/problem/65/)|Hard|[http://www.jiuzhang.com/solutions/median-of-two-sorted-arrays/](http://www.jiuzhang.com/solutions/median-of-two-sorted-arrays/)|
|41|[Maximum Subarray](https://www.lintcode.com/problem/41/)|Easy|[http://www.jiuzhang.com/solutions/maximum-subarray/](http://www.jiuzhang.com/solutions/maximum-subarray/)|
|138|[Subarray Sum](https://www.lintcode.com/problem/138/)|Easy|[http://www.jiuzhang.com/solutions/subarray-sum/](http://www.jiuzhang.com/solutions/subarray-sum/)|
|139|[Subarray Sum Closest](https://www.lintcode.com/problem/139/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/subarray-sum-closest/](http://www.jiuzhang.com/solutions/subarray-sum-closest/)|


## ch7 Two Pointers

* 同向雙指針
* 相向雙指針
* 各種 Two Sum
  * =, >=, <= target, difference = target, closest to target
  * unique pairs
  * 3 sum, 4 sum 
* 各種排序
  * Quick Sort
  * Merge Sort
  * [Pancake Sort](https://en.wikipedia.org/wiki/Pancake_sorting)
  * [Sleep Sort](https://rosettacode.org/wiki/Sorting_algorithms/Sleep_sort)
  * [Spaghetti Sort](https://en.wikipedia.org/wiki/Spaghetti_sort)
  * [Bogo Sort](https://en.wikipedia.org/wiki/Bogosort)

### Example (26 題) 

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
|604|[Window Sum](https://www.lintcode.com/problem/604/) (鎖住了)|Easy|[https://www.jiuzhang.com/solutions/window-sum/](https://www.jiuzhang.com/solutions/window-sum/)|
|539|[Move Zeroes](https://www.lintcode.com/problem/539/)|Easy|[https://www.jiuzhang.com/solutions/move-zeroes/](https://www.jiuzhang.com/solutions/move-zeroes/)|
|521|[Remove Duplicate Numbers in Array](https://www.lintcode.com/problem/521/) (鎖住了)|Easy|[https://www.jiuzhang.com/solutions/remove-duplicate-numbers-in-array/](https://www.jiuzhang.com/solutions/remove-duplicate-numbers-in-array/)|
|415|[Valid Palindrome](https://www.lintcode.com/problem/415/)|Medium|[https://www.jiuzhang.com/solutions/valid-palindrome/](https://www.jiuzhang.com/solutions/valid-palindrome/)|
||Rotat String||Not found|
|39|[Recover Rotated Sorted Array](https://www.lintcode.com/problem/39/)|Easy|[https://www.jiuzhang.com/solutions/recover-rotated-sorted-array/](https://www.jiuzhang.com/solutions/recover-rotated-sorted-array/)|
|56|[Two Sum](https://www.lintcode.com/problem/56/)|Easy|[http://www.jiuzhang.com/solutions/two-sum/](http://www.jiuzhang.com/solutions/two-sum/)|
|607 |[Two Sum III - Data structure design](https://www.lintcode.com/problem/607/)|Easy|[http://www.jiuzhang.com/solutions/two-sum-data-structure-design/](http://www.jiuzhang.com/solutions/two-sum-data-structure-design/) (不見了)|
|608|[Two Sum  II - input array is sorted](https://www.lintcode.com/problem/608/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/two-sum-input-array-is-sorted/](http://www.jiuzhang.com/solutions/two-sum-input-array-is-sorted/)|
|587|[Two Sum - Unique pairs](https://www.lintcode.com/problem/587/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/two-sum-unique-pairs/](http://www.jiuzhang.com/solutions/two-sum-unique-pairs/)|
|57|[3Sum](https://www.lintcode.com/problem/57/)|Medium|[http://www.jiuzhang.com/solutions/3sum/](http://www.jiuzhang.com/solutions/3sum/)|
|382|[Triangle Count](https://www.lintcode.com/problem/382/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/triangle-count/](http://www.jiuzhang.com/solutions/triangle-count/)|
|609|[Two Sum - less than or equal to target](https://www.lintcode.com/problem/609/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/two-sum-less-than-or-equal-to-target/](http://www.jiuzhang.com/solutions/two-sum-less-than-or-equal-to-target/)
|443|[Two Sum - Greater than target](https://www.lintcode.com/problem/443/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/two-sum-greater-than-target/](http://www.jiuzhang.com/solutions/two-sum-greater-than-target/)|
|533|[Two Sum - Closest to target](https://www.lintcode.com/problem/533/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/two-sum-closest/](http://www.jiuzhang.com/solutions/two-sum-closest/)|
|59|[3Sum Closest](https://www.lintcode.com/problem/59/)|Medium|[http://www.jiuzhang.com/solutions/3sum-closest/](http://www.jiuzhang.com/solutions/3sum-closest/)|
|58|[4Sum](https://www.lintcode.com/problem/58/)|Medium|[http://www.jiuzhang.com/solutions/4sum/](http://www.jiuzhang.com/solutions/4sum/)|
|610|[Two Sum - Difference equals to target](https://www.lintcode.com/problem/610/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/two-sum-difference-equals-to-target/](http://www.jiuzhang.com/solutions/two-sum-difference-equals-to-target/)|
|31|[Partition Array](https://www.lintcode.com/problem/31/)|Medium|[http://www.jiuzhang.com/solutions/partition-array/](http://www.jiuzhang.com/solutions/partition-array/)|
|461|[Kth Smallest Numbers in Unsorted Array](https://www.lintcode.com/problem/461/) (鎖住了)|Medium|[https://www.jiuzhang.com/solutions/kth-smallest-numbers-in-unsorted-array/](https://www.jiuzhang.com/solutions/kth-smallest-numbers-in-unsorted-array/)|
|5|[Kth Largest Element](https://www.lintcode.com/problem/5/)|Medium|[https://www.jiuzhang.com/solutions/kth-largest-element/](https://www.jiuzhang.com/solutions/kth-largest-element/)|
|373|[Partition Array by Odd and Even](https://www.lintcode.com/problem/373/) (鎖住了)|Easy|[http://www.jiuzhang.com/solutions/partition-array-by-odd-and-even/](http://www.jiuzhang.com/solutions/partition-array-by-odd-and-even/)|
|144|[Interleaving Positive and Negative Numbers](https://www.lintcode.com/problem/144/)|Medium|[http://www.jiuzhang.com/solutions/interleaving-positive-and-negative-integers/](http://www.jiuzhang.com/solutions/interleaving-positive-and-negative-integers/)|
|49|[Sort Letters by Case](https://www.lintcode.com/problem/49/)|Medium|[http://www.jiuzhang.com/solutions/sort-letters-by-case/](http://www.jiuzhang.com/solutions/sort-letters-by-case/)|
|148|[Sort Colors](https://www.lintcode.com/problem/148/)|Medium|[http://www.jiuzhang.com/solutions/sort-colors/](http://www.jiuzhang.com/solutions/sort-colors/)|
|143|[Sort Colors II](https://www.lintcode.com/problem/143/)|Medium|[http://www.jiuzhang.com/solutions/sort-colors-ii/](http://www.jiuzhang.com/solutions/sort-colors-ii/)|


## ch8 Hash & Heap

* Queue:
  * O(1): push, pop, top
  * BFS
* Stack:
  * O(1): push, pop, top
  * DFS
* Hash:
  * O(1): insert, find, delete
  * hash table, hash map, hash set 的差別
* Heap 哈希表
  * 飽和度 = 實際儲存元素的個數 / 總共開闢的空間大小 size / capasity
  * 支持 增: O(log N), 刪: O(log N), 最大值最小值 O(1)
* [https://docs.oracle.com/javase/7/docs/api/java/util/TreeMap.html](https://docs.oracle.com/javase/7/docs/api/java/util/TreeMap.html)

### Example (17 題) 

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
|129|[Rehashing](https://www.lintcode.com/problem/129/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/rehashing/](http://www.jiuzhang.com/solutions/rehashing/)|
|134|[LRU Cache](https://www.lintcode.com/problem/134/)|Hard|[http://www.jiuzhang.com/solutions/lru-cache/](http://www.jiuzhang.com/solutions/lru-cache/)|
|138|[Subarray Sum](https://www.lintcode.com/problem/138/)|Easy|[https://www.jiuzhang.com/solutions/subarray-sum/](https://www.jiuzhang.com/solutions/subarray-sum/)|
|105|[Copy List with Random Pointer](https://www.lintcode.com/problem/105/)|Medium|[https://www.jiuzhang.com/solutions/copy-list-with-random-pointer/](https://www.jiuzhang.com/solutions/copy-list-with-random-pointer/)|
|171|[Anagrams](https://www.lintcode.com/problem/171/)|Medium|[https://www.jiuzhang.com/solutions/anagrams/](https://www.jiuzhang.com/solutions/anagrams/)|
|124|[Longest Consecutive Sequence](https://www.lintcode.com/problem/124/)|Medium|[https://www.jiuzhang.com/solutions/longest-consecutive-sequence/](https://www.jiuzhang.com/solutions/longest-consecutive-sequence/)|
|4|[Ugly Number II](https://www.lintcode.com/problem/517/)|Medium|[http://www.jiuzhang.com/solutions/ugly-number-ii/](http://www.jiuzhang.com/solutions/ugly-number-ii/)|
|545|[Top k Largest Number II](https://www.lintcode.com/problem/545/) (鎖住了)|Medium|[http://www.jiuzhang.com/solutions/top-k-largest-number-ii/](http://www.jiuzhang.com/solutions/top-k-largest-number-ii/)|
|104|[Merge K Sorted Lists](https://www.lintcode.com/problem/104/)|Medimu|[https://www.jiuzhang.com/solutions/merge-k-sorted-lists/](https://www.jiuzhang.com/solutions/merge-k-sorted-lists/)|
|613|[High Five](https://www.lintcode.com/problem/613/) (鎖住了)|Medium|[https://www.jiuzhang.com/solutions/high-five/](https://www.jiuzhang.com/solutions/high-five/)|
|612|[K Closest Points](https://www.lintcode.com/problem/612/) (鎖住了)|Medium|[https://www.jiuzhang.com/solutions/k-closest-points/](https://www.jiuzhang.com/solutions/k-closest-points/)|
|486|[Merge K Sorted Arrays](https://www.lintcode.com/problem/486/) (鎖住了)|Medium|[https://www.jiuzhang.com/solutions/merge-k-sorted-arrays/](https://www.jiuzhang.com/solutions/merge-k-sorted-arrays/)|
||Data Stream Median||[https://www.jiuzhang.com/solutions/data-stream-median/](https://www.jiuzhang.com/solutions/data-stream-median/)
|544|[TopK Largest Numbers](https://www.lintcode.com/problem/544/) (鎖住了)|Medium|[https://www.jiuzhang.com/solutions/top-k-largest-numbers/](https://www.jiuzhang.com/solutions/top-k-largest-numbers/)|
|401|[Kth Smallest Number in Sorted Matrix](https://www.lintcode.com/problem/401/)|Medium|[https://www.jiuzhang.com/solutions/kth-smallest-number-in-sorted-matrix/](https://www.jiuzhang.com/solutions/kth-smallest-number-in-sorted-matrix/)
||Building Outline||[https://www.jiuzhang.com/solutions/building-outline/](https://www.jiuzhang.com/solutions/building-outline/)|
|471|[Top K Frequent Words](https://www.lintcode.com/problem/471/)|Medium|[https://www.jiuzhang.com/solutions/top-k-frequent-words/](https://www.jiuzhang.com/solutions/top-k-frequent-words/)|


## ch9 Dynamic Programming

* 遞歸三要素
  * 定義
  * 拆解
  * 出口
* 動規四要素
  * 狀態
  * 方程
  * 初始化
  * 答案
  
## Example (13 題) 

|No|Problem|Level|Solution|
|:---|:---|:---|:---|
|109|[Triangle](https://www.lintcode.com/problem/109/)|Medium|[http://www.jiuzhang.com/solutions/triangle/](http://www.jiuzhang.com/solutions/triangle/)|
|136|[Palindrome Partitioning](https://www.lintcode.com/problem/136/)|Medium|[https://www.jiuzhang.com/solutions/palindrome-partitioning/](https://www.jiuzhang.com/solutions/palindrome-partitioning/)|
|124|[Longest Consecutive Sequence](https://www.lintcode.com/problem/124/)|Medium|[https://www.jiuzhang.com/solutions/longest-consecutive-sequence/](https://www.jiuzhang.com/solutions/longest-consecutive-sequence/)|
|110|[Minimum Path Sum](https://www.lintcode.com/problem/110/)|Medium|[http://www.jiuzhang.com/solutions/minimum-path-sum/](http://www.jiuzhang.com/solutions/minimum-path-sum/)|
|114|[Unique Path](https://www.lintcode.com/problem/114/)|Easy|[http://www.jiuzhang.com/solutions/unique-paths/](http://www.jiuzhang.com/solutions/unique-paths/)|
|111|[Climbing Stairs](https://www.lintcode.com/problem/111/)|Easy|[http://www.jiuzhang.com/solutions/climbing-stairs/](http://www.jiuzhang.com/solutions/climbing-stairs/)|
|116|[Jump Game](https://www.lintcode.com/problem/116/)|Medium|[https://www.jiuzhang.com/solutions/jump-game/](https://www.jiuzhang.com/solutions/jump-game/)|
|117|[Jump Game II](https://www.lintcode.com/problem/117)|Medium|[https://www.jiuzhang.com/solutions/jump-game-ii/](https://www.jiuzhang.com/solutions/jump-game-ii/)|
|76|[Longest Increasing Subsequence](https://www.lintcode.com/problem/76/)|Medium|[http://www.jiuzhang.com/solutions/longest-increasing-subsequence/](http://www.jiuzhang.com/solutions/longest-increasing-subsequence/)|
|513|[Perfect Squares](https://www.lintcode.com/problem/513/)|Medium|[http://www.jiuzhang.com/solutions/perfect-squares/](http://www.jiuzhang.com/solutions/perfect-squares/)|
|603|[Largest Divisible Subset](https://www.lintcode.com/problem/603/)|Medium|[http://www.jiuzhang.com/solutions/largest-divisible-subset/](http://www.jiuzhang.com/solutions/largest-divisible-subset/)|
|602|[Russian Doll Envelopes](https://www.lintcode.com/problem/602/)|Hard|[https://www.jiuzhang.com/solutions/russian-doll-envelopes/](https://www.jiuzhang.com/solutions/russian-doll-envelopes/)|
|622|[Frog Jump](https://www.lintcode.com/problem/622/)|Hard|[https://www.jiuzhang.com/solutions/frog-jump/](https://www.jiuzhang.com/solutions/frog-jump/)|

