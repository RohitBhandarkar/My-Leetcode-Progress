# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=0
        n2=0
        count1=1
        count2=1
        while l1!=None:
            n1+=(count1*l1.val)
            count1*=10
            l1=l1.next
        while l2!=None:
            n2+=(count2*l2.val)
            count2*=10
            l2=l2.next
        
        print(n1,n2)
        sum=n1+n2
        ans = ListNode(sum%10)
        sum=sum//10
        ptr=ans
        while sum!=0:
            temp=ListNode()
            temp.val=sum%10
            sum=sum//10
            ans.next=temp
            ans=ans.next
        return ptr