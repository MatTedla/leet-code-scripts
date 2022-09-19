# Returns length of the last word in a string
# A "word" in this case is a maximal substring consisting of non-space characters only

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s_list = s.split(' ')
        s_list.reverse()
        
        # find last word
        for i in s_list:
            if i != "":
                word_len = len(i)
                break
        
        return word_len