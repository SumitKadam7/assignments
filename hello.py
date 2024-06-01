n=int(input("enter the number of rows:"))
num=1
for row in range (1, n+1):
    for col in range (row):
        print(num, end=" ")
        num=num+1
     
    print("")



