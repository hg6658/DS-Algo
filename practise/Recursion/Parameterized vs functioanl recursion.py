def parameterSum(num,sum):
    if(num<1):
        print(sum);
        return;

    parameterSum(num-1,sum+num);



def functionalSum(num):
    if(num<1):
        return num;

    return num+functionalSum(num-1);        


if __name__=='__main__':
    parameterSum(3,0);
    print(functionalSum(3))