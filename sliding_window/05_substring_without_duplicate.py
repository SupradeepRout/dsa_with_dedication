'''
Definition : Given a string s, find the length of the longest substring without repeating characters.
Approach : Sliding Window
Time Complexity : O(n) where n is the length of the string
Space Complexity : O(min(m,n)) where m is the size of the character set and n is the length of the string 
Difficulty : Medium
youtube Link : https://www.youtube.com/watch?v=v4pIgiBQMh8&list=PLbJhGqY-mq47k_WLUtzVjmarUm1EuXPj2&index=13
problem Link : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/'''

class substring_without_duplicate :
    def longestSubstring(self ,s : str)-> int :
        n = len(s)
        low , high = 0,0
        char_freq = {}
        max_len = float('-inf')
        
        for high in range (n):
            char_freq[s[high]] = char_freq.get(s[high] , 0 ) + 1
            window_size = high - low + 1 
            
            while(window_size > len(char_freq)):
                char_freq[s[low]] -= 1 
                if char_freq[s[low]] == 0 :
                    del char_freq[s[low]]
                low += 1
                window_size = high - low + 1
                    
            max_len = max(max_len , window_size)
        return max_len if max_len != float("-inf") else 0
    
if __name__ == "__main__" :
    s = input("Enter the string : ")
    obj = substring_without_duplicate()
    print(f"The length of longest substring without repeating characters is : {obj.longestSubstring(s)}")