class Solution(object):
    def climbIt(self,n,memo=None):

        if n==0:
            return 1
        if n<0:
            return 0
        if memo is None:
            memo={}
        if n in memo:
            return memo[n]
        memo[n]=self.climbIt(n-1,memo)+self.climbIt(n-2,memo)
        return memo[n]

    def climbStairs(self, n,memo={}):
        """
        :type n: int
        :rtype: int
        """
        return self.climbIt(n,memo)
      
      
            
            

        