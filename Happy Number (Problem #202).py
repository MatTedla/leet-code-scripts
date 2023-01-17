# Algorithm to determine if integer "n" is happy

# To determine a happy number:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.

class Solution:
    def isHappy(self, n: int, sum_list: List[Optional[int]] = []) -> bool:
        """
        Determines if integer input is "happy".
        A happy number is a positive integer that can be replaced by the sum 
        of squares of its digits repeatedly until the number equals 1.

        : n: the integer input that will tested
        : sum_list: a list of all sums made within the happy number cycle
        : return: bool that indicates whether input is a "happy" number
        """
        
        # recursive function, with base cases being if sum equals 1 or if sum equals a 
        # previously obtained sum

        num_digits: List[int] = self.split_digits(n)
        new_sum: int = self.sum_list_numbers(self.square_list_numbers(num_digits))

        if new_sum == 1:
            # clears list when a new "n" value is about to be used
            sum_list.clear()
            return True
        elif new_sum in sum_list:
            return False
        else:
            sum_list.append(new_sum)
            return self.isHappy(new_sum, sum_list)


    def split_digits(self, i: int) -> List[int]:
        """
        Takes an integer input and seperates its digits into items in a list

        :i: integer that will have its digits split
        :return: list of integers representing digits of input
        """
        i_list: List[Optional[int, str]] = []
        i_str: str = str(i)

        for num in i_str:
            i_list.append(int(num))
        return i_list


    def square_list_numbers(self, digits: List[int]) -> List[int]:
        """
        Squares all integers within an integer list

        :digits: integer list that will have its values squared
        :return: squared integer list
        """
        for index, digit in enumerate(digits):
            digits[index] = digit * digit
        return digits


    def sum_list_numbers(self, digits: List[int]) -> int:
        """
        Adds all integers within a list

        :digits: integer list that will have its values added together
        :return: sum of values within the input integer list
        """
        sum: int = 0
        for digit in digits:
            sum += digit
        return sum