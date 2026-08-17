class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=set(nums)
        n=len(nums)
        return [i for i in range(1,n+1) if i not in s]

       
