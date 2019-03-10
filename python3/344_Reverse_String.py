class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Because string is immutable, we
        # need to convert string to list.
        s = list(s)
        
        # Using two pointers
        head = 0
        tail = len(s) - 1
        
        while head < tail:
            # Switch the positions
            s[head], s[tail] = s[tail], s[head]
            
            head += 1
            tail -= 1
            
        return ''.join(s) # Neet to convert list back to string
