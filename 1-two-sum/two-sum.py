class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        for j in range(n):
            for i in range(j+1,n):
                if nums[i]+nums[j]==target:
                    return [j,i]
        
