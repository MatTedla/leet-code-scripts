class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        
        for i, word in enumerate(strs):
            if len(strs) == 1:
                return word
            
            elif word == "":
                return ""
            
            else:   
                word_length = len(word)
                
                
                # only do this for the first two words
                if i == 0:
                    # choose specific word to loop through based on length
                    if word_length < len(strs[i+1]):
                        for j, char in enumerate(word):
                            if char == strs[i+1][j]:
                                prefix.append(char)
                    else:
                        for k, char in enumerate(strs[i+1]):
                            if char == word[k]:
                                prefix.append(char)
                else:
                    for l, char in enumerate(word):
                        if l >= len(prefix):
                            break
                        
                        if char != prefix[l]:
                            for _ in range(len(prefix[l:])):
                                prefix.pop(-1)
                            break

                        else:
                            if l+1 == word_length:
                                while word_length < len(prefix):
                                    prefix.pop(-1)
                            continue
        
        if len(prefix) == 0:
            return ""
        else:
            return ''.join(prefix)