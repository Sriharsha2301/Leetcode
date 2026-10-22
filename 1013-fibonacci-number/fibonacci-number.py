class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo={}
        if n in memo:
            return memo[n]
        if n<=1:
            return n
        memo[n]=self.fib(n-1)+self.fib(n-2) 
        return memo[n]
        