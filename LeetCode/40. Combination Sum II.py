'''
Incomplete code can't able to return list to the callee......

'''
class Solution(object):     
    def getCombinations(self,candidates, target,temp,i):
        if(target==0):
            print(temp);
            return;

        for j in range(i,len(candidates)):
            if(j>i and candidates[j]==candidates[j-1]):
                continue
            if(candidates[j]>target):
                break;
            else:
                temp.append(candidates[j]);
                self.getCombinations(candidates,target-candidates[j],temp,j+1);
                temp.remove(candidates[j]) 




    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        temp=[]
        i=0
        self.getCombinations(candidates,target,temp,i)


if __name__=='__main__':
    ob=Solution()
    ob.combinationSum2([1,1,1,2,2],4)


