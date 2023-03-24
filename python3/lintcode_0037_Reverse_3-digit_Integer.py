class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        res = str(number)[2] + str(number)[1] + str(number)[0]
        return int(res)

class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverse_integer(self, number: int) -> int:
        # write your code here
        c = number % 10
        b = ((number - c) // 10) % 10
        a = ((number - (b * 10 + c)) // 100) % 10
        return c * 100 + b * 10 + a
