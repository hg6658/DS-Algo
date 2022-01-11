'''
This code cannot be able to run on leetcode...
It was able to input matrix in form of  zeros and ones not in the form of list of strings
It was not able to return the board of matrix.
'''

class Solution(object):
    def possible(self,matrix,i,j,n):
        for k in range(n):
            if(matrix[i][k]==1):
                return False;
        
        for k in range(n):
            if(matrix[k][j]==1):
                return False;
        c=i;
        k=j;
        while(c<n and k<n):

            if(matrix[c][k]==1):
                return False;
            c+=1;
            k+=1;
        
        c=i;
        k=j;

        while(c>=0 and k>=0):
            if(matrix[c][k]==1):
                return False;
            c-=1;
            k-=1;
       
        c=i;
        k=j;


        while(c>=0 and k<n):
            if(matrix[c][k]==1):
                return False;
            c-=1;
            k+=1;
        
        c=i;
        k=j;
        

        while(c<n and k>=0):
            if(matrix[c][k]==1):
                return False;
            c+=1;
            k-=1;

        return True; 


    def printMatrix(self,matrix,n):
            for i in range(n):
                for k in range(n):
                    print(matrix[i][k],end=" ")
                print()
            print("**************************************************")


    def check_cases(self,matrix,n,j):
        if((j+1)==n): 
            
            self.printMatrix(matrix,n);   
            return 1;

        count=0;
        for i in range(n):
            if(self.possible(matrix,i,j+1,n)):
                matrix[i][j+1]=1;
                count+=self.check_cases(matrix,n,j+1);
                matrix[i][j+1]=0;

        return count;        


    def number_of_Ways(self,n):
        matrix = [ [ 0 for i in range(n) ] for j in range(n) ]


        count =0;

        for i in range(n):
            matrix[i][0]=1;
            count+=self.check_cases(matrix,n,0);
            matrix[i][0]=0;

        return count;

if __name__ == '__main__':
    ob = Solution();
    print(ob.number_of_Ways(8)); 
'''
    matrix =[[0,0,1,0],[1,0,0,0],[0,0,0,0],[0,1,0,0]] 

    for j in range(4):
        if(ob.possible(matrix,j,3,4)):
            matrix[j][3]=1;
            ob.printMatrix(matrix,4);
            matrix[j][3]=0;      
'''