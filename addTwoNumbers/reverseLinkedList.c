//Thought I'd need this, but the program works fine without the function
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Define structs outside of main
struct ListNode {
        int val;
        struct ListNode* next;
    };

void reverseLinkedList(struct ListNode** head);

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