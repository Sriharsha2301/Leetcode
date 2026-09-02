class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=1
        for j in range(1,len(nums)):
            if nums[j]!=nums[j-1]:
                nums[k]=nums[j]
                k+=1
        
        return k

        