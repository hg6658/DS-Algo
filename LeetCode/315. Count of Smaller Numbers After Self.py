'''
CODE IS INCORRECT>>>
'''

class Solution(object):

    def merge(self,nums,counts,d,l,mid,r):
        leftBound = mid-l+1
        rightBound = r-mid;

        leftArr =[0]*leftBound;
        rightArr = [0]*rightBound;

        for i in range(0,leftBound):
            leftArr[i] = nums[i+l];

        for j in range(0,rightBound):
            rightArr[j] = nums[j+mid+1];

        i=0;
        j=0;
        k=l;

        while(i<leftBound and j<rightBound):
            if(leftArr[i]<=rightArr[j]):
                nums[k]=rightArr[j];
                k+=1;
                j+=1;
            else:
                counts[d[leftArr[i]]] += r-j+1;
                nums[k]=leftArr[i]
                k+=1;
                i+=1;
                

        while(i<leftBound):
            nums[k]=leftArr[i]
            k+=1;
            i+=1;

        while(j<rightBound):
            nums[k]=rightArr[j]
            k+=1;
            j+=1;




    def mergeSort(self,nums,counts,d,l,r):
        if(l<r):
            mid  = (l+r)//2;
            self.mergeSort(nums,counts,d,l,mid);
            self.mergeSort(nums,counts,d,mid+1,r);
            self.merge(nums,counts,d,l,mid,r);


    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = [0]*len(nums)
        d={}
        for i in range(len(nums)):
            d[nums[i]]=i;


        self.mergeSort(nums,counts,d,0,len(nums)-1);
        print(counts)

if __name__ == "__main__":
    ob = Solution();
    #l = [12, 11, 13, 5, 6, 7 ]
    l=[5,2,6,1]
    ob.countSmaller(l)
    print(l)        