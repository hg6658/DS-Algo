// Problem Link:: https://practice.geeksforgeeks.org/problems/maximum-weight-transformation-of-a-given-string3551/1/

#include <bits/stdc++.h>
using namespace std;
//Position this line where user code will be pasted.


class Solution{
    
    int recursiveHelper(string &s,int i,vector<int> &dp,int N){
        if(i>=N){
            return 0;
        }
        
        if(dp[i]!=-1){
            return dp[i];
        }
        
        char c = s[i];
        
        if(c=='A'){
            s[i]='B';
        }else{
            s[i]='A';
        }
        
        int cost1=-10000000;
        
        if((i+1)<N && s[i]!=s[i+1]){
            cost1=3+recursiveHelper(s,i+2,dp,N);
        }else if((i+1)<N && s[i]==s[i+1]){
            cost1=-1+recursiveHelper(s,i+2,dp,N);
        }
        
        int cost2=recursiveHelper(s,i+1,dp,N);
        
        s[i]=c;
        
        int cost3=-10000000;
        
        if((i+1)<N && s[i]!=s[i+1]){
            cost3=4+recursiveHelper(s,i+2,dp,N);
        }else if((i+1)<N && s[i]==s[i+1]){
            cost3=recursiveHelper(s,i+2,dp,N);
        }
        
        int cost4=1+recursiveHelper(s,i+1,dp,N);
        
        dp[i]=std::max(std::max(cost1,cost2),std::max(cost3,cost4));
        
        return dp[i];
        
    }

	public:
	int getMaxWeight(string s) 
	{ 
	    int N = s.length();
	    
	    vector<int> dp(N,-1);
	    
	    int ans = recursiveHelper(s,0,dp,N);
	    return ans;
	} 
  

};