'''

Definition : Given an array of integers, find the maximum absolute sum of a subarray.
Approach : Kadane's Algorithm
Time Complexity : O(n) where n is the length of the array
Space Complexity : O(1)
Difficulty : Medium
problem Link : https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/
YouTube Link : https://youtu.be/Bt9rgQgGf64?si=xvgnYPHAft7OP0o_

'''

class max_absolute_sum :
    def maxAbsoluteSum( self , nums ):
        max_sum = self.maxSum(nums)
        min_sum = self.minSum(nums)
        abs_min = abs(min_sum)
        result = max(max_sum , abs_min)
        return result 

        
    def maxSum(self , nums):
        n= len(nums)
        best_ans=nums[0]
        res=nums[0]
        for i in range(1,n):
            v1=best_ans +nums[i]
            v2= nums[i]
            best_ans = max(v1,v2)
            res = max(res , best_ans)
        return res
    
    def minSum(self , nums):
        n= len(nums)
        best_ans = nums[0]
        min_sum = nums[0]
        for i in range(1,n):
            v1 = best_ans + nums[i]
            v2 = nums[i]
            best_ans = min(v1,v2)
            min_sum = min(min_sum , best_ans)
        return min_sum
    
    
if __name__ == "__main__":
    arr=[1,-3,2,3,-4,5]
    obj = max_absolute_sum()
    result = obj.maxAbsoluteSum(arr)
    print(f"The maximum absolute sum is : {result}")