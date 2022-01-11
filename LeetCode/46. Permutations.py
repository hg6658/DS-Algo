'''
Incomplete code can't able to return list to the callee......

'''
class Solution(object):
    '''
    def permutations(self,nums,temp,visited):

        if(len(temp)==len(nums)):
            print(temp)
            return;

        for j in range(0,len(nums)):
            if(visited[j]==0):
                visited[j]=1;
                temp.append(nums[j]);
                self.permutations(nums,temp,visited);
                temp.remove(nums[j]);
                visited[j]=0;
    '''
    '''
    Alternate Approach;
    '''
    def permutations(self,nums,i):
        if(i>=len(nums)):
            print(nums);
            return;

        for j in range(i,len(nums)):
            nums[j],nums[i]=nums[i],nums[j];
            self.permutations(nums,i+1);
            nums[j],nums[i]=nums[i],nums[j];
            

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        self.permutations(nums,[],[0]*len(nums))
        '''
        self.permutations(nums,0) 
if __name__ =='__main__':
    ob = Solution();
    ob.permute([1,2,3]);