class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if not pages:
            return 0
            
        # 一個人花一分鐘抄一頁，
        # 如果只由一個人來抄全部的書，就要 sum(pages) 分鐘
        # 因為一本書是由一個人來抄，抄完一本書所需要的最多的時間是 max(pages) 分鐘
        # 把全部的書抄完，所需要的時間就是 max(pages) ~ sum(pages) 分鐘之間
        #
        # 因為 3 本書分別有 3, 2, 4 頁，由三個人來抄會最快，一個人抄一本
        # 當最後一本書抄完時，共費時 4 分鐘 (最短時間)
        # 由一個人來抄會最慢，全部抄完要 3+2+4 = 9 分鐘 (最長時間)
        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.get_last_people(pages, mid) <= k:
                end = mid
            else:
                start = mid
                
        if self.get_last_people(pages, start) <= k:
            return start
            
        return end
        
    def get_last_people(self, pages, time_limit):
        count = 0
        time_cost = 0
        for page in pages:
            if time_cost + page > time_limit:
                count += 1
                time_cost = 0
            time_cost += page
        
        return count + 1
