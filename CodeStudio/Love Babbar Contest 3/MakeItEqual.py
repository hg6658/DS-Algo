from typing import *

def makeItEqual(a: int, b: int, c: int)-> int:

    # Write your Code here
    newA=a
    newB=b
    newC = c;
    flips=0;
    for i in range(30):
        if((c>>i)&1==1):
            if((a>>i)&1==0):
                flips+=1;
            if((b>>i)&1==0):
                flips+=1;
        else:
            if((a>>i)&1==1 and (b>>i)&1==1):
                flips+=1;
    return flips
            
                
            