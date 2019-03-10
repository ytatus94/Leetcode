class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 先把 A 的元素分成基數的一群和偶數的一群
        odd = []
        even = []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        # 再依照 index 是奇數還是偶數把 odd 和 even 的元素合併
        merge = []
        for i in range(len(A)):
            if i % 2 == 0:
                merge.append(even[i // 2])
            else:
                merge.append(odd[(i - 1) // 2])
                
        return merge

class Solution:
    def sortArrayByParityII(self, A):
        # 原理一樣，但是跑比較快的寫法
        odd = [x for x in A if x % 2 == 1]
        even = [x for x in A if x % 2 == 0]
        merge = []
        for i in range(len(odd)):
            merge.append(even[i])
            merge.append(odd[i])
        return merge
