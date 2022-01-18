class Solution(object):

    def climbStairsHelper(self,n,dp,i):
        if(i<=0):
            return 0;
        if(dp[i]!=-1):
            return dp[i];

        dp[i]=1+self.climbStairsHelper(n,dp,i-1)+self.climbStairsHelper(n,dp,i-2);

        return dp[i];

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1]*n;
        p=self.climbStairsHelper(n,dp,n-1);
        return 1+p

ob=Solution()
print(ob.climbStairs(4))        