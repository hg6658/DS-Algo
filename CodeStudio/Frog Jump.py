from typing import *
import math;


def frogjumpHelper(n,heights,dp):
    if(n==1):
        return abs(heights[1]-heights[0]);
    if(n==0):
        return 0;    
    if(dp[n]!=-1):
        return dp[n];
    
    dp[n]=min(abs(heights[n]-heights[n-1])+frogjumpHelper(n-1,heights,dp),abs(heights[n]-heights[n-2])+frogjumpHelper(n-2,heights,dp))

    return dp[n]
  
def frogJump(n: int, heights: List[int]) -> int:

    dp = [-1]*(n);
    ans =frogjumpHelper(n-1,heights,dp);
    return ans;

if __name__ == "__main__":
    print(frogJump(4,[10,20,30,10]))
    print(frogJump(6,[4,8,3,10,4,4]))    

'''
TABULATION APPROACH 


from typing import *
import math;
  
def frogJump(n: int, heights: List[int]) -> int:

    dp = [0]*(n);
    dp[0]=0;
    dp[1]=abs(heights[1]-heights[0])
    for i in range(2,n):
        dp[i]=min(abs(heights[i]-heights[i-1])+dp[i-1],abs(heights[i]-heights[i-2])+dp[i-2])
    return dp[n-1];


'''






'''

CONSTANT SPACE APPROACH

from typing import *
import math;
  
def frogJump(n: int, heights: List[int]) -> int:

    prev=abs(heights[1]-heights[0])
    prev2=0;
    curr=0;
    for i in range(2,n):
        curr=min(abs(heights[i]-heights[i-1])+prev,abs(heights[i]-heights[i-2])+prev2)
        prev2=prev;
        prev=curr;
    return prev;

'''    