class Solution(object):
    def numDecodingsHelper(self,s,i):
        if(i>len(s)):
            return 0;
        if(i==len(s)):
            return 1;    

        if(s[i]==0):
            return 0;

        return self.numDecodingsHelper(s,i+1)+self.numDecodingsHelper(s,i+2)    



    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(self.numDecodingsHelper(s,0))

if __name__ =='__main__':
    ob = Solution();
    ob.numDecodings("11106")        