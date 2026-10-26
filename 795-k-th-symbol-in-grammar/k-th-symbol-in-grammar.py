class Solution(object):
    def gramIt(self,n,k,flip):
        if n==1:
            return 0 if flip%2==0 else 1

        if k%2==0:
            return self.gramIt(n-1,k/2,flip+1)
        return self.gramIt(n-1,(k+1)/2,flip)
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        return self.gramIt(n,k,0)
        