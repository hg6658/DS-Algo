'''
In Bubble sort what we do we compare adjacent elements and swap if one elements is previous elements greater than current. 
'''
def bubbleSort(nums):
    n = len(nums)
    # The outer loop will traverse n-1 times;
    for i in range(n):
        #Since after every iteration greatest elements will be at last i.e. sorted position the inner loop will run one less time.
        for j in range(n-i-1):
            #Swap if previous elements is greater than current element.
            if(nums[j]>nums[j+1]):
                t=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=t


if __name__=='__main__':
    nums = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(nums)

    for num in nums:
        print(num,end=" ")


