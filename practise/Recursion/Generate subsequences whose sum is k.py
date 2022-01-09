def printSubsequences(nums,temp,i,k,summation):
    if(i>=len(nums)):
        if(summation==k):
            print(temp)
            return True;
        return False;

    temp.append(nums[i]);
    if(printSubsequences(nums,temp,i+1,k,summation+nums[i])==True):
        return True;
    temp.remove(nums[i])
    if(printSubsequences(nums,temp,i+1,k,summation)==True):
        return True
    return False;    

printSubsequences([5, 12, 3, 17, 1, 18, 15, 3, 17, 2, 56, 4, 89, 6],[], 0, 6, 0)




