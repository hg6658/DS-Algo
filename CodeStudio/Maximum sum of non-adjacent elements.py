'''
APPROACH
helper(n-1,nums,dp)==> maximum subsequences that i can get till index n-1;
helper(n-2,nums,dp)====> maximum subsequences that i can get get till n-2;
since n-2 is not adjacent to the current index that i am standing on so i will add the value of current index to the ans of n-2;
now i will calculate the maximum of n-1 and n-2 + value to get the answer of the current index that i am standing on.
'''


def helper(n,nums,dp):

    if(n==0):
        return nums[n];

    if(n==1):
        return max(nums[n],nums[n-1]);    

    if(dp[n]!=-1):
        return dp[n];    

    dp[n]=max(helper(n-1,nums,dp),nums[n]+helper(n-2,nums,dp));

    return dp[n];    




def maximumNonAdjacentSum(nums):    
    # Write your code here.
    dp=[-1]*(len(nums))
    ans = helper(n-1,nums,dp)

    return ans;


# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1



'''
TABULATION APPROACH

def maximumNonAdjacentSum(nums):    
    # Write your code here.
    dp=[0]*(len(nums))
    if(len(nums)==1):
        return nums[0]
    dp[0]=nums[0];
    dp[1]=max(nums[1],nums[0]);
    for i in range(2,n):
        dp[i]=max(dp[i-1],nums[i]+dp[i-2]);
    
    return dp[n-1];

'''    

'''
CONSTANT SPACE APPROACH


def maximumNonAdjacentSum(nums):    
    # Write your code here.
    if(len(nums)==1):
        return nums[0]
    prev2=nums[0];
    prev=max(nums[1],nums[0]);
    curr=0;
    for i in range(2,n):
        curr=max(prev,nums[i]+prev2);
        prev2=prev;
        prev=curr;
    
    return prev;



'''