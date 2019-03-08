class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        # 檢查同一個 col 不同 row 的值
        for col in range(len(A[0])):
            for row in range(len(A) - 1):
                if A[row][col] > A[row + 1][col]:
                    count += 1
                    break # 只會 break for row loop
        return count
