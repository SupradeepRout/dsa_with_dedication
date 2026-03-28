n = int(input("enter no of element : "))
item = [int(input()) for _ in range(n)]
# this arr contain only 0 ,1 ,2
count_0  = item.count(0)
count_1 =  item.count(1)
print(count_0)