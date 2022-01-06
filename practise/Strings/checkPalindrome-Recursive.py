def checkPalindrome(str,i,j):
    if(i>j):
        return True;

    if(str[i]!=str[j]):
        return False;
    else:
        return checkPalindrome(str,i+1,j-1);


if __name__ == '__main__':
    str = "malxclam"
    print(checkPalindrome(str,0,len(str)-1))
