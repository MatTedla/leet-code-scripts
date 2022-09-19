class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        total = 0
        
        index_and_value = enumerate(s)
        s_length = len(s)
        skip_value = False
        
        for i, v in index_and_value:
            if skip_value:
                skip_value = False
                continue
            
            
            if v == "I":
                if i + 1 != s_length:
                    if s[i + 1] == "V":
                        total += 4
                        skip_value = True
                
                    elif s[i + 1] == "X":
                        i += 1
                        total += 9
                        skip_value = True
                    
                    else:
                        total += 1
                else:
                    total += 1
            
            elif v == "V":
                total += 5
            
            elif v == "X":
                if i + 1 != s_length:
                    if s[i + 1] == "L":
                        total += 40
                        skip_value = True
                
                    elif s[i + 1] == "C":
                        total += 90
                        skip_value = True
                    
                    else:
                        total += 10
                else:
                    total += 10
                
            elif v == "L":
                total += 50
                
            elif v == "C":
                if i + 1 != s_length:
                    if s[i + 1] == "D":
                        total += 400
                        skip_value = True
                
                    elif s[i + 1] == "M":
                        total += 900
                        skip_value = True
                    
                    else:
                        total += 100
                else:
                    total += 100
                
            
            elif v == "D":
                total += 500
            
            else:
                total += 1000
            
            print(total)
        
        
        return total