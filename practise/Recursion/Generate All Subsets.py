def subsetGenerate(arr,temp,i):
    if(i>=len(arr)):
        print(temp)
        return;
    
    temp.append(arr[i])
    subsetGenerate(arr,temp,i+1)
    temp.remove(arr[i])
    subsetGenerate(arr,temp,i+1)
    

subsetGenerate([4,5,1,2],[],0)