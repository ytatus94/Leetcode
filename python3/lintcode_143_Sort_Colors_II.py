class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        if colors is None or len(colors) == 0:
            return
        
        self.rainbow_sort(colors, 0, len(colors) - 1, 1, k)
        
    def rainbow_sort(self, colors, start, end, color_from, color_to):
        if color_from == color_to: # 只有一種顏色
            return
        
        if start >= end:
            return

        color_mid = (color_from + color_to) // 2
        left = start
        right = end
        
        while left <= right:
            while left <= right and colors[left] <= color_mid:
                left += 1
            while left <= right and colors[right] > color_mid:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
                
        self.rainbow_sort(colors, start, right, color_from, color_mid)
        self.rainbow_sort(colors, left, end, color_mid + 1, color_to)
