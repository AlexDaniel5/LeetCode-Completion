#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char* convert(char* s, int numRows) {
    //Special case
    if (numRows == 1) {
        return s;
    }

    int n = strlen(s);
    int currRow = 0, currCol = 0, currentStringIndex = 0;
    //The total number of characters divided by the number of characters in each section provides us the minimum number of sections to cover the entire string
    //The minus two is for the diagonal, so it's not counting the bottom and top space (empty)
    int sections = ceil(n / (2.0 * numRows - 2));
    //Using sections we can calculate the number of columns at the beginning of the code instead of dynamically growing the array
    int noColumns = sections * (numRows - 1);

    //Allocate space
    char** matrix = malloc(numRows * sizeof(char*));
    for (int i = 0; i < numRows; i++) {
        matrix[i] = malloc(noColumns * sizeof(char));
        //Set every index of the matrix as a space character
        memset(matrix[i], ' ', noColumns * sizeof(char));
    }
    //Loop for column
    while (currentStringIndex < n) {
        //Loop for row
        while (currRow < numRows && currentStringIndex < n) {
            matrix[currRow][currCol] = s[currentStringIndex];
            currRow++;
            currentStringIndex++;
        }
        currCol++;
        currRow -= 2;
        //Loop for diagonal
        while (currRow > 0 && currCol < noColumns && currentStringIndex < n) {
            matrix[currRow][currCol] = s[currentStringIndex];
            currRow--;
            currCol++;
            currentStringIndex++;
        }
    }

    char* ans = malloc((n + 1) * sizeof(char));
    int ansIndex = 0;
    //Copy every character that isn't a space to the answer string
    for (int i = 0; i < numRows; i++) {
        for (int j = 0; j < noColumns; j++) {
            if (matrix[i][j] != ' ') {
                ans[ansIndex++] = matrix[i][j];
            }
        }
    }

    ans[ansIndex] = '\0';

    for (int i = 0; i < numRows; i++) {
        free(matrix[i]);
    }
    free(matrix);

    return ans;
}

int main() {
    char* output = convert("PAYPALISHIRING", 4);
    printf("%s\n", output);
    free(output);
    return 0;
}