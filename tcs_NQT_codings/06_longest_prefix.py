def prefx (arr):
    n = len(arr[0])# the length of only 1st string 
    m= len(arr) # total length of the array
    
    for i in range(n):
        char = arr[0][i]
        
        for j in range(1,m) :
            if i >=len(arr[j]) or  arr[j][i] != char :
                return arr[0][:i]
    return arr[0]

n=int(input("Enter the no of strings : "))
#strs =[input() for _ in range(n)]
strs =[input().split(",")]
print(f"the common prefix is : {prefx(strs)}")
