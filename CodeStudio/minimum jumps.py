'''
MEMOIZED VERSION


import sys;
def mjHelper(arr,i,n,dp):
    if(i>=(n)):
        return 0;
    
    count=99999
    if(dp[i]!=-1):
        return dp[i];
    else:
        for j in range(1,arr[i]+1):
            if(j+i<=n):
                count = min(count,1+mjHelper(arr,j+i,n,dp));
    
    dp[i]= count;
    return dp[i];   


def minimumJumps(arr, n):
    
    dp=[-1]*n;
    ans = mjHelper(arr,0,n-1,dp);
    if(ans==99999):
        return -1;
    
    return ans;
'''
'''
TABULATION APPROACH


def minimumJumps(arr, n):
    
    dp=[99999]*n;
    dp[n-1]=0;     
    for i in range(n-1,-1,-1):
        for j in range(1,arr[i]+1):
            if(i+j<=(n-1)):
                dp[i]=min(dp[i],1+dp[j+i]);

    if(dp[0]>=99999):
        return -1;
    else:
        return dp[0];                

if __name__ =='__main__':
    print(minimumJumps([1,0,3,2,1],5))    

'''



