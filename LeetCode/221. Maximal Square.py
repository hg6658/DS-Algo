class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp=[]
        for i in range(len(matrix)+1):
            l=[]
            for j in range(len(matrix[0])+1):
                if(i==0 or j==0):
                    l.append(0)
                else:    
                    l.append(-1)
            dp.append(l)    

        maxim = 0;    

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if(matrix[i-1][j-1]=='0'):
                    dp[i][j]=0;
                else:
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]);
                maxim = max(maxim,dp[i][j]);

        return maxim*maxim;            


                        




if __name__ == '__main__':
    ob = Solution();
    matrix = matrix = [["1","0","1","0","0"],
                       ["1","0","1","1","1"],
                       ["1","1","1","1","1"],
                       ["1","0","0","1","0"]];
    ob.maximalSquare(matrix);