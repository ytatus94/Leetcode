class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        result = []
        self.dfs(s, 0, [], result)
        return result

    def dfs(self, s, start_index, curr_subset, result):
        if start_index == len(s):
            result.append(curr_subset.copy()) # 深拷貝

        for i in range(start_index, len(s)):
            substring = s[start_index : i + 1] # 所有以 s[start_index] 開頭的子字串
            # 檢查是否是迴文
            if substring != substring[::-1]:
                continue

            self.dfs(s, i + 1, curr_subset + [substring], result)
