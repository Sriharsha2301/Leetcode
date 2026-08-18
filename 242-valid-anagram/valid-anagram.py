class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n1=sorted(s)
        n2=sorted(t)
        if n1==n2:
            return True
        return False

        
        