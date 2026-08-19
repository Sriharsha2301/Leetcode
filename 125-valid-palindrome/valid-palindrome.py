class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=""
        for c in s:
            if c.isalnum():
                l+=c
        l=l.lower()
           
        return (l==l[::-1])

        