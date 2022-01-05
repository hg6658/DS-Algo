def binarySearch(nums,key,low,high):
    if(low<=high):
        mid = (low+high)//2;
        if(nums[mid]==key):
            return mid;
        elif(nums[mid]>key):
            return binarySearch(nums,key,low,mid-1);
        else:
            return binarySearch(nums,key,mid+1,high);
    else:
        return -1;


def check(index):
     if(index==-1):
        print("The key could not be found")
     else:
        print("Element found at: ",index)

if __name__=='__main__':
    nums = [2,4,6,1,51,67,89,24]
    key = 89
    low = 0
    high = len(nums)-1

    index = binarySearch(nums,key,low,high)
    check(index)
    key = 105
    index = binarySearch(nums,key,low,high)
    check(index)
   