class Solution(object):
    def searchIt(self,m,top,bottom,left,right,target):
        if left>right:
            return False
        if top>bottom:
            return False
        if target<m[top][left]:
            return False
        if target>m[bottom][right]:
            return False
        mid=left+(right-left)//2
        r=top
        while r<=bottom and m[r][mid]<=target:
            if m[r][mid]==target:
                return True
            r+=1
        return self.searchIt(m,r,bottom,left,mid-1,target) or self.searchIt(m,top,r-1,mid+1,right,target)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.searchIt(matrix,0,len(matrix)-1,0,len(matrix[0])-1,target)
        