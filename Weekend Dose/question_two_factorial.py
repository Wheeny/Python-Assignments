def factorial_calculation(number):
    factorial = 1
    
    for count in range(1, number+1):
        factorial *= count
    return factorial
    
number = int(input("Enter a positive integer: "))
result = factorial_calculation(number)

print(f"{number} factorial is: {result}")
