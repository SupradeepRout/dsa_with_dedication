class fruit_in_bucket:
    def total_fruits(self , fruits :list[int] )-> int :
        n = len(fruits)
        k = 2
        low , high = 0 , 0
        fruit_freq = {}
        max_fruits = float('-inf')
        
        for high in range (n) :
            fruit_freq[fruits[high]] = fruit_freq.get(fruits[high], 0) + 1
            
            while(len(fruit_freq) > k):
                fruit_freq[fruits[low]] -= 1
                
                if fruit_freq [fruits[low]] == 0 :
                    del fruit_freq[fruits[low]] 
                low += 1
            if(len(fruit_freq) <= k):
                max_fruits = max( max_fruits , high -low + 1)
        return max_fruits if max_fruits != float('-inf') else 0
if __name__ == "__main__":
    fruits = [2,2,11]
    obj = fruit_in_bucket()
    print(f"The maximum number of fruits that can be collected in two baskets is : {obj.total_fruits(fruits)}")