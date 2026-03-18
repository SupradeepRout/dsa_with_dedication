'''
Definition : Given a string s and an integer k,
return the length of the longest substring of s that contains exactly k distinct characters.
Approach : Sliding Window
Time Complexity : O(n) where n is the length of the string
Space Complexity : O(k) where k is the number of distinct characters allowed
Difficulty : Medium
youtube Link : https://www.youtube.com/watch?v=v4pIgiBQMh8&list=PLbJhGqY-mq47k_WLUtzVjmarUm1EuXPj2&index=13
'''

class longest_substring :
    def lengthOfLongestSubstring(self , nums : str , k : int )-> int :
        low , high = 0,0
        n= len(nums)
        char_freq ={}
        max_len = float("-inf")
        
        for high in range(n):
            char_freq[nums[high]] =char_freq.get(nums[high] ,0) + 1
            
            while(len(char_freq) > k):
                
                char_freq[nums[low]] -= 1
                if(char_freq[nums[low]] == 0):
                    del char_freq[nums[low]]
                low += 1
                
            if(len(char_freq) == k):
                max_len = max(max_len , high - low + 1)
                
        return max_len if max_len != float("-inf") else 0
if __name__ == "__main__":
    s = input("Enter the string : ")
    k = int(input("Enter the value of k : "))
    obj = longest_substring()
    print(f"The length of longest substring with at most {k} distinct characters is : {obj.lengthOfLongestSubstring(s,k)}")