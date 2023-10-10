#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * longestPalindrome (char * s);

int main () {
    char* str = longestPalindrome("abasooosk");
    free(str);
    return 0;
}

char* longestPalindrome (char * s){
    int len = strlen(s);
    int left = 0;
    int right = 0;
    int longest = 0;
    int index = 0;
    char* palindrome = NULL;
    for (int i = 0; i < len; i++) {
        //Odd palindrome
        left = right = i;
        while (left > -1 && right < len && s[left] == s[right]) {
            left--;
            right++;
        }
        if (longest < (right - 1) - left) {
            longest = (right - 1) - left;
            index = left + 1;
        }
        //Even palindrome
        left = i;
        right = i + 1;
        while (left > -1 && right < len && s[left] == s[right]) {
            left--;
            right++;
        }
        if (longest < (right - 1) - left) {
            longest = (right - 1) - left;
            index = left + 1;
        }
    }
    //Copy palindrome
    palindrome = malloc(sizeof(char) * (longest + 1));
    for (int i = 0; i < longest; i++) {
        palindrome[i] = s[index+i];
    }
    palindrome[longest] = '\0';
    return palindrome;
}