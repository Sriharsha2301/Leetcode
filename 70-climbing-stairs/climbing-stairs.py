class Solution(object):
    def climbIt(self,n,momo=None):
        if momo is None:
            momo={}
        if n in momo:
            return momo[n]
        if n==0:
            return 1
        if n<0:
            return 0
        
        momo[n]=self.climbIt(n-1,momo)+self.climbIt(n-2,momo)
        return momo[n]

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        momo={}
        return self.climbIt(n,momo)
        