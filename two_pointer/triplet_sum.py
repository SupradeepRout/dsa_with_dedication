"""
Problem: 3-Sum / find all unique triplets in an integer array whose sum equals zero.

Definition:
    Given an array of integers, return all unique triplets [a, b, c] such that
    a + b + c == 0. The order of triplets or elements within them is irrelevant,
    and duplicates must not appear in the output.

Example:
    Input:  [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

Platform: LeetCode #15 

Difficulty: Medium

Approach : two-pointer after sorting

Time Complexity: O(n^2) worst-case (sorting is O(n log n) plus two-pointer scan).
Space Complexity: O(k) for result list (k = number of found triplets), O(1)
extra space otherwise.
"""

class three_sum :
    def find_triplet(self,nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]
        n=len(nums)
        
        for i in range(n-2):
            
            if(i > 0 and nums[i]==nums[i-1]):
                continue
            
            ptr1=i+1 
            ptr2=n-1 
            sum= -nums[i]
            
            while(ptr1 < ptr2):
                s= nums[ptr1] + nums[ptr2]
                if(s == sum):
                    result.append([nums[i],nums[ptr1],nums[ptr2]])
                    ptr1+=1
                    ptr2-=1
                    while(ptr1 < n and nums[ptr1] == nums[ptr1-1]):
                        ptr1 += 1
                        
                    while(ptr2 > 0 and nums[ptr2] == nums[ptr2+1]):
                        ptr2 -= 1
                        
                elif(s < sum):
                    ptr1 += 1
                    
                else:
                    ptr2 -= 1
        return result
    
if __name__ == "__main__":
    nums=[-1,0,1,2,-1,-4]
    print(three_sum().find_triplet(nums))