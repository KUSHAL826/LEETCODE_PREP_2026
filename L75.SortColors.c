/*
75. Sort Colors
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

Explanation:

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.

Example 2:

Input: nums = [2,0,1]

Output: [0,1,2]

Explanation:

The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
*/

void sortColors(int* nums, int numsSize) {
    int count0=0,count1=0,count2=0,i;
    for(i=0;i<numsSize;i++){
        if(nums[i]==0){
            count0++;
        }
        else if(nums[i]==1){
            count1++;
        }
        else{
            count2++;
        }
    }
    for(i=0;i<count0;i++){
        nums[i]=0;
    }
    for(i=count0;i<(count0+count1);i++){
        nums[i]=1;
    }
    for(i=(count0+count1);i<numsSize;i++){
        nums[i]=2;
    }
}
