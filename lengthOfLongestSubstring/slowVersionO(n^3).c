#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lengthOfLongestSubstring(char * s);

int main() {
    char s[] = "dvdf";
    int length = lengthOfLongestSubstring(s);
    printf("Length of the longest substring without repeating characters: %d\n", length);
    return 0;
}

int lengthOfLongestSubstring(char * s) {
    char* tempString = malloc(sizeof(char));
    tempString[0] = '\0';
    int longestLength = 0, stringLength = 0;
    //Loop through the input string and copy each letter from it to a temporary string
    for (int i = 0; i < strlen(s); i++) {
        //Check if the letter from the input string exists in the temporary string
        for (int j = 0; j < strlen(tempString); j++) {
            if (s[i] == tempString[j]) {
                if (strlen(tempString) > longestLength) {
                    longestLength = strlen(tempString);
                }
                //Go to the front of the index after the duplicated character
                i -= stringLength-1;
                tempString = realloc(tempString, sizeof(char));
                stringLength = 0;
                tempString[stringLength] = '\0';
                break;
            }
        }
        //Add two for the added character and the null character
        tempString = realloc(tempString, sizeof(char) * (stringLength+2));
        tempString[stringLength] = s[i];
        tempString[stringLength + 1] = '\0';
        stringLength++;
    }
    //Case if the last set of characters is the longest length
    if (strlen(tempString) > longestLength) {
        longestLength = strlen(tempString);
    }
    free(tempString);
    return longestLength;
}