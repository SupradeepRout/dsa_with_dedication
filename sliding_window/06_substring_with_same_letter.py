''' 
Definition : Given a string s and an integer k, return the length of the longest substring of s 
that can be obtained by replacing at most k characters with any other character to make all characters in the substring the same.
Approach : Sliding Window
Time Complexity : O(n) where n is the length of the string
Space Complexity : O(1) as we are using a fixed size hashmap of 26 characters
Difficulty : Medium
youtube Link : https://www.youtube.com/watch?v=v4pIgiBQMh8&list=PLbJhGqY-mq47k_WLUtzVjmarUm1EuXPj2&index=14
problem Link : https://leetcode.com/problems/longest-repeating-character-replacement/description/
'''

class substring_with_same_letter :
    def longestSubstring(self , s : list[int] , k : int )-> int :
        n = len(s)
        low , high  = 0,0
        char_freq = {}
        max_len = float('-inf')
        
        for high in range(n):
            char_freq[s[high]] = char_freq.get(s[high], 0) + 1
            window_size = high - low + 1
            max_freq = max(char_freq.values())
            diff = (window_size - max_freq)
            
            while (diff > k ):          # we need to shrink the window as we cannot replace more than k characters to make all characters same
                char_freq[s[low]] -= 1
                
               # if char_freq[s[low]] == 0 :
               #     del char_freq[s[low]]
                    
                low += 1
                window_size =  high -low + 1 
                max_freq = max(char_freq.values())
                diff = window_size - max_freq
                
            if(diff <= k ):   # we can replace the characters to make all characters same
                max_len = max(max_len , window_size)
        return max_len if max_len != float('-inf') else 0

if __name__ == "__main__":
    s = input("Enter the string : ")
    k = int(input("Enter the value of k : "))
    obj = substring_with_same_letter()
    print(f"The length of longest substring with same letter after replacement is : {obj.longestSubstring(s,k)}")