class Solution(object):
    def pow(self,x,n):
        if not n:
            return 1
        result=self.pow(x*x,n/2)
        if n%2:
            return x*result
        return result

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            return 1.0/self.pow(x,-n)
        return self.pow(x,n)