class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        addends = []
        nums_range = range(len(nums))
        
        for i in nums_range:
            for j in nums_range:
                if j == i:
                    continue
                   
                else:
                    if nums[i] + nums[j] == target:
                        addends.append(i)
                        addends.append(j)
                        return addends
