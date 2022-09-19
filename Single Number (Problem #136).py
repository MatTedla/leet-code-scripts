class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numerate_nums = enumerate(nums)
        
        for i, item in numerate_nums:
            nums.remove(item)
            
            if item in nums:
                nums.insert(i, item)
            else:
                return item