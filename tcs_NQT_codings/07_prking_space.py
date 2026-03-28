m=int(input("Enter the row count: "))
n=int(input("enter the column count : "))
max_count= -1
res=-1
park =[[int(input()) for _ in range(n)] for _ in range(m)]

for i in range(m) :
    one_count = park[i].count(1)
    if one_count > max_count :
        max_count = one_count
        res =i+1 # 1 based indexing 
print(f"the row with highest one : {res}")