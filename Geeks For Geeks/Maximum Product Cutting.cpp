#include<bits/stdc++.h>
using namespace std;
class Solution{
	public:
	int mod  = 1000000007;
	
	int maxProduct(int n)
	{
	    if(n==3){
	        return 2;
	    }

		if(n==2){
			return 1;
		}
	    
	    vector<int>dp(n+1,-1);
	    
	    dp[0]=1;
	    dp[1]=1;
	    dp[2]=2;
	    int product=1;
	    for(int i=3;i<=n;i++){
	        product=1;
	        for(int j=1;j<=i;j++){
	            product = std::max(product,j*dp[i-j])%mod;
	        }
	        dp[i]=product;
	    }
	    
	    return dp[n];
	    
	}
};