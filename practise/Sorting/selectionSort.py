def selectionSort(nums):

    for i in range(len(nums)):
        max = -1;
        maxIndex = -1;
        for j in range(len(nums)-i):
            if(max<nums[j]):
                max=nums[j];
                maxIndex = j;
        t=nums[maxIndex];
        nums[maxIndex]=nums[len(nums)-i-1];
        nums[len(nums)-i-1]=t

if __name__=='__main__':
    nums = [64, 34, 25, 12, 22, 11, 90]
    selectionSort(nums)

    for num in nums:
        print(num,end=" ")




