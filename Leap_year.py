year = int(input("Enter the year: "))

if year % 400 == 0:
    print("Yes, it is a leap year")
elif year % 100 == 0:
    print("No, it is not a leap year")
elif year % 4 == 0:
    print("Yes, it is a leap year")
else:
    print("No, it is not a leap year")
