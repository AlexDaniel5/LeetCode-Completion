#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * longestPalindrome(char * s);

//Difficult testcases ccd, babad, aacabdkacaa
int main() {
    char* str = malloc(sizeof(char) * 12);
    strcpy(str, "aacabdkacaa");
    str = longestPalindrome(str);
    free(str);
    return 0;
}

char * longestPalindrome(char * s){
    int index = 0;
    int currLen = 0;
    int longest = 0;
    int longestIndex = 0;
    int leftMatch = 0;
    int len = strlen(s);
    char* palindrome = NULL;
    //i is for the leftmost character, j is for rightmost, leftMatch is for incrementing towards the rightmost to check for matching characters
    for (int i = 0; i < len; i++) {
            index = i;
            currLen = 0;
            leftMatch = i;
        for (int j = len - 1; j >= leftMatch; j--) {
            //Matching characters, add two to the length, unless if it's an even palindrome add one
            if (s[leftMatch] == s[j]) {
                currLen += 2;
                if (leftMatch == j) {
                    currLen--;
                }
            }
            leftMatch++;
        }
        //New longest palindrome
        if (currLen > longest) {
            longestIndex = index;
            longest = currLen;
        }
    }
    //Case for single letter
    if (longest == 0 && len > 0) {
        longest = 1;
    }
    //Copy palindrome
    palindrome = malloc(sizeof(char) * longest + 1);
    for (int i = 0; i < longest; i++) {
        palindrome[i] = s[longestIndex + i];
    }
    palindrome[longest] = '\0';
    printf("%s", palindrome);
    return palindrome;
}