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
            
            while (diff > k ):
                char_freq[s[low]] -= 1
                
                if char_freq[s[low]] == 0 :
                    del char_freq[s[low]]
                low += 1
                window_size =  high -low + 1 
                max_freq = max(char_freq.values())
                diff = window_size - max_freq
            if(diff <= k ):
                max_len = max(max_len , window_size)
        return max_len if max_len != float('-inf') else 0

if __name__ == "__main__":
    s = input("Enter the string : ")
    k = int(input("Enter the value of k : "))
    obj = substring_with_same_letter()
    print(f"The length of longest substring with same letter after replacement is : {obj.longestSubstring(s,k)}")