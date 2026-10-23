class Solution(object):
    def climbIt(self,n,memo=None):
        if memo is None:
            memo={}
        if n in memo:
            return memo[n]
        if n==1:
            return 1
        if n==2:
            return 2
        memo[n]=self.climbIt(n-1,memo)+self.climbIt(n-2,memo)
        return memo[n]
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        return self.climbIt(n,memo)
            
        