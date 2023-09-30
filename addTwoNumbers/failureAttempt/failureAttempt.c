#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Define structs outside of main
struct ListNode {
        int val;
        struct ListNode* next;
    };

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2);
void printAll(struct ListNode* head);
unsigned int sumVals(struct ListNode* head);
unsigned int power (unsigned int base, int exponent);
struct ListNode* convertNumToLinkedList(int *num, int* size);
int* numToArray(unsigned int num, int *size);
void freeLinkedList(struct ListNode** head);

int main() {
    struct ListNode* l1 = malloc(sizeof(struct ListNode));
    struct ListNode* l2 = malloc (sizeof(struct ListNode));
    l1->val = 1;
    l1->next = malloc(sizeof(struct ListNode));
    l1->next->val = 9;
    l1->next->next = malloc(sizeof(struct ListNode));
    l1->next->next->val = 9;
    l1->next->next->next = malloc(sizeof(struct ListNode));
    l1->next->next->next->val = 9;
    l1->next->next->next->next = malloc(sizeof(struct ListNode));
    l1->next->next->next->next->val = 9;
    l1->next->next->next->next->next = malloc(sizeof(struct ListNode));
    l1->next->next->next->next->next->val = 9;
    l1->next->next->next->next->next->next = malloc(sizeof(struct ListNode));
    l1->next->next->next->next->next->next->val = 9;
    l1->next->next->next->next->next->next->next = malloc(sizeof(struct ListNode));
    l1->next->next->next->next->next->next->next->val = 9;
    l1->next->next->next->next->next->next->next->next = malloc(sizeof(struct ListNode));
    l1->next->next->next->next->next->next->next->next->val = 9;
    l1->next->next->next->next->next->next->next->next->next = malloc(sizeof(struct ListNode));
    l1->next->next->next->next->next->next->next->next->next->val = 9;
    //Valgrind will complain about uninitalized values without this line
    l1->next->next->next->next->next->next->next->next->next->next = NULL;   
    l2->val = 9;
    //l2->next = malloc(sizeof(struct ListNode));
    // l2->next->val = 6;
    // l2->next->next = malloc(sizeof(struct ListNode));
    // l2->next->next->val = 4;
    // l2->next->next->next = malloc(sizeof(struct ListNode));
    // l2->next->next->next->val = 9;
    l2->next = NULL;   
    //Take the pointer of the linked list so modifications can occur
    struct ListNode* result = addTwoNumbers(l1, l2);
    freeLinkedList(&result);
    //printAll(l1);
    return 0;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int *listNum, *size = malloc(sizeof(int));
    unsigned int num1 = 0, num2 = 0, sum = 0;
    struct ListNode* linkedListSum;
    num1 = sumVals(l1);
    num2 = sumVals(l2);
    printf("\n%f %f\n", num1, num2);
    sum = num1 + num2;
    listNum = numToArray(sum, size);
    linkedListSum = convertNumToLinkedList(listNum, size);
    freeLinkedList(&l1);
    freeLinkedList(&l2);
    free(listNum);
    free(size);
    return linkedListSum;
}

void freeLinkedList(struct ListNode** head) {
    struct ListNode* ptr;
    while (*head != NULL) {
        ptr = *head;
        *head = (*head)->next;
        free(ptr);
    }
}

struct ListNode* convertNumToLinkedList(int* num, int* size) {
    struct ListNode* head = malloc(sizeof(struct ListNode));
    struct ListNode* ptr = head;
    //0 + 0 case
    if (num == 0) {
        ptr->val = 0;
        ptr->next = NULL;
        return head;
    }
    for ( int i = 0; i < *size; i++) {
        ptr->val = num[i];
        if (i < *size - 1) {
            ptr->next = malloc(sizeof(struct ListNode));
            ptr = ptr->next;
        }
    }
    //Valgrind will complain without an intialized value
    ptr->next = NULL;
    return head;
}

    
int* numToArray(unsigned int num, int* size) {
    unsigned int temp = num;
    int length = 0;
    int* listNum = malloc(sizeof(int));
    //Determine length of number
    while (temp != 0) {
        temp /=10;
        length++;
    }
    listNum = realloc(listNum, sizeof(int) * length);
    //Grab the lowest digit and add it to the array one by one
    for (int i = 0; i < length; i++) {
        listNum[i] = num % 10;
        num /= 10;
    }
    *size = length;
    return listNum;
}

void reverseLinkedList(struct ListNode** head) {
    struct ListNode* prev = NULL, *ptr = *head, *next = NULL;

    while (ptr != NULL) {
        //Store next node
        next = ptr->next;
        //Place the next node to the previous node
        ptr->next = prev;
        //Move to the next nodes
        prev = ptr;
        ptr = next;
    }
    //Update the head node to the end of the linked list
    *head = prev;
}

unsigned int sumVals(struct ListNode* head) {
    unsigned int multiplier = 0, total = 0;
    int exp = 0;
    while(head != NULL) {
        multiplier = power(10, exp);
        //Multiplier is for the digit placement
        total += head->val * multiplier;
        head = head->next;
        exp++;
    }
    return total;
}

void printAll(struct ListNode* head) {
    struct ListNode* ptr = head;
    if (head == NULL) {
        printf("Nothing in the linked list");
        return;
    }
    while (ptr != NULL) {
        printf("%d\n", ptr->val);
        ptr = ptr->next;
    }
}

//Do a power operation
unsigned int power (unsigned int base, int exponent) {
    unsigned int result = 1;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}