'''
Incomplete code can't able to return list to the callee......

'''
class Solution(object):
    def getCombinations(self,candidates,target,temp,i):

        if(i>=len(candidates)):
            if(target==0):
                print(temp);
            return;    
        
        if(target<0):
            return;

        temp.append(candidates[i])

        self.getCombinations(candidates,target-candidates[i],temp,i)
 
        temp.remove(candidates[i])

        self.getCombinations(candidates,target,temp,i+1)





    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.getCombinations(candidates,target,[],0);






if __name__ == '__main__':
    ob = Solution();
    ob.combinationSum([2,3,6,7],7)       