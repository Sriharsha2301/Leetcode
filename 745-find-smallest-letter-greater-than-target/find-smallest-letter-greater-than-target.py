class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        s=0
        e=len(letters)-1
        while(s<=e):
            mid=(s+e)//2
            if letters[mid]<=target:
                s=mid+1
            else:
                e=mid-1
            if s==len(letters):
                return letters[0]
        return letters[s]

        
        
        