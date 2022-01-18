def partition(arr,s,e):
    pivot = arr[s];
    pivotIndex =s;
    n=len(arr)
    while(s<e):
        while(s<n and arr[s]<=pivot):
            s+=1;
        while(e>0 and arr[e]>pivot):
            e-=1;
        
        if(s<e):
            arr[s],arr[e]=arr[e],arr[s];
    arr[e],arr[pivotIndex]=arr[pivotIndex],arr[e]
    
    return e;
            
    


def solve(arr,s,e):
    if(s<e):
        p = partition(arr,s,e);
        solve(arr,s,p-1);
        solve(arr,p+1,e);
    


def quickSort(arr):
    # Write the function here.
    solve(arr,0,len(arr)-1);
    
    return arr;
if __name__=='__main__':
    arr=[10,80,30,90,40,50,70];
    n=5;
    quickSort(arr);
    print(arr);

