class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string_x = str(x)
        length_of_x = len(string_x)
        list_x = list(string_x)
        
        for i, v in enumerate(list_x):
            if list_x[i] != list_x[-(i+1)]:
                return False
            elif i == length_of_x / 2:
                break
            else:
                pass
        
        return True