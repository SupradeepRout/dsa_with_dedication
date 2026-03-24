class max_subarray_sum :
    def maxSum(self, nums: list[int])-> int :
        n= len(nums)
        best_ans = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
            print(max_sum)
            v1 = best_ans + nums[i]
            v2 = nums[i]
            best_ans = max(v1,v2)
            max_sum = max(max_sum , best_ans)
        return max_sum

if __name__ == "__main__":
    arr= list(map(int,input("enter the elements : ").split(",")))
    obj=max_subarray_sum()
    result = obj.maxSum(arr)
    print(f"The maximum subarray sum is : {result}")