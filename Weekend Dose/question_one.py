""" number = int(input("Enter an integer: "))

total_sum = 0

for count in range (1, number + 1):
    total_sum += count
    
print(f"The sum of numbers from 1 to {n} is : {total_sum}")
"""







def calculate_sum(number):
    total_sum = 0
    for count in range (1, number + 1):
        total_sum += count
    return total_sum
        
number = int(input("Enter an integer: ")) 
result = calculate_sum(number)
   
print(f"The sum of numbers from 1 to {number} is : {result}")
