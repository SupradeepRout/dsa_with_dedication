'''
Problem: Max Consecutive Ones III

Definition:
Given a binary array nums and an integer k, the task is to find the maximum number of consecutive 1s
that can be obtained if you are allowed to flip at most k zeroes. The goal is to return the length of
the longest valid subarray containing at most k zeroes.

Algorithm (Sliding Window):
1. Initialize two pointers:
   - low  → left boundary of the sliding window
   - high → right boundary of the sliding window

2. Maintain a variable zero_count to track how many zeroes are currently inside the window.

3. Expand the window by moving high from left to right:
   - If nums[high] is 0, increment zero_count.

4. If zero_count becomes greater than k:
   - Shrink the window from the left by moving low forward
   - If nums[low] is 0, decrement zero_count

5. At every step, calculate the current window size:
   - high - low + 1
   - Update the maximum length found so far

6. Continue until the entire array is processed.

This ensures we always maintain the longest window with at most k zeroes.

Time Complexity: O(n)  Each element is visited at most twice, once by high and once by low.
Space Complexity: O(1)
Difficulty Level: Medium
Platform: LeetCode

Problem Link: https://leetcode.com/problems/max-consecutive-ones-iii/
youtube Link : https://www.youtube.com/watch?v=lyZp-49pdzQ&list=PLbJhGqY-mq47k_WLUtzVjmarUm1EuXPj2&index=14
'''



class max_one :
    '''{ here I use dictionary to track the freq of 0 , 1 }
    
    def max_consicutive_one(self , nums: list[int] , k : int)-> int :
        n=  len(nums)
        low , high =0,0
        max_len = float('-inf')
        char_freq = {}
        
        for high in range(n):
            char_freq[nums[high]] = char_freq.get(nums[high],0) + 1
            zero_count = char_freq.get(0 ,0)
            
            while(zero_count > k ):
                char_freq[nums[low]] -= 1
                
                if char_freq[nums[low]] == 0 :
                    del char_freq[nums[low]]
                low += 1
                zero_count = char_freq.get(0,0)
                
            size = high - low + 1
            max_len = max(size , max_len)
        return max_len 
    '''
    def max_consicutive_one(self , nums , k):
        n=  len(nums)
        low , high = 0,0
        zero_count = 0  # here we use a normal variable to count freq. of 0 insted of use dictionary 
        max_len = float('-inf')
        
        for high in range(n) :
            if nums[high] == 0 :
                zero_count += 1
                
            while ( zero_count > k ):
                if nums[low] == 0:    # only if , low point to a 0 not 1 then only we increase the count of zero count 
                    zero_count -= 1
                low += 1

            size = high - low + 1
            max_len = max(size , max_len)
            
        return max_len 
        
if __name__ == "__main__" :
    nums =[1,1,1,1,0,0,0,1,1,1,0,0]
    k = 2
    obj = max_one()
    print(f"the max length of the substring is {obj.max_consicutive_one(nums , k)}")