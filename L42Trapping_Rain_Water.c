/*
42. Trapping Rain Water
Solved
Hard
Topics
premium lock icon
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
*/
int min_value(int a,int b){
    return ((a<b)?a:b);
}

int trap(int* height, int heightSize) {
    int i,total=0;
    int* leftmax=(int *)malloc(heightSize*sizeof(int));
    int* rightmax=(int *)malloc(heightSize*sizeof(int));
    leftmax[0]=height[0];
    for(i=1;i<heightSize;i++){
        leftmax[i]=height[i]>leftmax[i-1]?height[i]:leftmax[i-1];
    }
    rightmax[heightSize-1]=height[heightSize-1];
    for(i=heightSize-2;i>=0;i--){
        rightmax[i]=height[i]>rightmax[i+1]?height[i]:rightmax[i+1];
    }
    for(i=0;i<heightSize;i++){
        int min=min_value(leftmax[i],rightmax[i]);
        total+=min-height[i];
    }
    return total;
}