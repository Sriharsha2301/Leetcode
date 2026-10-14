class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None:
            return 0
        i=0
        j=len(nums)-1
        if len(nums)==0: return 0
        if len(nums)==1:
            if nums[i]==val:
                return 0
            else:
                return len(nums)
           
        
        while i<=j:

            if nums[i]!=val:
                i+=1
            else:
                    
                nums[i],nums[j]=nums[j],nums[i]
                j-=1
        
        return i

        