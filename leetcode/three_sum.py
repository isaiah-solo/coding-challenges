# UNFINISHED
# https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        initMap = {}
        solution = []
        
        if len(nums) < 3:
            return solution
        
        for i, num in enumerate(nums):
            if num not in initMap or i > initMap[num]:
                initMap[num] = i
        
        for i, x in enumerate(nums[: -2]):
            for j_base, y in enumerate(nums[i + 1 : - 1]):
                j = i + j_base + 1
                
                z = 0 - x - y
                
                if z in initMap and initMap[z] > j:
                    ans = [x, y, z]
                    ans.sort()
                    
                    if ans not in solution:
                        solution.append(ans)
        
        solution.sort()
        
        return solution
