def printer(i):
    if(i<1):
        return;

    printer(i-1);

    print(i,end=' ')


if __name__ == '__main__':
    printer(5)     
