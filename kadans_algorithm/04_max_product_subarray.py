'''
Definition : Given an array of integers, find the maximum product of a subarray.
Approach : Kadane's Algorithm
Time Complexity : O(n) where n is the length of the array
Space Complexity : O(1)
Difficulty : Medium
problem Link : https://leetcode.com/problems/maximum-product-subarray/description/
YouTube Link : https://youtu.be/EcQN1jziwDo?si=3lFSpWRYFqbgu9nm
'''

class max_product_subarray :
    def maxProduct(self , nums):
        n= len(nums)
        prev_min = nums[0]
        prev_max = nums[0]
        result = nums[0]
        
        for i in range(1,n):
            v1 = prev_max * nums[i] 
            v2 = prev_min * nums[i] 
            v3 = nums[i] 
            
            prev_max = max(v1,v2,v3)
            prev_min = min(v1,v2,v3)
            result = max(result, prev_max)
        return result

if __name__ == "__main__":
    arr=[-2,3,-2,-4]
    obj = max_product_subarray()
    result = obj.maxProduct(arr)
    print(f"The maximum product subarray is : {result}")