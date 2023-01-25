# Finds length of longest contiguous non-empty, non-repeating character sequence (substring)
# within input string "s"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds length of longest non-repeating substring
        :param s: input string where the desired substring will be found
        :return: the length of the longest non-repeating substring within the string input
        """

        # "longest_len" variable to capture length of longest substring
        longest_len: int = 0

        # List to catch all observed letters in string
        substring_chars: List[Optional[str]] = []
        current_len: int = 0

        # if repeating character found, delete the repeating character within in the List,
        # AS WELL AS all characters that appear before the repeating character
        # then append the once-repeating character to the List
        for char in s:
            if substring_chars and char in substring_chars:
                # finds index of repeated character
                del_index: int = substring_chars.index(char)

                # delete repeated character
                substring_chars.pop(del_index)

                # if repeated was not in first index (0), delete prior characters as well
                while del_index != 0:
                    del_index -= 1
                    substring_chars.pop(del_index)
                
                # append once repeated character
                substring_chars.append(char)

                # reset length
                current_len = len(substring_chars)

                
        # As letters are added to list, count length, change longest_len variable if
        # current_len > longest_len

            else:
                substring_chars.append(char)
                current_len += 1

                if current_len > longest_len:
                    longest_len = current_len
        return longest_len

        