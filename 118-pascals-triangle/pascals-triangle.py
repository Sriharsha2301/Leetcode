class Solution(object):
    def generateIt(self,row,col,memo=None):
        if memo is None:
            memo={}
        if row==0 or col==0 or row==col:
            return 1
        if (row,col) in (memo):
            return memo[(row,col)]

        memo[(row,col)]=self.generateIt(row-1,col-1,memo)+self.generateIt(row-1,col,memo)
        return memo[(row,col)]

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        memo={}
        l=[]
        row=numRows
        for row in range(numRows):
            l1=[]
            for col in range(row+1):
                l1.append(self.generateIt(row,col,memo))
            l.append(l1)
            
        return l

        
        
       
 
        