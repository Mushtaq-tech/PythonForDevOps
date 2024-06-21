a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
if a>b:
    a=a+b #30
    b=a-b #10
    a=a-b #20
    print(a,b)
else:
    b=a+b #30
    a=b-a #20
    b=b-a #10
    print(a,b)
