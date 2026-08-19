class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        l=""
        for c in s:
            if c.isalnum():
                l+=c
       
        return (l==l[::-1])

        