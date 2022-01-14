class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(image)
        for i in range(n):
            for j in range(n):
                if(j<n//2):
                    t=image[i][j]
                    image[i][j]=image[i][n-j-1];
                    image[i][n-j-1]=t
                
                image[i][j]^=1;    
        
        return image
        