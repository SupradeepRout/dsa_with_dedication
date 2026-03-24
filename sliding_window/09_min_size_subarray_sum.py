'''
Definition : Given an array of positive integers and a target, return the minimal length of a contiguous subarray whose sum is greater than or equal to the target.
Approach : Sliding Window

Time Complexity : O(n) where n is the length of the array
Space Complexity : O(1)
Difficulty : Medium

problem Link : https://leetcode.com/problems/minimum-size-subarray-sum/description/
'''


class min_size_subarray_sum :
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        low , high = 0, 0
        sum = 0
        min_len = float('inf')
        for high in range(n) :
            sum += nums[high]
            
            while( sum >= target):
                length = high - low + 1 
                min_len = min(min_len , length )
                sum -= nums[low]
                low += 1
        return min_len if min_len != float('inf') else 0