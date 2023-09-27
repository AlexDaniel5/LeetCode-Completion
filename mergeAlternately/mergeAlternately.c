#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char * mergeAlternately(char * word1, char * word2);

int main() {
    char * word1 = "abcd";
    char * word2 = "pq";
    char * result = mergeAlternately(word1, word2);
    printf("%s\n", result);
    return 0;
}

char * mergeAlternately(char * word1, char * word2){
    char * mergedWord;
    int length = strlen(word1) + strlen(word2);
    int j = 0;
    mergedWord = malloc((length + 1) * sizeof(char));
    for (int i = 0; i < length; i++) {
        if ((i % 2 == 0) && (*word1 != '\0')) {
            mergedWord[i] = * word1;
            word1++;
        }
        else {
            if (*word2 != '\0') {
                mergedWord[i] = * word2;
                word2++;
            }
            else {
                mergedWord[i] = * word1;
                word1++;
            }
        }
        j++;
    }
    mergedWord[j] = '\0';
    return mergedWord;
}