from sortedcontainers import SortedList
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        SList=SortedList()
        for i in range(len(nums)):
            if i>indexDiff: SList.remove(nums[i-indexDiff-1])
            pos1=SortedList.bisect_left(SList,nums[i]-valueDiff)
            pos2=SortedList.bisect_right(SList,nums[i]+valueDiff)

            if pos1!=pos2 : return True

            SList.add(nums[i])
        return False
    