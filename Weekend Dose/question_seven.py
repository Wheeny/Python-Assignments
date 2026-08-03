n = int(input("Enter a number (n): "))

count = 0

for number in range(1, 101):
    if number % n == 0:
        count += 1  

print(f"There are {count} multiples of {n} between 1 and 100.")
