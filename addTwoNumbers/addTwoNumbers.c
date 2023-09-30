#include <stdio.h>
#include <stdlib.h>

//Define structs outside of main
struct ListNode {
        int val;
        struct ListNode* next;
    };

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2);
void printAll(struct ListNode* head);
//Take the pointer of the linked list so modifications can occur
void freeLinkedList(struct ListNode** head);

int main() {
    struct ListNode* l1 = malloc(sizeof(struct ListNode));
    struct ListNode* l2 = malloc (sizeof(struct ListNode));
    l1->val = 2;
    l1->next = malloc(sizeof(struct ListNode));
    l1->next->val = 4;
    l1->next->next = malloc(sizeof(struct ListNode));
    l1->next->next->val = 3;
    //Valgrind will complain about uninitalized values without this line
    l1->next->next->next = NULL;   
    l2->val = 5;
    l2->next = malloc(sizeof(struct ListNode));
    l2->next->val = 6;
    l2->next->next = malloc(sizeof(struct ListNode));
    l2->next->next->val = 4;
    l2->next->next->next = NULL;   
    struct ListNode* result = addTwoNumbers(l1, l2);
    printAll(result);
    freeLinkedList(&result);
    return 0;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* ptr1 = l1;
    struct ListNode* ptr2 = l2;
    struct ListNode* sumNode = malloc(sizeof(struct ListNode));
    struct ListNode* headSum = sumNode;
    int sum = 0, carry = 0;
    while(ptr1 != NULL || ptr2 != NULL || carry != 0) {
        //Reset/initialize values;
        sumNode->val = carry;
        sum = 0, carry = 0;
        //If the node isn't empty add it to the sum node
        if (ptr1 != NULL) {
            sum += ptr1->val;
            ptr1 = ptr1->next;
        }
        if (ptr2 != NULL) {
            sum += ptr2->val;
            ptr2 = ptr2->next;
        }
        sumNode->val += sum;
        //If the number is more than one digit, increment carry
        if (sumNode->val > 9) {
            carry = 1;
            sumNode->val -= 10;
        }
        //If we're looping again allocate space for the next node
        if (ptr1 != NULL || ptr2 != NULL || carry != 0) {
            sumNode->next = malloc(sizeof(struct ListNode));
            sumNode = sumNode->next;
        }
    }
    //Set the last node to NULL to avoid initialization erros
    sumNode->next = NULL;
    //Go back to the first node
    sumNode = headSum;
    freeLinkedList(&l1);
    freeLinkedList(&l2);
    return sumNode;
}

void freeLinkedList(struct ListNode** head) {
    struct ListNode* ptr;
    while (*head != NULL) {
        ptr = *head;
        *head = (*head)->next;
        free(ptr);
    }
}

void printAll(struct ListNode* head) {
    struct ListNode* ptr = head;
    if (head == NULL) {
        printf("Nothing in the linked list\n");
        return;
    }
    while (ptr != NULL) {
        printf("%d\n", ptr->val);
        ptr = ptr->next;
    }
}