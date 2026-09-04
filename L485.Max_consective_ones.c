/*
485. Max Consecutive Ones
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
*/

int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int i,max_ones=0,cur_ones=0;
    for(i=0;i<numsSize;i++){
        if(nums[i]==1){
            cur_ones++;
        }
        if(nums[i]==0){
            cur_ones=0;
        }
        max_ones=(cur_ones>max_ones)?cur_ones:max_ones;
    }
    return max_ones;
}
