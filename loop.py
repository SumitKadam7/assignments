#q1 ->
# loop -> odd numbers n 

#q2
# 1
# 1 2 
# 1 2 3


#q3
# 1
# 1 3
# 1 3 5 
n = int(input("enter the number of rows:"))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()