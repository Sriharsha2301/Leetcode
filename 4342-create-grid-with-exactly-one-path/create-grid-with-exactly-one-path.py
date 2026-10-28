class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        grid=[]
        row=0
        while row<m:
            str=""
            col=0
            while col<n:
                if row==0 or col==n-1:
                    str+="."
                else:
                    str+="#"
                col+=1
            row+=1
            grid.append(str)
        return grid