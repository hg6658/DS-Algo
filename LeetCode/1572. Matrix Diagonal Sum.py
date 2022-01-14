class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        summation=0;
        n=len(mat)-1
        for i in range(len(mat)):
            summation+=mat[i][i]
            if(i!=(n-i)):
                summation+=mat[i][n-i]    
        return summation    