import sys;
class Solution(object):
    '''
    def coinChangeHelper(self,coins,amount,dp):
        if(amount ==0):
            return 0;
        if(dp[amount]!=sys.maxsize):
            return dp[amount];
        minVal = sys.maxsize;
        for coin in coins:
            if(amount-coin>=0):
               minVal = min(minVal,self.coinChangeHelper(coins,amount-coin,dp));
        dp[amount] = 1+minVal;
        return dp[amount];            

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[sys.maxsize]*(amount+1)
        ans  = self.coinChangeHelper(coins,amount,dp);
        print(ans)
'''
    def coinChange(self, coins, amount):
        dp = [sys.maxsize]*(amount+1);
        dp[0]=0;
        for i in range(amount+1):
            for j in range(len(coins)):
                if(i-coins[j]>=0):
                    if(dp[i]>dp[i-coins[j]]):
                        dp[i]=1+dp[i-coins[j]];
        if(dp[amount]==sys.maxsize+1):
            return -1;
        else:
            return dp[amount];




if __name__ =="__main__":
    coins = [2,5,10,1];
    amount = 27;
    ob = Solution();
    print(ob.coinChange(coins,amount));