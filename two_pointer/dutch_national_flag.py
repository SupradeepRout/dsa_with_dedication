"""
Problem: Dutch National Flag / Sort Colors

Definition:
The Dutch National Flag problem requires sorting an array containing only three distinct values
(typically 0, 1, and 2) in a single traversal. The goal is to rearrange the elements so that all
0s appear first, followed by 1s, and then 2s. This problem is commonly used to demonstrate the
two-pointer / three-pointer technique and in-place array manipulation.

Algorithm (Dutch National Flag Algorithm):
1. Initialize three pointers:
   - low  → tracks the boundary for the next position of 0
   - mid  → current element being examined
   - high → tracks the boundary for the next position of 2

2. Traverse the array while mid <= high:
   a. If nums[mid] == 0:
      - Swap nums[mid] with nums[low]
      - Increment both low and mid
   b. If nums[mid] == 1:
      - Move mid forward
   c. If nums[mid] == 2:
      - Swap nums[mid] with nums[high]
      - Decrement high (do NOT increment mid because the swapped value needs evaluation)

3. Continue until mid crosses high.

This ensures all elements are sorted in a single pass.

Time Complexity: O(n)  Each element is processed at most once.

Space Complexity: O(1)   Sorting is performed in-place without extra memory.

Difficulty Level: Medium

Platform: LeetCode

Problem Link: https://leetcode.com/problems/sort-colors/description/
"""



class dutch_national_flag:
    def sort(self ,nums :list[int] )-> list[int] :
        n= len(nums)
        low = 0  
        mid = 0 
        high = n-1 
        
        while(mid <= high):
            
            if(nums[mid] == 0):
                nums[mid],nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1
            elif(nums[mid] == 1):
                mid += 1
            else:
                nums[mid] , nums[high] = nums[high],nums[mid]
                high -= 1
        return nums
    
if __name__ == "__main__":
    nums=[2,0,2,1,1,0]
    obj = dutch_national_flag()
    print(obj.sort(nums))        