def insertionSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,0,-1):
            if(arr[j-1]>arr[j]):
                t=arr[j-1]
                arr[j-1]=arr[j]
                arr[j]=t
            else:
                break;    
       
       





if __name__=='__main__':
    nums = [64, 34, 25, 12, 22, 11, 90]
    insertionSort(nums)

    for num in nums:
        print(num,end=" ")

'''
nums = [12, 25, 34, 64, 22, 11, 90]

'''        