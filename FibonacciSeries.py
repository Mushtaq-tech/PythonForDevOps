index=int(input("Enter the index position till where you want series: "))
num1=0
num2=1
temp=0
print(num1)
print(num2)
for i in range(0,index):
    temp=num1+num2
    num1=num2
    num2=temp
    print(temp)