def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

index=int(input("Enter the index position till where you want series: "))
if index<=0:
    print("Add a positive number")
else:
    for i in range(0,index):
        print(fibonacci(i),end=" ")

