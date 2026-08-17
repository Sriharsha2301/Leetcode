class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        nums1=sorted(nums)
        i=0
        for i in range(n-1):
            if nums1[i]==nums1[i+1]:
                return True
        return False




        
            

        

