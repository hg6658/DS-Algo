class Solution(object):
    def numDecodingsHelper(self,s,i,dp):
        if(i>len(s)):
            return 0;
        if(i==len(s)):
            return 0;    

        if(s[i]=='0'):
            return 0;
        if(dp[i]!=-1):
            return dp[i];
        dp[i]=0;
        dp[i]+=self.numDecodingsHelper(s,i+1,dp);

        if(i<len(s)-1 and (s[i]=='1' or (s[i]=='2' and s[i+1]<'7'))):
             dp[i]+=self.numDecodingsHelper(s,i+2,dp);

        return 1+dp[i];   



    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[-1]*len(s)
        return self.numDecodingsHelper(s,0,dp)


