"Score 91/100"
def uniquePaths(m, n):
	
    prev = [0]*n;
    prev[0]=1;
    for i in range(m):
        current = [0]*n;
        for j in range(n):
            if(j!=0):
                current[j]=current[j-1]+prev[j];
            else:
                current[j]=prev[j];
        prev = current;

    return current[n-1];    


if __name__=='__main__':
    print(uniquePaths(2,2))