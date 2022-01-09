def countSubsequences(nums,sum,i,k):
    if(i>=len(nums)):
        if(sum==k):
            return 1;
        return 0;

    summation=0;
    summation+=(countSubsequences(nums,sum+nums[i],i+1,k)+countSubsequences(nums,sum,i+1,k));

    return summation; 


'''def countSubsequences(nums,summation,count,i,k):
    if(i>=len(nums)):
        if(summation==k):
            count+=1;
            return count;
        return 0;
    c1 = countSubsequences(nums,summation+nums[i],count,i+1,k)
    c2 = countSubsequences(nums,summation,count,i+1,k)
    
    return c1+c2;
'''



print(countSubsequences([5, 12, 3, 17, 1, 18, 15, 3, 17, 2, 56, 4, 89, 6],0, 0, 6))    