'''

Definition : Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Approach : Kadane's Algorithm
Time Complexity : O(n) where n is the length of the array
Space Complexity : O(1)
Difficulty : Medium
problem Link : https://leetcode.com/problems/maximum-subarray/description/
YouTube Link : https://www.youtube.com/watch?v=5WZlEdbKEeY&list=PLbJhGqY-mq47k_WLUtzVjmarUm1EuXPj2&index=22

'''




class max_subarray_sum :
    def maxSum(self, nums: list[int])-> int :
        n= len(nums)
        best_ans = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
            print(max_sum)
            v1 = best_ans + nums[i]
            v2 = nums[i]
            best_ans = max(v1,v2)
            max_sum = max(max_sum , best_ans)
        return max_sum

if __name__ == "__main__":
    arr= list(map(int,input("enter the elements : ").split(",")))
    obj=max_subarray_sum()
    result = obj.maxSum(arr)
    print(f"The maximum subarray sum is : {result}")