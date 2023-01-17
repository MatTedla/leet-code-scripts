# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
	
	# saves location of latest zero with slow; if non-zero found with i, they are swapped
	# this means non-zero is placed ahead of the array, while the 0 is placed further back in the array
	# values are sorted completed by going through the array only once

        for i in range(len(nums)):
	    # even if value at slow index is 0, this is skipped if value at "i" index is also 0
            if nums[i] !=0 and nums[slow] == 0:
                nums[i], nums[slow] = nums[slow], nums[i]
            
	    # skipped if value at slow index is 0; "i" will go up by 1, slow stays the same
            if nums[slow] != 0:
                slow +=1