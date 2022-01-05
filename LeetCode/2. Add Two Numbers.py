# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t= ListNode();
        l3 = t;
        previous = 0;
        pre=None;
        while(l1!=None or l2!=None):
            av=0;
            bv=0;
            sum1=0;
            if(l1!=None):
                av = l1.val;
            else:
                av=0;
            if(l2!=None):
                bv = l2.val;
            else:
                bv=0;
            
            sum1 = av+bv+previous;
            l3.val=sum1%10;
            previous = sum1//10;
            l3.next = ListNode();
            pre = l3;
            l3=l3.next;
            if(l1!=None):
                l1=l1.next;
            if(l2!=None):
                l2=l2.next;
        if(previous!=0):
            l3.val+=previous;
        else:
            pre.next=None;
        return t;    