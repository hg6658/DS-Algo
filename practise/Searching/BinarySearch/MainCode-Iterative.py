if __name__=='__main__':
    arr =[2,4,6,10,14,18]    
    s=0;
    e=len(arr)-1
    mid = -1;
    key = 6
    
    while(s<e):
        mid = (s+e)//2;
        if(arr[mid]==key):
            print("Element Found");
            break;
        elif(arr[mid]>key):
            e=mid-1;
        else:
            s=mid+1;

    if(arr[mid]!=key):
        print("Element Not Found")        

