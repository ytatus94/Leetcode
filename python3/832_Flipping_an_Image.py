class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        flipped = []
        for row in A:
            flipped.append(row[::-1])
        
        inverted = []
        for row in flipped:
            inverted_row = []
            for pixel in row:
                if pixel == 1:
                    pixel = 0
                elif pixel == 0:
                    pixel = 1
                inverted_row.append(pixel)
            inverted.append(inverted_row)
        
        return inverted 
