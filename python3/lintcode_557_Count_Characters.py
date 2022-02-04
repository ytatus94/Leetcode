class Solution:
    """
    @param: : a string
    @return: Return a hash map
    """

    def countCharacters(self, str):
        # write your code here
        d = {}
        for i in str:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        return d
