#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int intVal(char s);
int romanToInt(char* s);

int main() {
    char* s = malloc(sizeof(char)* 9);
    strcpy(s, "MCMXCIIV");
    printf("%d", romanToInt(s));
    free(s);
    return 0;
}

int romanToInt(char * s){
    //Taking copy of the arguement makes the code 100% faster
    char* romanStr = strdup(s);
    //Take strlen here to make the code 200% faster instead of finding it each loop
    int total = 0, add = 0, buildup = 0, length = strlen(romanStr);
    //Buildup are roman values that are negative, other values are positive
    for (int i = 0; i < length; i++) {
        add = intVal(romanStr[i]);
        //Check the roman integers ahead if they're larger, indicating the current roman value is negative
        if (intVal(romanStr[i+1]) > add) {
            buildup += add;
            add = 0;
        }
        else if (intVal(romanStr[i+1]) < add) {
        }
        else if (intVal(romanStr[i+2]) > add) {
            buildup += add;
            add = 0;
        }
        else if(intVal(romanStr[i+2]) < add) {
        }
        else if (intVal(romanStr[i+3]) > add) {
            buildup += add;
            add = 0;

        }
        if (add > buildup) {
            total -= buildup;
            buildup = 0;
        }
        total += add;
    }
    free(romanStr);
    return total;
}

int intVal(char c) {
    int value = 0;
    switch(c) {
        case 'I': value = 1; break;
        case 'V': value = 5; break;
        case 'X': value = 10; break;
        case 'L': value = 50; break;
        case 'C': value = 100; break;
        case 'D': value = 500; break;
        case 'M': value = 1000; break;
        case '\0': value = 0; break;
        default: value = -1;
    }
    return value;
}