class Solution:
    def solver(self,n,A,x,k,i,dp):
        if(i>=n):
            return i;
        if(k==0 and x<=0):
            return i;
        
        if(dp[i][x][k]!=-1):
            return dp[i][x][k];

        if(k==0 and x>0):
            dp[i][x][k]=self.solver(n,A,x-A[i],k,i+1,dp)
            return dp[i][x][k]

        if(k>0 and x<=0):
            k-=1
            ans=self.solver(n,A,x,k,i+1,dp)
            k+=1;
            dp[i][x][k]=ans
            return dp[i][x][k];

        k-=1;
        op2 = self.solver(n,A,x,k,i+1,dp)
        k+=1 
        op1 =  self.solver(n,A,x-A[i],k,i+1,dp);
        
        dp[i][x][k]=max(op1,op2)
        return dp[i][x][k]  








    def solve(self,n,A,x,k):
        #code here
        dp=[];
        for l in range(n):
            p=[]
            for i in range(x+1):
                q=[];
                for j in range(k+1):
                    q.append(-1);
                p.append(q);
            dp.append(p)        
        l=[0]*(len(A)-1)
        for i in range(1,n):
            l[i-1]=A[i]-A[i-1]

        ans = self.solver(len(l),l,x,k,0,dp)

        return ans


if __name__=="__main__":
    for _ in range(int(input())):
        n,x,k=map(int,input().strip().split())
        A=[int(i) for i in input().strip().split()]
        obj=Solution()
        ans=obj.solve(n,A,x,k)
        print(ans)