def insertionSort(nums,size):
    
    if(size==len(nums)-1):
        return ;

    for j in range(size+1,0,-1):
        if(nums[j-1]>nums[j]):
            t=nums[j-1]
            nums[j-1]=nums[j]
            nums[j]=t
        else: 
            break  

    insertionSort(nums,size+1)      



if __name__=='__main__':
    nums = [64, 34, 25, 12, 22, 11, 90]
    insertionSort(nums,0)

    for num in nums:
        print(num,end=" ")


