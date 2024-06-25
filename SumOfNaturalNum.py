def calculate_sum_of_natural_numbers():
    n = int(input("Sum of how many natural numbers you want to calculate: "))
    if n < 0:
        print("Please enter a non-negative number")
    elif n == 0:
        print("Sum of 0 natural numbers is 0")
    elif n == 1:
        print("Sum of 1 natural number is 1")
    else:
        sum = (n * (n + 1)) // 2
        print("Sum of", n, "natural numbers is", sum)

calculate_sum_of_natural_numbers()
