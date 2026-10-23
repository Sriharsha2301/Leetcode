class Solution(object):
    def pow(self,x,n):
        if not n:
            return 1
        # if n==1:
        #     return x
            
        # result=self.pow(x,n/2)
        if n%2:
            return x*self.pow(x,n-1)
        return self.pow(x*x,n/2)
        
      

        
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            return 1.0/self.pow(x,-n)
        return self.pow(x,n)