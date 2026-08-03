numbers = [5,2,8,10,12,3,15]

even_number_count = 0
odd_number_count = 0

for num in numbers:
    if num % 2 == 0:
        even_number_count += 1
        
    else:
        
        odd_number_count += 1
        
        
print(f"Count of even numbers = {even_number_count}")
print(f"Count of odd numbers = {odd_number_count}")
