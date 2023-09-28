#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lengthOfLongestSubstring(char * s);

int main() {
    char s[] = "abcdefghijklmnopqrstuvwxyz,./;'[]\1234567890)(*&^%$#@!) ABCDEFGHIJKLMNOPQSTUVWXYZabcdef";
    int length = lengthOfLongestSubstring(s);
    printf("Length of the longest substring without repeating characters: %d\n", length);
    return 0;
}

int lengthOfLongestSubstring(char * s) {
    int length = 0, leftBound = 0;
    int seen[128]; //Array to store the index of each ASCII character

    //Initialize all values to -1 to indicate the ASCII character hasn't been seen
    for (int i = 0; i < 128; i++) {
        seen[i] = -1;
    }
    for (int i = 0; i < strlen(s); i++) {
        /*If the character has been seen and it's not currently in the substring being created,
        set the leftbound to it's index value; add one to negate the starting index of 0.*/
        if (seen[s[i]] != -1 && seen[s[i]] >= leftBound) {
            leftBound = seen[s[i]] + 1;
        }
        //Check if our leftbound to right bound is greater than it ever has been
        else {
            /*Calculates the length of the current index by the last duplicate character or
            starting index. BEDMAS doesn't occur, simply left-to-right.*/
            if (length <= i - leftBound + 1) {
                length = i - leftBound + 1;
            }
        }
        //Set the seen character's ASCII value to its index
        seen[s[i]] = i;
    }
    return length;
}