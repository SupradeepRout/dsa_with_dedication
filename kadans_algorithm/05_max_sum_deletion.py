'''
Definiton : Given an array of integers, find the maximum sum of a subarray where you are allowed to delete at most one element from the subarray.
Approach : Kadane's Algorithm
Time Complexity : O(n) where n is the length of the array
Space Complexity : O(1)
Difficulty : Medium
problem Link : https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/
YouTube Link : https://youtu.be/JUV-Hdtuzsw?si=V573LfntgcSCO4jC
'''


class maxSumDeletion :
    def max_sum_deletion(self , nums):
        n= len(nums)
        no_delete  = nums[0]
        one_delete = 0
        result = nums[0]
        for i in range(1,n):
            prev_no_delete = no_delete  # store the previous no_delete value before updating it
            no_delete = max(no_delete + nums[i] , nums[i])
            one_delete = max(prev_no_delete ,one_delete + nums[i])
            result = max(result , no_delete , one_delete)
        return result
    
if __name__ == "__main__":
    arr=[1,-2,0,3]
    obj = maxSumDeletion()
    result = obj.max_sum_deletion(arr)
    print(f"The maximum sum after at most one deletion is : {result}")