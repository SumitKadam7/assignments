n=int(input("enter the number of rows: "))
num=1
for row in range(1,n+1):
    for col in range(1,row+1):
        print (num,end=" ")
        num+=2
    print()