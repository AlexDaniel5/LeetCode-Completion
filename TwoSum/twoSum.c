#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize);

int main() {
    int* nums = malloc(sizeof(int)*4);
    nums[0] = 2;
    nums[1] = 7;
    nums[2] = 11;
    nums[3] = 15;
    int numsSize = 4;
    int target = 9;
    int* returnSize = malloc(sizeof(int));
    int* sumNums = twoSum(nums, numsSize, target, returnSize);
    for (int i = 0; i < *returnSize; i++) {
        printf("%d\n", sumNums[i]);
    }
    return 0;
}
//Note: The returned array must be malloced, assume caller calls free().
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int* sumNums = malloc(sizeof(int) * 2);
    *returnSize = 2;
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                sumNums[0] = i;
                sumNums[1] = j;
                return sumNums;
            }
        }
    }
    return sumNums;
}   