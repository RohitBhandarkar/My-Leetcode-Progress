#include <stdio.h>
#include <stdlib.h>

struct ListNode
{
    int val;
    struct ListNode *next;
};

typedef struct ListNode node;

node *get(int val)
{
    node *Node;
    Node = malloc(sizeof(node));
    Node->val = val;
    Node->next = NULL;
    return Node;
}

struct ListNode *mergeTwoLists(struct ListNode *list1, struct ListNode *list2)
{
    if (list1 == NULL)
        return list2;
    if (list2 == NULL)
        return list1;
    node *ans;
    ans = malloc(sizeof(node));
    node *ret;
    ret = ans;
    if (list1->val <= list2->val)
    {
        ans->val = list1->val;
        list1 = list1->next;
    }
    else
    {
        ans->val = list2->val;
        list2 = list2->next;
    }
    while (list1 != NULL && list2 != NULL)
    {
        if (list1 != NULL && list2 != NULL && list1->val <= list2->val)
        {
            ans->next = get(list1->val);
            list1 = list1->next;
            ans = ans->next;
        }
        else if (list1 != NULL && list2 != NULL)
        {
            ans->next = get(list2->val);
            ans = ans->next;
            list2 = list2->next;
        }
    }
    if (list1 != NULL)
    {
        ans->next = list1;
    }
    else if (list2 != NULL)
    {
        ans->next = list2;
    }
    return ret;
}

int main()
{
    return 0;
}