class Solution(object):
    
    def present(self,i,s):
        if(i in s):
            return True
        else:
            return False
    def minDeletions(self, string):
        """
        :type s: str
        :rtype: int
        """
        '''
        First created a dictionary with chracter frequency... Created a set to tore unique frequency. If frequency is not unique 
        then decrease the frquecny till its unique and increase the deletions.
        '''

        s=set();
        d={}
        for char in string:
            if(char in d):
                d[char]+=1;
            else:
                d[char]=1;    
        deletions=0;  
        for char in d:
            if(d[char] not in s):
                s.add(d[char])
            else:
                while(self.present(d[char],s)==True):
                    deletions+=1;
                    d[char]-=1;
                if(d[char]!=0):    
                    s.add(d[char])       
        return deletions        
