"""
3Sum Closest Problem

Definition:
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Algorithm:
1. Sort the array in ascending order.
2. Initialize the minimum difference to infinity and a variable to store the result sum.
3. Iterate through the array with the first pointer i from 0 to n-3.
4. For each i, use two pointers: left = i+1, right = n-1.
5. Calculate the sum of nums[i] + nums[left] + nums[right].
6. Update the minimum difference and result sum if the current sum is closer to the target.
7. If sum == target, return the sum immediately.
8. If sum < target, move left pointer right (increase sum).
9. If sum > target, move right pointer left (decrease sum).
10. Return the result sum after checking all possibilities.

Time Complexity: O(n^2) - Sorting takes O(n log n), and the two-pointer approach for each i takes O(n).

Difficulty Level: Medium

Platform: LeetCode (Problem 16: 3Sum Closest)
"""


class triplet_sum_closest:
    def closest_sum(self ,nums :list[int], target : int)-> int :
        nums.sort()
        diff= float('inf')
        n= len(nums)
        res_sum = 0
        for i in range (n-2):
            left = i+1
            right = n-1
            
            while(left < right ):
                
                sum = nums[i]+nums[left]+nums[right]
                d = abs(sum - target )
                
                if(d < diff):  ## it find the closest sum to target and update diff .
                    diff = d
                    res_sum = sum
                    
                if sum == target :
                    return res_sum
                
                elif sum < target :
                    left += 1
                else:
                    right -= 1
        return res_sum
if __name__== "__main__" :
    nums=[-1,2,1,-4]
    target=1
    print(f"the closest sum to the target {target} is :{triplet_sum_closest().closest_sum(nums,target)}")