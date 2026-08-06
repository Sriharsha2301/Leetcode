class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # l=[]
        # n=len(nums)
        # c=set(nums)
        # for i in range(1,n+1):
        #     if i not in c:
        #         l.append(i)

        # return l
        s=set(nums)
        return [i for i in range(1,len(nums)+1) if i not in s]