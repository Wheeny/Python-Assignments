number = int(input("Enter an integer: "))

temp = number
total_sum = 0

        
while temp > 0: 
    last_digit = temp % 10
    total_sum += last_digit  
    temp = temp // 10 
print(f"The sum of the digits of {number} is: {total_sum}")




