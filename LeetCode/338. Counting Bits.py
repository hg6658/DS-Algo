import math
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if(n==0):
            return [0];
        if(n==1):
            return [0,1];    
        logval=math.log(n, 2)
        if((logval).is_integer()):
            logval+=1;
        else:
            logval=math.ceil(logval)   
        logval=int(logval)
        value=2**(logval)
        dp=[0]*(int(value))
        dp[0]=0;
        dp[1]=1;
        for i in range(1,logval):
            for j in range(0,2**(i)):
                dp[2**(i)+j]=dp[j]+1;

        return dp[:n+1]       


if __name__ == "__main__":
    n=int(input())
    ob = Solution();
    print(ob.countBits(n))