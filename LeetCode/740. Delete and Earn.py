class Solution(object):

    def helper(self,nums,i,dp):
        if(i==len(nums)):
            return 0;

        if(dp[i]!=-1):
            return dp[i]; 
        op=0;
        j=i;
        while(j<len(nums) and nums[i]==nums[j]):
            op+=nums[j];
            j+=1;
        
        if(j==len(nums)):
            dp[i]=op;
            return dp[i]

        

        n =j;
        
        op2=0;
        while(n<len(nums) and nums[n]==nums[j]):
            op2+=nums[n];
            n+=1            

        if(n==len(nums)):
            if(nums[j]==nums[i]+1):
                dp[i]= max(op,op2);
                return dp[i]
            else:
                dp[i] =op+ self.helper(nums,j,dp)
                return dp[i]    


        if(nums[j]==nums[i]+1):
            dp[i] = max(self.helper(nums,j,dp),op+self.helper(nums,n,dp))
        else:
            dp[i]=op+self.helper(nums,j,dp)

        return dp[i]            








    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[-1]*len(nums);
        nums.sort();
        print(nums)
        ans = self.helper(nums,0,dp);
        print(dp)
        return ans


if __name__ == '__main__':
    ob = Solution();
    print(ob.deleteAndEarn([8,10,4,9,1,3,5,9,4,10])) 




