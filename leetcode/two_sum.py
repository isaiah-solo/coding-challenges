# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ref = {}
        
        for i, num in enumerate(nums):
            compliment = target - num
            
            if compliment in ref:
                return [ref[compliment], i]
            
            ref[num] = i
