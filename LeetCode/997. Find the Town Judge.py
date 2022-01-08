def findJudge( n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        d={}
        if(n==1):
            return 1
        for a,b in trust:
            if(b in d):
                d[b]+=1;
            else:
                d[b]=1;
            if(a in d):
                d[a]-=1;
            else:
                d[a]=-1;    
        
        for b in d:
            if(d[b]==(n-1)):
                return b;   
            
        return -1;    


print(findJudge(3,[[1,3],[2,3]]))