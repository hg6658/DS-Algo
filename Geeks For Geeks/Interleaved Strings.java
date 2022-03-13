// Problem Link :: https://practice.geeksforgeeks.org/problems/interleaved-strings/1

// MEMOIZED SOLUTION

/*you are required to complete this method */
class Solution {
    
    public boolean recursionHelper(String A,String B,String C,int i,int j,Boolean[][] dp){
        if(i==A.length() && j== B.length()){
            return true;
        }
        
        if(dp[i][j]!=null){
            return dp[i][j];
        }
        
        if(i<A.length() && A.charAt(i)==C.charAt(i+j)){
            boolean ans  = recursionHelper(A,B,C,i+1,j,dp);
            dp[i][j]=ans;
            if(ans==true){
                return true;
            }
        }
        
        if(j<B.length() && B.charAt(j)==C.charAt(i+j)){
            boolean ans  = recursionHelper(A,B,C,i,j+1,dp);
            dp[i][j]=ans;
            if(ans==true){
                return true;
            }
        }
        
        return dp[i][j]=false;
        
    }
    
    
	public boolean isInterLeave(String a,String b,String c)
	{
        if((a.length()+b.length())!=c.length()){
            return false;
        }
        boolean ans = recursionHelper(a,b,c,0,0,new Boolean [a.length()+1][b.length()+1]);
        return ans;
	}
}



