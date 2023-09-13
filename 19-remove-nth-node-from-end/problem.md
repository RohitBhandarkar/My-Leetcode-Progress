## Problem: Remove Nth Node From End of List

# Statement:

<p>
Given the head of a linked list, remove the nth node from the end of the list and return its head.
</p>

- Date: 13th September 2023
- Difficulty: Medium
- Solved: Yes
- Problem type: Linked List
- Language used: C++

### Initial thoughts / approaches

- Seems easy
- Just have to parse the list till nth element
- Keep a track of nth and (n-1)th element
- Make the next of n-1 = next of n
- return head

- misread the question, it said nth element from the end not front
- parse through the list once to count the total number of elements
- subtract n from total and add 1. thats the element to be removed
- follow the above procedure to remove that element

- works but does not look very efficient

### My solution

```
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        struct ListNode *ptr=head;
        int count=0;
        while(ptr!=NULL)
        {
            count+=1;
            ptr=ptr->next;
        }
        if (count==1)
            return head->next;
        ptr=head;
        n = count-n;
        if(n==0)
        {
            return head->next;
        }
        for(int i=0;i<n-1;i++)
        {
            head=head->next;
        }
        if (head != NULL && head->next != NULL)
            head->next=head->next->next;
        return ptr;
    }
};
```

### Result

<img src="../images/problem19.jpg">

### Optimal Solutions

- The fast pointer, slow pointer approach

### Concepts learnt / to be learnt

- Fast and slow pointer approach
