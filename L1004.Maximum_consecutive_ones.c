/*
1004. Max Consecutive Ones III
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length*/

int longestOnes(int* nums, int numsSize, int k) {
    int zero_count=0,max_ones=0,start=0,end=0;
    for(end=0;end<numsSize;end++){
        if(nums[end]==0){
            zero_count++;
        }
        if(zero_count>k){
            if(nums[start]==0){
                zero_count--;
            }
            start++;
        }
        max_ones=(max_ones<end-start+1)?end-start+1:max_ones;
    }
    return max_ones;
}