def merge(arr,s,e,mid,n):
    leftArr = [0]*(mid-s+1)
    rightArr = [0]*(e-mid)
    
    for i in range(len(leftArr)):
        leftArr[i]=arr[s+i];
        
    for i in range(len(rightArr)):
        rightArr[i] =arr[mid+1+i];
        
    i=0
    j=0
    k=s
    while(i<len(leftArr) and j<len(rightArr)):
        if(leftArr[i]<=rightArr[j]):
            arr[k]=leftArr[i]
            k+=1;
            i+=1;
        else:
            arr[k]=rightArr[j]
            k+=1;
            j+=1;
    while(i<len(leftArr)):
        arr[k]=leftArr[i]
        k+=1;
        i+=1;
        
    while(j<len(rightArr)):
        arr[k]=rightArr[j]
        k+=1;
        j+=1;

def mergeHelper(arr,s,e,n):
    if(s<e):
        mid = (s+e)//2;
        mergeHelper(arr,s,mid,n);
        mergeHelper(arr,mid+1,e,n);
        merge(arr,s,e,mid,n);
    return arr    

def mergeSort(arr, n):
    return mergeHelper(arr,0,n-1,n)

