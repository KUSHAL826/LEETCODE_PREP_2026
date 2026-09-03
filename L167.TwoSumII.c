/*167. Two Sum II - Input Array Is Sorted
Solved
Medium
Topics
premium lock icon
Companies
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.*/

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int start=0,end=numsSize-1,cur;
    *returnSize=0;
    if(numsSize==0||nums==NULL){
        *returnSize=0;
        return NULL;
    }
    int *ret=(int *)malloc(2*sizeof(int));
    while(start<end){
        cur=nums[start]+nums[end];
        if(cur==target){
            *returnSize=2;
            ret[0]=start+1;
            ret[1]=end+1;
            return ret;
        }
        else if(cur>target){
            end--;
        }
        else{
            start++;
        }
    }
    free(ret);
    return NULL;
}