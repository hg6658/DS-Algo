class Solution:
    def driver(self,arr,n,i,summation):
        if(i>=n):
            print(summation,end=" ")
            return;
            
        self.driver(arr,n,i+1,summation+arr[i]);
        self.driver(arr,n,i+1,summation)
            
            
    def subsetSums(self, arr, N):
		# code here
		     self.driver(arr,N,0,0)

if __name__ == "__main__":
    ob=Solution();
    ob.subsetSums([2,3],2)        