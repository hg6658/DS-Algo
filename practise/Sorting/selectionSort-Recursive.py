def selectionSort(nums,size):
    
    if(size==0 or size==1):
        return ;
    max = -1;
    maxIndex= -1;

    for i in range(size+1):
        if(max<nums[i]):
            max=nums[i];
            maxIndex = i;
    
    t=nums[maxIndex];
    nums[maxIndex]=nums[size];
    nums[size]=t
    selectionSort(nums,size-1); 
       

if __name__=='__main__':
    nums = [64, 34, 25, 12, 22, 11, 90]
    selectionSort(nums,len(nums)-1)

    for num in nums:
        print(num,end=" ")