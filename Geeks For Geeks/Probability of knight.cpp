// Problem Link :: https://practice.geeksforgeeks.org/problems/probability-of-knight5529/1#


#include<bits/stdc++.h>
using namespace std;
class Solution{
    
	public:
	
	void printMatrix(int N,vector<vector<double>> &Matrix){
	    
	    for(int i=0;i<N;i++){
	        for(int j=0;j<N;j++){
	            std::cout<<Matrix[i][j]<<" ";
	        }
	        std::cout<<"\n";
	    }
	    
	    std::cout<<"\n";
	    
	}
	
	
	
	double findProb(int N,int start_x, int start_y, int s)
{
     vector<vector<double>>curr(N,vector<double>(N,0.0));
     vector<vector<double>>next(N,vector<double>(N,0.0));
     curr[start_x][start_y]=1.0;
     int dx[] = {-2, -1, +1, +2, +2, +1, -1, -2};
	 int dy[] = {+1, +2, +2, +1, -1, -2, -2, -1};

     for(int step=1;step<=s;step++)
     {
         for(int i=0;i<N;i++)
         {
             for(int j=0;j<N;j++)
             {
                 int ni,nj;
                 if(curr[i][j]!=0)
                 {
                 for(int k=0;k<8;k++)
                 {
                     ni=i+dx[k],nj=j+dy[k];
                     if(ni>=0 and ni<N and nj>=0 and nj<N)
                     {
                         next[ni][nj]+=(curr[i][j])/8.0;

                     }            
                                
                 }
               }
             }
         }
          curr=next;
          for(int p=0;p<N;p++){
              for(int l=0;l<N;l++){
                  next[p][l]=0.0;
              }
          }
         
     }
     //return ans;
     double ans=0.0;
     for(int i=0;i<N;i++)
     {
         for(int j=0;j<N;j++)
         {
             ans+=curr[i][j];
             
         }
        
     }
     return ans;
}



};