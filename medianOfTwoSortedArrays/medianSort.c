#include <stdio.h>
#include <stdlib.h>
//Testing commits
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size);
int* bubbleSort(int* arr, int size);

int main() {
    int* nums1 = malloc(2 * sizeof(int));
    nums1[0] = 1;
    nums1[1] = 3;
    int* nums2 = malloc(2 * sizeof(int));
    nums2[0] = 2;
    nums2[1] = 4;
    int nums1Size = 2, nums2Size = 2;
    double median = findMedianSortedArrays(nums1, nums1Size, nums2, nums2Size);
    free(nums1);
    free(nums2);
    return 0;
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int medianSize = nums1Size + nums2Size;
    int* medianArray = malloc((medianSize) * sizeof(int));
    double median = 0;
    int middle = 0;
    //Initalize the values of the array
    for (int i = 0; i < nums1Size; i++) {
        medianArray[i] = nums1[i];
    }
    for(int i = nums1Size; i < medianSize; i++) {
        medianArray[i] = nums2[i-nums1Size];
    }
    medianArray = bubbleSort(medianArray, medianSize - 1);
    middle = medianSize / 2;
    //If the array has an odd amount of numbers
    if (medianSize % 2 == 1) {
        median = medianArray[middle];
    }
    //If the array has an even amount of numbers
    else {
        median = (double)(medianArray[middle-1] + medianArray[middle]) / 2.0;
    }
    free(medianArray);
    return median;
}

//Examines each set of adjacent numbers and switches their positions if they're out of order
int* bubbleSort(int* arr, int size) {
    int temp = 0;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    return arr;
}