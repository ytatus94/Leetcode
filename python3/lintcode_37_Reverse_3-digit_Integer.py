class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        res = str(number)[2] + str(number)[1] + str(number)[0]
        return int(res)
