## Problem: Add Two Numbers

# Statement:

<p>
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

</p>

- Date: 26th August 2023
- Difficulty: Medium
- Solved: Yes
- Problem type: linked list
- Language used: Python

### Initial thoughts / approaches

### My solution

```
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
```

### Result

<img src="../images/problem3.jpg">
