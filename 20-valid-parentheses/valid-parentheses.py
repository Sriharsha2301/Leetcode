class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                l.append(i)
            else:
                if l:
                    if i==")" and l[-1]=="(":
                        l.pop()
                    elif i=="]" and l[-1]=="[":
                        l.pop()
                    elif i=="}" and l[-1]=="{":
                        l.pop()
                    else:
                        return False
                else:
                    return False
        if not l:
            return True
        else:
            return False
        # return l

                        
        
        
        
            
        