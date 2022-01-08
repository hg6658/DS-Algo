def bubbleSort(arr,size):

    if(size==0 or size ==1):
        return 
 
    for i in range(size):
        if(arr[i]>arr[i+1]):
            t=arr[i];
            arr[i]=arr[i+1];
            arr[i+1]=t;
    
    bubbleSort(nums,size-1);

if __name__=='__main__':
    nums = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(nums,len(nums)-1)

    for num in nums:
        print(num,end=" ")
