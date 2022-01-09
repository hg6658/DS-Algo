from typing import *
import sys
def minimumNet(n: int, k: int, fish: List[int]) -> int:
    # Write your code here.
    l=0;
    r=0;
    mini = 10**5;
    cnt=0;
    for i in range(n):
        l=i;
        r=max(r,i);
        if(i-1>=0 and fish[i-1]>0):
            cnt-=1;
        while(r<n and cnt<k):
            if(fish[r]==1):
                cnt+=1;
            r+=1;     
        if(cnt==k):
            mini = min(mini,r-l);
    if(mini==10**5):
        return -1;
    return mini        
        
    
        
        
        
    
   