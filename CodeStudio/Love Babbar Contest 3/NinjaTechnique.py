from typing import *

def ninjaTechnique(n: int, a: List[List[int]])-> int:
    
    for i in range(n):
        if(a[i][0]>a[i][1]):
            t=a[i][0]
            a[i][0]=a[i][1]
            a[i][1]=t;
    a.sort(key = lambda x:x[0])
    l=[]
    for interval in a:
        if(len(l)==0):
            l.append(interval)
        elif(l[-1][1]<interval[0]):
            l.append(interval)
        else:
            l[-1][1]=min(l[-1][1],interval[1])
            l[-1][0]=max(l[-1][0],interval[0])
    return len(l)        
            
            
      
    