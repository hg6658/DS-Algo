def linearSearch(nums,key,i):
    if(i ==  len(nums)):
        return -1;
    
    if(nums[i]==key):
        return i;
    else:
        return linearSearch(nums,key,i+1)

def check(index):
     if(index==-1):
        print("The key could not be found")
     else:
        print("Element found at: ",index)

if __name__=='__main__':
    nums = [2,4,6,1,51,67,89,24]
    key = 67
    index = linearSearch(nums,key,0)
    check(index)
    key = 105
    index = linearSearch(nums,key,0)
    check(index)
               
