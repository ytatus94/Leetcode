class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # 先找出中間的 index
        mid = (0 + (len(A) - 1)) // 2
        # 可能的情形有
        # a[a]bc, a[b]cc, a[b]bc 括號中的是 mid 元素
        # 觀察可知 mid = mid-1 時，重複元素在前半段
        # 如果不同時則 mid + 1 是重複的那個
        B = sorted(A)
        if B[mid] == B[mid - 1]:
            return B[mid]
        else:
            return B[mid + 1]
            
class Solution:
    # 方法二: 不重複的元素只會出現一次，如果已經在 hash 中了表示是重複的元素
    def repeatedNTimes(self, A: List[int]) -> int:
        hash = {}
        for num in A:
            if num in hash:
                return num
            else:
                hash[num] = 1
