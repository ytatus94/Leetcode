class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        results = []
        if s is None:
            return results
        
        partition = []
        self.dfs(s, 0, results, partition)
        return results
    
    def dfs(self, s, start_index, results, partition):
        # 當指到底了，就把 partition 塞入 result
        # 注意是和 len(s) 比，不是和 len(s) - 1 比
        # 因為當 start_index 是指向最後一個元素的時候，還會再執行一次 dfs
        # 在新的 dfs 中 start_index 會被往後挪一個
        if start_index == len(s):
            results.append(partition[:])
            return
        
        # 以第一個 a 開頭的有 a|a|b, a|ab
        # 以 aa 開頭的有 aa|b
        # 以 aab 開頭的就是 aab 而已
        for i in range(start_index, len(s)):
            substring = s[start_index : i + 1]
            # 判斷是不是迴文
            if not self.isPalindrome(substring):
                continue
            partition.append(substring)
            self.dfs(s, i + 1, results, partition)
            partition.pop()
            
    def isPalindrome(self, string):
        i = 0
        j = len(string) - 1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True
    
    # 更簡潔的寫法，但是比較慢
    # def isPalindrome(self, string):
    #     return string == string[::-1]
