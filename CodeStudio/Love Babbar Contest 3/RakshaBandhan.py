from typing import *

def rakshaBandhan(arr: List[int], n: int)-> int:
    
    arr.sort(reverse=True);
    summation=arr[0];
    count=1;
    i=1;
    while(summation>0 and i<len(arr)):
        summation+=arr[i]
        if(summation<=0):
            break;
        count+=1
        i=i+1;
        
    return count
    