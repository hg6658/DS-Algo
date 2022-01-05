class Solution(object):
    def lengthOfLongestSubstring(self, string):
        """
        :type s: str
        :rtype: int
        """
        i=0;
        d={};
        maxi =0;
        if(len(string)==1):
            return 1;
        
        j=0;
            
        while(j<len(string)):
            if(string[j] in d and d[string[j]]>=i and d[string[j]]<=j):
                if(maxi<(j-i)):
                    maxi=j-i;
                i=d[string[j]]+1;
                d[string[j]]=j
            else:
                d[string[j]]=j;
            j+=1    
        if(maxi<(j-i)):
            maxi=j-i;        
            
        return maxi     