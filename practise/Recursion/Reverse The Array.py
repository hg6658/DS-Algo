def reverseArray(nums,i):

    if(i>=(len(nums)-i-1)):
        return;

    t=nums[i]    
    nums[i]=nums[len(nums)-i-1]
    nums[len(nums)-i-1] =t;

    reverseArray(nums,i+1)

if __name__ == '__main__':
    nums=[64, 34, 25, 12, 22, 11, 90];
    reverseArray(nums,0)

    for i in nums:
        print(i,end=' ')    