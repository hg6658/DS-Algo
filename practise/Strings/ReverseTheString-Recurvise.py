'''
Given a string you need to reverse the string.
'''

def reverseString(string,s,e):
    if(s>=e):
        return;
    else:
        t=string[s]
        string[s] = string[e]
        string[e]=t 
        s+=1;
        e-=1;
        reverseString(string,s,e)

if __name__=="__main__":
    string=['a','b','c','d','e']
    reverseString(string,0,len(string)-1);
    print(string)

    string=['a','b','a','b']
    reverseString(string,0,len(string)-1);
    print(string)
               