str=input("Enter the string: ")
str=str.lower()
revstr=""
for i in str:
    revstr=str[::-1]
print(revstr)