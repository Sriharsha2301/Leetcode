class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l=[]
        r=[]
        for i in s:
            if  i!="#":
                l.append(i)
            else:
                if l:
                    l.pop()
        for j in t:
            if  j!="#":
                r.append(j)
            else:
                if r:
                    r.pop()
        return (l==r)
        

        