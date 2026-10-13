
class Solution(object):
    def reverseIt(self,s,start,end):
        if start>=end:
            return 
        
        temp=s[start]
        s[start]=s[end]
        s[end]=temp

        self.reverseIt(s,start+1,end-1)
        

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.reverseIt(s,0,len(s)-1)