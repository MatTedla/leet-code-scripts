# Given value n, returns true if it is a power of four
# An integer is a power of four, if there exists an integer x such that n == 4^x

import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
	# Any integer that is below or equal to 0 cannot be a power of four
        if n <= 0:
            return False
        else:
	    # math.log outputs float x, i.e. log4(n) = x
	    # is_integer() checks if x is also an integer (i.e. 2.0, 3.0, 4.0, etc.)
            return math.log(n,4).is_integer()
        